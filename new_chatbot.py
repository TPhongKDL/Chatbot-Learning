import json
import spacy
from googletrans import Translator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Khởi tạo Chatbot...")

# 1. Tải mô hình spaCy NLP và khởi tạo Translator
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Mô hình 'en_core_web_sm' chưa được tải về. Vui lòng chạy lệnh:")
    print("python -m spacy download en_core_web_sm")
    exit()

translator = Translator()

# 2. Tải dữ liệu từ file JSON
data_filename = "privacy_policy_filtered.json"
try:
    with open(data_filename, "r", encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tệp dữ liệu '{data_filename}'.")
    print("Vui lòng chạy 'python scrape.py' trước để tạo tệp dữ liệu.")
    exit()

# 3. Xử lý và chuẩn bị dữ liệu cho chatbot
def flatten_json(json_obj, parent_key='', sep='_'):
    items = []
    for k, v in json_obj.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            items.append((new_key, ', '.join(v)))
        else:
            items.append((new_key, v))
    return dict(items)

flattened_data = flatten_json(data)
documents = list(flattened_data.values())
keys = list(flattened_data.keys())

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# 4. Các hàm chức năng của Chatbot
def find_most_relevant_passage(question):
    question_vector = vectorizer.transform([question])
    similarities = cosine_similarity(question_vector, tfidf_matrix).flatten()
    best_idx = similarities.argmax()
    return keys[best_idx], documents[best_idx]

def chatbot():
    print("--------------------------------------------------")
    print("Chatbot: Chào bạn! Tôi có thể trả lời các câu hỏi về Chính sách Bảo mật.")
    print("Gõ 'exit' hoặc 'quit' để thoát.")
    print("--------------------------------------------------")
    
    while True:
        question = input("Bạn: ")
        if question.lower() in ["exit", "quit"]:
            print("Chatbot: Tạm biệt!")
            break
        
        detected_lang = translator.detect(question).lang
        if detected_lang != "en":
            translated_question = translator.translate(question, src=detected_lang, dest="en").text
        else:
            translated_question = question
        
        doc = nlp(translated_question)
        processed_question = " ".join([token.lemma_ for token in doc if not token.is_stop])
        
        key, passage = find_most_relevant_passage(processed_question)
        
        if detected_lang != "en":
            passage = translator.translate(passage, src="en", dest=detected_lang).text
        
        print(f"Chatbot: {passage}")

# Bắt đầu chatbot
if __name__ == "__main__":
    chatbot()