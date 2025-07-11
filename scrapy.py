# scrape.py
# Chịu trách nhiệm cào dữ liệu và lưu vào file JSON

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

print("Bắt đầu quá trình cào dữ liệu...")

# Cấu hình Selenium
options = Options()
options.add_argument("--headless")  # Chạy trình duyệt ở chế độ ẩn
options.add_argument("--disable-gpu")
# Thay thế bằng đường dẫn đến chromedriver của bạn hoặc đảm bảo nó nằm trong PATH
# service = Service('C:\\Users\\ASUS\\Documents\\chromedriver-win64\\chromedriver-win64.exe') 
# driver = webdriver.Chrome(service=service, options=options)

# Cách tốt hơn: Không cần Service nếu chromedriver đã được quản lý bởi selenium manager
driver = webdriver.Chrome(options=options)

# Mở trình duyệt và tải trang web
url = "https://www.presight.io/privacy-policy.html"
driver.get(url)

# Lấy nội dung HTML từ trang
html_content = driver.page_source
driver.quit()  # Đóng trình duyệt

# Phân tích HTML với BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Hàm trích xuất nội dung tiêu đề, đoạn văn và danh sách từ thẻ div cụ thể
def extract_content_from_div(soup, div_class):
    sections = {}
    current_title = None

    target_div = soup.find("div", class_=div_class)
    if not target_div:
        print(f"Không tìm thấy thẻ div với class '{div_class}'")
        return sections

    for tag in target_div.find_all(['h1', 'h2', 'h3', 'p', 'ul']):
        if tag.name in ['h1', 'h2', 'h3']:
            current_title = tag.get_text(strip=True).replace(" ", "_").replace(":", "").replace(".", "")
            sections[current_title] = {}
        elif tag.name == 'p' and current_title:
            paragraph_text = tag.get_text(strip=True)
            key = f"{current_title}_Content_{len(sections[current_title]) + 1}"
            sections[current_title][key] = paragraph_text
        elif tag.name == 'ul' and current_title:
            list_items = [li.get_text(strip=True) for li in tag.find_all('li')]
            key = f"{current_title}_List_{len(sections[current_title]) + 1}"
            sections[current_title][key] = list_items

    return sections

# Gọi hàm trích xuất với class cụ thể
div_class = "chakra-stack css-1uji4px"
structured_content = extract_content_from_div(soup, div_class)

# Lưu dữ liệu vào file JSON
output_filename = "privacy_policy_filtered.json"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(structured_content, f, ensure_ascii=False, indent=4)

print(f"Dữ liệu đã được cào và lưu thành công vào file '{output_filename}'")