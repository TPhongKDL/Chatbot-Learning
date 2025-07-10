# AI-Powered Q&A Chatbot for Web Content

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Một chatbot thông minh được xây dựng bằng Python, có khả năng tự động thu thập dữ liệu từ một trang web, xây dựng cơ sở tri thức và trả lời các câu hỏi của người dùng về nội dung đó với sự hỗ trợ đa ngôn ngữ.

## Mục lục

- [Giới thiệu](#giới-thiệu)
- [Tính năng chính](#tính-năng-chính)
- [Cách hoạt động](#cách-hoạt-động)
- [Công nghệ sử dụng](#công-nghệ-sử-dụng)
- [Cài đặt và Chạy thử](#cài-đặt-và-chạy-thử)
- [Cách sử dụng](#cách-sử-dụng)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Các hướng phát triển trong tương lai](#các-hướng-phát-triển-trong-tương-lai)
- [Giấy phép](#giấy-phép)

## Giới thiệu

Dự án này là một chatbot hỏi-đáp (Q&A) được thiết kế để đơn giản hóa việc tìm kiếm thông tin trong các tài liệu dài và phức tạp trên web, ví dụ như chính sách bảo mật, điều khoản dịch vụ, hoặc các bài viết chuyên ngành. Chatbot sẽ tự động "đọc" trang web, hiểu nội dung và cung cấp câu trả lời chính xác cho câu hỏi của người dùng, hỗ trợ nhiều ngôn ngữ khác nhau.

## Tính năng chính

- **Thu thập dữ liệu web tự động**: Sử dụng **Selenium** để truy cập các trang web động và lấy nội dung HTML.
- **Phân tích và cấu trúc hóa dữ liệu**: Dùng **BeautifulSoup** để bóc tách thông tin quan trọng (tiêu đề, đoạn văn) và lưu trữ dưới dạng file **JSON** có cấu trúc.
- **Hệ thống truy xuất thông tin thông minh**:
  - Áp dụng mô hình **TF-IDF** để biến văn bản thành vector.
  - Sử dụng **Cosine Similarity** để tìm ra đoạn văn bản phù hợp nhất với câu hỏi của người dùng.
- **Xử lý ngôn ngữ tự nhiên (NLP)**: Dùng **spaCy** để tiền xử lý văn bản (lemmatization, loại bỏ stop words) nhằm tăng độ chính xác.
- **Hỗ trợ đa ngôn ngữ**: Tích hợp **Google Translate API** để tự động dịch câu hỏi và câu trả lời, mang lại trải nghiệm liền mạch cho người dùng toàn cầu.
- **Giao diện dòng lệnh (CLI)**: Tương tác với chatbot một cách trực tiếp và đơn giản qua terminal.

## Cách hoạt động

Luồng xử lý của chatbot được thực hiện theo các bước sau:

```mermaid
graph TD
    A[Bắt đầu] --> B{Cung cấp URL};
    B --> C[1. Selenium: Tải nội dung trang web];
    C --> D[2. BeautifulSoup: Bóc tách & cấu trúc hóa dữ liệu];
    D --> E[3. Lưu vào file JSON (Cơ sở tri thức)];
    E --> F[4. Scikit-learn: Vector hóa cơ sở tri thức bằng TF-IDF];
    F --> G{Người dùng nhập câu hỏi};
    G --> H[5. Googletrans: Nhận diện ngôn ngữ & dịch sang tiếng Anh];
    H --> I[6. spaCy: Tiền xử lý câu hỏi];
    I --> J[7. Scikit-learn: Tính Cosine Similarity giữa câu hỏi và cơ sở tri thức];
    J --> K[8. Tìm ra câu trả lời phù hợp nhất];
    K --> L[9. Googletrans: Dịch câu trả lời về ngôn ngữ gốc];
    L --> M{Hiển thị câu trả lời};
    M --> G;
```

## Công nghệ sử dụng

- **Ngôn ngữ**: Python 3
- **Web Scraping**: Selenium, BeautifulSoup4
- **NLP & Machine Learning**: Scikit-learn, spaCy
- **Dịch thuật**: Googletrans
- **Xử lý dữ liệu**: JSON

## Cài đặt và Chạy thử

Làm theo các bước sau để chạy dự án trên máy của bạn.

### 1. Yêu cầu cần có

- Python 3.8+
- Trình duyệt Google Chrome
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) (Tải phiên bản phù hợp với phiên bản Chrome của bạn)

### 2. Các bước cài đặt

1.  **Clone repository này về máy:**
    ```bash
    git clone https://github.com/TPhongKDL/Chatbot-Learning.git
    cd Chatbot-Learning
    ```

2.  **Tạo và kích hoạt môi trường ảo (khuyến khích):**
    ```bash
    # Đối với Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Đối với macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Tải mô hình ngôn ngữ của spaCy:**
    ```bash
    python -m spacy download en_core_web_sm
    ```

5.  **Cấu hình đường dẫn ChromeDriver:**
    Mở file `your_script_name.py` và thay đổi đường dẫn đến file `chromedriver.exe` bạn vừa tải về:
    ```python
    # Thay đổi dòng này
    service = Service('C:\\path\\to\\your\\chromedriver.exe')
    ```

### 3. Chạy chương trình

Thực thi file Python chính để bắt đầu chatbot:
```bash
python your_script_name.py
```

## Cách sử dụng

Sau khi chương trình khởi chạy, chatbot sẽ tự động thu thập dữ liệu và xây dựng cơ sở tri thức. Sau đó, bạn có thể bắt đầu đặt câu hỏi.

**Ví dụ:**

```
Dữ liệu đã được lưu vào file privacy_policy_filtered.json
Chatbot: Hello! I support multiple languages. Ask me anything about the Privacy Policy.
You: What information do you collect?
Chatbot: We collect information you provide directly to us, such as when you create an account, fill out a form, or communicate with us. We may also collect information automatically, such as your IP address and browsing activity.

You: bạn có chia sẻ dữ liệu của tôi không?
Chatbot: (Translated Question: do you share my data?)
Chatbot: Chúng tôi không bán thông tin cá nhân của bạn cho bên thứ ba. Chúng tôi chỉ có thể chia sẻ thông tin với các nhà cung cấp dịch vụ đáng tin cậy giúp chúng tôi vận hành dịch vụ, hoặc khi pháp luật yêu cầu.

You: exit
Chatbot: Goodbye!
```

## Cấu trúc dự án

```
.
├── your_script_name.py          # File mã nguồn chính của chatbot
├── privacy_policy_filtered.json # File JSON được tạo ra để lưu cơ sở tri thức
├── requirements.txt             # Danh sách các thư viện Python cần thiết
└── README.md                    # File tài liệu hướng dẫn này
```

## Các hướng phát triển trong tương lai

- [ ] Xây dựng giao diện đồ họa (GUI) bằng Tkinter hoặc Streamlit.
- [ ] Đóng gói dự án bằng Docker để dễ dàng triển khai.
- [ ] Nâng cấp mô hình NLP bằng các mô hình Transformer (ví dụ: BERT) để cải thiện độ chính xác.
- [ ] Triển khai chatbot thành một web app sử dụng Flask hoặc FastAPI.
- [ ] Cải thiện khả năng xử lý lỗi và các trường hợp ngoại lệ.

## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.
