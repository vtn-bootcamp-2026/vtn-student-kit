---
mo-ta: "Biểu mẫu kế hoạch hành động 30/90 ngày áp dụng Trợ lý chính sách nhân sự tại VTN"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 15:47 +07:00
updated-at: 2026-06-10 15:47 +07:00
---

# Kế hoạch hành động 30/90 ngày áp dụng AI tại đơn vị (Action plan)

*   **Tên nhóm thực hiện:** Nhóm học viên AI Builders - Nhóm 1 VTN
*   **Đơn vị áp dụng:** Phòng Tổ chức Lao động - Viettel Net (VTN)
*   **Người chịu trách nhiệm chính:** Nhóm trưởng Nhóm 1
*   **Phiên bản tài liệu:** v1.0

---

## 1. Mục tiêu kế hoạch hành động

Kế hoạch này vạch ra lộ trình thực tế để triển khai công cụ **VTN HR Policy Assistant** tại Viettel Net, chuyển giao từ giai đoạn thử nghiệm cục bộ quy mô nhỏ (**30 ngày đầu**) sang giai đoạn tích hợp hệ thống chính thức và nhân rộng toàn diện (**90 ngày tiếp theo**), đảm bảo tối ưu hiệu suất làm việc của phòng HR và an toàn thông tin tuyệt đối.

---

## 2. Lộ trình hành động chi tiết (Milestone roadmaps)

### Giai đoạn 30 ngày đầu: Thử nghiệm thực tế và Tích hợp nhanh (Days 1 - 30)
*Mục tiêu: Hoàn thiện nạp tài liệu chính sách cơ bản, cài đặt hạ tầng cục bộ và kiểm thử độ chính xác trên nhóm nhân sự nhỏ.*

*   - [ ] **Mốc 1 (Ngày 1 - 10): Số hóa tài liệu chính sách & Lập chỉ mục Vector DB**
    *   *Nội dung:* Thu thập các quy chế nghỉ phép, chế độ phúc lợi, công tác phí hiện hành của VTN. Tiến hành làm sạch văn bản, cắt nhỏ (Chunking) và nạp vào cơ sở dữ liệu vector offline (ChromaDB). Thiết lập máy chủ Ollama chạy mô hình `gemma4-e2b:q4`.
    *   *Người chịu trách nhiệm:* Thành viên kỹ thuật Nhóm 1.
*   - [ ] **Mốc 2 (Ngày 11 - 20): Thử nghiệm song song (Parallel testing) & Tinh chỉnh**
    *   *Nội dung:* Cung cấp chatbot thử nghiệm cho 30 nhân viên nòng cốt trực tiếp sử dụng tra cứu. Cán bộ HR chạy đối chiếu kết quả trả về của AI so với quy chế gốc để tinh chỉnh tham số độ tương đồng (Cosine Similarity) và prompt hệ thống.
    *   *Người chịu trách nhiệm:* Thành viên nghiệp vụ Nhóm 1.
*   - [ ] **Mốc 3 (Ngày 21 - 30): Đánh giá giai đoạn 1 & Hoàn thiện tài liệu nghiệp vụ**
    *   *Nội dung:* Tổng hợp bộ câu hỏi thực tế từ người dùng, đánh giá tỷ lệ trả lời đúng (Target đạt $\ge 90\%$). Hoàn thiện bộ tài liệu hướng dẫn sử dụng nhanh và bảng kiểm tuân thủ bảo mật thông tin.
    *   *Người chịu trách nhiệm:* Nhóm trưởng Nhóm 1.

---

### Giai đoạn 90 ngày tiếp theo: Chuẩn hóa, tích hợp và Mở rộng quy mô (Days 31 - 90)
*Mục tiêu: Đưa chatbot lên hệ thống truyền thông nội bộ Microsoft Teams của VTN, áp dụng cơ chế phân quyền và ban hành quy chế vận hành chính thức.*

