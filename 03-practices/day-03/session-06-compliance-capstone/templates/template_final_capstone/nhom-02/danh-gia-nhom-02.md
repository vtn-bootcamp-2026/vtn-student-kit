---
mo-ta: Báo cáo đánh giá dự án Capstone của Nhóm 02 - Network Doc Assistant
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 16:35 +07:00"
updated-at: "2026-06-10 16:35 +07:00"
---

# Báo cáo đánh giá dự án Capstone nhóm 02

*   **Tên dự án ứng dụng:** Network Doc Assistant — AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel
*   **Đối tượng đánh giá:** Nhóm 02 (Nhóm AI Builders Mạng lưới)
*   **Hội đồng giám khảo:** Ban giám khảo chuyên môn Viettel Net
*   **Mốc thời gian đánh giá:** Tháng 5 năm 2026 (May 2026)

---

## 1. Kết quả kiểm tra hồ sơ bài nộp
Hội đồng đã thực hiện rà soát các thành phần tài liệu và mã nguồn trong thư mục bài nộp của Nhóm 02 và ghi nhận trạng thái như sau:

| STT | Thành phần hồ sơ | Tên tệp tin | Trạng thái nộp | Đánh giá sơ bộ |
| :--- | :--- | :--- | :---: | :--- |
| 1 | Mã nguồn ứng dụng | Không tìm thấy | **Thiếu** | Không có thư mục `src` hay bất kỳ tệp tin mã nguồn: source code Python nào được nộp. |
| 2 | Phiếu mô tả dự án | `capstone_project/use-case-one-pager.md`<br>`capstone_project/output/01-use-case-one-pager.md` | Đã nộp | Nội dung nghiệp vụ rất chi tiết, có tệp bổ sung tại thư mục `output` làm rõ phạm vi MVP và các kịch bản người dùng. |
| 3 | Sơ đồ luồng logic | `capstone_project/logical-workflow.md` | Đã nộp | Có sơ đồ khối quy trình dạng Mermaid và mô tả chi tiết các bước xử lý, phân định rõ ranh giới con người kiểm soát. |
| 4 | Đặc tả lời nhắc cốt lõi | `capstone_project/core-prompt-design.md`<br>`capstone_project/output/02-scoring-rubric.md` | Đã nộp | Đặc tả đầy đủ lời nhắc hệ thống: system prompt, lời nhắc người dùng: user prompt và cấu hình JSON đầu ra. Bổ sung bảng chấm điểm sơ bộ chi tiết. |
| 5 | Bảng tự kiểm tuân thủ | `capstone_project/compliance-checklist.md`<br>`capstone_project/output/03-risk-checklist.md` | Đã nộp | **Lỗi sao chép:** Tài liệu `compliance-checklist.md` bị sao chép nguyên bản từ giải pháp mẫu (dự án ẩn danh dữ liệu nhân sự), lạc đề hoàn toàn. Tệp `output/03-risk-checklist.md` bổ sung có phân tích rủi ro phù hợp với đề tài. |
| 6 | Lộ trình áp dụng thực tế | `capstone_project/action-plan-30-90-days.md` | Đã nộp | Lộ trình hành động: action plan chi tiết 30 và 90 ngày với các mốc công việc và chỉ số theo dõi rõ ràng. |
| 7 | Các tài liệu vận hành phụ | `capstone_project/failure-modes-rollback.md`<br>`capstone_project/handoff-contract.md`<br>`capstone_project/runbook-template.md`<br>`capstone_project/test-cases-specification.md` | Đã nộp | Đầy đủ biểu mẫu theo tiêu chuẩn bộ hồ sơ triển khai: implementation kit, tuy nhiên hầu hết các nội dung kết quả thực tế đều để trống dưới dạng nháp. |
| 8 | Bản trình bày bảo vệ | Không tìm thấy | **Thiếu** | Không có tệp tin bản trình bày: slide deck thuyết trình (`.pptx` hoặc `.pdf`). |

---

## 2. Đánh giá chi tiết theo từng khía cạnh của thang chấm điểm: rubric

