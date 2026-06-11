---
mo-ta: Báo cáo đánh giá dự án Capstone của Nhóm 03 - NetSaveAI
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 16:15 +07:00"
updated-at: "2026-06-10 16:15 +07:00"
---

# Báo cáo đánh giá dự án Capstone nhóm 03

*   **Tên dự án ứng dụng:** NetSaveAI — Chatbot RAG cho Vận hành Mạng Viễn thông
*   **Đối tượng đánh giá:** Nhóm 03 (Nhóm AI Builders NOC)
*   **Hội đồng giám khảo:** Ban giám khảo chuyên môn Viettel Net
*   **Mốc thời gian đánh giá:** Tháng 5 năm 2026 (May 2026)

---

## 1. Kết quả kiểm tra hồ sơ bài nộp
Hội đồng đã thực hiện rà soát các thành phần tài liệu và mã nguồn trong thư mục bài nộp của Nhóm 03 và ghi nhận trạng thái như sau:

| STT | Thành phần hồ sơ | Tên tệp tin | Trạng thái nộp | Đánh giá sơ bộ |
| :--- | :--- | :--- | :---: | :--- |
| 1 | Mã nguồn ứng dụng | `src/anonymizer.py` | Đã nộp | Chỉ chứa mã nguồn bộ lọc biểu thức chính quy: regex cơ bản, chưa tích hợp mô hình ngôn ngữ lớn cục bộ: local LLM và RAG. |
| 2 | Phiếu mô tả dự án | `capstone_project/use-case-one-pager.md`<br>`capstone_project/UseCase_NetSaveAI.md` | Đã nộp | Nội dung nghiệp vụ rất chi tiết, có tệp bổ sung chuyên sâu làm rõ các trường hợp sử dụng: use cases. |
| 3 | Sơ đồ luồng logic | `capstone_project/logical-workflow.md` | Đã nộp | Đầy đủ sơ đồ Mermaid và mô tả các bước. |
| 4 | Đặc tả lời nhắc cốt lõi | `capstone_project/core-prompt-design.md` | Đã nộp | Có đặc tả lời nhắc hệ thống: system prompt, JSON Schema và nhật ký chạy thử. |
| 5 | Bảng tự kiểm tuân thủ | `capstone_project/compliance-checklist.md` | Đã nộp | Điền đầy đủ các cam kết tuân thủ an toàn dữ liệu nội bộ. |
| 6 | Lộ trình áp dụng thực tế | `capstone_project/action-plan-30-90-days.md` | Đã nộp | Có lộ trình hành động: action plan chi tiết 30/90 ngày và 3 ý tưởng tiếp theo. |
| 7 | Các tài liệu vận hành phụ | `failure-modes-rollback.md`<br>`handoff-contract.md`<br>`runbook-template.md`<br>`test-cases-specification.md` | Đã nộp | Đầy đủ biểu mẫu theo tiêu chuẩn bộ hồ sơ triển khai: implementation kit. |
| 8 | Bản trình bày bảo vệ | Không tìm thấy | **Thiếu** | Không có tệp tin bản trình bày: slide deck thuyết trình (`.pptx` hoặc `.pdf`). |

---

## 2. Đánh giá chi tiết theo từng khía cạnh của thang chấm điểm: rubric

