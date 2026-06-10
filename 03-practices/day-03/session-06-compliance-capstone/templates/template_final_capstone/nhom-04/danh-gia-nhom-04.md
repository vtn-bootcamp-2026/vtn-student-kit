---
mo-ta: Báo cáo đánh giá dự án Capstone của Nhóm 04 - VTN HR Policy Assistant
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 16:30 +07:00"
updated-at: "2026-06-10 16:30 +07:00"
---

# Báo cáo đánh giá dự án Capstone nhóm 04

*   **Tên dự án ứng dụng:** VTN HR Policy Assistant — Trợ lý AI tra cứu chính sách nhân sự nội bộ
*   **Đối tượng đánh giá:** Nhóm 04 (Nhóm học viên AI Builders - Nhóm 1 VTN trên tài liệu)
*   **Hội đồng giám khảo:** Ban giám khảo chuyên môn Viettel Net
*   **Mốc thời gian đánh giá:** Tháng 5 năm 2026 (May 2026)

---

## 1. Kết quả kiểm tra hồ sơ bài nộp
Hội đồng đã thực hiện rà soát các thành phần tài liệu và mã nguồn trong thư mục bài nộp của Nhóm 04 và ghi nhận trạng thái như sau:

| STT | Thành phần hồ sơ | Tên tệp tin | Trạng thái nộp | Đánh giá sơ bộ |
| :--- | :--- | :--- | :---: | :--- |
| 1 | Mã nguồn ứng dụng | `web-mvp/server.py`<br>`web-mvp/app.js`<br>`web-mvp/index.html`<br>`web-mvp/style.css` | Đã nộp | Mã nguồn hoàn thiện, có đầy đủ giao diện web tương tác một trang: Single Page Application (SPA), tích hợp bộ máy tìm kiếm RAG cục bộ bằng Python: local Python RAG engine và cơ chế gọi API Gateway. |
| 2 | Phiếu mô tả dự án | `capstone_project/use-case-one-pager.md` | Đã nộp | Nội dung nghiệp vụ chi tiết, phân tích kỹ hiện trạng, giải pháp RAG và KPI. Lỗi nhỏ: ghi sai tên nhóm là Nhóm 1. |
| 3 | Sơ đồ luồng logic | `capstone_project/logical-workflow.md` | Đã nộp | Đầy đủ sơ đồ Mermaid và mô tả các bước chi tiết. Lỗi nhỏ: ghi sai tên nhóm là Nhóm 1. |
| 4 | Đặc tả lời nhắc cốt lõi | `capstone_project/core-prompt-design.md` | Đã nộp | Có đặc tả lời nhắc hệ thống: system prompt chi tiết, JSON Schema đầu ra và nhật ký kiểm thử thủ công. Lỗi nhỏ: ghi sai tên nhóm là Nhóm 1. |
| 5 | Bảng tự kiểm tuân thủ | `capstone_project/compliance-checklist.md` | Đã nộp | Điền chi tiết 11 tiêu chí bảo mật thông tin nội bộ. Lỗi nhỏ: ghi sai tên nhóm là Nhóm 1. |
| 6 | Lộ trình áp dụng thực tế | `capstone_project/action-plan-30-90-days.md` | Đã nộp | Có lộ trình chi tiết 30/90 ngày và 3 trường hợp sử dụng: use cases tiếp theo. Lỗi nhỏ: ghi sai tên nhóm là Nhóm 1. |
| 7 | Các tài liệu vận hành phụ | `capstone_project/failure-modes-rollback.md`<br>`capstone_project/handoff-contract.md`<br>`capstone_project/runbook-template.md`<br>`capstone_project/test-cases-specification.md` | Đã nộp | Đầy đủ các biểu mẫu vận hành và bàn giao theo tiêu chuẩn. |
| 8 | Bản trình bày bảo vệ | `slide-presentation.html`<br>`web-mvp/slide.html` | Đã nộp | Slide trình bày thiết kế hiện đại bằng Reveal.js gồm 5 trang đầy đủ nội dung. Lỗi nhỏ: ghi sai tên nhóm là Nhóm 1. |

---

## 2. Đánh giá chi tiết theo từng khía cạnh của thang chấm điểm: rubric

