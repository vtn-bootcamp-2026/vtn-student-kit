---
mo-ta: "Phân tích tình huống lỗi và phương án ứng phó cho AI Agent tra cứu tài liệu kỹ thuật mạng lưới Viettel"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Tài liệu sử dụng dữ liệu mô phỏng. Không chứa thông tin thật hoặc cấu hình mạng thật của VTN."
---

# Phân tích tình huống lỗi và Phương án ứng phó (Failure modes & Rollback/Fallback)

*   **Tên công cụ/dự án:** AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel (Network Doc Assistant)
*   **Nhóm chịu trách nhiệm:** [Tên nhóm thực hành — mô phỏng]
*   **Ngày cập nhật cuối cùng:** 10/06/2026

---

## 1. Định nghĩa và Mục đích

Bảng phân tích các tình huống lỗi (Failure modes) và phương án ứng phó (Rollback/Fallback) giúp đội ngũ vận hành kỹ thuật tại **Viettel Net** chủ động kiểm soát rủi ro, duy trì tính ổn định của hệ thống và đảm bảo chất lượng thông tin tra cứu ngay cả khi gặp sự cố kỹ thuật hoặc sự cố về chất lượng tri thức.

---

## 2. Bảng phân tích các tình huống lỗi kỹ thuật (Failure modes analysis)

### Tình huống lỗi 1: Mất kết nối Local LLM (Local LLM connection failure)
*   **Mô tả sự cố:** Hệ thống RAG không kết nối được tới máy chủ Local LLM (Ollama) đang chạy nền, khiến bước tổng hợp câu trả lời bị dừng lại.
*   **Mức độ nghiêm trọng (S):** Cao — Người dùng không nhận được câu trả lời tổng hợp từ AI.
*   **Tác động kinh doanh:** Kỹ sư phải quay lại tra cứu thủ công trong tài liệu PDF/Word — mất đi lợi ích tiết kiệm thời gian chính của hệ thống.
*   **Phương án Fallback dự phòng lập tức:**
    *   *Bước 1:* Hệ thống bắt lỗi `ConnectionError` và hiển thị thông báo thân thiện: `[THÔNG BÁO: Máy chủ AI tạm thời không phản hồi. Đang chuyển sang chế độ tìm kiếm nhanh từ khóa]`.
    *   *Bước 2:* Tự động chuyển sang chế độ **"Fallback Keyword Search"** — chỉ tìm kiếm và trả về các đoạn tài liệu liên quan nhất mà không có bước tổng hợp LLM. Kỹ sư tự đọc đoạn tài liệu gốc.
    *   *Bước 3:* Ghi log sự cố vào file log hệ thống để người quản trị xử lý.

---

### Tình huống lỗi 2: AI trả lời sai lệch thông tin kỹ thuật — Hallucination
*   **Mô tả sự cố:** Local LLM tổng hợp câu trả lời không có căn cứ trong tài liệu nguồn, hoặc pha trộn thông tin từ nhiều tài liệu không liên quan dẫn đến câu trả lời sai.
*   **Mức độ nghiêm trọng (S):** Cực kỳ nghiêm trọng — Kỹ sư có thể áp dụng thông số kỹ thuật sai gây cấu hình lỗi thiết bị.
*   **Tác động kinh doanh:** Ảnh hưởng chất lượng mạng nếu thông số sai được áp dụng vào thiết bị thực.
*   **Phương án kiểm soát và Khắc phục (Rollback/HITL):**
    *   *Bước 1 (Phòng ngừa kỹ thuật):* Bắt buộc hiển thị trích dẫn nguồn tài liệu kèm mọi câu trả lời. Nếu AI không tìm được nguồn → hiển thị "Không tìm thấy nguồn xác thực" thay vì bịa đặt.
    *   *Bước 2 (HITL bắt buộc):* Mọi câu trả lời liên quan đến gợi ý cấu hình tham số mạng đều bắt buộc kỹ sư cấp cao xem xét và ký xác nhận phiếu kiểm tra trước khi áp dụng.
    *   *Bước 3 (Rollback tri thức):* Nếu phát hiện KB có tài liệu cũ hoặc sai → người quản lý KB kích hoạt quy trình rà soát khẩn cấp, cập nhật hoặc loại bỏ tài liệu lỗi khỏi hệ thống.
    *   *Bước 4 (Phản hồi cải thiện):* Kỹ sư báo cáo câu trả lời sai qua nút "🚩 Báo cáo thông tin không chính xác" → đưa vào hàng đợi rà soát KB.

---

