---
mo-ta: "Biểu mẫu đề xuất dự án một trang Use Case One Pager cho Trợ lý chính sách nhân sự tại VTN"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 15:43 +07:00
updated-at: 2026-06-10 15:43 +07:00
---

# Đề xuất dự án một trang (Use case one pager)

*   **Tên dự án ứng dụng:** Trợ lý AI tra cứu chính sách nhân sự nội bộ (VTN HR Policy Assistant)
*   **Đơn vị đề xuất:** Phòng Tổ chức Lao động - Tổng Công ty Mạng lưới Viettel (Viettel Net)
*   **Người đầu mối liên hệ:** Nhóm học viên AI Builders - Nhóm 1 VTN
*   **Mức độ ưu tiên:** Cao (Phục vụ giảm tải nghiệp vụ và tuân thủ bảo mật thông tin)
*   **Mốc thời gian dự kiến thí điểm:** Tháng 07/2026

---

## 1. Vấn đề và Nhu cầu thực tế (Problem statement)
*Mô tả ngắn gọn nỗi đau (pain point) hiện tại tại đơn vị mà giải pháp này sẽ giải quyết.*

*   **Hiện trạng:** Viettel Net có quy mô nhân sự lớn với hàng nghìn cán bộ nhân viên (CBNV). Hàng ngày, phòng Tổ chức Lao động phải tiếp nhận và trả lời thủ công hàng trăm câu hỏi lặp đi lặp lại từ CBNV về chế độ phúc lợi, quy định nghỉ phép, bảo hiểm xã hội, tiêu chuẩn công tác phí, quy trình thăng tiến... 
*   **Rủi ro:** 
    *   Quy trình phản hồi thủ công qua email/điện thoại gây trễ thời gian xử lý (trung bình 1 - 2 giờ/yêu cầu), giảm trải nghiệm của CBNV.
    *   Nghiêm trọng hơn, nhiều CBNV tự ý sao chép tài liệu quy chế, chính sách nội bộ tải lên các công cụ AI đám mây công cộng (như ChatGPT, Gemini công cộng) để tra cứu hoặc tóm tắt. Hành vi này vi phạm nghiêm trọng **Nghị định 356/2025/NĐ-CP** về Bảo vệ dữ liệu cá nhân và quy chế bảo mật thông tin nội bộ của Viettel Net.

---

## 2. Giải pháp đề xuất (Proposed solution)
*Mô tả cách thức ứng dụng AI/Local LLM giải quyết vấn đề trên.*

*   **Giải pháp:** Phát triển công cụ **VTN HR Policy Assistant** ứng dụng công nghệ **RAG (Retrieval-Augmented Generation)** chạy hoàn toàn cục bộ (offline) trên hạ tầng máy chủ Private Cloud của Viettel Net.
*   **Cơ chế hoạt động:** 
    *   Tài liệu chính sách chính thức của VTN được số hóa, cắt nhỏ thành các đoạn văn bản (chunks) và chuyển đổi sang không gian vector bằng mô hình embedding offline, sau đó lưu trữ trong cơ sở dữ liệu vector cục bộ (Vector DB - ChromaDB/Qdrant).
    *   Khi CBNV gửi câu hỏi, hệ thống sẽ thực hiện tìm kiếm ngữ cảnh có độ tương đồng cao nhất trong Vector DB.
    *   Sử dụng mô hình ngôn ngữ lớn cục bộ siêu nhẹ **gemma4-e2b:q4** hoặc **qwen3.5:1.5b-instruct** chạy thông qua **Ollama** để tổng hợp câu trả lời chính xác dựa trên đúng ngữ cảnh tìm được, kèm theo nguồn trích dẫn cụ thể (Tên quy chế, số Điều, số trang).
    *   Cung cấp cơ chế phân quyền (Role-based): Nhân viên thông thường chỉ tra cứu được quy định phúc lợi cơ bản, cán bộ HR tra cứu được các chính sách quản lý chuyên sâu.

---

## 3. Hiệu quả mang lại (Business value & Impact)
*Định lượng hiệu quả (thời gian, chi phí, mức độ an toàn) của dự án.*

