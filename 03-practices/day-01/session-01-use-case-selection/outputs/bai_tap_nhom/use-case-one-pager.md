---
mo-ta: phieu mo ta truong hop su dung mot trang cho bai toan phan tich cam xuc khao sat noi bo cua nhom ho tro
trang-thai: active
phien-ban: v2.2
created-at: 2026-05-17 13:54 +07:00
updated-at: 2026-06-11 11:30 +07:00
---

# Phiếu mô tả trường hợp sử dụng: use case 01 trang

## Thông tin chung

| Mục | Nội dung |
| --- | --- |
| Tên nhóm | Nhóm Hỗ trợ |
| Tên bài toán | Công cụ phân tích cảm xúc và tổng hợp từ khóa khảo sát nội bộ (tiếng Việt: Feedback Sentiment Analyzer) |
| Người dùng chính | Chuyên viên đào tạo, Chuyên viên truyền thông nội bộ, Quản lý chất lượng |
| Người chịu trách nhiệm trình bày | Đại diện Nhóm Hỗ trợ |
| Phiên bản | v2.2 |

## Mô tả bài toán

Trong hoạt động quản lý chất lượng và đào tạo nội bộ tại Viettel Network (VTN), đơn vị thường xuyên thực hiện các cuộc khảo sát ý kiến nhân viên định kỳ. Tuy nhiên, phần câu hỏi mở (tiếng Anh: open-ended questions) chứa rất nhiều ý kiến phản hồi sâu sắc bằng văn bản tự do nhưng lại đang bị bỏ qua hoặc chỉ được đọc lướt do số lượng lên tới hàng ngàn dòng, tốn khoảng 8 giờ làm việc thủ công của chuyên viên để tổng hợp. Việc này làm chậm tiến trình cải tiến liên tục (tiếng Nhật: Kaizen) và có nguy cơ bỏ lọt các phản hồi nhạy cảm hoặc khủng hoảng nội bộ. Công cụ phân tích cảm xúc và tổng hợp từ khóa khảo sát nội bộ ứng dụng mô hình ngôn ngữ lớn (tiếng Anh: Large Language Model - LLM) thấu hiểu ngữ cảnh xuất sắc sẽ tự động hóa việc đọc, phân loại cảm xúc, trích xuất ý chính và cảnh báo sớm phản hồi tiêu cực cho chuyên viên kiểm duyệt.

## Đầu vào

| Loại đầu vào | Mô tả | Nguồn dữ liệu mô phỏng |
| --- | --- | --- |
| Tài liệu | Hướng dẫn định nghĩa thang đo cảm xúc và các bộ tiêu chí phân loại của đơn vị | Dữ liệu mô phỏng: file chính sách/quy chuẩn nội bộ |
| Bảng dữ liệu | Bảng dữ liệu dạng CSV chứa phản hồi của nhân viên gồm các trường: mã định danh: ID, phòng ban, nội dung phản hồi khảo sát mở | Dữ liệu mô phỏng: bảng CSV chứa 100 câu phản hồi giả lập, đa dạng sắc thái |
| Log/ticket/email | Không áp dụng | Không áp dụng |

## Đầu ra mong muốn

| Đầu ra | Định dạng | Người sử dụng |
| --- | --- | --- |
| Báo cáo kết quả phân tích cảm xúc chi tiết | Bảng dữ liệu dạng CSV bổ sung các cột: nhãn cảm xúc (Tích cực/Tiêu cực/Trung tính), điểm tự tin: confidence score, từ khóa chính: keywords, và ý tóm tắt chính | Chuyên viên đào tạo, Chuyên viên truyền thông nội bộ |
| Báo cáo tổng hợp xu hướng và kiến nghị | Văn bản báo cáo dạng Markdown tổng hợp tỷ lệ cảm xúc: sentiment ratio, 3 xu hướng chính nổi bật và đề xuất hành động tương ứng | Quản lý chất lượng, Lãnh đạo đơn vị |

## Giá trị kỳ vọng

- **Thời gian tiết kiệm dự kiến**: Giảm thời gian xử lý và làm báo cáo hậu kiểm (tiếng Anh: post-mortem report) từ 8 giờ xuống còn 1 giờ cho mỗi đợt khảo sát 1000 mẫu.
- **Lỗi hoặc thiếu sót muốn giảm**: Hạn chế tối đa việc bỏ lọt phản hồi nhạy cảm; giảm thiểu sự chủ quan hoặc thiên kiến cá nhân của người đọc thủ công khi gán nhãn cảm xúc.
- **Chỉ số đo hiệu quả**: 
  - Thời gian hoàn thành báo cáo phân tích cảm xúc giảm từ 8 giờ xuống dưới 1 giờ.
  - Tỷ lệ phát hiện chính xác phản hồi nhạy cảm/tiêu cực đạt trên 90%.