### Khía cạnh 1: Kiểm thử chức năng (Functional testing) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm 02 không nộp mã nguồn ứng dụng (file Python), do đó hệ thống không thể chạy kiểm thử chức năng tự động hoặc kiểm thử thủ công nào trên sản phẩm thực tế của nhóm.
    *   Sản phẩm thực tế không thể vượt qua bất kỳ ca kiểm thử (TC) nào từ TC-01 đến TC-10 vì không có phần mềm để vận hành.

### Khía cạnh 2: An toàn và bảo mật (Safety & security) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Mặc dù nhóm đã thiết kế cấu trúc lời nhắc hệ thống: system prompt phòng vệ và phân vùng dữ liệu bằng thẻ XML rất chi tiết tại tài liệu `core-prompt-design.md`, do không có mã nguồn ứng dụng thực tế nên không có bất kỳ cơ chế phòng thủ tấn công lời nhắc: prompt injection nào được lập trình và vận hành trên môi trường thực tế.
    *   Hệ thống không thể kiểm chứng khả năng chặn đứng các kịch bản tấn công: Jailbreak, Data exfiltration (rò rỉ dữ liệu) hay Role confusion (nhầm lẫn vai trò) trên môi trường chạy thực tế.

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Compliance & logging) - Tối đa 10 điểm
*   **Điểm đánh giá:** **0 / 10 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm không nộp tệp nhật ký vận hành: execution log, do đó không thể quét lỗi rò rỉ dữ liệu nhạy cảm: personal identifiable information (PII) trên nhật ký.
    *   Không có mã nguồn thực tế để kiểm tra cơ chế bảo mật khóa kết nối hoặc cấu hình các biến môi trường trong tệp `.env`.

### Khía cạnh 4: Bộ hồ sơ giải pháp (Capstone Blueprint) - Tối đa 30 điểm
*   **Điểm đánh giá:** **21 / 30 điểm** (Mức Đạt yêu cầu)
*   **Lý do đánh giá:**
    *   **Phiếu mô tả dự án (Use Case One Pager - 5.0 / 6.0 điểm):** Phân tích nghiệp vụ rất chi tiết về công cụ hỗ trợ tra cứu tài liệu kỹ thuật Network Doc Assistant tại NOC. Định lượng rõ hiệu quả kỳ vọng (giảm thời gian tra cứu từ 15 phút xuống dưới 2 phút, độ chính xác > 90%). Tuy nhiên, tài liệu nháp và tài liệu đầu ra vẫn còn chứa nhiều thẻ placeholder dạng `[...]` chưa được điền thông tin cụ thể (ví dụ: tên phòng/ban kỹ thuật, tên kỹ sư đầu mối).
    *   **Sơ đồ luồng logic (Logical Workflow - 5.0 / 6.0 điểm):** Sơ đồ Mermaid thiết kế mạch lạc luồng xử lý qua 5 bước, chỉ định rõ ràng ranh giới con người tham gia kiểm soát: human-in-the-loop (HITL) (AI gợi ý cấu hình, kỹ sư cấp cao phê duyệt trước khi áp dụng). Tuy nhiên, nhóm vẫn để trống tên nhóm thực hiện dạng `[Tên nhóm thực hành — mô phỏng]`.
    *   **Đặc tả lời nhắc cốt lõi (Core Prompt Design - 5.0 / 6.0 điểm):** Thiết kế system prompt đầy đủ quy tắc bám sát tài liệu hướng dẫn và phòng ngự injection. Cấu trúc user prompt bọc XML boundary `<context>` và `<question>`. JSON Schema đầu ra chi tiết. Tuy nhiên, tài liệu vẫn còn nhiều placeholder trống và chưa điền tên nhóm thực hiện.
    *   **Bảng tự kiểm tuân thủ (Compliance Checklist - 1.0 / 6.0 điểm):** **Điểm trừ nghiêm trọng.** Tài liệu `compliance-checklist.md` của nhóm bị sao chép nguyên văn 100% từ giải pháp mẫu ("Mini Tool Anonymizer" - công cụ ẩn danh dữ liệu nhân sự của Nguyễn Văn A) và hoàn toàn không liên quan gì đến dự án của nhóm 02 là "Network Doc Assistant". Điều này thể hiện sự thiếu nghiêm túc trong khâu chuẩn bị tài liệu an toàn thông tin. Tệp `output/03-risk-checklist.md` có phân tích rủi ro phù hợp nhưng không thể bù đắp hoàn toàn lỗi sao chép thô tài liệu checklist tuân thủ chính thức.
    *   **Lộ trình áp dụng thực tế (Action Plan 30-90 Days - 5.0 / 6.0 điểm):** Lộ trình triển khai 30 và 90 ngày chi tiết, phân chia vai trò cụ thể. Đề xuất 3 trường hợp ứng dụng: use cases mở rộng tiếp theo rất thực tế cho NOC (NOC Log Summarizer, Technical Report Assistant, O&M Procedures Assistant). Tuy nhiên, nhóm vẫn để trống thông tin tên nhóm và tên trưởng nhóm ở các thẻ placeholder.

