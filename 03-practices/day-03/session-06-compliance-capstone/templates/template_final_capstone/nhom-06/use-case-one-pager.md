---
mo-ta: Phieu mo ta truong hop su dung 01 trang - Case 1: Tro ly du an gia lap
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-08 11:20 +07:00
updated-at: 2026-06-08 11:20 +07:00
---

# Phiếu mô tả trường hợp sử dụng 01 trang

## Thông tin chung

| Mục | Nội dung |
| --- | --- |
| Tên nhóm | Nhóm 06 |
| Tên bài toán | Trợ lý dự án giả lập (Project Assistant Simulation) |
| Người dùng chính | Project Manager (PM), Sub-Project Manager (subPM) 
| Người chịu trách nhiệm trình bày | Trưởng nhóm 06 |
| Phiên bản | v0.1 |

## Mô tả bài toán

Hiện nay, các PM và subPM phải theo dõi tiến độ dự án bằng cách đọc thủ công các báo cáo tuần, lục tìm lịch sử tin nhắn cập nhật từ các nhóm chat của nhân sự phụ trách và tổng hợp lại vào các bảng tiến độ. Việc này lặp đi lặp lại hàng ngày/hàng tuần, tốn nhiều thời gian và dễ dẫn đến sai sót hoặc trễ hạn phát hiện chậm tiến độ. Trợ lý AI được xây dựng nhằm giúp PM truy vấn nhanh chóng, chính xác về tiến độ lũy kế và các chỉ số dự án bằng ngôn ngữ tự nhiên dựa trên dữ liệu mô phỏng được cung cấp, đồng thời đưa ra nguồn trích dẫn rõ ràng để PM đối chiếu.

## Đầu vào

| Loại đầu vào | Mô tả | Nguồn dữ liệu mô phỏng |
| --- | --- | --- |
| Tài liệu | Tài liệu mô tả dự án (Project Charter, WBS mô phỏng) | `project_charter_mock.txt` chứa thông tin về mục tiêu, phạm vi và kế hoạch tổng thể của dự án. |
| Bảng dữ liệu | Bảng theo dõi tiến độ và chỉ số KPI | `project_progress_mock.csv` chứa danh sách task, nhân sự phụ trách, ngày bắt đầu/kết thúc, trạng thái và % hoàn thành. |
| Log/ticket/email | Tin nhắn cập nhật tiến độ hàng ngày từ nhân sự | `chat_logs_mock.json` mô phỏng các đoạn hội thoại cập nhật tiến độ công việc hàng ngày từ các thành viên dự án. |

## Đầu ra mong muốn

| Đầu ra | Định dạng | Người sử dụng |
| --- | --- | --- |
| Báo cáo tiến độ lũy kế theo từng nhân sự phụ trách | Văn bản tóm tắt có cấu trúc (bảng hoặc danh sách bullet points) | PM, subPM |
| Nguồn trích dẫn từ tài liệu giả lập | Danh sách tài liệu tham chiếu (tên file, dòng/đoạn trích dẫn, người gửi tin nhắn, thời gian gửi tin nhắn mô phỏng) | PM, subPM |
| Khuyến nghị liên hệ nhân sự | Câu thông báo hướng dẫn liên hệ nhân sự phụ trách khi câu hỏi vượt quá phạm vi dữ liệu cung cấp | PM, subPM |

## Giá trị kỳ vọng

- Thời gian tiết kiệm dự kiến: Giảm thời gian tổng hợp tiến độ dự án từ 4 tiếng mỗi tuần xuống còn 15 phút truy vấn trực tiếp với AI (tiết kiệm ~90% thời gian tổng hợp thông tin).
- Lỗi hoặc thiếu sót muốn giảm: Giảm thiểu việc bỏ sót tin nhắn cập nhật của nhân viên; rút ngắn thời gian phát hiện chậm trễ tiến độ từ 3 ngày xuống dưới 24 giờ.
- Chỉ số đo hiệu quả: % câu hỏi về tiến độ được AI trả lời chính xác dựa trên dữ liệu đầu vào (mục tiêu > 95% sau khi có con người duyệt); số lượng cảnh báo chậm tiến độ được phát hiện kịp thời; thời gian trung bình PM cần để cập nhật tình trạng dự án.

## Phạm vi bản thử nghiệm tối thiểu (MVP)

