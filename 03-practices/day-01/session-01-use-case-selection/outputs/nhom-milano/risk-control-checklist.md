---
mo-ta: bang kiem rui ro va kiem soat so bo - Tro ly chinh sach nhan su gia lap - Nhom Milano
trang-thai: active
phien-ban: v0.1
created-at: 2026-06-08 11:15 +07:00
updated-at: 2026-06-08 11:15 +07:00
---

# Bảng kiểm rủi ro và kiểm soát

## Dữ liệu

- [x] Không dùng dữ liệu thật của VTN
- [x] Không dùng thông tin khách hàng thật
- [x] Không dùng IP thật, mã trạm thật hoặc cấu hình thật
- [x] Có dữ liệu mô phỏng thay thế
- [x] Có mô tả nguồn dữ liệu mô phỏng

## Phân quyền và điểm kết nối

- [x] Không dùng token thật
- [x] Không dùng API key thật
- [x] Không hard-code thông tin bí mật
- [x] Không đưa API key hoặc token vào prompt, ảnh chụp màn hình, log, n8n export hoặc bài nộp
- [x] Nếu mô tả điểm kết nối (endpoint), chỉ dùng endpoint giả lập
- [x] Quyền truy cập trong bài thực hành là quyền đọc hoặc quyền mô phỏng

## Con người trong vòng lặp

- [x] Có bước con người trong vòng lặp (human in the loop)
- [x] Có người chịu trách nhiệm duyệt đầu ra
- [x] Có tiêu chí duyệt hoặc từ chối
- [x] Không để AI tự quyết định việc có rủi ro kỹ thuật, pháp lý, nhân sự hoặc vận hành

## Nhật ký và truy vết

- [x] Có lưu đầu vào mẫu
- [x] Có lưu đầu ra mẫu
- [x] Có ghi phiên bản prompt hoặc hướng dẫn
- [x] Có ghi trạng thái thành công hoặc lỗi
- [x] Có cách truy lại lý do AI đưa ra kết quả
- [x] Nhật ký vận hành chỉ chứa dữ liệu phi nhạy cảm

## Lan can an toàn

- [x] Có quy tắc từ chối nếu câu hỏi vượt phạm vi
- [x] Có quy tắc không suy đoán khi thiếu dữ liệu
- [x] Có quy tắc yêu cầu trích dẫn hoặc nêu căn cứ khi dùng tài liệu
- [x] Có quy tắc chuyển sang con người khi rủi ro cao

## Kết luận

| Mục | Kết luận |
| --- | --- |
| Bài toán đủ an toàn để làm trong lớp? | Có |
| Điều kiện cần sửa trước khi chốt | Không có (Đã đảm bảo chỉ dùng dữ liệu mô phỏng và có HITL đầy đủ) |
| Người xác nhận | Nhóm Milano |

## Phân tích Rủi ro và Rào cản An toàn (Guardrails)

Dưới đây là phân tích chi tiết về 4 rủi ro bảo mật thông tin và tuân thủ dữ liệu nhạy cảm (PII) tiềm ẩn đối với bài toán Trợ lý chính sách nhân sự cùng các giải pháp kiểm soát tương ứng:

### 1. Rủi ro 1: Rò rỉ thông tin nhạy cảm của cá nhân (PII) do người dùng nhập vào khung chat
- **Mô tả:** Trong quá trình tương tác, nhân viên có thể vô tình nhập các dữ liệu nhạy cảm thực tế như Họ và tên thật, Số điện thoại, Số định danh cá nhân (CCCD), Mã số nhân viên hoặc thông tin sức khỏe cá nhân khi hỏi về chế độ nghỉ phép.
- **Rào cản an toàn (Guardrail):** 
  - Tích hợp một module khử trùng dữ liệu đầu vào (Input Sanitizer) chạy trước khi gửi câu hỏi đến mô hình LLM. Module này sử dụng các biểu thức chính quy (Regex) và mô hình nhận diện thực thể (NER) cục bộ để phát hiện và che giấu các thông tin PII bằng nhãn `[REDACTED_PII]`.
  - Hiển thị cảnh báo trực quan ngay bên dưới khung nhập liệu: *"Không nhập thông tin cá nhân thật, mật khẩu hoặc dữ liệu nội bộ của đơn vị vào đây."*

### 2. Rủi ro 2: AI ảo tưởng (Hallucination) trả lời sai quy định hoặc tự tạo ra chính sách
- **Mô tả:** AI có thể tự sinh ra các thông tin sai lệch về thời gian xin phép nghỉ, định mức công tác phí hoặc thủ tục xác nhận công tác không có trong tài liệu FAQ giả lập, gây hiểu lầm cho nhân viên và ảnh hưởng đến vận hành.
- **Rào cản an toàn (Guardrail):**
  - Áp dụng cấu trúc RAG (Retrieval-Augmented Generation) nghiêm ngặt. System Instruction của mô hình được thiết lập rõ: *"Bạn chỉ được phép trả lời câu hỏi dựa trên tài liệu FAQ được cung cấp. Tuyệt đối không tự suy diễn hoặc giả định thông tin. Nếu không tìm thấy thông tin trong FAQ, hãy trả lời: 'Tôi không tìm thấy thông tin này trong tài liệu hướng dẫn giả lập. Xin vui lòng liên hệ phòng Nhân sự (HRBP) để được hỗ trợ cụ thể.' và cung cấp thông tin liên hệ."*
  - Yêu cầu mô hình bắt buộc phải xuất kèm trường trích dẫn (`source_citation`) tương ứng từ tài liệu nguồn để người dùng dễ đối chiếu.

### 3. Rủi ro 3: Tấn công Prompt Injection để vượt qua các quy tắc an toàn
- **Mô tả:** Người dùng có thể cố tình sử dụng các kỹ thuật tinh vi để ép trợ lý AI thoát khỏi vai trò tra cứu chính sách nhân sự, yêu cầu AI viết mã độc, thảo luận về các vấn đề chính trị hoặc đưa ra các phát ngôn không phù hợp.
- **Rào cản an toàn (Guardrail):**
  - Cấu hình bộ lọc an toàn của Gemini API (Safety Settings) ở mức tối đa (Block Most) đối với các nội dung quấy rối, thù hận, bạo lực và thô tục.
  - Sử dụng cơ chế Prompt Guarding bằng cách kiểm tra ngữ cảnh câu hỏi đầu vào để đảm bảo câu hỏi thuộc phạm vi liên quan đến chính sách nhân sự trước khi chuyển đến LLM cốt lõi.

### 4. Rủi ro 4: Rò rỉ dữ liệu nhạy cảm thông qua nhật ký hệ thống (Logs)
- **Mô tả:** Hệ thống lưu toàn bộ lịch sử trò chuyện của người dùng dưới dạng văn bản thô vào log vận hành, dẫn đến nguy cơ các quản trị viên hệ thống hoặc bên thứ ba tiếp cận được thông tin nhạy cảm của nhân viên.
- **Rào cản an toàn (Guardrail):**
  - Quy định cấu trúc bản ghi nhật ký vận hành chặt chẽ: Chỉ ghi nhận các siêu dữ liệu (metadata) không nhạy cảm như `session_id`, `timestamp`, `intent_category`, `confidence_score`, `hitl_flag`, và `response_status`.
  - Không lưu trữ trực tiếp nội dung văn bản câu hỏi thô của người dùng vào cơ sở dữ liệu nhật ký hệ thống chung.

## Ghi chú

Bảng này là rà rủi ro sơ bộ ở session 01, không thay thế bảng kiểm tuân thủ trước khi thí điểm trong session 06.
