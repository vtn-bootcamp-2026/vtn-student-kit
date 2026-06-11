---
mo-ta: thang cham diem rubbric danh gia y tuong khao sat noi bo cho nhom ho tro
trang-thai: active
phien-ban: v2.2
created-at: 2026-05-17 13:54 +07:00
updated-at: 2026-06-11 11:30 +07:00
---

# Thang chấm điểm: rubbric lựa chọn bài toán

## Cách dùng

Chấm từng bài toán ứng viên theo thang 100 điểm. Ưu tiên bài toán đạt từ 70 điểm trở lên, không dùng dữ liệu thật và có điểm con người duyệt rõ ràng.

## Bảng điểm

| Tiêu chí | Điểm tối đa | Câu hỏi kiểm tra | Điểm nhóm tự chấm |
| --- | ---: | --- | ---: |
| Giá trị nghiệp vụ (tiếng Anh: business value) | 20 | Bài toán có giảm thời gian, giảm lỗi hoặc tăng chất lượng đầu ra không? | 18 |
| Tính khả thi trong lớp (tiếng Anh: class feasibility) | 15 | Có thể tạo bản thử nghiệm tối thiểu: minimum viable product (MVP) trong 6 buổi không? | 14 |
| Dữ liệu mô phỏng (tiếng Anh: synthetic data) | 15 | Có thể tạo dữ liệu mô phỏng đủ đại diện mà không dùng dữ liệu thật không? | 15 |
| Mức độ đo lường (tiếng Anh: measurability) | 10 | Có chỉ số đo hiệu quả tối thiểu không? | 10 |
| Khả năng phát triển (tiếng Anh: scalability) | 10 | Bài toán có thể mở rộng sau lớp mà không đổi toàn bộ thiết kế không? | 9 |
| Kiểm soát rủi ro (tiếng Anh: risk control) | 20 | Có điểm con người duyệt, ghi nhật ký: logging, truy vết: trace và lan can an toàn: guardrail không? | 19 |
| Năng lực AI phù hợp (tiếng Anh: AI capability alignment) | 10 | AI có phù hợp với tác vụ đọc, tóm tắt, phân loại, trích xuất hoặc tạo nháp không? | 10 |
| **Tổng** | **100** | | **95** |

## Quy tắc loại nhanh

Loại hoặc thu hẹp bài toán nếu có một trong các điều kiện sau:

- Cần dữ liệu thật của VTN.
- Cần token thật, khóa giao diện lập trình ứng dụng: API key thật hoặc chứng thư số: certificate thật.
- Cần quyền ghi hoặc thực thi trên hệ thống thật.
- Không có người duyệt trước khi sử dụng đầu ra.
- Không mô tả được đầu vào hoặc đầu ra.
- Không thể đo hiệu quả tối thiểu.

## Kết luận nhóm

- **Bài toán được chọn**: Công cụ phân tích cảm xúc và tổng hợp từ khóa khảo sát nội bộ (tiếng Việt: Feedback Sentiment Analyzer).
- **Tổng điểm**: 95/100.
- **Lý do chọn**: Bài toán đạt điểm rất cao về năng lực AI phù hợp (LLM xử lý văn bản, cảm xúc và tóm tắt cực tốt), tính khả thi chuẩn bị dữ liệu mô phỏng cao (chỉ cần tạo CSV 100 câu phản hồi khảo sát mở), và mang lại giá trị nghiệp vụ rõ ràng khi giảm thời gian lập báo cáo của chuyên viên từ 8 giờ xuống 1 giờ, đáp ứng quy tắc an toàn tuyệt đối khi không sử dụng dữ liệu thật của VTN.
- **Danh sách quy trình ưu tiên của nhóm**:
  1. Xây dựng bộ dữ liệu mô phỏng chứa 100 câu phản hồi tự do bằng tiếng Việt với nhiều sắc thái (tích cực, tiêu cực, mỉa mai, trung tính).
  2. Dựng luồng phân tích cảm xúc và chấm điểm tự tin: confidence score bằng LLM.
  3. Xây dựng luồng trích xuất từ khóa: keywords và tóm tắt ý chính.
  4. Triển khai nhánh con người trong vòng lặp: human in the loop (HITL) để duyệt các phản hồi tiêu cực hoặc có độ tự tin thấp.
- **Điều kiện cần chuẩn bị trước buổi 2 để dựng quy trình làm việc AI: AI workflow**: 
  - File dữ liệu mô phỏng dạng CSV đã làm sạch cấu trúc.
  - Định nghĩa chuẩn thang phân loại cảm xúc (Tích cực/Tiêu cực/Trung tính) và định nghĩa thế nào là phản hồi khẩn cấp cần cảnh báo ngay.
