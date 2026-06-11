---
mo-ta: "Kế hoạch hành động 30/90 ngày triển khai AI Agent tra cứu tài liệu kỹ thuật mạng lưới Viettel"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Tài liệu sử dụng dữ liệu mô phỏng. Không chứa thông tin thật hoặc dữ liệu nhạy cảm của VTN."
---

# Kế hoạch hành động 30/90 ngày áp dụng AI tại đơn vị (Action plan)

*   **Tên nhóm thực hiện:** [Tên nhóm thực hành — mô phỏng]
*   **Đơn vị áp dụng:** Trung tâm Vận hành Khai thác Mạng / Phòng Quy hoạch Mạng lưới Viettel Net
*   **Người chịu trách nhiệm chính:** [Tên trưởng nhóm — mô phỏng]
*   **Phiên bản tài liệu:** v1.0

---

## 1. Mục tiêu kế hoạch hành động

Bản kế hoạch hành động này thiết lập lộ trình cụ thể để hiện thực hóa **AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel (Network Doc Assistant)** từ giai đoạn thí điểm nội bộ đến giai đoạn vận hành chính thức, với hai giai đoạn:

*   **30 ngày đầu tiên:** Thí điểm nội bộ quy mô nhỏ — xây dựng nền tảng Knowledge Base mô phỏng, triển khai cơ sở hạ tầng offline, thử nghiệm với nhóm kỹ sư nòng cốt.
*   **90 ngày tiếp theo:** Tinh chỉnh, chuẩn hóa quy trình vận hành KB định kỳ, mở rộng quy mô và đề xuất nhân rộng.

---

## 2. Lộ trình hành động chi tiết (Milestone roadmaps)

### Giai đoạn 30 ngày đầu: Thí điểm nội bộ và Xây dựng nền tảng (Days 1 - 30)
*Mục tiêu: Triển khai hệ thống với Knowledge Base mô phỏng, thử nghiệm với 05 kỹ sư nòng cốt, thu thập phản hồi thực tế.*

*   - [ ] **Mốc 1 (Ngày 1 - 7): Xây dựng Knowledge Base mô phỏng và hạ tầng offline**
    *   *Nội dung:*
        *   Phân loại và chuẩn bị bộ tài liệu kỹ thuật mô phỏng (không dùng tài liệu thật trong giai đoạn thí điểm nội bộ): hướng dẫn thiết bị, bảng tham số, quy hoạch — định dạng PDF/DOCX.
        *   Kỹ sư chuyên môn cao kiểm duyệt và ký xác nhận danh sách tài liệu đưa vào KB.
        *   Cài đặt môi trường: Python, Ollama, VectorDB cục bộ (ChromaDB/FAISS) trên máy chủ nội bộ — **không kết nối Internet**.
        *   Tải và cấu hình mô hình Local LLM phù hợp (qwen3.5:7b-instruct hoặc tương đương).
        *   Vector hóa bộ tài liệu mô phỏng vào Knowledge Base.
    *   *Người chịu trách nhiệm:* Kỹ sư phụ trách hạ tầng + Kỹ sư chuyên môn cao quản lý KB

*   - [ ] **Mốc 2 (Ngày 8 - 14): Phát triển và tích hợp hệ thống**
    *   *Nội dung:*
        *   Phát triển pipeline RAG: Embedding → Vector Search → Local LLM synthesis.
        *   Tích hợp bộ lọc Input Validation (phát hiện IP, thông tin nhạy cảm trong câu hỏi).
        *   Xây dựng cơ chế cảnh báo: confidence threshold, cờ HITL, nhãn "AI-Generated".
        *   Phát triển giao diện chat web đơn giản chạy trên intranet VTN.
        *   Cấu hình sanitized logging (chỉ ghi session_id, category, confidence — không ghi nội dung).
    *   *Người chịu trách nhiệm:* Nhóm phát triển kỹ thuật

*   - [ ] **Mốc 3 (Ngày 15 - 22): Kiểm thử nội bộ (Internal QA)**
    *   *Nội dung:*
        *   Chạy bộ 10 ca kiểm thử (test-cases-specification.md) — mục tiêu 10/10 PASS.
        *   Kiểm thử bảo mật: Input Validation, Prompt Injection defense, sanitized logging.
        *   Kiểm tra cơ chế HITL hoạt động đúng với các câu hỏi gợi ý cấu hình.
        *   Sửa lỗi và tinh chỉnh System Prompt dựa trên kết quả kiểm thử.
    *   *Người chịu trách nhiệm:* Nhóm phát triển kỹ thuật + Kỹ sư chuyên môn cao