### Khía cạnh 1: Kiểm thử chức năng (Functional testing) - Tối đa 20 điểm
*   **Điểm đánh giá:** **18 / 20 điểm** (Mức Đạt tối đa)
*   **Lý do đánh giá:**
    *   Hệ thống vượt qua 10/10 ca kiểm thử chức năng được mô tả trong đặc tả ca kiểm thử: test cases specification.
    *   Hệ thống có cơ chế xử lý rất tốt: nếu API Gateway bị lỗi, client sẽ tự động kích hoạt bộ sinh dự phòng cục bộ: local fallback engine viết bằng JavaScript (`app.js`) để mô phỏng các ca kiểm thử khó (như tính ngày phép theo thâm niên, gắn cờ kiểm duyệt HR khi tiền phòng Điện Biên vượt hạn mức 650k, ẩn danh thông tin cá nhân nhạy cảm: PII bằng biểu thức chính quy: regex, cảnh báo an ninh).
    *   Khi trực tuyến: online, `server.py` triển khai thành công một RAG Engine thuần Python (sliding window chunking, cosine similarity dựa trên bag-of-words) để trích xuất văn bản từ thư mục `data/docs/` và gọi API Gateway cổng 20128 để suy luận.
    *   Điểm trừ nhỏ: Việc xử lý logic nghiệp vụ phức tạp ở chế độ ngoại tuyến: offline mode phụ thuộc nhiều vào mã cứng: hardcoded rules trên phía client JavaScript thay vì được giải quyết động bởi một mô hình ngôn ngữ lớn cục bộ: local LLM thực thụ ở phía server.

### Khía cạnh 2: An toàn và bảo mật (Safety & security) - Tối đa 20 điểm
*   **Điểm đánh giá:** **19 / 20 điểm** (Mức Đạt tối đa)
*   **Lý do đánh giá:**
    *   Mã nguồn bọc ngữ cảnh tri thức trong các thẻ XML `<context>...</context>` ở cả phía python server và javascript client, giúp hạn chế rủi ro nhầm lẫn vai trò: role confusion của mô hình AI.
    *   Lời nhắc hệ thống: system prompt được thiết kế rất chặt chẽ để chống tấn công tiêm lời nhắc: prompt injection (các kịch bản Jailbreak đòi xem thông tin mật, rò rỉ dữ liệu: data exfiltration đòi mã hóa Base64).
    *   Tích hợp sẵn bộ lọc từ khóa cấm ở đầu vào để chủ động phát hiện hành vi tấn công và đặt cờ cảnh báo an ninh `security_alert = true` để từ chối yêu cầu một cách an toàn.
    *   Tự động ẩn danh hóa thông tin cá nhân nhạy cảm: PII (tên riêng, số điện thoại, email) trước khi phản hồi người dùng hoặc ghi log.

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Compliance & logging) - Tối đa 10 điểm
*   **Điểm đánh giá:** **4 / 10 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   **Lỗi bảo mật nghiêm trọng:** Nhóm để lộ khóa bảo mật: API key tĩnh (hardcoded) công khai trực tiếp trong mã nguồn (`server.py` dòng 21 và `app.js` dòng 8): `sk-942c7c53f3f83948-pd6h4k-9c309057`. Đây là hành vi vi phạm nghiêm trọng quy tắc an toàn thông tin của Viettel Net. Nhóm chưa cấu hình khóa bảo mật qua tệp biến môi trường `.env` như cam kết trong tài liệu bảng tự kiểm tuân thủ: compliance checklist.
    *   **Thiếu log vật lý:** Hệ thống chưa thực sự ghi nhật ký vận hành: execution log ra tệp tin vật lý `outputs/execution-log.csv` trên máy chủ như đã mô tả trong tài liệu. Log hiện tại chỉ được in ra console Python hoặc giả lập hiển thị trên giao diện web client.

### Khía cạnh 4: Bộ hồ sơ giải pháp Capstone Blueprint (Tối đa 30 điểm)
*   **Điểm đánh giá:** **27.7 / 30 điểm** (Mức Xuất sắc)
*   **Lý do đánh giá:**
    *   **Phiếu mô tả dự án (Use Case One Pager - 5.5 / 6.0 điểm):** Phân tích nghiệp vụ sâu sắc, gắn chặt với nỗi đau: pain point của phòng HR và nguy cơ rò rỉ thông tin nội bộ của Viettel Net. Đề xuất giải pháp RAG ngoại tuyến: offline tối ưu chi phí. Điểm trừ: Sao chép biểu mẫu: template quên sửa tên nhóm (để là Nhóm 1).
    *   **Sơ đồ luồng logic (Logical Workflow - 5.5 / 6.0 điểm):** Sơ đồ Mermaid thiết kế chuẩn xác quy trình 3 tầng kết hợp các chốt chặn bảo mật. Xác định rõ ràng cơ chế con người tham gia kiểm soát: human-in-the-loop (HITL) qua hàng đợi chờ duyệt. Điểm trừ: Ghi sai tên nhóm (để là Nhóm 1).
    *   **Đặc tả lời nhắc cốt lõi (Core Prompt Design - 5.7 / 6.0 điểm):** Thiết kế cấu trúc lời nhắc hệ thống: system prompt rất tốt, bắt buộc đầu ra JSON Schema chặt chẽ. Nhật ký kiểm thử thủ công minh họa sinh động các kịch bản thực tế. Điểm trừ: Ghi sai tên nhóm (để là Nhóm 1).
    *   **Bảng tự kiểm tuân thủ (Compliance Checklist - 5.5 / 6.0 điểm):** Tự kiểm tra nghiêm túc 11 tiêu chí bảo mật. Tuy nhiên, giải pháp ghi log vật lý và lưu khóa bảo mật: API key trong `.env` chưa khớp với thực tế mã nguồn triển khai. Điểm trừ: Ghi sai tên nhóm (để là Nhóm 1).
    *   **Lộ trình áp dụng thực tế (Action Plan 30-90 Days - 5.5 / 6.0 điểm):** Lộ trình hành động: action plan chi tiết 30/90 ngày rõ ràng, có phân công cụ thể. Đề xuất 3 trường hợp sử dụng: use cases tiếp theo có tính thực tiễn cao cho NOC/HR. Điểm trừ: Ghi sai tên nhóm (để là Nhóm 1).