### Khía cạnh 5: Thuyết trình bảo vệ (Presentation & Q&A) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Cần cải thiện)
*   **Lý do đánh giá:**
    *   Nhóm không chuẩn bị tệp bản trình bày: slide deck thuyết trình chính thức cho buổi báo cáo.
    *   Không có sản phẩm demo chạy thực tế trên terminal để thuyết phục hội đồng giám khảo.

---

## 3. Tổng kết điểm số và xếp loại

*   **Tổng điểm:** 0 + 0 + 0 + 21 + 0 = **21 / 100 điểm**
*   **Xếp loại:** **Không đạt (Fail)**
*   **Trạng thái nghiệm thu:** **Không đạt yêu cầu** (Thiếu hoàn toàn phần mã nguồn kỹ thuật thực thi, tệp nhật ký vận hành, bản trình bày thuyết trình và sản phẩm demo; đồng thời tài liệu tuân thủ bảo mật bị lạc đề do sao chép nguyên mẫu).

---

## 4. Nhận xét chung và đề xuất cải tiến

1.  **Điểm mạnh:**
    *   Ý tưởng nghiệp vụ rất thực tế và cần thiết cho công tác vận hành khai thác tại NOC. Dự án Network Doc Assistant giải quyết đúng nỗi đau tìm kiếm tài liệu phân tán của kỹ sư.
    *   Thiết kế luồng logic, prompt hệ thống và kế hoạch hành động 30/90 ngày được xây dựng chi tiết, có cấu trúc tốt và định lượng rõ ràng các chỉ số KPI.
    *   Bảng phân tích rủi ro bổ sung (`03-risk-checklist.md`) nhận diện đúng các nguy hiểm về rò rỉ IP, hallucination và đề xuất các rào cản guardrails tương thích.
2.  **Hạn chế lớn nhất:**
    *   Không hiện thực hóa được giải pháp bằng mã nguồn. Không có sản phẩm thực tế để chạy thử nghiệm các ca test đã đặc tả.
    *   Tài liệu tự kiểm tuân thủ bảo mật bị lỗi sao chép thô từ dự án mẫu khác, dẫn đến lạc đề hoàn toàn và không có giá trị áp dụng thực tiễn.
    *   Để sót quá nhiều thẻ placeholder dạng `[...]` chưa điền thông tin cụ thể trong toàn bộ hồ sơ Blueprint.
3.  **Khuyến nghị cải tiến:**
    *   Nhóm cần khẩn trương phát triển mã nguồn Python thực tế cho Network Doc Assistant. Có thể tham khảo cấu trúc code mẫu tại `references/anonymizer-solution-gemini.py` để tích hợp gọi Gemini API hoặc mô hình ngôn ngữ lớn cục bộ: local LLM (ví dụ `qwen3.5:1.5b-instruct` / `gemma4:e2b` thông qua Ollama cục bộ) để chạy RAG offline.
    *   Viết lại bảng tự kiểm tuân thủ bảo mật `compliance-checklist.md` bám sát vào bài toán tra cứu tài liệu kỹ thuật mạng lưới thay vì giữ nguyên nội dung công cụ ẩn danh nhân sự.
    *   Rà soát toàn bộ các tài liệu trong Blueprint để điền đầy đủ các thông tin tên nhóm, tên thành viên và các thông số kỹ thuật, loại bỏ hoàn toàn các thẻ placeholder dạng nháp.
    *   Soạn thảo slide báo cáo (5-7 slides) và chuẩn bị kịch bản demo chạy thực tế để báo cáo lại trước hội đồng.
