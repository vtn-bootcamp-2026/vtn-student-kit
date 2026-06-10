---
mo-ta: "Biểu mẫu kế hoạch hành động 30/90 ngày áp dụng AI tại đơn vị và danh mục use case tiếp theo"
trang-thai: active
phien-ban: v1.1
created-at: 2026-06-10 15:45 +07:00
updated-at: 2026-06-10 15:45 +07:00
---

# Kế hoạch hành động 30/90 ngày áp dụng AI tại đơn vị (Action plan)

*   **Tên nhóm thực hiện:** Nhóm 01 - AI Builders Viettel Net
*   **Đơn vị áp dụng:** Trung tâm Điều hành Mạng (NOC) - Tổng Công ty Mạng lưới Viettel (Viettel Net)
*   **Người chịu trách nhiệm chính:** Nguyễn Minh Huy
*   **Phiên bản tài liệu:** v1.0

---

## 1. Mục tiêu kế hoạch hành động

Bản kế hoạch hành động này thiết lập lộ trình cụ thể nhằm hiện thực hóa tri thức và công cụ AI đã được trang bị từ khóa học `vtn-ai-builders-bootcamp-2026` vào quy trình làm việc thực tế tại đơn vị trong **30 ngày đầu tiên** (giai đoạn thử nghiệm, thích ứng nhanh) và **90 ngày tiếp theo** (giai đoạn tối ưu hóa, chuẩn hóa quy trình và đề xuất ý tưởng mới).

---

## 2. Lộ trình hành động chi tiết (Milestone roadmaps)

### Giai đoạn 30 ngày đầu: Thử nghiệm thực tế và Tích hợp nhanh (Days 1 - 30)
*Mục tiêu: Đưa công cụ NetBI-KARA vào vận hành thực tế tại phòng trực NOC, đánh giá và tinh chỉnh độ chính xác.*

*   - [x] **Mốc 1 (Ngày 1 - 10): Hoàn thiện cài đặt hạ tầng cục bộ**
    *   *Nội dung:* Triển khai cài đặt Python, Ollama và tải mô hình cục bộ `qwen3.5:7b-instruct` lên máy chủ GPU chuyên dụng của NOC. Cấu hình dịch vụ API Ollama kết nối ổn định.
    *   *Người chịu trách nhiệm:* Trần Quốc Bảo
*   - [x] **Mốc 2 (Ngày 11 - 20): Thử nghiệm song song (Parallel testing)**
    *   *Nội dung:* Áp dụng công cụ NetBI-KARA song song với quy trình tổng hợp báo cáo thủ công hiện tại của 5 kỹ sư trực ca. So sánh độ chính xác của báo cáo AI sinh ra so với báo cáo do con người viết để tinh chỉnh Prompt và thuật toán phát hiện Anomaly.
    *   *Người chịu trách nhiệm:* Lê Hoàng Nam
*   - [x] **Mốc 3 (Ngày 21 - 30): Đánh giá vòng 1 và Hoàn thiện tài liệu**
    *   *Nội dung:* Thu thập ý kiến phản hồi từ 5 kỹ sư trực ca NOC về trải nghiệm giao diện Web UI, mức độ thực tế của email cảnh báo soạn sẵn để cập nhật System Prompt.
    *   *Người chịu trách nhiệm:* Phạm Minh Đức

---

### Giai đoạn 90 ngày tiếp theo: Chuẩn hóa, tối ưu và Mở rộng quy mô (Days 31 - 90)
*Mục tiêu: Quy chuẩn hóa công cụ thành quy trình vận hành chính thức tại NOC, kết nối tự động.*

*   - [x] **Mốc 4 (Ngày 31 - 60): Tích hợp hệ thống Email nội bộ và Tự động hóa kết xuất**
    *   *Nội dung:* Kết nối API của NetBI-KARA với máy chủ thư điện tử nội bộ (Microsoft Exchange) của Viettel Net để thực hiện gửi email cảnh báo tự động ngay khi được kỹ sư NOC duyệt trên giao diện Web UI.
    *   *Người chịu trách nhiệm:* Vũ Khánh Huyền
*   - [x] **Mốc 5 (Ngày 61 - 75): Xây dựng quy chế vận hành và Hướng dẫn an toàn thông tin**
    *   *Nội dung:* Ban hành văn bản hướng dẫn nghiệp vụ trực ca NOC mới kết hợp công cụ AI, ban hành quy định bảo mật dữ liệu vận hành khi sử dụng AI cục bộ tại NOC.
    *   *Người chịu trách nhiệm:* Nguyễn Minh Huy
*   - [x] **Mốc 6 (Ngày 76 - 90): Nghiệm thu và Đánh giá hiệu quả vận hành**
    *   *Nội dung:* Lập báo cáo định lượng hiệu quả (tổng số giờ lao động tiết kiệm được, tỷ lệ rút ngắn thời gian phản hồi KPI suy giảm của các owner) trình Ban giám đốc Viettel Net.
    *   *Người chịu trách nhiệm:* Nguyễn Minh Huy

---

## 3. Danh mục đề xuất 03 trường hợp ứng dụng (Use cases) tiếp theo

Dựa trên nhu cầu thực tế của đơn vị, nhóm đề xuất 3 ý tưởng ứng dụng AI thực chiến tiếp theo để phát triển sau khóa học:

### Use case 1: Trợ lý AI tóm tắt nhật ký vận hành trạm truyền dẫn (SCADA log summarizer)
*   **Mục tiêu:** Tự động tóm tắt các tệp tin log sự cố SCADA dài hàng nghìn dòng thành báo cáo cô đọng 10 dòng bằng mô hình cục bộ.
*   **Dữ liệu sử dụng:** Log hệ thống SCADA dạng text thô của Viettel Net.
*   **Hiệu quả mong đợi:** Kỹ sư trực ca nắm bắt nguyên nhân lỗi hệ thống trong vòng 2 phút thay vì mất 45 phút đọc log thủ công.

### Use case 2: Công cụ AI sinh mã kịch bản tự động hóa hạ tầng (Infrastructure-as-code generator)
*   **Mục tiêu:** Hỗ trợ kỹ sư hạ tầng viết nhanh các đoạn mã Ansible/Terraform để cấu hình tự động trạm phát sóng thông qua mô tả ngôn ngữ tự nhiên tiếng Việt.
*   **Dữ liệu sử dụng:** Các tài liệu thiết kế mạng chuẩn và tệp script Ansible mẫu của VTN.
*   **Hiệu quả mong đợi:** Giảm thiểu 50% thời gian viết script cấu hình hạ tầng mạng mới, hạn chế lỗi cú pháp do con người gõ sai.

### Use case 3: Chatbot tra cứu quy trình kỹ thuật vận hành O&M offline (Offline O&M procedures assistant)
*   **Mục tiêu:** Tạo trợ lý AI hỏi đáp (RAG offline) tra cứu hàng nghìn trang tài liệu quy trình vận hành và bảo trì trạm biến áp, truyền dẫn mà không cần kết nối internet.
*   **Dữ liệu sử dụng:** Các file PDF quy trình vận hành tiêu chuẩn kỹ thuật nội bộ của tập đoàn.
*   **Hiệu quả mong đợi:** Kỹ sư hiện trường tra cứu tức thời cách xử lý sự cố thiết bị tại trạm mà không cần liên hệ trung tâm hỗ trợ kỹ thuật.