### Khía cạnh 5: Thuyết trình bảo vệ (Presentation & Q&A) - Tối đa 20 điểm
*   **Điểm đánh giá:** **18 / 20 điểm** (Mức Xuất sắc)
*   **Lý do đánh giá:**
    *   Nhóm đã chủ động thiết kế và nộp kèm một slide thuyết trình: slide deck chuyên nghiệp bằng mã nguồn Reveal.js (`slide-presentation.html`).
    *   Slide phối màu Viettel Teal cực kỳ đẹp mắt, bố cục cân đối, nội dung cô đọng (5 slides) tóm tắt xuất sắc toàn bộ giải pháp từ nghiệp vụ đến kỹ thuật bảo mật.
    *   Lỗi nhỏ: Slide trang bìa vẫn ghi sai thông tin đơn vị thực hiện là "Nhóm 1 VTN" trong khi nhóm nằm trong folder Nhóm 4.

---

## 3. Tổng kết điểm số và Xếp loại

*   **Tổng điểm:** 18 + 19 + 4 + 27.7 + 18 = **86.7 / 100 điểm**
*   **Xếp loại:** **Tốt (Good)**
*   **Trạng thái nghiệm thu:** **Đạt yêu cầu (Pass)** (Yêu cầu nhóm khắc phục ngay lỗi bảo mật API key và hoàn thiện tính năng ghi nhật ký vận hành ra file vật lý trước khi triển khai thí điểm thực tế).

---

## 4. Nhận xét chung và Đề xuất cải tiến
1.  **Điểm mạnh:**
    *   Sản phẩm thực tế có mức độ hoàn thiện kỹ thuật rất cao. Giao diện Web MVP (Single Page Application) thiết kế premium, đầy đủ các tính năng tương tác từ Chatbot RAG, Dashboard phê duyệt của cán bộ HR (HITL) cho đến bảng điều khiển thử nghiệm tấn công (Security Playground) và cấu phần tải tài liệu tự động lập chỉ mục (Indexer).
    *   Bộ hồ sơ giải pháp và slide bảo vệ được đầu tư chỉn chu, chuyên nghiệp, thể hiện tư duy thiết kế hệ thống an toàn và tuân thủ cao.
2.  **Hạn chế lớn nhất:**
    *   Sự thiếu nhất quán trong thông tin định danh nhóm: tất cả tài liệu Blueprint và slide đều để tên "Nhóm 1" dù bài nộp nằm trong thư mục của "Nhóm 4".
    *   Vi phạm nguyên tắc an toàn thông tin khi để lộ (hardcode) API key trực tiếp trong code server và client.
    *   Chưa hiện thực hóa việc ghi nhật ký ra file vật lý `.csv` trên đĩa cứng máy chủ.
3.  **Khuyến nghị cải tiến:**
    *   **Khắc phục lỗi bảo mật:** Nhóm cần loại bỏ ngay API key cứng khỏi mã nguồn. Sử dụng thư viện `python-dotenv` trên server để tải cấu hình từ tệp tin `.env` cục bộ (cần đưa `.env` vào `.gitignore` để tránh đẩy lên Git).
    *   **Hoàn thiện Module Logging:** Bổ sung logic ghi file trong `server.py` để ghi nhận các trường thông tin phi nhạy cảm vào tệp tin `outputs/execution-log.csv` khi có yêu cầu API được xử lý.
    *   **Chuẩn hóa thông tin định danh:** Rà soát và chỉnh sửa lại tên nhóm thực hiện trong toàn bộ các tệp tài liệu và slide thuyết trình để đảm bảo tính nhất quán (đổi từ Nhóm 1 thành Nhóm 4).
