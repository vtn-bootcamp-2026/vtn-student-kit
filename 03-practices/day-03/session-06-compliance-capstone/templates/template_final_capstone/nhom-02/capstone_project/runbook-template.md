---
mo-ta: "Hướng dẫn vận hành AI Agent tra cứu tài liệu kỹ thuật mạng lưới Viettel - chạy Local LLM offline"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Tài liệu sử dụng dữ liệu mô phỏng. Không chứa cấu hình mạng thật của VTN."
---

# Hướng dẫn vận hành công cụ: AI Agent Tra Cứu Tài Liệu Kỹ Thuật (Runbook)

*   **Mã tài liệu:** VTN-RB-NETDOC-01
*   **Người biên soạn:** [Tên nhóm thực hành — mô phỏng]
*   **Đơn vị phê duyệt:** Tổng Công ty Mạng lưới Viettel (Viettel Net)
*   **Phiên bản hệ thống áp dụng:** v1.0

---

## 1. Tổng quan hệ thống (System overview)

Tài liệu này hướng dẫn cài đặt, cấu hình, vận hành và xử lý sự cố **AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel (Network Doc Assistant)** — hệ thống hỏi đáp thông minh (RAG) chạy hoàn toàn cục bộ (offline/intranet) trên hạ tầng của Viettel Net, hỗ trợ kỹ sư tra cứu tài liệu kỹ thuật thiết bị, tham số cấu hình và quy hoạch mạng lưới qua giao diện chat web nội bộ.

> ⚠️ **Cam kết bảo mật cốt lõi:** Hệ thống này **tuyệt đối không kết nối Internet bên ngoài**. Mọi xử lý (Vector Search, LLM inference) đều thực hiện trên hạ tầng nội bộ VTN.

---

## 2. Yêu cầu hệ thống và Chuẩn bị môi trường (Prerequisites)

### Yêu cầu phần cứng tối thiểu (Server/Máy chủ):
*   **RAM:** Tối thiểu 16 GB (Khuyến nghị 32 GB để chạy mô hình chất lượng cao).
*   **CPU:** Tối thiểu 8 Cores.
*   **GPU (Tùy chọn):** GPU NVIDIA với VRAM >= 8 GB để tăng tốc inference đáng kể.
*   **Ổ cứng trống:** Tối thiểu 50 GB SSD (mã nguồn + VectorDB + file mô hình cục bộ).
*   **Mạng:** Chỉ kết nối mạng intranet nội bộ VTN — **không cấu hình kết nối Internet**.

### Yêu cầu phần mềm cài đặt sẵn:
1.  **Python:** Phiên bản 3.10 trở lên.
2.  **Ollama:** Trình quản lý Local LLM chạy nền — cài đặt từ gói nội bộ VTN (không download từ Internet trong môi trường production).
3.  **Mô hình cục bộ đã tải sẵn** (chọn phù hợp với cấu hình phần cứng):
    ```powershell
    # Option 1: Server RAM 16GB — Cân bằng chất lượng và hiệu năng
    ollama pull qwen3.5:7b-instruct

    # Option 2: Server RAM >= 32GB — Chất lượng cao hơn
    ollama pull qwen3.5:14b-instruct

    # Option 3: Tối ưu cho tiếng Việt và máy RAM 16GB
    ollama pull batiai/gemma4-e4b:q4
    ```
4.  **VectorDB cục bộ:** ChromaDB hoặc FAISS (cài đặt offline từ gói nội bộ).

---

## 3. Quy trình cài đặt chi tiết (Deployment steps)

### Bước 1: Thiết lập môi trường ảo Python
```powershell
# Di chuyển vào thư mục mã nguồn
cd C:\VTN\network-doc-assistant

# Tạo môi trường ảo Python
python -m venv .venv

# Kích hoạt môi trường ảo trên Windows
.venv\Scripts\Activate.ps1

# Cài đặt thư viện từ gói nội bộ (không dùng pip online)
pip install --no-index --find-links=.\offline-packages\ -r requirements.txt
```

### Bước 2: Cấu hình các biến môi trường
Tạo file `.env` tại thư mục gốc của dự án:

```env
# Địa chỉ máy chủ Ollama cục bộ (chỉ localhost - không mở ra ngoài)
OLLAMA_API_URL=http://127.0.0.1:11434/api/generate

# Tên mô hình Local LLM sử dụng
LOCAL_MODEL_NAME=qwen3.5:7b-instruct

# Ngưỡng độ tin cậy tối thiểu (dưới ngưỡng này hiển thị cảnh báo)
CONFIDENCE_THRESHOLD=0.70

# Đường dẫn Knowledge Base VectorDB
VECTORDB_PATH=.\knowledge-base\vectordb\

# Cấu hình log (INFO, WARNING, ERROR — không dùng DEBUG ở production)
LOG_LEVEL=INFO

# Thời gian tự động xóa session chat (giây)
SESSION_TTL_SECONDS=86400
```

### Bước 3: Khởi động hệ thống
```powershell
# Bước 3a: Đảm bảo Ollama đang chạy nền
ollama serve

# Bước 3b: Khởi động AI Agent (RAG backend)
python app.py --host 127.0.0.1 --port 8080

# Bước 3c: Truy cập giao diện chat web qua trình duyệt nội bộ
# http://[IP-SERVER-INTRANET]:8080
```

---

## 4. Quy trình vận hành Knowledge Base (KB Management)

### 4.1 Quy trình đưa tài liệu mới vào Knowledge Base

