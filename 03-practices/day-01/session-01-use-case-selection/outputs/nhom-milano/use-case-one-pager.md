---
mo-ta: phieu mo ta case nhom milano chon o muc ban nhap session 01 - Tro ly chinh sach nhan su gia lap
trang-thai: active
phien-ban: v0.1
created-at: 2026-06-08 11:15 +07:00
updated-at: 2026-06-08 11:15 +07:00
---

# Phiếu mô tả trường hợp sử dụng 01 trang

## Thông tin chung

| Mục | Nội dung |
| --- | --- |
| Tên nhóm | nhom-milano |
| Tên bài toán | Trợ lý chính sách nhân sự giả lập |
| Người dùng chính | Nhân viên (cần tra cứu thông tin nghỉ phép, công tác phí, xác nhận công tác) và Nhân sự trực ban / HRBP (cần giải đáp thắc mắc của nhân viên) |
| Người chịu trách nhiệm trình bày | Nhóm Milano |
| Phiên bản | v0.1 |

## Mô tả bài toán

Hiện tại, việc tra cứu các quy định, chính sách nhân sự về nghỉ phép, công tác phí và xác nhận công tác của nhân viên hoàn toàn thủ công. Nhân viên phải tự tìm kiếm trong các văn bản hướng dẫn dài dòng hoặc gửi câu hỏi trực tiếp đến bộ phận nhân sự. Điều này dẫn đến sự lặp đi lặp lại của các câu hỏi cơ bản, gây quá tải cho bộ phận nhân sự và kéo dài thời gian chờ đợi phản hồi của nhân viên. Hệ thống Trợ lý AI giả lập được xây dựng nhằm hỗ trợ nhân viên tra cứu nhanh chóng và chính xác các thông tin cơ bản từ tài liệu FAQ giả lập, giúp tự động hóa khâu trả lời ban đầu và giảm thiểu thời gian xử lý thủ công.

## Đầu vào

| Loại đầu vào | Mô tả | Nguồn dữ liệu mô phỏng |
| --- | --- | --- |
| Tài liệu | Văn bản FAQ về chính sách nghỉ phép, công tác phí và xác nhận công tác giả lập | `synthetic-data/sample-hr-policy-faq.md` |
| Bảng dữ liệu | Không áp dụng (hoặc bảng quy tắc định tuyến câu hỏi) | Tự xây dựng trong kịch bản giả lập |
| Log/ticket/email | Câu hỏi bằng ngôn ngữ tự nhiên của nhân viên liên quan đến chính sách nhân sự | Câu hỏi giả lập do nhóm tự biên soạn |

## Đầu ra mong muốn

| Đầu ra | Định dạng | Người sử dụng |
| --- | --- | --- |
| Câu trả lời ngắn gọn, chính xác | Văn bản (Markdown) kèm trích dẫn điều khoản cụ thể từ tài liệu FAQ | Nhân viên tra cứu |
| Khuyến nghị & thông tin liên hệ HR | Văn bản hướng dẫn (nếu câu hỏi nằm ngoài tài liệu FAQ hoặc cần duyệt đặc biệt) | Nhân viên tra cứu |

## Giá trị kỳ vọng

- **Thời gian tiết kiệm dự kiến:** Tiết kiệm khoảng 80% thời gian tra cứu của nhân viên (từ 15 phút tìm kiếm thủ công xuống dưới 1 phút phản hồi từ AI) và giảm 50% số lượng câu hỏi trùng lặp gửi đến bộ phận nhân sự.
- **Lỗi hoặc thiếu sót muốn giảm:** Hạn chế tối đa việc nhân viên hiểu sai quy trình đăng ký nghỉ phép hoặc chuẩn bị thiếu hóa đơn thanh toán công tác phí.
- **Chỉ số đo hiệu quả:** Tỷ lệ câu hỏi được AI giải đáp thành công và có trích dẫn nguồn đúng (> 90%), thời gian phản hồi trung bình (< 5 giây), mức độ hài lòng của nhân viên (đạt trên 4.5/5 sao).

## Phạm vi bản thử nghiệm tối thiểu (MVP)

- **Chỉ xử lý:** 
  - Tra cứu các thông tin có sẵn trong tệp `sample-hr-policy-faq.md` (bao gồm: quy tắc xin nghỉ phép trước 2 ngày và duyệt bởi quản lý; điều kiện công tác phí cần đề nghị trước chuyến đi và hóa đơn hợp lệ; thời hạn phản hồi giấy xác nhận công tác trong 3 ngày làm việc).
