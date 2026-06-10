---
mo-ta: "Biểu mẫu hướng dẫn vận hành công cụ VTN HR Policy Assistant cho đội ngũ kỹ thuật"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 15:49 +07:00
updated-at: 2026-06-10 15:49 +07:00
---

# Hướng dẫn vận hành hệ thống: VTN HR Policy Assistant (Runbook)

*   **Mã tài liệu:** VTN-RB-HR-ASSIST-01
*   **Người biên soạn:** Nhóm học viên AI Builders - Nhóm 1 VTN
*   **Đơn vị phê duyệt:** Tổng Công ty Mạng lưới Viettel (Viettel Net)
*   **Phiên bản hệ thống áp dụng:** v1.0

---

## 1. Tổng quan hệ thống (System overview)

Tài liệu này hướng dẫn cài đặt, cấu hình, chạy thử và xử lý sự cố đối với **VTN HR Policy Assistant** - Trợ lý AI chạy offline hoàn toàn để tự động hóa giải đáp các thắc mắc về chính sách nhân sự, quy chế làm việc tại Viettel Net dựa trên công nghệ RAG (Retrieval-Augmented Generation) và mô hình ngôn ngữ lớn cục bộ.

---

## 2. Yêu cầu hệ thống và Chuẩn bị môi trường (Prerequisites)

### Yêu cầu phần cứng tối thiểu:
*   **RAM:** Tối thiểu 8 GB (Khuyến nghị 16 GB trở lên để chạy mượt mà).
*   **CPU:** Tối thiểu 4 Cores.
*   **Ổ cứng trống:** Tối thiểu 12 GB SSD để lưu trữ mã nguồn, cơ sở dữ liệu vector và mô hình cục bộ.

### Yêu cầu phần mềm cài đặt sẵn:
1.  **Python:** Phiên bản 3.10 trở lên.
2.  **Ollama:** Trình quản lý và chạy mô hình ngôn ngữ lớn cục bộ (Background Service).
3.  **Mô hình cục bộ:** Đã được tải sẵn về máy chủ bằng một trong các lệnh sau:
    ```powershell
    # Dành cho máy RAM 8GB (Siêu nhẹ)
    ollama pull qwen3.5:1.5b-instruct
    # HOẶC bản gemma4 siêu nhẹ (4GB) tối ưu tiếng Việt:
    ollama pull batiai/gemma4-e2b:q4

    # Dành cho máy RAM >= 16GB (Khuyến nghị cho server nội bộ)
    ollama pull qwen3.5:7b-instruct
    ```

---

## 3. Quy trình cài đặt chi tiết (Deployment steps)

### Bước 1: Thiết lập thư mục làm việc và Môi trường ảo Python
Mở PowerShell tại thư mục chứa mã nguồn dự án và chạy các lệnh sau để kích hoạt môi trường cô lập:

```powershell
# Tạo môi trường ảo Python
python -m venv .venv

# Kích hoạt môi trường ảo trên Windows
.venv\Scripts\Activate.ps1

# Nâng cấp pip lên bản mới nhất
python -m pip install --upgrade pip
```

### Bước 2: Cài đặt các thư viện phụ thuộc (Dependencies)
Cài đặt các gói thư viện Python cần thiết phục vụ cho RAG Pipeline và kết nối mô hình:

```powershell
# Cài đặt trực tiếp qua pip các thư viện cần thiết
pip install requests pydantic colorama chromadb sentence-transformers
```

### Bước 3: Cấu hình các biến môi trường
Tạo file `.env` tại thư mục gốc của dự án và cấu hình các thông số kết nối:

```env
# Địa chỉ API của máy chủ Ollama cục bộ
OLLAMA_API_URL=http://127.0.0.1:11434/api/generate

# Tên mô hình ngôn ngữ lớn cục bộ sử dụng
LOCAL_MODEL_NAME=gemma4-e2b:q4

# Đường dẫn tới thư mục lưu trữ Vector DB chính sách
VECTOR_DB_PATH=./data/vector_db

# Cấu hình mức độ log hiển thị (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO
```

---

## 4. Hướng dẫn vận hành và Sử dụng (Execution guide)

### Khởi chạy công cụ ở chế độ dòng lệnh (CLI Interactive):
Chạy script Python bằng lệnh dưới đây để nạp tài liệu chính sách và khởi chạy chatbot hỏi đáp:

```powershell
python hr_assistant.py --db-path ./data/vector_db --interactive
```

### Các tham số tùy chọn hỗ trợ:
*   `--db-path`: Đường dẫn tới thư mục lưu Vector DB (mặc định lấy từ `.env`).
*   `--update-docs`: Chỉ định đường dẫn tới thư mục chứa file PDF/Word chính sách mới để hệ thống tự động cập nhật lập chỉ mục vào Vector DB.
*   `--model`: Ghi đè tên mô hình cấu hình trong file `.env` (ví dụ: `--model qwen3.5:7b-instruct`).

---

## 5. Cấu hình và Cập nhật cơ sở dữ liệu chính sách (Rules & Docs Indexing)

Hệ thống hỗ trợ tự động cắt nhỏ văn bản và cập nhật Vector DB. Để thêm tài liệu quy chế mới, hãy đặt tệp tin vào thư mục `./data/documents/` và chạy lệnh sau để cập nhật cơ sở dữ liệu tri thức:

```powershell
python hr_assistant.py --update-docs ./data/documents/
```

---

## 6. Xử lý nhật ký lỗi và Khắc phục sự cố (Troubleshooting)

### Các mã lỗi thường gặp và Giải pháp:

| Mã lỗi / Trạng thái | Nguyên nhân | Hướng khắc phục |
| :--- | :--- | :--- |
| **`ConnectionError: Failed to connect to Ollama`** | Dịch vụ Ollama chưa được khởi động hoặc cổng 11434 bị tường lửa chặn. | 1. Mở cửa sổ cmd mới chạy lệnh `ollama serve`. <br>2. Kiểm tra xem Ollama có phản hồi tại cổng 11434 bằng cách gõ `curl http://localhost:11434` trên trình duyệt. |
| **`VectorDBNotFoundError`** | Cơ sở dữ liệu Vector chưa được khởi tạo hoặc chỉ định sai đường dẫn. | Chạy lệnh `--update-docs` trỏ đến thư mục chứa các văn bản chính sách để hệ thống tiến hành lập chỉ mục ban đầu. |
| **`JSONDecodeError`** | LLM cục bộ bị tràn bộ nhớ dẫn đến phản hồi bị đứt đoạn hoặc sai cấu trúc JSON. | 1. Đổi tên mô hình sang bản nhẹ hơn trong tệp `.env` (ví dụ: `qwen3.5:1.5b-instruct`). <br>2. Giải phóng dung lượng RAM máy tính, tắt bớt các ứng dụng chạy ngầm nặng. |

### Hướng dẫn kiểm tra nhật ký log:
Mọi hoạt động và cảnh báo bảo mật được ghi tự động vào file `logs/hr_assistant.log`. Để theo dõi log thời gian thực trên Windows PowerShell, sử dụng lệnh:

```powershell
Get-Content -Path .\logs\hr_assistant.log -Wait -Tail 20
```
