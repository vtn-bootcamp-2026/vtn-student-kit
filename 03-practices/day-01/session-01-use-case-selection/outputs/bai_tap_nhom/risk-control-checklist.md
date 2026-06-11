---
mo-ta: bang kiem kiem soat rui ro cho bai toan phan tich cam xuc khao sat noi bo cua nhom ho tro
trang-thai: active
phien-ban: v2.2
created-at: 2026-05-17 13:54 +07:00
updated-at: 2026-06-11 11:30 +07:00
---

# Bảng kiểm rủi ro và kiểm soát

## Dữ liệu

- [x] Không dùng dữ liệu thật của VTN
- [x] Không dùng thông tin khách hàng thật
- [x] Không dùng địa chỉ giao thức mạng: IP thật, mã trạm thật hoặc cấu hình thật
- [x] Có dữ liệu mô phỏng thay thế (CSV 100 dòng phản hồi khảo sát giả định)
- [x] Có mô tả nguồn dữ liệu mô phỏng rõ ràng

## Phân quyền và điểm kết nối

- [x] Không dùng mã thông báo: token thật
- [x] Không dùng khóa giao diện lập trình ứng dụng: API key thật
- [x] Không hard-code thông tin bí mật vào mã nguồn
- [x] Không đưa khóa giao diện lập trình ứng dụng: API key hoặc mã thông báo: token vào hướng dẫn: prompt, ảnh chụp màn hình, nhật ký: log, luồng n8n export hoặc bài nộp
- [x] Nếu mô tả điểm kết nối (tiếng Anh: endpoint), chỉ dùng điểm kết nối giả lập: mock endpoint
- [x] Quyền truy cập trong bài thực hành là quyền đọc hoặc quyền mô phỏng

## Con người trong vòng lặp: human in the loop

- [x] Có bước con người trong vòng lặp: human in the loop (HITL) để duyệt lại báo cáo
- [x] Có người chịu trách nhiệm duyệt đầu ra (Chuyên viên đào tạo/truyền thông nội bộ)
- [x] Có tiêu chí duyệt hoặc từ chối rõ ràng (ví dụ: duyệt thủ công khi điểm tự tin: confidence score < 0.7 hoặc phát hiện từ lóng nhạy cảm)
- [x] Không để AI tự quyết định các vấn đề có rủi ro kỹ thuật, pháp lý, nhân sự hoặc vận hành doanh nghiệp

## Nhật ký và truy vết

- [x] Có lưu đầu vào mẫu (nội dung câu phản hồi tự do)
- [x] Có lưu đầu ra mẫu (kết quả phân tích cảm xúc và từ khóa)
- [x] Có ghi phiên bản lời nhắc: prompt hoặc hướng dẫn vận hành
- [x] Có ghi trạng thái thành công hoặc lỗi của hệ thống
- [x] Có cách truy lại lý do AI đưa ra kết quả thông qua căn cứ trích dẫn hoặc phân tích ngữ cảnh
- [x] Nhật ký vận hành: operation log chỉ chứa dữ liệu phi nhạy cảm

## Lan can an toàn: guardrail

- [x] Có quy tắc từ chối nếu câu hỏi hoặc yêu cầu đầu vào vượt ngoài phạm vi phân tích khảo sát nội bộ
- [x] Có quy tắc không tự ý suy đoán khi dữ liệu phản hồi bị thiếu hoặc không rõ ràng
- [x] Có quy tắc yêu cầu nêu rõ căn cứ cụ thể khi trích xuất hoặc tóm tắt ý kiến nhân viên
- [x] Có quy tắc tự động chuyển sang con người xử lý khi phát hiện phản hồi có tính chất nghiêm trọng (cảnh báo khủng hoảng nội bộ)

## Kết luận

| Mục | Kết luận |
| --- | --- |
| Bài toán đủ an toàn để làm trong lớp? | **Có** |
| Điều kiện cần sửa trước khi chốt | Chuẩn bị và làm sạch tệp CSV chứa 100 câu phản hồi khảo sát mô phỏng, đảm bảo loại bỏ hoàn toàn các thông tin thật của nhân viên VTN |
| Người xác nhận | Nhóm Hỗ trợ - Feedback Sentiment Analyzer Team |

## Ghi chú

Bảng này là rà soát rủi ro sơ bộ ở buổi học 1 (tiếng Anh: session 01), không thay thế bảng kiểm tuân thủ trước khi thí điểm trong buổi học 6 (tiếng Anh: session 06).
