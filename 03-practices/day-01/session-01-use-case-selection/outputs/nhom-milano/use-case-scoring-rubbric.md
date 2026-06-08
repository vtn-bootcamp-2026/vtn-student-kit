---
mo-ta: phieu cham diem rubbric lua chon bai toan - Tro ly chinh sach nhan su gia lap - Nhom Milano
trang-thai: active
phien-ban: v0.1
created-at: 2026-06-08 11:15 +07:00
updated-at: 2026-06-08 11:15 +07:00
---

# Thang chấm điểm (rubbric) lựa chọn bài toán

## Cách dùng

Chấm từng bài toán ứng viên theo thang 100 điểm. Ưu tiên bài toán đạt từ 70 điểm trở lên, không dùng dữ liệu thật và có điểm con người duyệt rõ ràng.

## Bảng điểm

| Tiêu chí | Điểm tối đa | Câu hỏi kiểm tra | Điểm nhóm tự chấm |
| --- | ---: | --- | ---: |
| Giá trị nghiệp vụ | 20 | Bài toán có giảm thời gian, giảm lỗi hoặc tăng chất lượng đầu ra không? | 18 |
| Tính khả thi trong lớp | 15 | Có thể tạo bản thử nghiệm tối thiểu (MVP) trong 6 buổi không? | 15 |
| Dữ liệu mô phỏng | 15 | Có thể tạo dữ liệu mô phỏng đủ đại diện mà không dùng dữ liệu thật không? | 15 |
| Mức độ đo lường | 10 | Có chỉ số đo hiệu quả tối thiểu không? | 9 |
| Khả năng phát triển | 10 | Bài toán có thể mở rộng sau lớp mà không đổi toàn bộ thiết kế không? | 8 |
| Kiểm soát rủi ro | 20 | Có điểm con người duyệt, logging, trace và guardrail không? | 18 |
| Năng lực AI phù hợp | 10 | AI có phù hợp với tác vụ đọc, tóm tắt, phân loại, trích xuất hoặc tạo nháp không? | 10 |
| Tổng | 100 | | 93 |

## Quy tắc loại nhanh

Loại hoặc thu hẹp bài toán nếu có một trong các điều kiện sau:

- Cần dữ liệu thật của VTN. [Đạt yêu cầu - Không dùng dữ liệu thật]
- Cần token thật, API key thật hoặc certificate thật. [Đạt yêu cầu - Không dùng]
- Cần quyền ghi hoặc thực thi trên hệ thống thật. [Đạt yêu cầu - Chỉ mô phỏng tra cứu]
- Không có người duyệt trước khi sử dụng đầu ra. [Đạt yêu cầu - Có HITL rõ ràng]
- Không mô tả được đầu vào hoặc đầu ra. [Đạt yêu cầu - Đầy đủ đầu vào/đầu ra]
- Không thể đo hiệu quả tối thiểu. [Đạt yêu cầu - Có chỉ số rõ ràng]

## Kết luận nhóm

- **Bài toán được chọn:** Trợ lý chính sách nhân sự giả lập (HR Policy Assistant Simulator)
- **Tổng điểm:** 93/100
- **Lý do chọn:** Bài toán giải quyết nhu cầu thực tế về tối ưu hóa thời gian tra cứu và giải đáp của phòng nhân sự, tính khả thi cực kỳ cao trong phạm vi lớp học do đã chuẩn bị sẵn file FAQ giả lập `sample-hr-policy-faq.md`. Bài toán sử dụng các tính năng cơ bản và ổn định nhất của LLM là phân loại, trích xuất và RAG. Đồng thời, cấu trúc dữ liệu mô phỏng được tách biệt hoàn toàn khỏi hệ thống thật nên an toàn tuyệt đối.
- **Danh sách quy trình ưu tiên của nhóm:**
  1. Phân loại ý định của câu hỏi nhân viên (Intent Classification).
  2. Truy xuất tài liệu FAQ tương thích (Knowledge Retrieval).
  3. Trả lời bằng ngôn ngữ tự nhiên và dẫn nguồn trích dẫn.
  4. Cơ chế chuyển giao khẩn cấp sang con người (Human-in-the-loop) khi AI gặp câu hỏi ngoài phạm vi hoặc nhận phản hồi tiêu cực.
- **Điều kiện cần chuẩn bị trước buổi 2 để dựng AI workflow/Case 10:**
  - Nghiên cứu sơ đồ luồng dữ liệu của Case 10 (Smart Ticket Triage).
  - Chuẩn bị dữ liệu mẫu từ file excel `smart_ticket_triage.xlsx`.
  - Hiểu cách cấu hình API Gateway hoặc kết nối cơ sở dữ liệu trên n8n để phục vụ bài thực hành session 02.
