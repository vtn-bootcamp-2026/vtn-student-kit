---
mo-ta: "Biểu mẫu hướng dẫn vận hành công cụ NetBI-KARA cho đội ngũ kỹ thuật VTN"
trang-thai: active
phien-ban: v1.1
created-at: 2026-06-10 15:45 +07:00
updated-at: 2026-06-10 15:45 +07:00
---

# Hướng dẫn vận hành công cụ: NetBI KPI Auto-Reporter (Runbook)

*   **Mã tài liệu:** VTN-RB-KPI-01
*   **Người biên soạn:** Nhóm 01 - AI Builders Viettel Net
*   **Đơn vị phê duyệt:** Tổng Công ty Mạng lưới Viettel (Viettel Net)
*   **Phiên bản hệ thống áp dụng:** v1.0

---

## 1. Tổng quan hệ thống (System overview)

Tài liệu này hướng dẫn cài đặt, cấu hình, chạy thử và xử lý sự cố đối với **NetBI-KARA** - Công cụ cục bộ hỗ trợ tự động xử lý số liệu KPI mạng, phát hiện anomaly và sinh báo cáo nhận định kèm email dự thảo gửi KPI owners tại Trung tâm Điều hành Mạng (NOC) của Viettel Net.

---

## 2. Yêu cầu hệ thống và Chuẩn bị môi trường (Prerequisites)

### Yêu cầu phần cứng tối thiểu:
*   **RAM:** Tối thiểu 16 GB (Khuyến nghị 32 GB để chạy mượt mà mô hình 7B).
*   **CPU:** Tối thiểu 8 Cores.
*   **GPU:** Khuyến nghị có GPU NVIDIA (VRAM >= 8GB) để suy luận LLM nhanh dưới 10 giây.
*   **Ổ cứng trống:** Tối thiểu 15 GB SSD để lưu trữ cơ sở dữ liệu lịch sử và các tệp mô hình cục bộ.

### Yêu cầu phần mềm cài đặt sẵn:
1.  **Python:** Phiên bản 3.11 trở lên.
2.  **Ollama:** Trình quản lý mô hình ngôn ngữ lớn cục bộ chạy nền.
3.  **Mô hình cục bộ:** Đã tải sẵn bằng lệnh sau:
    ```powershell
    # Tải mô hình Qwen 7B chuyên về lý luận và tiếng Việt cực tốt:
    ollama pull qwen3.5:7b-instruct
    ```

---

## 3. Quy trình cài đặt chi tiết (Deployment steps)

### Bước 1: Thiết lập thư mục làm việc và Môi trường ảo Python
Mở PowerShell tại thư mục làm việc và chạy các lệnh sau để cô lập môi trường:

```powershell
# Tạo môi trường ảo Python
python -m venv .venv

# Kích hoạt môi trường ảo trên Windows
.venv\Scripts\Activate.ps1

# Nâng cấp pip lên bản mới nhất
python -m pip install --upgrade pip
```

### Bước 2: Cài đặt các thư viện phụ thuộc (Dependencies)
Cài đặt các gói thư viện Python cần thiết cho xử lý dữ liệu và kết nối API:

```powershell
# Cài đặt trực tiếp qua pip
pip install requests pandas openpyxl pydantic colorama
```

### Bước 3: Cấu hình các biến môi trường
Tạo file `.env` tại thư mục gốc của dự án và cấu hình các thông số kết nối:

```env
# Địa chỉ cổng máy chủ Ollama cục bộ
OLLAMA_API_URL=http://127.0.0.1:11434/api/generate

# Tên mô hình cục bộ sử dụng
LOCAL_MODEL_NAME=qwen3.5:7b-instruct

# Cấu hình ngưỡng cảnh báo lệch tiêu chuẩn (z-score) để phát hiện Anomaly
KPI_ANOMALY_THRESHOLD=2.5

# Cấu hình mức độ log
LOG_LEVEL=INFO
```

---

## 4. Hướng dẫn vận hành và Sử dụng (Execution guide)

### Khởi chạy công cụ ở chế độ dòng lệnh (CLI Mode):
Chạy script Python bằng lệnh dưới đây:

```powershell
python report_generator.py --input data/netbi_weekly_raw.xlsx --output outputs/report_week_24.json
```

### Các tham số tùy chọn hỗ trợ:
*   `--input`: Đường dẫn tới tệp tin Excel chứa 200 KPI xuất từ NetBI (bắt buộc).
*   `--output`: Đường dẫn lưu tệp JSON kết quả chứa báo cáo nháp và email soạn sẵn (bắt buộc).
*   `--model`: Ghi đè tên mô hình cấu hình trong file `.env`.
*   `--approve`: Tự động gửi email cảnh báo mà không cần giao diện duyệt (chỉ dùng cho môi trường tự động hóa hoàn toàn tin cậy).

---

## 5. Quy trình cấu hình và Cập nhật luật lọc dữ liệu (Rules configuration)

Có thể cấu hình các chỉ tiêu target cho từng KPI trong file cấu hình cục bộ `kpi_targets.json`. Dưới đây là cấu trúc khai báo:

```json
{
  "CELL_DROP_RATE": {
    "target": 1.5,
    "direction": "lower_is_better",
    "owner": "Nguyễn Văn An",
    "email": "annv5@viettel.com.vn"
  },
  "GPON_AVAILABILITY": {
    "target": 99.9,
    "direction": "higher_is_better",
    "owner": "Trần Văn Bình",
    "email": "binhtv12@viettel.com.vn"
  }
}
```

---

## 6. Xử lý nhật ký lỗi và Khắc phục sự cố (Troubleshooting)

### Các mã lỗi thường gặp và Giải pháp:

| Mã lỗi / Trạng thái | Nguyên nhân | Hướng khắc phục |
| :--- | :--- | :--- |
| **`ConnectionError: Failed to connect to Ollama`** | Máy chủ Ollama chưa được bật hoặc GPU bị quá tải dẫn đến crash service. | 1. Mở terminal mới chạy lệnh `ollama serve`. <br>2. Kiểm tra tài nguyên GPU bằng `nvidia-smi` để xem dung lượng VRAM còn trống. |
| **`ValueError: Excel file format is invalid`** | File kết xuất từ NetBI bị lỗi định dạng cấu trúc cột hoặc thiếu sheet dữ liệu KPI. | Kiểm tra xem file NetBI export có đúng định dạng .xlsx tiêu chuẩn không. Cần tải lại file từ hệ thống NetBI. |
| **`JSONDecodeError`** | Mô hình cục bộ phản hồi đầu ra không đúng định dạng JSON Schema cấu trúc. | 1. Sử dụng Prompt được cấu trúc tốt hơn.<br>2. Chuyển cấu hình sang mô hình lượng tử hóa nhẹ hơn để tiết kiệm bộ nhớ. |
| **`Out of Memory (OOM)`** | Máy tính bị tràn bộ nhớ GPU khi đang chạy mô hình suy luận. | Giải phóng bộ nhớ GPU bằng cách khởi động lại service Ollama: `Restart-Service -Name "Ollama"`. |

### Hướng dẫn kiểm tra nhật ký log:
Toàn bộ hoạt động và cảnh báo của hệ thống được lưu tự động vào tệp `logs/netbi_kara.log`. Đội ngũ vận hành có thể giám sát liên tục log bằng lệnh PowerShell sau:

```powershell
Get-Content -Path .\logs\netbi_kara.log -Wait -Tail 20
```
