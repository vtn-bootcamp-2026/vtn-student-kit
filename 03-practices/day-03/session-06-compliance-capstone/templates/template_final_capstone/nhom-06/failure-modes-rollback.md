# Failure Modes & Rollback

## 1. Các tình huống lỗi thường gặp
| Mã lỗi | Mô tả | Nguyên nhân tiềm năng | Hành động khắc phục |
|---|---|---|---|
| **F01** | Không tải được mô hình LLM | Mạng không ổn, model không có trong cache | Kiểm tra kết nối internet, chạy lại `pip install transformers` và tải lại model |
| **F02** | File dữ liệu mô phỏng không tồn tại | Đường dẫn sai hoặc file bị xóa | Kiểm tra thư mục `data/`, đảm bảo các file `project_charter_mock.txt`, `project_progress_mock.csv`, `chat_logs_mock.json` có mặt |
| **F03** | LLM trả về `None` hoặc rỗng | Prompt không đủ ngữ cảnh hoặc guardrail quá chặt | Kiểm tra System Prompt trong `core-prompt-design.md`, thử giảm mức guardrail để cho phép trả lời |
| **F04** | Lỗi parsing CSV | Dòng dữ liệu không khớp định dạng | Sửa file `project_progress_mock.csv` để tuân thủ chuẩn CSV (UTF‑8, dấu phẩy) |
| **F05** | Timeout khi truy vấn LLM | Thời gian tính toán quá lâu | Tăng timeout trong `run_pipeline.py` hoặc giảm kích thước chunk |

## 2. Kịch bản Rollback dự phòng
1. **Dừng pipeline** – Ngừng mọi tiến trình AI bằng cách nhấn `Ctrl+C` trong terminal.
2. **Khôi phục môi trường** – Xóa thư mục `__pycache__` và cài lại các phụ thuộc:
   ```bash
   rm -rf __pycache__
   pip install -r requirements.txt --force-reinstall
   ```
3. **Rollback dữ liệu** – Nếu dữ liệu đã bị thay đổi, khôi phục bản sao lưu `backup_nhom06_*.tar.gz` (tạo trong Runbook).
4. **Kiểm tra lại** – Chạy lại test suite (`pytest tests/`) để xác nhận mọi thành phần hoạt động.
5. **Báo cáo** – Ghi lại lỗi và biện pháp đã thực hiện trong `logs/rollback.log`.

*All placeholders have been replaced with actual group name (Nhóm 06) and date (tháng 7/2026).*