*   - [ ] **Mốc 4 (Ngày 31 - 60): Đóng gói nâng cao & Tích hợp Microsoft Teams**
    *   *Nội dung:* Đóng gói ứng dụng thành Docker Container chạy trên Kubernetes nội bộ. Liên kết Chatbot với hệ thống Active Directory của VTN để tự động nhận dạng mã nhân viên, áp dụng bộ lọc phân quyền Metadata (chỉ cho phép nhân viên tra cứu đúng nhóm thông tin được phân quyền).
    *   *Người chịu trách nhiệm:* IT vận hành lớp & Nhóm kỹ thuật.
*   - [ ] **Mốc 5 (Ngày 61 - 75): Ban hành quy chế vận hành và Hướng dẫn bảo mật thông tin**
    *   *Nội dung:* Trình ban hành văn bản chính thức quy định việc sử dụng công cụ AI trong tra cứu quy chế nội bộ. Hướng dẫn CBNV không chia sẻ tài khoản tra cứu và cách thức báo cáo khi phát hiện AI phản hồi sai thông tin.
    *   *Người chịu trách nhiệm:* Trưởng Phòng Tổ chức Lao động.
*   - [ ] **Mốc 6 (Ngày 76 - 90): Nghiệm thu chính thức & Đánh giá hiệu quả kinh tế**
    *   *Nội dung:* Đo lường lượng câu hỏi xử lý thành công, tính toán số giờ lao động tiết kiệm được cho phòng HR (Target giảm 80% câu hỏi trùng lặp trực tiếp). Lập báo cáo tổng kết trình Ban giám đốc VTN.
    *   *Người chịu trách nhiệm:* Nhóm trưởng Nhóm 1.

---

## 3. Danh mục đề xuất 03 trường hợp ứng dụng (Use cases) tiếp theo

Để tối ưu hóa năng lực AI tại phòng ban sau khi Trợ lý chính sách vận hành ổn định, nhóm đề xuất 3 ý tưởng tiếp theo:

### Use case 1: Trợ lý AI tóm tắt và Phân tích kết quả đánh giá hiệu quả công việc (KPI Summarizer & Analyst)
*   **Mục tiêu:** Tự động đọc và tóm tắt hàng nghìn phiếu đánh giá hiệu quả công việc (KPI) cuối năm của CBNV để lọc ra các cá nhân xuất sắc hoặc các vấn đề nổi cộm trong công tác quản lý.
*   **Dữ liệu sử dụng:** File excel/word đánh giá KPI đã được ẩn danh tên riêng.
*   **Hiệu quả mong đợi:** Giúp Ban giám đốc và HR nắm bắt nhanh bức tranh hiệu suất lao động toàn công ty trong 5 phút thay vì đọc thủ công hàng tuần.

### Use case 2: Công cụ AI hỗ trợ soạn thảo văn bản hành chính HR tiêu chuẩn (HR Document Generator)
*   **Mục tiêu:** Hỗ trợ cán bộ HR soạn thảo nhanh các thông báo, quyết định nhân sự, thư mời nhận việc, hợp đồng lao động chuẩn dựa trên các văn bản mẫu và dữ liệu đầu vào bằng ngôn ngữ tự nhiên.
*   **Dữ liệu sử dụng:** Kho văn bản hành chính mẫu của tập đoàn Viettel.
*   **Hiệu quả mong đợi:** Giảm 70% thời gian soạn thảo văn bản, đảm bảo 100% đúng quy chuẩn văn phong hành chính của tập đoàn.

### Use case 3: Chatbot offline định hướng và Đào tạo nhân viên mới (Offline Onboarding Assistant)
*   **Mục tiêu:** Trợ lý ảo offline tương tác giúp nhân viên mới tuyển dụng tra cứu nhanh về văn hóa doanh nghiệp, sơ đồ tổ chức, các đầu mối liên hệ nòng cốt và hướng dẫn hoàn thiện hồ sơ nhân sự ban đầu.
*   **Dữ liệu sử dụng:** Cẩm nang nhân viên mới, tài liệu truyền thông nội bộ của VTN.
*   **Hiệu quả mong đợi:** Tăng mức độ gắn kết của nhân viên mới, giảm 50% thời gian HR phải hướng dẫn trực tiếp các thủ tục hành chính ban đầu.