### Khía cạnh 1: Kiểm thử chức năng (Functional testing) - Tối đa 20 điểm
*   **Điểm đánh giá:** **5 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Mã nguồn `anonymizer.py` thực tế của nhóm chỉ triển khai bộ lọc biểu thức chính quy: regex tĩnh để ẩn danh 3 trường thông tin: email, số điện thoại, và số CCCD.
    *   Mã nguồn hoàn toàn chưa tích hợp thư viện API của Google Gemini hay mô hình ngôn ngữ lớn cục bộ: local LLM (như `qwen3.5:1.5b-instruct` hay `gemma4:e2b` thông qua Ollama) như đã đề xuất trong tài liệu lý thuyết.
    *   Hệ thống không có khả năng thực hiện tìm kiếm kết hợp: hybrid search trên Vector DB để truy xuất các quy trình kỹ thuật. Do đó, sản phẩm thực tế không chạy được các ca kiểm thử chức năng liên quan đến RAG viễn thông (từ TC-01 đến TC-07).
    *   Mã nguồn chỉ vượt qua các ca kiểm thử ẩn danh hóa chuỗi ký tự cơ bản, thiếu hoàn toàn khả năng nhận diện các PII phức tạp hơn như Ngày sinh, Số tài khoản ngân hàng, Địa chỉ nhà hay Họ tên riêng (vốn được hỗ trợ trong phiên bản giải pháp mẫu).

### Khía cạnh 2: An toàn và bảo mật (Safety & security) - Tối đa 20 điểm
*   **Điểm đánh giá:** **6 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm đã thiết kế cấu trúc lời nhắc hệ thống: system prompt phòng vệ và phân vùng dữ liệu bằng thẻ XML rất tốt trên lý thuyết tại tài liệu `core-prompt-design.md`.
    *   Tuy nhiên, do mã nguồn thực tế hoàn toàn không tích hợp LLM nên không có bất kỳ cơ chế kiểm soát lời nhắc: prompt engineering hay phòng thủ tấn công lời nhắc: prompt injection defense nào được lập trình.
    *   Mặc dù ứng dụng không thể bị jailbreak hay bị dụ dỗ thực thi mã độc một cách chủ động (do không chạy LLM), hệ thống vẫn gặp lỗi rò rỉ thông tin nhạy cảm: data exfiltration thụ động vì bộ lọc regex không che giấu được các thông tin cá nhân như Họ tên riêng của nhân sự xuất hiện trong kịch bản tấn công (ví dụ: "Nguyễn Tuấn Anh", "Trần Quốc Bảo", "Phạm Minh Đông" vẫn hiển thị nguyên văn ở đầu ra).

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Compliance & logging) - Tối đa 10 điểm
*   **Điểm đánh giá:** **4 / 10 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Mã nguồn hoàn toàn thiếu cơ chế ghi nhật ký vận hành: execution log. Không có tệp tin `execution-log.csv` nào được tạo ra để lưu lịch sử hoạt động và quét lỗi rò rỉ thông tin nhạy cảm.
    *   Điểm cộng duy nhất là nhóm không để lộ khóa bảo mật: API key trong mã nguồn (do không gọi API nào).

### Khía cạnh 4: Bộ hồ sơ giải pháp (Capstone Blueprint) - Tối đa 30 điểm
*   **Điểm đánh giá:** **28 / 30 điểm** (Mức Xuất sắc)
*   **Lý do đánh giá:**
    *   **Phiếu mô tả dự án (Use Case One Pager - 5.5 / 6.0 điểm):** Nội dung nghiệp vụ rất sâu sắc gắn với thực tế tại NOC. Tệp chi tiết `UseCase_NetSaveAI.md` thể hiện sự đầu tư cao khi phân tích rõ các actors, use cases nghiệp vụ và so sánh điểm khác biệt của NetSaveAI. Lỗi nhỏ: Quên sửa các thẻ thông tin như `[Điền tên]`, `[Điền tháng/năm]`.
    *   **Sơ đồ luồng logic (Logical Workflow - 5.5 / 6.0 điểm):** Sơ đồ Mermaid thiết kế mạch lạc các bước từ Query Analyzer đến Hybrid Search và LLM. Định vị ranh giới con người tham gia kiểm soát: human-in-the-loop (HITL) rất tốt (AI gợi ý, kỹ sư duyệt và tự gõ terminal). Lỗi nhỏ: Để trống tên nhóm.
    *   **Đặc tả lời nhắc cốt lõi (Core Prompt Design - 5.5 / 6.0 điểm):** Thiết kế system prompt đầy đủ quy tắc bám sát tài liệu và phòng ngự. JSON Schema đầu ra chuẩn hóa. Ca kiểm thử playground đa dạng. Lỗi nhỏ: Để trống tên nhóm.
    *   **Bảng tự kiểm tuân thủ (Compliance Checklist - 6.0 / 6.0 điểm):** Điền chi tiết, cam kết an toàn dữ liệu 100% on-premise rất phù hợp với môi trường Viettel Net.
    *   **Lộ trình áp dụng thực tế (Action Plan 30-90 Days - 5.5 / 6.0 điểm):** Lộ trình triển khai rõ ràng, phân vai cụ thể. Đề xuất 3 trường hợp ứng dụng: use cases mở rộng tiếp theo rất thực tiễn và khả thi cho NOC. Lỗi nhỏ: Để trống tên nhóm và trưởng nhóm.

