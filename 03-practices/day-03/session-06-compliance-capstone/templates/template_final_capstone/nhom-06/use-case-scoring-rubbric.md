---
mo-ta: Bang tu cham diem rubric cho bai toan - Case 1: Tro ly du an gia lap
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-08 11:20 +07:00
updated-at: 2026-06-08 11:20 +07:00
---

# Thang chấm điểm (rubbric) lựa chọn bài toán

## Cách dùng

Chấm từng bài toán ứng viên theo thang 100 điểm. Ưu tiên bài toán đạt từ 70 điểm trở lên, không dùng dữ liệu thật và có điểm con người duyệt rõ ràng.

## Bảng điểm

| Tiêu chí | Điểm tối đa | Câu hỏi kiểm tra | Điểm nhóm tự chấm | Giải trình ngắn gọn |
| --- | ---: | --- | ---: | --- |
| Giá trị nghiệp vụ | 20 | Bài toán có giảm thời gian, giảm lỗi hoặc tăng chất lượng đầu ra không? | 18 | Giúp PM/subPM cắt giảm 90% thời gian tổng hợp thủ công dữ liệu tiến độ từ chat log và Excel, đồng thời tránh bỏ sót chậm trễ. |
| Tính khả thi trong lớp | 15 | Có thể tạo bản thử nghiệm tối thiểu (MVP) trong 6 buổi không? | 14 | Cực kỳ khả thi. Cấu trúc bài toán RAG trên tài liệu text, CSV tiến độ và JSON chat logs có thể dễ dàng dựng và kiểm thử nhanh. |
| Dữ liệu mô phỏng | 15 | Có thể tạo dữ liệu mô phỏng đủ đại diện mà không dùng dữ liệu thật không? | 15 | Dễ dàng mô phỏng dữ liệu tên dự án, tên thành viên giả định, file CSV tiến độ và chat log hội thoại mà không động tới dữ liệu thật của VTN. |
| Mức độ đo lường | 10 | Có chỉ số đo hiệu quả tối thiểu không? | 9 | Có chỉ số đo lường cụ thể gồm: thời gian tổng hợp tiến độ của PM, tỷ lệ AI trả lời chính xác có trích dẫn đúng, thời gian trễ phát hiện sự cố. |
| Khả năng phát triển | 10 | Bài toán có thể mở rộng sau lớp mà không đổi toàn bộ thiết kế không? | 8 | Có thể tích hợp thông qua Webhook API của các nền tảng chat doanh nghiệp (MS Teams, Slack) và các công cụ quản lý Task (Jira, Redmine) thật. |
| Kiểm soát rủi ro | 20 | Có điểm con người duyệt, logging, trace và guardrail không? | 18 | Cơ chế HITL chặt chẽ (PM duyệt đối chiếu nguồn trích dẫn trước khi dùng); có guardrails từ chối trả lời nếu thiếu căn cứ; lưu log đầy đủ. |
| Năng lực AI phù hợp | 10 | AI có phù hợp với tác vụ đọc, tóm tắt, phân loại, trích xuất hoặc tạo nháp không? | 10 | Tận dụng tuyệt đối thế mạnh của LLM trong đọc hiểu ngữ cảnh văn bản không cấu trúc (chat logs) và trích xuất/tổng hợp thông tin theo cấu trúc. |
| **Tổng** | **100** | | **92** | |

## Quy tắc loại nhanh

Loại hoặc thu hẹp bài toán nếu có một trong các điều kiện sau:

- Cần dữ liệu thật của VTN. (Đã kiểm tra: Không cần)
- Cần token thật, API key thật hoặc certificate thật. (Đã kiểm tra: Không cần)
- Cần quyền ghi hoặc thực thi trên hệ thống thật. (Đã kiểm tra: Không cần, chỉ đọc dữ liệu mô phỏng)
- Không có người duyệt trước khi sử dụng đầu ra. (Đã kiểm tra: PM duyệt trước khi xuất báo cáo)
- Không mô tả được đầu vào hoặc đầu ra. (Đã kiểm tra: Đầu vào và đầu ra đã được mô tả chi tiết và rõ ràng)
- Không thể đo hiệu quả tối thiểu. (Đã kiểm tra: Có các chỉ số đo lường cụ thể)

## Kết luận nhóm

- **Bài toán được chọn**: Trợ lý dự án giả lập (Project Assistant Simulation).
- **Tổng điểm**: 92 / 100 điểm.
- **Lý do chọn**: Bài toán có tính thực tiễn cực kỳ cao trong công việc hàng ngày của PM, giúp giảm tải công việc hành chính tổng hợp số liệu. Giải pháp an toàn 100% nhờ việc sử dụng dữ liệu mô phỏng hoàn toàn trong môi trường lớp học, quy trình nghiệp vụ rõ ràng, khả thi để hoàn thành MVP trong 6 buổi học và có cơ chế HITL đảm bảo độ tin cậy.
- **Danh sách quy trình ưu tiên của nhóm**:
  1. Xây dựng cấu trúc dữ liệu mô phỏng (Charter, CSV progress, JSON chat logs).
  2. Thiết lập quy trình RAG (Retrieval-Augmented Generation) để truy vấn thông tin dự án.
  3. Xây dựng prompt chuyên biệt cho AI bao gồm các guardrails về trích dẫn và giới hạn phạm vi trả lời.
  4. Thiết kế giao diện HITL để PM kiểm duyệt và so sánh dữ liệu AI trả về với tài liệu gốc.
- **Điều kiện cần chuẩn bị trước buổi 2 để dựng AI workflow/Case 10**:
  - Tạo sẵn bộ dữ liệu giả lập gồm 3 file: `project_charter_mock.txt`, `project_progress_mock.csv`, `chat_logs_mock.json`.
  - Định nghĩa sẵn bộ quy tắc trích dẫn nguồn (như định dạng trích dẫn tên file, dòng, timestamp và người gửi).
  - Chuẩn bị sẵn khung kịch bản test với 10 câu hỏi từ PM đại diện cho các mức độ phức tạp khác nhau.
