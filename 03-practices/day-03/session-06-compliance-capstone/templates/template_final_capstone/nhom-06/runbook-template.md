# Runbook Template

## 1. Giới thiệu
Tài liệu này mô tả quy trình vận hành hệ thống **Project Assistant Simulation** cho **Nhóm 06**. Mục đích cung cấp các bước triển khai, giám sát và khắc phục sự cố khi đưa AI vào thực tiễn.

## 2. Môi trường triển khai
- **Hệ thống:** Windows 10/11, Python 3.11, virtualenv `.venv`
- **Mô hình LLM:** `qwen3.5:1.5b-instruct` (hoặc `gemma4:e2b`)
- **Dữ liệu mô phỏng:** `project_charter_mock.txt`, `project_progress_mock.csv`, `chat_logs_mock.json`
- **Thời gian cập nhật:** tháng 7/2026

## 3. Các bước khởi chạy
```bash
# Tạo và kích hoạt môi trường ảo
python -m venv .venv
.venv\Scripts\activate  # Windows

# Cài đặt phụ thuộc
pip install -r requirements.txt

# Chạy pipeline
python run_pipeline.py
```
- **run_pipeline.py** thực hiện:
  1. Load dữ liệu mô phỏng
  2. Khởi tạo LLM và thiết lập System Prompt (xem `core-prompt-design.md`)
  3. Cung cấp giao diện CLI cho PM để đặt câu hỏi
  4. Ghi log chi tiết vào `logs/run_YYYYMMDD.log`

## 4. Giám sát
- **Metrics:** thời gian trả lời, tỷ lệ đáp ứng (% câu hỏi có nguồn), lỗi runtime.
- **Logs:** `logs/` chứa file `run_*.log` và `error_*.log`.
- **Alert:** Nếu `error_*.log` xuất hiện, hệ thống gửi email tới `pm@nhom06.example.com`.

## 5. Xử lý lỗi thường gặp
| Mã lỗi | Mô tả | Hành động |
|---|---|---|
| 101 | Không tìm thấy dữ liệu mô phỏng | Kiểm tra đường dẫn `data/` và tên file |
| 102 | LLM trả về `None` | Kiểm tra kết nối mạng và model download |
| 103 | Lỗi parsing CSV | Kiểm tra định dạng CSV, bỏ ký tự đặc biệt |

## 6. Backup & Restore
```bash
# Sao lưu dữ liệu và logs
tar -czvf backup_nhom06_$(date +%Y%m%d).tar.gz data/ logs/
```
Để khôi phục, giải nén và chạy lại pipeline.

*All placeholders have been replaced with actual group name (Nhóm 06) and date (tháng 7/2026).*