## Phạm vi sản phẩm khả dụng tối thiểu: minimum viable product (MVP)

- **Chỉ xử lý**:
  - Đọc đầu vào gồm 100 câu nhận xét mẫu từ file CSV.
  - Phân loại chính xác 3 nhãn cảm xúc cơ bản: Tích cực (Positive), Tiêu cực (Negative), Trung tính (Neutral) kèm điểm tự tin: confidence score.
  - Trích xuất tối đa 3 ý chính đại diện và tổng hợp 3 khuyến nghị nổi bật nhất.
  - Nhận diện đúng các câu mỉa mai: sarcasm trong văn cảnh cơ bản của nhân viên Việt Nam.
- **Chưa xử lý**:
  - Chưa kết nối trực tiếp đến giao diện lập trình ứng dụng: API của các hệ thống khảo sát thời gian thực (như Microsoft Forms, Google Forms).
  - Chưa tự động hóa gửi thông báo cảnh báo qua các ứng dụng chat (như Mocha, Telegram) hoặc Email/SMS đến Lãnh đạo.
- **Điều kiện để xem là hoàn thành**:
  - Hệ thống chạy thông suốt quy trình làm việc AI: AI workflow xử lý hàng loạt tập tin CSV mô phỏng.
  - Nhận diện đúng cảm xúc của ít nhất 90% câu phản hồi mẫu và tóm tắt chính xác 3 xu hướng ý kiến chính.

## Kiểm soát rủi ro

| Rủi ro | Cách kiểm soát |
| --- | --- |
| Dữ liệu thật hoặc nhạy cảm | Chỉ sử dụng dữ liệu mô phỏng, tuyệt đối không dùng thông tin cá nhân thật của nhân viên VTN |
| AI trả lời sai hoặc gán nhãn nhầm | Thiết lập cơ chế con người trong vòng lặp: human in the loop (HITL) để duyệt lại các kết quả có điểm tự tin: confidence score thấp |
| Đầu ra vượt phạm vi hoặc phản hồi lệch lạc | Cài đặt lan can an toàn: guardrail nghiêm ngặt trong hướng dẫn hệ thống chỉ tập trung vào phân tích khảo sát nội bộ |
| Thiếu truy vết và kiểm thử | Ghi nhật ký vận hành: operation log đầy đủ phiên bản lời nhắc: prompt, đầu vào mẫu, nhãn phân loại và điểm tự tin |

## Điểm con người duyệt

Thiết lập bước con người trong vòng lặp: human in the loop (HITL) để chuyên viên nhân sự/đào tạo duyệt lại:
1. Toàn bộ các phản hồi bị gán nhãn "Tiêu cực" để kịp thời có phương án truyền thông.
2. Các phản hồi có điểm tự tin: confidence score của AI dưới 0.7 để hiệu chỉnh nhãn và ý chính thủ công trước khi xuất báo cáo tổng hợp cuối cùng.

## Dữ liệu mô phỏng và bàn giao sang buổi 2

Liệt kê các dữ liệu mô phỏng và bảng quy tắc có thể dùng để dựng quy trình làm việc AI: AI workflow ở buổi 2, áp dụng bài học từ Smart Ticket Triage:

- **Dữ liệu mô phỏng cần chuẩn bị**: File CSV chứa 100 dòng phản hồi mẫu của nhân viên (gồm các nội dung như phàn nàn về công cụ làm việc, khen ngợi chương trình đào tạo, trung lập về chính sách gửi xe, mỉa mai về giờ làm việc).
- **Quy tắc định tuyến hoặc phân loại**: 
  - Nếu nhãn cảm xúc là "Tiêu cực" AND điểm tự tin: confidence score > 0.8: Định tuyến vào luồng cảnh báo khẩn cấp cho chuyên viên truyền thông.
  - Nếu điểm tự tin: confidence score <= 0.7: Định tuyến vào luồng "Chờ duyệt thủ công".
- **Điểm con người duyệt**: Giao diện duyệt nhanh (approve/reject/edit) nhãn cảm xúc và ý chính của AI.
- **Trường nhật ký vận hành cần ghi**: `ID`, `phong_ban`, `noi_dung_phoi`, `nhan_cam_xuc`, `diem_tu_tin`, `tu_khoa`, `trang_thai_duyet`, `thoi_gian_ghi_log`.