*   **Tiết kiệm thời gian & Tăng hiệu suất:** Giảm thời gian phản hồi câu hỏi chính sách từ **2 giờ** xuống **dưới 3 giây** (Phản hồi tức thì 24/7). Giải phóng **80%** thời gian làm việc lặp lại của bộ phận HR để tập trung vào các công việc chiến lược.
*   **Đảm bảo tuân thủ bảo mật 100%:** Dữ liệu quy chế chính sách và câu hỏi của CBNV được xử lý hoàn toàn trong mạng nội bộ của Viettel Net. Đáp ứng tối đa Nghị định 356/2025/NĐ-CP về bảo vệ dữ liệu nội bộ, triệt tiêu rủi ro rò rỉ tài liệu ra internet.
*   **Tiết kiệm chi phí vận hành:** Sử dụng mã nguồn mở và chạy offline trên hạ tầng máy chủ ảo hóa có sẵn của VTN, chi phí bản quyền API bằng **0 VNĐ**.

---

## 4. Kiến trúc kỹ thuật và Phương án triển khai (Technical architecture)

*   **Tầng Giao diện (Client):** Tích hợp trực tiếp dưới dạng Chatbot trên nền tảng truyền thông nội bộ **Microsoft Teams** của Viettel Net hoặc giao diện Web portal nội bộ.
*   **Tầng Xử lý Core (RAG Pipeline):** Python 3.10+, thư viện LangChain/LlamaIndex để kết nối luồng RAG, Vector DB cục bộ (ChromaDB/Qdrant) để lưu trữ và truy xuất ngữ cảnh chính sách.
*   **Tầng Mô hình (AI Model):** Ollama Server chạy cục bộ trên máy chủ private cloud của VTN, sử dụng mô hình `gemma4-e2b:q4` hoặc `qwen3.5:7b-instruct` (suy luận tiếng Việt và lý luận cực tốt).
*   **Phương án triển khai:** Đóng gói thành Docker Container chạy trên Kubernetes Cluster nội bộ của VTN, cho phép tự động co giãn (auto-scaling) khi số lượng CBNV truy cập tăng cao.

---

## 5. Rủi ro và Biện pháp phòng ngừa (Risks & Defenses)

*   **Rủi ro 1: Hiện tượng AI bịa đặt thông tin chính sách (Hallucination).**
    *   *Phòng ngừa:* Ép Prompt cấu trúc chặt chẽ (System Prompt Hardening): *"Nếu thông tin không nằm trong ngữ cảnh được cung cấp, hãy lịch sự từ chối trả lời, tuyệt đối không tự bịa đặt"*. Bắt buộc mô hình trích dẫn rõ nguồn gốc (Điều, Khoản, số văn bản quy chế) để người dùng tự đối chiếu.
*   **Rủi ro 2: Nhân viên hỏi dò thông tin bảo mật/lương thưởng của người khác (Prompt Injection/Unauthorized access).**
    *   *Phòng ngừa:* Áp dụng cơ chế lọc phân quyền tài liệu trước khi đưa vào Vector DB (Metadata Filtering theo vai trò người dùng). Thiết lập bộ lọc câu hỏi đầu vào để nhận diện và chặn các lệnh cố tình khai thác dữ liệu nhạy cảm.

---

## 6. Đề xuất kế hoạch hành động tiếp theo (Next steps)

1.  **Tuần 1:** Thu thập và chuẩn hóa bộ tài liệu quy chế chính sách nhân sự (nghỉ phép, công tác phí, chế độ phúc lợi). Số hóa và nạp vào Vector DB.
2.  **Tuần 2:** Cài đặt hạ tầng Ollama cục bộ, chạy thử nghiệm kỹ thuật RAG Pipeline, tối ưu hóa các tham số cắt nhỏ văn bản (Chunking size) và tinh chỉnh System Prompt.
3.  **Tuần 3:** Triển khai thử nghiệm diện hẹp (Beta Test) cho 30 CBNV nòng cốt để thu thập bộ câu hỏi thực tế và đánh giá độ chính xác của câu trả lời.
4.  **Tuần 4:** Nghiệm thu toàn trình kỹ thuật, đóng gói ứng dụng và tích hợp chính thức lên kênh MS Teams nội bộ của Viettel Net.