- **Chưa xử lý:**
  - Không truy cập hoặc xử lý thông tin cá nhân cụ thể của nhân viên (như số ngày phép còn lại, bảng lương chi tiết, lịch sử công tác).
  - Không thực hiện các hành động ghi hoặc thay đổi dữ liệu trên các hệ thống quản trị nhân sự thật.
  - Từ chối các câu hỏi nằm ngoài phạm vi chính sách nhân sự được cung cấp.
- **Điều kiện để xem là hoàn thành:**
  - Hệ thống phân loại đúng loại câu hỏi của nhân viên.
  - Đưa ra câu trả lời khớp với nội dung FAQ giả lập, trích dẫn chính xác nguồn thông tin.
  - Đối với câu hỏi nằm ngoài phạm vi FAQ, trợ lý từ chối khéo léo và hướng dẫn người dùng liên hệ bộ phận nhân sự (HRBP).

## Kiểm soát rủi ro

| Rủi ro | Cách kiểm soát |
| --- | --- |
| Dữ liệu thật hoặc nhạy cảm | Chỉ sử dụng dữ liệu FAQ giả lập và câu hỏi giả định; tuyệt đối không đưa thông tin cá nhân thật (PII) hoặc dữ liệu thật của VTN vào hệ thống. |
| AI trả lời sai | Đính kèm thông báo miễn trừ trách nhiệm (disclaimer) nêu rõ đây là hệ thống trợ giúp giả lập; khuyến nghị nhân viên kiểm tra lại chính sách chính thức của đơn vị. |
| Đầu ra vượt phạm vi | Thiết lập system prompt (lan can an toàn) chặt chẽ, giới hạn AI chỉ được trả lời dựa trên ngữ cảnh FAQ được cung cấp, không tự suy diễn thông tin bên ngoài. |
| Thiếu truy vết | Lưu trữ nhật ký vận hành gồm: câu hỏi của người dùng (đã ẩn danh), câu trả lời của AI, nguồn trích dẫn và phiên bản prompt được áp dụng. |

## Điểm con người duyệt

- **Human-in-the-loop (HITL):**
  - **Phía người dùng:** Nhân viên tự kiểm tra lại câu trả lời và đối chiếu với nguồn trích dẫn chính thức được AI hiển thị trước khi tiến hành thực hiện các thủ tục hành chính.
  - **Phía quản trị:** Đối với các câu hỏi phức tạp vượt quá phạm vi tài liệu FAQ hoặc khi người dùng đánh giá phản hồi của AI không hữu ích (dưới 3 sao), hệ thống sẽ tự động chuyển tiếp câu hỏi kèm theo lịch sử trò chuyện sang phòng Nhân sự (HRBP) để nhân viên nhân sự thực tế kiểm duyệt và giải đáp trực tiếp.

## Dữ liệu mô phỏng và bàn giao sang buổi 2

- **Dữ liệu mô phỏng cần chuẩn bị:** File FAQ chính sách nhân sự giả lập dạng Markdown (`sample-hr-policy-faq.md`).
- **Quy tắc định tuyến hoặc phân loại:** Bộ quy tắc phân loại câu hỏi đầu vào thành các chủ đề: `Nghỉ phép`, `Công tác phí`, `Xác nhận công tác` và `Khác (Ngoài phạm vi)`.
- **Điểm con người duyệt:** Tạo cờ `hitl_trigger` tự động bật lên khi câu hỏi thuộc nhóm `Khác (Ngoài phạm vi)` hoặc khi người dùng nhấn nút "Yêu cầu gặp HRBP".
- **Trường nhật ký vận hành cần ghi:** `session_id`, `timestamp`, `category_detected`, `ai_response`, `source_citation`, `hitl_triggered` (True/False), `user_rating`.
- **Bài học áp dụng cho Case 10 - Smart Ticket Triage:** Quy trình phân loại tự động kết hợp định tuyến dựa trên nội dung (routing logic) và cơ chế kích hoạt con người kiểm duyệt (HITL) khi gặp ticket thuộc nhóm không xác định (Unknown) là bài học cốt lõi sẽ được áp dụng trực tiếp để thiết kế workflow cho Case 10.
