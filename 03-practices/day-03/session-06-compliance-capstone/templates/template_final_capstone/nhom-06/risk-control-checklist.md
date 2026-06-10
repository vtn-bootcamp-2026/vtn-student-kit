---
mo-ta: Bang kiem va phan tich chi tiet rui ro - Case 1: Tro ly du an gia lap
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-08 11:20 +07:00
updated-at: 2026-06-08 11:20 +07:00
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

## Phân tích chi tiết rủi ro & Rào cản an toàn (Guardrails)

### Rủi ro 1: Lộ lọt thông tin nhạy cảm của dự án thực tế hoặc thông tin định danh cá nhân (PII) thật
- **Mô tả chi tiết**: Trong quá trình sử dụng hệ thống, PM hoặc subPM có thể theo thói quen dán các đoạn tin nhắn thực tế có chứa tên khách hàng, số điện thoại hoặc IP thật của VTN, hoặc tải lên các tài liệu thiết kế hệ thống thật chứa thông tin nhạy cảm để hỏi AI.
- **Rào cản an toàn (Guardrail) tương ứng**:
  1. **Bộ lọc PII đầu vào (Anonymization Filter)**: Tích hợp một module tiền xử lý dữ liệu trước khi gửi tới API LLM. Sử dụng Regex kết hợp mô hình nhận dạng thực thể (NER) để tự động phát hiện, che giấu hoặc thay thế các mẫu thông tin nhạy cảm (như email, số điện thoại, địa chỉ IP, tên riêng) bằng các nhãn giả lập (ví dụ: `[CLIENT_NAME_MASKED]`, `[IP_MASKED]`).
  2. **Ràng buộc chính sách hệ thống**: Thiết lập chính sách chỉ tải dữ liệu từ các thư mục lưu trữ được phê duyệt và được gắn thẻ an toàn (Simulated Data).

### Rủi ro 2: AI tự suy diễn dữ liệu tiến độ dự án hoặc sinh ra thông tin ảo tưởng (Hallucination)
- **Mô tả chi tiết**: Khi dữ liệu tiến độ trong file CSV hoặc nội dung chat log của nhân sự bị thiếu hoặc không rõ ràng, AI có thể tự suy diễn hoặc tự ý tính toán ra các con số % hoàn thành lũy kế không đúng thực tế, khiến PM đưa ra các quyết định điều phối sai lệch.
- **Rào cản an toàn (Guardrail) tương ứng**:
  1. **Prompt giới hạn nghiêm ngặt (Strict Grounding Prompt)**: Định nghĩa rõ trong system prompt: *"Chỉ được phép trả lời dựa trên thông tin chính xác có trong tài liệu được cung cấp. Nếu không tìm thấy thông tin hoặc thiếu dữ liệu, bắt buộc phải trả lời: 'Tôi không tìm thấy thông tin này trong dữ liệu dự án hiện tại, vui lòng liên hệ nhân sự phụ trách [Tên Nhân Sự] để xác nhận trực tiếp'. Tuyệt đối không tự suy đoán hoặc ngoại suy số liệu."*
  2. **Trích dẫn nguồn bắt buộc (Mandatory Source Citation)**: AI bắt buộc phải trả về chỉ số kèm đoạn văn bản gốc được trích dẫn cụ thể (ví dụ: *"Nguyen Van A báo cáo đã hoàn thành 80% (nguồn: Chat log lúc 15:30 ngày 05/06/2026)"*). Nếu không có nguồn trích dẫn, hệ thống sẽ tự động chặn phản hồi đó.

### Rủi ro 3: Sự phụ thuộc quá mức vào AI và bỏ qua bước kiểm duyệt của con người (Over-reliance)
- **Mô tả chi tiết**: PM có thể tin tưởng hoàn toàn vào các báo cáo tổng hợp nhanh của AI mà bỏ qua bước đối chiếu nguồn gốc, trực tiếp sử dụng số liệu để gửi báo cáo tuần cho Ban giám đốc hoặc đánh giá hiệu suất của nhân viên.
- **Rào cản an toàn (Guardrail) tương ứng**:
  1. **Giao diện HITL cưỡng chế (Forced HITL UI)**: Thiết kế giao diện quản trị hiển thị câu trả lời của AI và tài liệu gốc được highlight ở hai cửa sổ song song. Nút "Xuất báo cáo" hoặc "Sử dụng dữ liệu" chỉ được kích hoạt sau khi PM đã nhấp chọn xác nhận đã kiểm tra đối chiếu từng nguồn trích dẫn.
  2. **Cảnh báo trách nhiệm (Disclaimer Label)**: Đặt nhãn cảnh báo rõ ràng ở đầu trang phản hồi: *"Chú ý: Đây là báo cáo tổng hợp tự động bởi trợ lý AI. Vui lòng đối chiếu kỹ với nguồn trích dẫn bên dưới trước khi phê duyệt."*

### Rủi ro 4: Rò rỉ thông tin khóa API và lịch sử hội thoại dự án trên hạ tầng công cộng
- **Mô tả chi tiết**: Dữ liệu tiến độ dự án và lịch sử chat của PM có thể bị lưu lại trên các máy chủ public của bên thứ ba, hoặc khóa API của hệ thống bị lộ ra ngoài do hard-code trong mã nguồn hoặc log.
- **Rào cản an toàn (Guardrail) tương ứng**:
  1. **Quản lý biến môi trường bảo mật**: Lưu trữ toàn bộ khóa API thông qua các biến môi trường bảo mật (Environment Variables / Vault), tuyệt đối không lưu trong code hoặc n8n workflow file xuất ra.
  2. **Chính sách không lưu trữ dữ liệu của nhà cung cấp LLM (Zero Data Retention)**: Lựa chọn sử dụng các mô hình LLM qua cổng kết nối bảo mật của doanh nghiệp hoặc cam kết của nhà cung cấp API không sử dụng dữ liệu đầu vào để huấn luyện mô hình (Data privacy terms).

## Kết luận

| Mục | Kết luận |
| --- | --- |
| Bài toán đủ an toàn để làm trong lớp? | **Có** |
| Điều kiện cần sửa trước khi chốt | Rà soát toàn bộ tệp dữ liệu mô phỏng để đảm bảo không trùng tên với bất kỳ nhân sự thật hoặc dự án thật nào của VTN. |
| Người xác nhận | Nhóm 06 |

## Ghi chú

Bảng này là rà rủi ro sơ bộ ở session 01, không thay thế bảng kiểm tuân thủ trước khi thí điểm trong session 06.