### Khía cạnh 5: Thuyết trình bảo vệ (Presentation & Q&A) - Tối đa 20 điểm
*   **Điểm đánh giá:** **10 / 20 điểm** (Mức Đạt yêu cầu)
*   **Lý do đánh giá:**
    *   Nhóm chuẩn bị nội dung tài liệu thiết kế nghiệp vụ cực kỳ xuất sắc và có tính thực chiến cao.
    *   Tuy nhiên, nhóm thiếu hoàn toàn tệp bản trình bày: slide deck chính thức cho buổi báo cáo và không có sản phẩm demo chạy thực tế trên terminal để thuyết phục hội đồng.

---

## 3. Tổng kết điểm số và Xếp loại

*   **Tổng điểm:** 5 + 6 + 4 + 28 + 10 = **53 / 100 điểm**
*   **Xếp loại:** **Trung bình (Pass)**
*   **Trạng thái nghiệm thu:** **Đạt yêu cầu tối thiểu** (Đạt phần thiết kế hồ sơ giải pháp nhưng phần mã nguồn kỹ thuật cần phải nâng cấp bổ sung nghiêm túc).

---

## 4. Nhận xét chung và Đề xuất cải tiến
1.  **Điểm mạnh:**
    *   Tư duy nghiệp vụ viễn thông tại NOC cực kỳ xuất sắc. Giải pháp RAG NetSaveAI được định nghĩa chuẩn xác từ cấu trúc dữ liệu, cơ chế hybrid search cho tới ranh giới vận hành an toàn giữa AI và kỹ sư NOC (HITL).
    *   Hồ sơ tài liệu chuẩn bị vô cùng chỉn chu, chi tiết và vượt trội hơn so với yêu cầu tối thiểu của Capstone Blueprint.
2.  **Hạn chế lớn nhất:**
    *   Sự đứt gãy lớn giữa tài liệu thiết kế lý thuyết và mã nguồn phát triển thực tế. Code `anonymizer.py` nộp lên không có bất kỳ tính năng AI/RAG nào được hiện thực hóa.
    *   Thiếu cơ chế ghi nhật ký vận hành: execution log và slide trình chiếu chính thức.
3.  **Khuyến nghị cải tiến:**
    *   Nhóm cần tích hợp ngay thư viện SDK của Google Gemini (sử dụng API key trong `.env`) hoặc thiết lập kết nối Ollama local để đưa logic System Prompt đã thiết kế vào mã nguồn.
    *   Tham chiếu tệp mã nguồn giải pháp `references/anonymizer-solution.py` và `references/anonymizer-solution-gemini.py` để bổ sung đầy đủ các bộ lọc regex nâng cao cho ngày sinh, số tài khoản ngân hàng, địa chỉ và logic gọi LLM an toàn.
    *   Bổ sung module logging để tự động ghi nhận hoạt động vào tệp tin `execution-log.csv` nhằm phục vụ việc kiểm toán an toàn dữ liệu nội bộ.
