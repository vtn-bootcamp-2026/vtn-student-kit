---
mo-ta: loi nhac dong sang tao y tuong khao sat noi bo cho nhom ho tro
trang-thai: active
phien-ban: v1.2
created-at: 2026-05-26 12:09 +07:00
updated-at: 2026-06-11 11:30 +07:00
---

# Lời nhắc đồng sáng tạo trường hợp sử dụng: use case cùng AI

## Cách sử dụng

Học viên sao chép toàn bộ nội dung lời nhắc: prompt bên dưới để gửi cho trợ lý AI Antigravity trên IDE nhằm tự động đồng sáng tạo và làm mịn chi tiết cho 3 tài liệu: One-Pager, thang chấm điểm: rubbric và Risk Checklist của bài toán được chọn.

## Nội dung lời nhắc thực tế của Nhóm Hỗ trợ

```text
Bạn là trợ lý AI chuyên nghiệp về thiết kế và đánh giá các trường hợp sử dụng: use cases trong doanh nghiệp.

Tôi có một ý tưởng bài toán muốn triển khai trí tuệ nhân tạo: AI tại đơn vị dựa trên danh sách bài toán ưu tiên của VTN:

- Tên bài toán: Công cụ phân tích cảm xúc và tổng hợp từ khóa khảo sát nội bộ (tiếng Việt: Feedback Sentiment Analyzer).
- Mô tả công việc thủ công hiện tại: Hàng tháng và hàng quý, chuyên viên đào tạo và truyền thông nội bộ tại VTN phải thu thập khảo sát ý kiến nhân viên. Phần phản hồi tự do bằng chữ (tiếng Anh: open-ended questions) lên tới hàng ngàn dòng. Chuyên viên phải đọc thủ công từng dòng để gán nhãn thái độ và tóm tắt ý kiến đóng góp, tốn trung bình 8 giờ làm việc, dễ mệt mỏi dẫn đến bỏ sót các phản hồi nhạy cảm hoặc nhận định mang tính cảm tính, chủ quan.
- Mong muốn AI hỗ trợ: Ứng dụng quy trình làm việc AI: AI workflow để tự động xử lý hàng loạt tập tin CSV chứa nhận xét. AI tự động đọc nhận xét, gán nhãn cảm xúc (Tích cực/Tiêu cực/Trung tính), chấm điểm tự tin: confidence score, nhận diện mỉa mai: sarcasm, trích xuất từ khóa chính và tổng hợp 3 xu hướng ý kiến chính. Đồng thời, thiết lập nhánh con người trong vòng lặp: human in the loop (HITL) để chuyên viên duyệt lại các ca nhạy cảm hoặc có điểm tự tin thấp.

Hãy giúp tôi đồng sáng tạo và tự động phác thảo nội dung chi tiết cho 3 tài liệu sau dưới dạng Markdown (chỉ sử dụng dữ liệu mô phỏng, không suy đoán dữ liệu thật):

1. Nội dung cho "Phiếu mô tả trường hợp sử dụng 01 trang" (One-Pager):
   - Đề xuất người dùng chính (tiếng Anh: primary user), đầu vào dự kiến (tiếng Anh: input) và đầu ra mong muốn (tiếng Anh: output).
   - Xác định giá trị kỳ vọng (thời gian tiết kiệm làm báo cáo hậu kiểm: post-mortem report, chỉ số đo hiệu quả).
   - Xác định phạm vi sản phẩm khả dụng tối thiểu: minimum viable product (MVP) - những gì CHƯA xử lý để đảm bảo an toàn.
   - Đề xuất điểm dừng kiểm duyệt của con người trong vòng lặp: human in the loop (HITL).

2. Bảng chấm điểm sơ bộ theo "thang chấm điểm: rubbric" (Scoring Rubbric):
   - Đánh giá sơ bộ điểm số của bài toán này theo các tiêu chí: tính khả thi của dữ liệu, mức độ lặp lại, khả năng đo lường, rủi ro bảo mật và sự tham gia của con người (HITL).
   - Đưa ra điểm số ước lượng trên thang điểm 100 và nhận xét ngắn gọn.

3. Bản rà soát "Danh sách kiểm tra rủi ro" (Risk Checklist):
   - Phân tích 3-4 rủi ro bảo mật thông tin và tuân thủ dữ liệu cá nhân nhạy cảm (tiếng Anh: personally identifiable information - PII).
   - Đề xuất các lan can an toàn: guardrails tương ứng để kiểm soát rủi ro.

Yêu cầu ràng buộc:
- Tuyệt đối không sử dụng hoặc suy đoán bất kỳ dữ liệu thật, tên khách hàng thật, số điện thoại thật hoặc thông tin nhạy cảm của VTN.
- Đảm bảo có cơ chế con người kiểm duyệt (HITL) rõ ràng trước khi sử dụng kết quả của AI.
- Chỉ trả lời bằng tiếng Việt.
```
