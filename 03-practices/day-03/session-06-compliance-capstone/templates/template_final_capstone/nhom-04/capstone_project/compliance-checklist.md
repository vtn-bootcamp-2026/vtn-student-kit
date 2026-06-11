---
mo-ta: "Biểu mẫu bảng kiểm tuân thủ bảo mật và dữ liệu trước khi thí điểm Trợ lý chính sách nhân sự tại VTN"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 15:46 +07:00
updated-at: 2026-06-10 15:46 +07:00
---

# Bảng kiểm tuân thủ trước khi thí điểm (Compliance checklist)

*   **Tên dự án/công cụ:** Trợ lý AI tra cứu chính sách nhân sự nội bộ (VTN HR Policy Assistant)
*   **Đơn vị phát triển:** Nhóm học viên AI Builders - Nhóm 1 VTN
*   **Người chịu trách nhiệm kỹ thuật:** Nhóm học viên AI Builders - Nhóm 1 VTN
*   **Người phê duyệt nghiệp vụ:** Đại diện Phòng Tổ chức Lao động / Ban giám đốc VTN

---

## 1. Mục đích bảng kiểm

Bảng tự kiểm tra tuân thủ bảo mật thông tin nội bộ này được thiết lập nhằm bảo đảm dự án **VTN HR Policy Assistant** hoạt động an toàn trong môi trường mạng nội bộ của Viettel Net, bảo vệ dữ liệu quy chế và dữ liệu cá nhân của CBNV theo đúng **Nghị định 356/2025/NĐ-CP** và quy chế an toàn thông tin của tập đoàn trước khi đưa vào chạy thử nghiệm chính thức.

---

## 2. Các hạng mục kiểm tra tuân thủ

### Hạng mục A: An toàn dữ liệu cá nhân nhạy cảm (PII compliance)
*Đảm bảo không rò rỉ dữ liệu cá nhân nhạy cảm của CBNV Viettel ra các API đám mây công cộng và bảo mật thông tin nội bộ.*

*   - [x] **Tiêu chí A1: Che giấu thông tin định danh trực tiếp**
    *   *Yêu cầu:* Tên người, số điện thoại cá nhân, email cá nhân bắt buộc phải được lọc bỏ hoặc ẩn danh hóa bằng nhãn đại diện trước khi hiển thị cho người dùng khác hoặc lưu trữ.
    *   *Giải pháp kỹ thuật đã áp dụng:* System prompt cấu hình luật ẩn danh nghiêm ngặt đối với bất kỳ thông tin định danh cá nhân cụ thể nào lọt vào câu trả lời, tự động chuyển đổi sang nhãn `[REDACTED_NAME]`, `[REDACTED_PHONE]` hoặc `[REDACTED_EMAIL]`.
*   - [x] **Tiêu chí A2: Xử lý dữ liệu tại máy trạm/server cục bộ (Local processing)**
    *   *Yêu cầu:* Toàn bộ dữ liệu thô, câu hỏi tra cứu và tài liệu chính sách của VTN phải được lưu trữ và xử lý hoàn toàn offline trên hạ tầng máy chủ Private Cloud nội bộ. Không gửi dữ liệu thô sang các API bên thứ ba nằm ngoài mạng lưới.
    *   *Giải pháp kỹ thuật đã áp dụng:* Thiết lập RAG Pipeline sử dụng các thư viện offline hoàn toàn. Kết nối với máy chủ Ollama cục bộ qua cổng nội bộ đã được cấu hình bảo mật. Sử dụng mô hình `gemma4-e2b:q4` tải trực tiếp về máy chủ, không kết nối internet khi suy luận.
*   - [x] **Tiêu chí A3: Ngăn chặn lưu trữ tạm thời dữ liệu nhạy cảm (No caching raw data)**
    *   *Yêu cầu:* Công cụ không được lưu trữ hoặc cache lại nội dung các câu hỏi chứa dữ liệu nhạy cảm của CBNV dưới dạng bản rõ (clear text) trong thư mục tạm hoặc file log công khai.
    *   *Giải pháp kỹ thuật đã áp dụng:* Áp dụng cơ chế xử lý trực tiếp trên RAM (In-Memory Processing). Dữ liệu câu hỏi được mã hóa tạm thời trong bộ nhớ và tự động giải phóng ngay sau khi kết thúc phiên hỏi đáp của người dùng.

---

### Hạng mục B: Quản lý phân quyền và cổng kết nối (Endpoint & Access control)
*Đảm bảo an toàn cổng kết nối mạng và phân quyền truy cập.*

*   - [x] **Tiêu chí B1: Giới hạn cổng kết nối mô hình (API port binding)**
    *   *Yêu cầu:* Cổng dịch vụ của máy chủ mô hình cục bộ (Ollama - mặc định `11434`) phải được cấu hình chỉ lắng nghe trên giao diện cục bộ (`localhost` / `127.0.0.1`), chỉ cho phép các máy chủ thuộc dải IP được cấu hình VPN nội bộ truy cập.
    *   *Giải pháp kỹ thuật đã áp dụng:* Cổng kết nối được cấu hình thông qua file biến môi trường `.env` và được phân quyền truy cập thông qua lớp bảo vệ tường lửa (Firewall) của máy chủ ảo hóa nội bộ.
*   - [x] **Tiêu chí B2: Kiểm soát quyền thực thi của mã nguồn (Scripts execution policy)**
    *   *Yêu cầu:* Ứng dụng chạy chatbot/web portal không yêu cầu quyền Admin/Root tối cao của hệ điều hành máy chủ để hoạt động, giảm thiểu rủi ro leo thang đặc quyền.
    *   *Giải pháp kỹ thuật đã áp dụng:* Các tiến trình dịch vụ Python, Node.js (nếu có) được đóng gói dưới dạng Docker Container và thực thi dưới quyền User không có đặc quyền (Non-root user) bên trong container.

