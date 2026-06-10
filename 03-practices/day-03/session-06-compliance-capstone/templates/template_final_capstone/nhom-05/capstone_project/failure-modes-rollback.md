---
mo-ta: "Biểu mẫu phân tích các tình huống lỗi và phương án khôi phục/dự phòng cho hệ thống NetBI-KARA"
trang-thai: active
phien-ban: v1.2
created-at: 2026-06-10 15:45 +07:00
updated-at: 2026-06-10 15:45 +07:00
---

# Phân tích tình huống lỗi và Phương án ứng phó (Failure modes & Rollback/Fallback)

*   **Tên công cụ/dự án:** Hệ thống Tự động hóa Báo cáo & Phân tích Anomaly KPI NetBI (NetBI-KARA)
*   **Nhóm chịu trách nhiệm:** Nhóm 01
*   **Ngày cập nhật cuối cùng:** 10/06/2026

---

## 1. Định nghĩa và Mục đích

Bảng phân tích các tình huống lỗi (Failure modes) và phương án ứng phó (Rollback/Fallback) giúp đội ngũ vận hành kỹ thuật tại **Viettel Net** chủ động kiểm soát rủi ro, duy trì tính ổn định của hệ thống giám sát KPI mạng lưới ngay cả khi gặp sự cố phần cứng, phần mềm hoặc bị tấn công mạng.

---

## 2. Bảng phân tích các tình huống lỗi kỹ thuật (Failure modes analysis)

Dưới đây là các kịch bản lỗi hệ thống phát sinh trong quá trình vận hành thực tế và giải pháp xử lý tương ứng:

### Tình huống lỗi 1: Mất kết nối tới máy chủ mô hình cục bộ (Local LLM connection failure)
*   **Mô tả sự cố:** Script chạy nhưng không kết nối được tới service Ollama (cổng 11434) trên server GPU, gây dừng luồng sinh báo cáo.
*   **Mức độ nghiêm trọng (S):** Cao (Hệ thống ngưng hoạt động phần tính năng thông minh).
*   **Tác động kinh doanh:** Không thể sinh báo cáo nhận định tự động bằng văn bản tiếng Việt và không soạn thảo được email cảnh báo.
*   **Phương án Fallback dự phòng lập tức:**
    *   *Bước 1:* Bắt ngoại lệ `ConnectionError` trong module kết nối Ollama API.
    *   *Bước 2:* Tự động chuyển đổi sang chế độ **"Pandas Fallback Mode"**: Chỉ xuất ra file Excel/HTML chứa danh sách bảng số liệu KPI vi phạm tĩnh, không kèm theo văn bản tóm tắt và email nháp.
    *   *Bước 3:* Hiển thị cảnh báo trên Web UI: `[WARNING: LOCAL LLM OFFLINE - RUNNING IN PANDAS FALLBACK MODE]`.

---

### Tình huống lỗi 2: Tràn bộ nhớ VRAM GPU khi chạy đồng thời nhiều tiến trình suy luận (GPU Out of memory - OOM)
*   **Mô tả sự cố:** Khi nạp dữ liệu lớn hoặc máy chủ chạy song song nhiều tác vụ phân tích, bộ nhớ VRAM của GPU bị tràn, làm treo tiến trình suy luận của Ollama.
*   **Mức độ nghiêm trọng (S):** Cao (Làm treo cứng dịch vụ Ollama).
*   **Tác động kinh doanh:** Báo cáo bị kẹt ở trạng thái đang xử lý, không thể hoàn thành báo cáo đúng hạn.
*   **Phương án ứng phó và Fallback:**
    *   *Bước 1 (Giới hạn đầu vào):* Thiết lập cấu hình đầu vào chỉ gửi tối đa 30 KPI suy giảm nghiêm trọng nhất sang LLM phân tích, tránh quá tải cửa sổ ngữ cảnh.
    *   *Bước 2 (Chuyển đổi GPU sang CPU):* Cấu hình Ollama tự động chuyển một phần luồng tính toán sang RAM/CPU thông qua tham số `num_thread` để tránh crash dịch vụ khi VRAM bị nghẽn.

---

### Tình huống lỗi 3: AI phân tích sai lệch xu hướng hoặc soạn thảo email gửi nhầm owner
*   **Mô tả sự cố:** Do dữ liệu đầu vào bị nhiễu hoặc mô hình bị ảo giác (hallucination), AI viết nhận định sai lệch về KPI mạng hoặc gán nhầm email liên hệ của KPI owner.
*   **Mức độ nghiêm trọng (S):** Nghiêm trọng (Gửi thông tin cảnh báo sai lệch ảnh hưởng uy tín và gây hoang mang cho các đơn vị).
*   **Tác động kinh doanh:** Mất thời gian xác minh lại, làm trễ tiến độ xử lý sự cố.
*   **Phương án kiểm soát và Khắc phục (Rollback/HITL):**
    *   *Bước 1 (Cơ chế duyệt HITL):* Thiết lập cơ chế khóa mặc định: Không tự động gửi email. Mọi email dự thảo bắt buộc phải được kỹ sư NOC nhấn nút phê duyệt trên giao diện Web UI trước khi chuyển tiếp đến hệ thống Exchange.
    *   *Bước 2 (Chỉnh sửa trực tiếp):* Cho phép kỹ sư NOC bấm vào nút "Edit" trên giao diện để ghi đè lại nội dung thư và email người nhận trước khi duyệt.

---

## 3. Quy trình khôi phục phiên bản mã nguồn cũ (Rollback runbook)

Khi phát hiện phiên bản cập nhật mới của NetBI-KARA gặp lỗi nghiêm trọng (ví dụ lỗi bảo mật, sập hệ thống liên tục), đội ngũ kỹ thuật thực hiện quy trình Rollback phiên bản theo các bước sau:

```powershell
# Bước 1: Di chuyển phiên bản lỗi hiện tại vào thư mục lưu trữ sự cố để phân tích sau
mv .\report_generator.py .\logs\report_generator_failed_v1.2.py

# Bước 2: Khôi phục phiên bản ổn định gần nhất từ Git
git checkout HEAD -- .\report_generator.py

# Bước 3: Khởi động lại dịch vụ Ollama cục bộ để giải phóng hoàn toàn VRAM bị treo
Restart-Service -Name "Ollama"

# Bước 4: Chạy thử lại bộ 10 ca kiểm thử (TC-01 đến TC-10) để xác nhận hệ thống đã hoạt động bình thường
python report_generator.py --input .\synthetic-data\netbi-sample-test.xlsx --output .\outputs\test-result.json
```