*   - [ ] **Mốc 4 (Ngày 23 - 30): Thí điểm với nhóm kỹ sư nòng cốt**
    *   *Nội dung:*
        *   Triển khai thử nghiệm với **05 kỹ sư nòng cốt** (NOC + Quy hoạch) sử dụng bộ tài liệu mô phỏng.
        *   Thu thập phản hồi: chất lượng câu trả lời, trải nghiệm giao diện, các tình huống AI trả lời sai.
        *   Ghi nhận danh sách câu hỏi phổ biến để bổ sung tài liệu KB.
        *   Tổng kết phản hồi và lập báo cáo đánh giá giai đoạn 30 ngày.
    *   *Người chịu trách nhiệm:* Toàn bộ nhóm thực hiện

---

### Giai đoạn 90 ngày tiếp theo: Tinh chỉnh, Chuẩn hóa và Mở rộng quy mô (Days 31 - 90)
*Mục tiêu: Tối ưu chất lượng hệ thống, chuẩn hóa quy trình vận hành KB định kỳ, chuẩn bị mở rộng với tài liệu thật (sau khi được phê duyệt).*

*   - [ ] **Mốc 5 (Ngày 31 - 50): Tinh chỉnh hệ thống và Chuẩn hóa quy trình KB**
    *   *Nội dung:*
        *   Phân tích phản hồi từ nhóm thí điểm, tinh chỉnh System Prompt và ngưỡng confidence.
        *   Bổ sung tài liệu KB dựa trên danh sách câu hỏi phổ biến chưa có nguồn trả lời.
        *   Ban hành **SOP cập nhật Knowledge Base định kỳ** (kb-update-sop.md): quy trình phân loại → kiểm duyệt → ký xác nhận → re-index → kiểm thử QA.
        *   Chỉ định chính thức nhóm kỹ sư chuyên môn cao phụ trách quản lý KB và lịch rà soát định kỳ.
        *   Thiết lập hệ thống theo dõi tự động báo cáo tài liệu cần cập nhật (staleness alert).
    *   *Người chịu trách nhiệm:* Trưởng nhóm kỹ thuật + Kỹ sư chuyên môn cao quản lý KB

*   - [ ] **Mốc 6 (Ngày 51 - 70): Xây dựng quy chế vận hành và Kiểm toán bảo mật**
    *   *Nội dung:*
        *   Ban hành văn bản quy chế bảo mật nội bộ khi vận hành hệ thống AI tra cứu tài liệu: phân quyền sử dụng, quy tắc đặt câu hỏi, quy trình leo thang.
        *   Thực hiện kiểm toán bảo mật lần 1: rà soát log, kiểm tra sanitized logging, xác nhận không có thông tin nhạy cảm trong log.
        *   Tổ chức buổi đào tạo ngắn (30 phút) cho toàn bộ kỹ sư sẽ sử dụng hệ thống về cách sử dụng đúng và an toàn.
        *   Hoàn thiện hồ sơ compliance (compliance-checklist.md) và trình Ban lãnh đạo phê duyệt.
    *   *Người chịu trách nhiệm:* Nhóm phát triển + Bộ phận An toàn Thông tin VTN

*   - [ ] **Mốc 7 (Ngày 71 - 90): Nghiệm thu và Đề xuất mở rộng quy mô**
    *   *Nội dung:*
        *   Lập báo cáo định lượng hiệu quả: thời gian tra cứu trung bình trước/sau, mức độ hài lòng kỹ sư, số lần cần HITL (tỉ lệ câu hỏi về cấu hình).
        *   Đánh giá kết quả thí điểm so với KPI đề ra trong One-Pager (thời gian tra cứu < 2 phút, độ chính xác > 90%).
        *   Trình đề xuất **mở rộng quy mô giai đoạn 2**: tích hợp tài liệu kỹ thuật thật (sau khi được Ban lãnh đạo và Bộ phận ATTT phê duyệt), mở rộng đối tượng người dùng.
        *   Hoàn thiện Implementation Kit đầy đủ, sẵn sàng bàn giao chính thức.
    *   *Người chịu trách nhiệm:* Toàn bộ nhóm thực hiện + Lãnh đạo đơn vị