- Chỉ xử lý: Đọc và phân tích dữ liệu tiến độ của tối đa 3 dự án giả lập; phân tích tin nhắn cập nhật dạng văn bản đơn giản của tối đa 5 nhân sự; trả lời các câu hỏi về tiến độ lũy kế kèm nguồn trích dẫn rõ ràng.
- Chưa xử lý: Chưa tích hợp trực tiếp vào các hệ thống chat thực tế (Slack, MS Teams); chưa phân tích hình ảnh, file PDF quét (scanned PDF); chưa xử lý các yêu cầu tự động điều phối nguồn lực hay tự động gửi tin nhắn nhắc nhở nhân viên.
- Điều kiện để xem là hoàn thành: AI trả lời chính xác tiến độ lũy kế của từng nhân sự từ dữ liệu mô phỏng trong ít nhất 10 kịch bản thử nghiệm; hiển thị đúng nguồn trích dẫn; đưa ra khuyến nghị liên hệ nhân sự khi câu hỏi nằm ngoài tài liệu cung cấp.

## Kiểm soát rủi ro

| Rủi ro | Cách kiểm soát |
| --- | --- |
| Dữ liệu thật hoặc nhạy cảm | Tuyệt đối chỉ dùng dữ liệu mô phỏng hoàn toàn (tên dự án, tên nhân viên giả lập như Nguyen Van A, Tran Thi B, không dùng thông tin của VTN). |
| AI trả lời sai | Bắt buộc hiển thị nguồn trích dẫn (citations) song song với câu trả lời để PM dễ dàng đối chiếu và kiểm duyệt trước khi sử dụng. |
| Đầu ra vượt phạm vi | Thiết lập bộ lọc từ chối câu hỏi (guardrails) trong Prompt. Nếu thông tin không có trong dữ liệu mô phỏng, AI phải từ chối trả lời và hướng dẫn liên hệ nhân sự. |
| Thiếu truy vết | Lưu trữ toàn bộ nhật ký hội thoại bao gồm: câu hỏi của người dùng, phiên bản prompt, câu trả lời của AI và nguồn tài liệu được truy xuất. |

## Điểm con người duyệt

PM hoặc subPM là người kiểm duyệt (HITL). PM sẽ duyệt kết quả của AI trước khi đưa vào báo cáo tuần chính thức hoặc trước khi thực hiện các quyết định quản trị dự án (như nhắc nhở nhân viên, điều chỉnh kế hoạch). Tiêu chí duyệt: Đối chiếu số liệu tiến độ lũy kế do AI tổng hợp với nội dung gốc trong file CSV và chat logs được trích dẫn để đảm bảo không có sự sai lệch hoặc tự suy diễn (hallucination).

## Dữ liệu mô phỏng và bàn giao sang buổi 2

- Dữ liệu mô phỏng cần chuẩn bị:
  1. `project_charter_mock.txt`: Tài liệu mô tả mục tiêu, phạm vi và kế hoạch 3 dự án giả lập (Project Alpha, Project Beta, Project Gamma).
  2. `project_progress_mock.csv`: Bảng chứa danh sách task, nhân sự phụ trách, ngày bắt đầu/kết thúc, trạng thái, % hoàn thành.
  3. `chat_logs_mock.json`: Tin nhắn mô phỏng cập nhật tiến độ hàng ngày từ nhân sự (ví dụ: "Nguyen Van A: Đã hoàn thành code API Login, đang chuyển sang viết testcase").
- Quy tắc định tuyến hoặc phân loại:
  - Nếu câu hỏi về tiến độ tổng thể: Tra cứu file CSV và Chat Log.
  - Nếu câu hỏi về phạm vi/yêu cầu dự án: Tra cứu file Project Charter.
  - Nếu câu hỏi về lý do chậm trễ hoặc giải pháp kỹ thuật chưa có trong tài liệu: Định tuyến yêu cầu người dùng liên hệ trực tiếp với nhân sự phụ trách dự án đó.
- Điểm con người duyệt: Giao diện web hiển thị câu trả lời của AI song song với tài liệu gốc được highlight để PM duyệt và bấm "Xác nhận/Sử dụng".
- Trường nhật ký vận hành cần ghi: `timestamp`, `user_id`, `user_query`, `ai_response`, `sources_cited`, `is_approved` (True/False), `user_feedback`.