---

### Hạng mục C: Cơ chế kiểm soát của con người (Human-in-the-loop - HITL)
*Không để AI tự ý quyết định các tác vụ hoặc đưa ra thông tin chính sách nhạy cảm mà không có sự kiểm soát.*

*   - [x] **Tiêu chí C1: Giao diện phê duyệt kết quả câu trả lời nhạy cảm**
    *   *Yêu cầu:* Hệ thống phải tự động gắn cờ cảnh báo đối với các câu trả lời liên quan đến vấn đề tài chính đặc biệt hoặc trường hợp vượt định mức để chuyển qua cán bộ HR duyệt trước khi gửi đến CBNV.
    *   *Giải pháp kỹ thuật đã áp dụng:* Thiết lập thuộc tính `needs_human_review = True` trong JSON đầu ra của LLM. Khi cờ này được kích hoạt, câu trả lời sẽ tạm thời nằm trong hàng đợi chờ duyệt (Approve Queue) trên Dashboard của cán bộ HR.
*   - [x] **Tiêu chí C2: Cơ chế ghi đè thủ công (Manual override protocol)**
    *   *Yêu cầu:* Cho phép cán bộ HR thay đổi, chỉnh sửa trực tiếp nội dung câu trả lời của AI trước khi gửi phê duyệt hoặc cập nhật thủ công các luật trả lời cứng đối với các quy chế mới ban hành.
    *   *Giải pháp kỹ thuật đã áp dụng:* Giao diện quản trị (HR Dashboard) tích hợp khung soạn thảo tương tác cho phép sửa tay trực tiếp câu trả lời của AI và lưu vết lịch sử sửa đổi.

---

### Hạng mục D: Phòng thủ tấn công lời nhắc (Prompt injection defense)
*Đảm bảo hệ thống không bị điều khiển hoặc thao túng bởi người dùng cuối.*

*   - [x] **Tiêu chí D1: Ép cấu trúc đầu ra nghiêm ngặt (Output schema enforcement)**
    *   *Yêu cầu:* Thiết lập cơ chế bắt buộc mô hình trả về cấu trúc JSON Schema cố định nhằm ngăn chặn việc in ra mã độc hoặc các kịch bản thực thi lệnh do Prompt Injection mang lại.
    *   *Giải pháp kỹ thuật đã áp dụng:* Sử dụng tính năng Structured Output của thư viện LangChain để ép LLM trả về cấu trúc JSON gồm 4 trường định danh. Bất kỳ văn bản tiêm lệnh phá hoại nào lọt vào câu hỏi cũng chỉ được trả về dưới dạng chuỗi nằm trong schema JSON, không thể thực thi.
*   - [x] **Tiêu chí D2: Đóng khung dữ liệu đầu vào bằng thẻ XML**
    *   *Yêu cầu:* System prompt của tác tử phải tách biệt rõ ràng giữa hướng dẫn hệ thống và dữ liệu người dùng nhằm tránh mô hình nhầm lẫn dữ liệu đầu vào là mệnh lệnh hệ thống.
    *   *Giải pháp kỹ thuật đã áp dụng:* Áp dụng cấu trúc XML đóng khung: Ngữ cảnh chính sách được bọc trong thẻ `<context>...</context>`, câu hỏi của người dùng được bọc trong thẻ `<question>...</question>`.

---

### Hạng mục E: Nhật ký giám sát và xử lý sự cố (Logging & Error tracking)
*Khả năng theo dõi trạng thái hệ thống và khắc phục sự cố.*

*   - [x] **Tiêu chí E1: Logging phi nhạy cảm (Sanitized logging)**
    *   *Yêu cầu:* File log hệ thống chỉ ghi lại thời gian, vai trò người dùng, mã sự kiện và tài liệu được truy xuất. Tuyệt đối KHÔNG ghi lại nội dung câu hỏi/trả lời gốc chứa PII vào log công khai.
    *   *Giải pháp kỹ thuật đã áp dụng:* Hàm ghi log chỉ ghi nhận các thông số kỹ thuật (Latency, token count, status) ra tệp `outputs/execution-log.csv`.
*   - [x] **Tiêu chí E2: Xử lý ngoại lệ an toàn (Graceful degradation)**
    *   *Yêu cầu:* Khi mất kết nối API mô hình cục bộ hoặc cơ sở dữ liệu vector bị lỗi, hệ thống phải tự động chuyển sang chế độ dự phòng thông báo lỗi thân thiện cho CBNV và ghi nhận mã lỗi vào log nội bộ.
    *   *Giải pháp kỹ thuật đã áp dụng:* Thiết lập cấu trúc `try-except` toàn diện. Khi hệ thống RAG mất kết nối máy chủ Ollama, giao diện chatbot hiển thị lời xin lỗi kèm theo thông tin hướng dẫn CBNV gửi email trực tiếp đến địa chỉ Phòng Tổ chức Lao động nội bộ, đảm bảo tính liên tục của trải nghiệm người dùng.

---

## 3. Kết luận đánh giá tuân thủ

*   **Tổng số tiêu chí đánh giá:** 11 tiêu chí
*   **Số tiêu chí ĐẠT (Pass):** 11 / 11 (100% ĐẠT)
*   **Số tiêu chí CHƯA ĐẠT (Needs work):** 0 / 11
*   **Đánh giá chung:** **ĐỦ ĐIỀU KIỆN ĐỂ TRIỂN KHAI THÍ ĐIỂM THỰC TẾ** tại Viettel Net nhờ tính năng bảo mật offline tuyệt đối và cơ chế phân quyền truy xuất dữ liệu tối ưu.