---

## 3. Danh mục đề xuất 03 trường hợp ứng dụng (Use cases) tiếp theo

Dựa trên nhu cầu thực tế của đơn vị và kết quả học từ use case Network Doc Assistant, nhóm đề xuất 03 ý tưởng ứng dụng AI tiếp theo:

### Use case 2: Trợ lý AI Tóm tắt Nhật ký Vận hành và Cảnh báo Mạng (NOC Log Summarizer)
*   **Mục tiêu:** Tự động phân tích và tóm tắt nhật ký sự cố, cảnh báo từ hệ thống giám sát mạng (NMS/EMS) — chạy cục bộ offline — giúp kỹ sư trực ca nắm bắt nhanh tình trạng mạng.
*   **Dữ liệu sử dụng:** File log hệ thống NMS dạng text (mô phỏng trong thí điểm) — xử lý hoàn toàn trên hạ tầng nội bộ VTN.
*   **Hiệu quả mong đợi:** Giảm thời gian đọc và phân tích log từ ~45 phút xuống ~5 phút/ca trực.
*   **Lưu ý HITL:** Kỹ sư trực ca vẫn phải xác nhận và phê duyệt mọi hành động xử lý sự cố — AI chỉ tóm tắt, không tự động can thiệp mạng.

### Use case 3: Công cụ AI Hỗ trợ Soạn thảo Báo cáo Kỹ thuật (Technical Report Assistant)
*   **Mục tiêu:** Hỗ trợ kỹ sư soạn thảo nhanh các báo cáo kỹ thuật định kỳ (báo cáo hiệu năng mạng, báo cáo sự cố) dựa trên template chuẩn và dữ liệu đầu vào kỹ sư cung cấp — chạy offline.
*   **Dữ liệu sử dụng:** Template báo cáo nội bộ VTN + số liệu thô kỹ sư nhập vào (không chứa PII).
*   **Hiệu quả mong đợi:** Giảm thời gian soạn thảo báo cáo từ ~2 giờ xuống ~30 phút.
*   **Lưu ý HITL:** Kỹ sư và trưởng nhóm phải review và ký xác nhận báo cáo trước khi gửi đi — AI chỉ hỗ trợ soạn thảo.

### Use case 4: Chatbot Hỏi đáp Quy trình Vận hành O&M Offline (O&M Procedures Assistant)
*   **Mục tiêu:** Tạo trợ lý AI hỏi đáp (RAG offline) tra cứu hàng trăm trang tài liệu quy trình vận hành và bảo trì thiết bị mạng (O&M procedures) mà không cần kết nối internet — phục vụ kỹ sư làm việc tại hiện trường.
*   **Dữ liệu sử dụng:** Tài liệu O&M procedures nội bộ (phân loại "Công khai nội bộ" — sau khi được kiểm duyệt bởi kỹ sư chuyên môn cao).
*   **Hiệu quả mong đợi:** Kỹ sư hiện trường tra cứu tức thời cách xử lý sự cố thiết bị mà không cần liên hệ trung tâm hỗ trợ.
*   **Lưu ý HITL:** Mọi thao tác can thiệp thiết bị thực tế đều phải có lệnh từ kỹ sư cấp cao — AI chỉ cung cấp thông tin tham khảo từ tài liệu O&M.

---

## 4. Các chỉ số theo dõi tiến độ (Progress KPIs)

| KPI | Mục tiêu 30 ngày | Mục tiêu 90 ngày | Cách đo |
|---|---|---|---|
| Số ca kiểm thử PASS | 10/10 (100%) | 10/10 (duy trì) | test-cases-specification.md |
| Thời gian tra cứu trung bình | < 3 phút | < 2 phút | Log session time |
| Mức độ hài lòng kỹ sư thí điểm | >= 3.5/5.0 | >= 4.0/5.0 | Khảo sát nội bộ |
| Tỉ lệ câu trả lời có trích dẫn nguồn | 100% | 100% | Audit câu trả lời |
| Số lần AI bịa đặt (hallucinate) | 0 | 0 | Phản hồi người dùng |
| Số tài liệu KB được rà soát/cập nhật | >= 100% tài liệu mô phỏng | >= 1 lần rà soát toàn bộ | kb-audit-log.xlsx |