> ⚠️ **Bắt buộc:** Chỉ kỹ sư chuyên môn cao được phân quyền quản lý KB mới được thực hiện các bước dưới đây.

```powershell
# Bước 1: Kiểm tra phân loại bảo mật tài liệu
# Chỉ tài liệu nhãn "Công khai nội bộ" mới được tiếp tục

# Bước 2: Đặt tài liệu vào thư mục chờ kiểm duyệt
# Thư mục: .\knowledge-base\pending-review\

# Bước 3: Kỹ sư chuyên môn cao kiểm tra nội dung và ký xác nhận
# File: .\knowledge-base\kb-audit-log.xlsx (ghi: tên file, phiên bản, ngày, người duyệt)

# Bước 4: Chạy script index tài liệu vào VectorDB
python kb_manager.py --action add --file ".\knowledge-base\pending-review\TL-BTS-X200-v3.0.pdf" --version "v3.0" --approved-by "KS-CHUYEN-MON-X"

# Bước 5: Chạy bộ kiểm thử QA nhanh (10 câu hỏi mẫu)
python run_qa_test.py --mode quick

# Bước 6: Xác nhận kết quả kiểm thử trước khi đưa vào production
```

### 4.2 Lịch rà soát Knowledge Base định kỳ

| Chu kỳ | Hành động | Người thực hiện |
|---|---|---|
| Hàng tháng | Kiểm tra log báo cáo "Tài liệu có thể lỗi thời" từ người dùng | Kỹ sư quản lý KB |
| Hàng quý | Rà soát toàn bộ danh sách tài liệu trong KB, xác nhận phiên bản mới nhất | Kỹ sư chuyên môn cao |
| Theo sự kiện | Cập nhật ngay khi nhà cung cấp phát hành tài liệu kỹ thuật mới | Kỹ sư chuyên môn cao |
| 6 tháng/lần | Kiểm toán toàn bộ KB — loại bỏ tài liệu đã lỗi thời | Trưởng nhóm kỹ thuật |

---

## 5. Hướng dẫn vận hành và Sử dụng dành cho Kỹ sư (End-user Guide)

### Các nguyên tắc sử dụng an toàn:
*   ✅ **NÊN:** Đặt câu hỏi về thông tin kỹ thuật tổng quát từ tài liệu (tính năng, thông số, quy hoạch).
*   ✅ **NÊN:** Kiểm tra lại trích dẫn nguồn tài liệu kèm theo mọi câu trả lời.
*   ✅ **NÊN:** Báo cáo nếu thông tin có vẻ lỗi thời qua nút "🚩 Báo cáo".
*   ❌ **KHÔNG NÊN:** Nhập địa chỉ IP thực tế, tên hostname thiết bị đang vận hành, thông số cấu hình đang chạy vào ô chat.
*   ❌ **KHÔNG NÊN:** Áp dụng bất kỳ gợi ý cấu hình tham số nào từ AI mà không có phê duyệt của kỹ sư cấp cao.

### Ví dụ câu hỏi tốt (mô phỏng):
```
✅ "Tính năng handover của thiết bị BTS loại A là gì?"
✅ "Thông số RSRP khuyến nghị cho vùng phủ đô thị trong tài liệu quy hoạch là bao nhiêu?"
✅ "Bảng tham số RACH trong tài liệu hướng dẫn cấu hình LTE ở trang mấy?"
```

### Ví dụ câu hỏi cần tránh (mô phỏng):
```
❌ "Thiết bị tại địa điểm X đang dùng IP 10.x.x.x, tôi muốn thay đổi tham số Y"
❌ "Hệ thống đang chạy cấu hình Z, tôi có nên thay đổi không?"
```

---

## 6. Xử lý nhật ký lỗi và Khắc phục sự cố (Troubleshooting)

### Các mã lỗi thường gặp và Giải pháp:

| Mã lỗi / Trạng thái | Nguyên nhân | Hướng khắc phục |
| :--- | :--- | :--- |
| **`ConnectionError: Ollama không phản hồi`** | Máy chủ Ollama chưa bật hoặc bị tắt. | 1. Mở terminal chạy `ollama serve`.<br>2. Kiểm tra Ollama đang lắng nghe tại `127.0.0.1:11434`. |
| **`⚠️ Độ tin cậy thấp`** | Câu hỏi không có tài liệu liên quan trong KB hoặc KB chưa có tài liệu phù hợp. | 1. Kỹ sư liên hệ người quản lý KB để bổ sung tài liệu.<br>2. Tra cứu trực tiếp tài liệu gốc. |
| **`JSONDecodeError`** | Local LLM phản hồi không đúng định dạng JSON. | 1. Kiểm tra RAM server còn đủ.<br>2. Khởi động lại Ollama: `Restart-Service Ollama`. |
| **`Tài liệu có thể lỗi thời ⚠️`** | Tài liệu trong KB chưa được cập nhật hơn 6 tháng. | Báo cáo qua nút "🚩 Báo cáo" — Kỹ sư chuyên môn cao sẽ rà soát trong 5 ngày làm việc. |
| **`Out of Memory`** | RAM server bị tràn khi chạy inference LLM. | 1. Giải phóng RAM bằng cách tắt các tiến trình không cần thiết.<br>2. Chuyển sang mô hình nhẹ hơn trong `.env`. |

### Hướng dẫn kiểm tra nhật ký log (phi nhạy cảm):
```powershell
# Xem log hệ thống theo thời gian thực (chỉ ghi session_id, category, confidence — không ghi nội dung)
Get-Content -Path .\logs\network-doc-assistant.log -Wait -Tail 20
```