### Tình huống lỗi 3: Knowledge Base lỗi thời — Tài liệu không được cập nhật kịp thời
*   **Mô tả sự cố:** Nhà cung cấp thiết bị phát hành phiên bản tài liệu kỹ thuật mới với thay đổi quan trọng về tham số. Knowledge Base vẫn chứa tài liệu phiên bản cũ → AI trả lời theo thông số đã lỗi thời.
*   **Mức độ nghiêm trọng (S):** Cao — Kỹ sư có thể áp dụng thông số không còn phù hợp.
*   **Tác động kinh doanh:** Giảm hiệu quả mạng lưới hoặc không tương thích với thiết bị phiên bản mới.
*   **Phương án ứng phó và Fallback:**
    *   *Bước 1 (Metadata phiên bản):* Mỗi tài liệu trong KB có trường `updated_at` và `version`. Hệ thống tự động cảnh báo "⚠️ Tài liệu này chưa được cập nhật trong 6 tháng" khi hiển thị trích dẫn.
    *   *Bước 2 (Quy trình cập nhật định kỳ):* Kỹ sư chuyên môn cao rà soát và cập nhật tài liệu KB tối thiểu **hàng quý** hoặc ngay sau khi nhà cung cấp phát hành tài liệu mới.
    *   *Bước 3 (Cơ chế báo cáo nhanh):* Kỹ sư có thể báo cáo "Tài liệu có thể lỗi thời" ngay trong giao diện chat → người quản lý KB nhận thông báo và xử lý trong vòng 5 ngày làm việc.

---

### Tình huống lỗi 4: Câu hỏi người dùng chứa thông tin cấu hình mạng thực tế
*   **Mô tả sự cố:** Kỹ sư vô tình nhập địa chỉ IP, tên hostname thiết bị đang vận hành hoặc thông số cấu hình thực tế vào ô chat → thông tin này có thể bị ghi vào log hệ thống.
*   **Mức độ nghiêm trọng (S):** Cao — Rủi ro tiết lộ cấu hình hạ tầng mạng nội bộ.
*   **Tác động kinh doanh:** Vi phạm quy chế bảo mật thông tin nội bộ của Viettel Net.
*   **Phương án kiểm soát và Fallback:**
    *   *Bước 1 (Input Validation):* Bộ lọc Regex quét câu hỏi trước khi xử lý, phát hiện địa chỉ IP, yêu cầu người dùng chỉnh sửa.
    *   *Bước 2 (Sanitized Logging):* Hệ thống KHÔNG ghi nội dung câu hỏi đầy đủ vào log — chỉ ghi `category`, `timestamp`, `confidence_score`.
    *   *Bước 3 (Xóa tự động):* Lịch sử phiên chat tạm thời bị xóa tự động sau 24 giờ.

---

## 3. Quy trình khôi phục Knowledge Base (KB Rollback Runbook)

Khi phát hiện tài liệu sai hoặc lỗi thời trong Knowledge Base, người quản lý KB thực hiện quy trình sau:

```powershell
# Bước 1: Xác định tài liệu cần thu hồi hoặc cập nhật
# Ghi nhận: tên file, phiên bản hiện tại, lý do thu hồi

# Bước 2: Tạm thời đánh dấu tài liệu là "Suspended" (không cho AI truy cập)
# Thực hiện trong giao diện quản lý KB của người quản trị
# Ví dụ lệnh vector DB (mô phỏng):
# vectordb.update_metadata(doc_id="DOC-BTS-X200-v2.1", status="suspended")

# Bước 3: Cập nhật hoặc thay thế bằng tài liệu mới đã được kỹ sư chuyên môn cao phê duyệt
# Người có thẩm quyền ký xác nhận phiếu kiểm duyệt tài liệu mới

# Bước 4: Re-index tài liệu mới vào Knowledge Base
# vectordb.add_document(file="new_doc_v3.0.pdf", metadata={version: "v3.0", approved_by: "KS-CHUYEN-MON-CAO"})

# Bước 5: Chạy bộ kiểm thử nhanh (5 câu hỏi mẫu) để xác nhận tài liệu mới hoạt động đúng
# python run_qa_test.py --doc "new_doc_v3.0"

# Bước 6: Ghi biên bản cập nhật KB vào sổ theo dõi (KB audit log)
# Ghi: ngày cập nhật, tài liệu thay thế, người phê duyệt, lý do thay thế
```

---

## 4. Ma trận Mức độ ưu tiên xử lý lỗi

| Tình huống lỗi | Nghiêm trọng | Tần suất | Ưu tiên | Chủ thể xử lý |
|---|---|---|---|---|
| AI hallucinate thông số kỹ thuật | Rất cao | Trung bình | 🔴 Khẩn cấp | HITL bắt buộc + Kỹ sư cấp cao |
| Tài liệu KB lỗi thời | Cao | Cao (định kỳ) | 🔴 Cao | Kỹ sư chuyên môn cao (theo lịch định kỳ) |
| Mất kết nối Local LLM | Cao | Thấp | 🟠 Trung bình | Người quản trị hệ thống + Fallback tự động |
| Câu hỏi chứa thông tin nhạy cảm | Cao | Thấp | 🟠 Trung bình | Bộ lọc tự động + Cảnh báo người dùng |
