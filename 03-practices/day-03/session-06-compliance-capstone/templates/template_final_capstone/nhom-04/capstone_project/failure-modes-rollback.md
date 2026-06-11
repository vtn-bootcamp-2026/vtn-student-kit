---
mo-ta: "Biểu mẫu phân tích các tình huống lỗi và phương án khôi phục/dự phòng cho VTN HR Policy Assistant"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 15:50 +07:00
updated-at: 2026-06-10 15:50 +07:00
---

# Phân tích tình huống lỗi và Phương án ứng phó (Failure modes & Rollback/Fallback)

*   **Tên công cụ/dự án:** Trợ lý AI tra cứu chính sách nhân sự nội bộ (VTN HR Policy Assistant)
*   **Nhóm chịu trách nhiệm:** Nhóm học viên AI Builders - Nhóm 1 VTN
*   **Ngày cập nhật cuối cùng:** 10/06/2026

---

## 1. Định nghĩa và Mục đích

Tài liệu này phân tích các tình huống lỗi kỹ thuật (Failure modes) có thể phát sinh trong quá trình vận hành **VTN HR Policy Assistant** và định nghĩa các phương án ứng phó khẩn cấp (Rollback/Fallback) nhằm bảo vệ tính liên tục của nghiệp vụ và an toàn dữ liệu tại Viettel Net.

---

## 2. Bảng phân tích các tình huống lỗi kỹ thuật (Failure modes analysis)

### Tình huống lỗi 1: Mất kết nối tới máy chủ mô hình Ollama hoặc Vector DB (Connection failure)
*   **Mô tả sự cố:** Hệ thống không thể kết nối tới cổng API của Ollama hoặc Vector Database bị khóa do phân quyền lỗi.
*   **Mức độ nghiêm trọng (S):** Cao (Hệ thống ngừng hoạt động hoàn toàn).
*   **Tác động kinh doanh:** CBNV không thể tra cứu được chính sách nhân sự, gây dồn ứ các cuộc gọi thắc mắc lên phòng HR.
*   **Phương án Fallback dự phòng lập tức:**
    *   *Bước 1:* Khối code RAG Pipeline bắt ngoại lệ `try-except` đối với các kết nối API và truy xuất cơ sở dữ liệu.
    *   *Bước 2:* Nếu phát hiện mất kết nối, hệ thống tự động chuyển sang chế độ **"Graceful Degradation Mode"** (Chế độ dự phòng lỗi).
    *   *Bước 3:* Trả về thông báo xin lỗi người dùng trên giao diện chatbot: *"Hệ thống tra cứu tự động đang bảo trì. Vui lòng gửi câu hỏi trực tiếp qua email của Phòng Tổ chức Lao động: hr-support@viettel.com.vn để được cán bộ hỗ trợ ngay lập tức."* Đồng thời ghi nhận mã lỗi chi tiết vào log hệ thống.

---

### Tình huống lỗi 2: Tràn bộ nhớ RAM máy chủ gây sập tiến trình (OOM Error)
*   **Mô tả sự cố:** Khi nhiều CBNV truy cập cùng lúc hoặc người dùng gửi câu hỏi quá dài vượt quá ngữ cảnh cho phép, tiến trình suy luận của LLM chiếm dụng 100% RAM dẫn đến hệ điều hành tự động tắt dịch vụ Ollama.
*   **Mức độ nghiêm trọng (S):** Cao (Sập dịch vụ máy chủ).
*   **Tác động kinh doanh:** Dịch vụ chatbot bị gián đoạn đối với toàn bộ người dùng trong mạng nội bộ.
*   **Phương án ứng phó và Fallback:**
    *   *Bước 1 (Giới hạn tài nguyên):* Cấu hình giới hạn độ dài câu hỏi nhập vào tối đa không quá 1.000 ký tự.
    *   *Bước 2 (Tự động khởi động lại):* Thiết lập script giám sát dịch vụ (Systemd trên Linux hoặc Windows Service Manager) để tự động khởi động lại dịch vụ Ollama trong vòng 10 giây nếu phát hiện tiến trình bị tắt đột ngột.
    *   *Bước 3 (Chuyển đổi cấu hình):* Nếu sập RAM xảy ra liên tục (> 3 lần/giờ), hệ thống tự động chuyển cấu hình sang sử dụng mô hình siêu nhẹ `qwen3.5:1.5b-instruct` thay thế cho mô hình lớn hơn.

---

### Tình huống lỗi 3: AI bịa đặt thông tin chính sách hoặc rò rỉ thông tin cá nhân (Hallucination / Data leak)
*   **Mô tả sự cố:** LLM tổng hợp thông tin sai so với quy định thực tế của VTN hoặc vô tình để lộ thông tin nhạy cảm của CBNV khác do lỗi ngữ cảnh.
*   **Mức độ nghiêm trọng (S):** Cực kỳ nghiêm trọng (Critical - Vi phạm nghiêm trọng Nghị định 356/2025/NĐ-CP).
*   **Tác động kinh doanh:** Rủi ro pháp lý cao, gây hiểu nhầm về chính sách của tập đoàn, ảnh hưởng uy tín nội bộ.
*   **Phương án kiểm soát và Khắc phục (Rollback/HITL):**
    *   *Bước 1:* Bắt buộc áp dụng cơ chế đánh dấu cờ `needs_human_review = True` đối với các câu trả lời liên quan đến số tiền hỗ trợ vượt định mức hoặc các trường hợp đặc biệt không được định nghĩa rõ ràng.
    *   *Bước 2 (Thu hồi & Hiệu chỉnh):* Khi phát hiện AI trả về thông tin sai lệch đã gửi cho người dùng, cán bộ HR truy cập bảng quản trị Admin, thu hồi tin nhắn lỗi trên MS Teams và cập nhật prompt hệ thống hoặc hiệu chỉnh trực tiếp các chunk văn bản bị sai lệch trong Vector DB.

---

## 3. Quy trình khôi phục phiên bản ổn định gần nhất (Rollback runbook)

Khi phiên bản nâng cấp gặp lỗi bảo mật hoặc sập hệ thống liên tiếp mà không thể khắc phục nhanh, kỹ thuật viên thực hiện các bước rollback sau:

```powershell
# Bước 1: Di chuyển phiên bản lỗi hiện tại vào thư mục tạm
mv .\hr_assistant.py .\logs\hr_assistant_failed_v1.1.py

# Bước 2: Checkout khôi phục phiên bản mã nguồn ổn định từ Git
git checkout HEAD -- .\hr_assistant.py

# Bước 3: Khởi động lại dịch vụ Ollama cục bộ để giải phóng RAM giải tỏa nghẽn
Restart-Service -Name "Ollama"

# Bước 4: Chạy thử lại bộ 10 ca kiểm thử (TC-01 đến TC-10) để xác nhận hệ thống hoạt động ổn định trở lại
python hr_assistant.py --test-suite
```
