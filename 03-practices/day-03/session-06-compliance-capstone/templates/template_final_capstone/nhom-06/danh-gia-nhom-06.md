---
mo-ta: Báo cáo đánh giá dự án Capstone của nhóm 06 - Project Assistant Simulation
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 16:25 +07:00"
updated-at: "2026-06-10 16:25 +07:00"
---

# Báo cáo đánh giá dự án Capstone nhóm 06

*   **Tên dự án ứng dụng:** Project Assistant Simulation — Trợ lý dự án giả lập giúp truy vấn tiến độ và chỉ số dự án
*   **Đối tượng đánh giá:** Nhóm 06
*   **Hội đồng giám khảo:** Ban giám khảo chuyên môn Viettel Net
*   **Mốc thời gian đánh giá:** Tháng 5 năm 2026 (May 2026)

---

## 1. Kết quả kiểm tra hồ sơ bài nộp
Hội đồng đã thực hiện rà soát các thành phần tài liệu và mã nguồn: source code trong thư mục bài nộp của nhóm 06 và ghi nhận trạng thái như sau:

| STT | Thành phần hồ sơ | Tên tệp tin | Trạng thái nộp | Đánh giá sơ bộ |
| :--- | :--- | :--- | :---: | :--- |
| 1 | Mã nguồn ứng dụng | Không tìm thấy | **Thiếu** | Không có thư mục mã nguồn: source code `src/` hay tệp Python nào được nộp. |
| 2 | Phiếu mô tả dự án | `use-case-one-pager.md` | Đã nộp | Nội dung mô tả nghiệp vụ tốt, rõ ràng về đầu vào, đầu ra và cách kiểm soát rủi ro. |
| 3 | Sơ đồ luồng logic | `logical-workflow.md` | Đã nộp | Có sơ đồ Mermaid nhưng rất đơn giản, mang tính chất chung chung, chưa cụ thể hóa luồng dữ liệu của dự án. |
| 4 | Đặc tả lời nhắc cốt lõi | `core-prompt-design.md` | Đã nộp | Có lời nhắc hệ thống: system prompt cơ bản nhưng còn lỗi cú pháp nhỏ và thiếu phần đặc tả chi tiết (ví dụ: JSON Schema, few-shot examples). |
| 5 | Bảng tự kiểm tuân thủ | `compliance-checklist.md` | Đã nộp | Điền đầy đủ trạng thái tự đánh giá tuân thủ bảo mật thông tin nội bộ. |
| 6 | Lộ trình áp dụng thực tế | `action-plan-30-90-days.md` | Đã nộp | Nội dung lộ trình bị bỏ trống nhiều thông tin người chịu trách nhiệm và đơn vị áp dụng. |
| 7 | Các tài liệu vận hành phụ | `failure-modes-rollback.md`<br>`handoff-contract.md`<br>`runbook-template.md`<br>`test-cases-specification.md`<br>`use-case-scoring-rubbric.md`<br>`risk-control-checklist.md` | Đã nộp | Nộp đầy đủ các biểu mẫu phụ thuộc bộ hồ sơ triển khai: implementation kit. |
| 8 | Bản trình bày bảo vệ | Không tìm thấy | **Thiếu** | Không có tệp tin bản trình bày: slide deck thuyết trình (`.pptx` hoặc `.pdf`). |

---

## 2. Đánh giá chi tiết theo từng khía cạnh của thang chấm điểm: rubbric

### Khía cạnh 1: Kiểm thử chức năng (Functional testing) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm hoàn toàn không nộp mã nguồn: source code (thiếu tệp `run_pipeline.py` và các script bổ trợ như đã ghi trong tài liệu bàn giao).
    *   Hội đồng không thể thực hiện bất kỳ ca kiểm thử chức năng tự động hoặc thủ công nào trên sản phẩm thực tế của nhóm.
    *   Sản phẩm thực tế không thể vượt qua bất kỳ ca kiểm thử nào từ TC-01 đến TC-10 vì không có phần mềm để vận hành.

### Khía cạnh 2: An toàn và bảo mật (Safety & security) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Mặc dù nhóm có phác thảo các rào cản an toàn lý thuyết tại tài liệu `risk-control-checklist.md` (như bộ lọc ẩn danh thông tin nhạy cảm: personal identifiable information (PII) bằng biểu thức chính quy: regex và mô hình nhận dạng thực thể có tên: Named Entity Recognition (NER)), do không có mã nguồn ứng dụng thực tế nên không có bất kỳ cơ chế phòng thủ tấn công lời nhắc: prompt injection nào được lập trình và vận hành.
    *   Không thể thực nghiệm và đánh giá năng lực phòng thủ thực tế trước 3 kịch bản tấn công: Jailbreak, Rò rỉ dữ liệu, và Nhầm lẫn vai trò.

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Compliance & logging) - Tối đa 10 điểm
*   **Điểm đánh giá:** **0 / 10 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm không nộp tệp nhật ký vận hành: execution log (thiếu thư mục `logs/` và tệp log vận hành chạy thử). Do đó, không thể quét lỗi rò rỉ dữ liệu nhạy cảm trên nhật ký.
    *   Không có mã nguồn thực tế để kiểm tra cơ chế bảo mật khóa kết nối hoặc cấu hình các biến môi trường trong tệp `.env`.

### Khía cạnh 4: Bộ hồ sơ giải pháp Capstone Blueprint - Tối đa 30 điểm
*   **Điểm đánh giá:** **21.5 / 30 điểm** (Mức Đạt yêu cầu)
*   **Lý do đánh giá:**
    *   **Phiếu mô tả dự án (Use Case One Pager - 5.5 / 6.0 điểm):** Phân tích nghiệp vụ tốt, mô tả rõ ràng vấn đề theo dõi tiến độ của PM/subPM. Định lượng được giá trị kỳ vọng (tiết kiệm 90% thời gian tổng hợp). Có mô tả rủi ro và điểm con người tham gia kiểm soát: human-in-the-loop (HITL) rõ ràng. Lỗi nhỏ: Thiếu dấu gạch dọc phân cách ở dòng 17 trong bảng thông tin chung.
    *   **Sơ đồ luồng logic (Logical Workflow - 3.5 / 6.0 điểm):** Sơ đồ Mermaid thiết kế quá đơn giản và mang tính chất chung chung cho mọi ứng dụng AI (Start -> AI xử lý -> HITL -> End). Sơ đồ chưa thể hiện được luồng dữ liệu nghiệp vụ đặc thù của dự án (ví dụ: cách trích xuất từ dữ liệu Excel/CSV tiến độ, cách phân tích log chat JSON, cách kết hợp RAG và định tuyến câu hỏi).
    *   **Đặc tả lời nhắc cốt lõi (Core Prompt Design - 3.5 / 6.0 điểm):** Lời nhắc hệ thống: system prompt tương đối ngắn gọn và có lỗi cú pháp nhỏ ở đầu dòng số 8 (thiếu dấu ngoặc kép đóng). Đặc tả lời nhắc cốt lõi còn rất sơ sài: thiếu cấu trúc định dạng đầu vào bằng thẻ XML, thiếu các ví dụ minh họa cụ thể (few-shot examples) và thiếu JSON Schema quy chuẩn đầu ra như đã nêu trong thuyết minh.
    *   **Bảng tự kiểm tuân thủ (Compliance Checklist - 5.0 / 6.0 điểm):** Nhóm đã điền đầy đủ trạng thái "Đạt" cho các tiêu chí bảo mật, tuy nhiên các cam kết này hoàn toàn chỉ nằm trên giấy do chưa có sản phẩm thực tế để đối chiếu và kiểm chứng.
    *   **Lộ trình áp dụng thực tế (Action Plan 30-90 Days - 4.0 / 6.0 điểm):** Lộ trình triển khai 30 ngày và 90 ngày được chia mốc rõ ràng, đề xuất 3 trường hợp sử dụng: use cases tiếp theo khá thực tiễn (tóm tắt log SCADA, sinh mã Ansible/Terraform, tra cứu O&M offline). Tuy nhiên, nhóm đã để trống toàn bộ thông tin tại các thẻ placeholder `[Điền tên]` (người chịu trách nhiệm cho từng mốc) và thẻ `[Ví dụ: ...]` (đơn vị áp dụng).

### Khía cạnh 5: Thuyết trình bảo vệ (Presentation & Q&A) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Cần cải thiện)
*   **Lý do đánh giá:**
    *   Nhóm không chuẩn bị tệp bản trình bày: slide deck thuyết trình chính thức cho buổi báo cáo.
    *   Không có sản phẩm demo chạy thực tế trên terminal để thuyết phục hội đồng giám khảo.

---

## 3. Tổng kết điểm số và xếp loại

*   **Tổng điểm:** 0 + 0 + 0 + 21.5 + 0 = **21.5 / 100 điểm**
*   **Xếp loại:** **Không đạt (Fail)**
*   **Trạng thái nghiệm thu:** **Không đạt yêu cầu** (Thiếu hoàn toàn phần mã nguồn kỹ thuật thực thi, tệp nhật ký vận hành, bản trình bày thuyết trình, sản phẩm demo và bộ hồ sơ giải pháp còn nhiều nội dung sơ sài, bỏ trống placeholder).

---

## 4. Nhận xét chung và đề xuất cải tiến

1.  **Điểm mạnh:**
    *   Ý tưởng xây dựng Trợ lý dự án giả lập để tự động tổng hợp tiến độ và chat log phục vụ PM/subPM là rất thực tiễn, giải quyết tốt bài toán tiết kiệm thời gian vận hành.
    *   Nội dung nghiệp vụ ban đầu trong phiếu mô tả một trang (one-pager) và đề xuất 3 use cases mở rộng được thiết kế tương đối tốt và bám sát nhu cầu thực tế của Viettel Net.
2.  **Hạn chế lớn nhất:**
    *   Hoàn toàn không có sự hiện thực hóa kỹ thuật. Nhóm không nộp bất kỳ mã nguồn Python hay tệp notebook chạy thử nào, dẫn đến việc sập toàn bộ điểm số kỹ thuật (chức năng, an toàn, nhật ký vận hành).
    *   Thiếu slide báo cáo chính thức và demo sản phẩm trước hội đồng.
    *   Tài liệu thiết kế luồng logic và cấu trúc prompt còn mang tính chất đối phó, sơ sài và để sót nhiều placeholder chưa điền thông tin.
3.  **Khuyến nghị cải tiến:**
    *   Nhóm cần nhanh chóng hoàn thiện mã nguồn Python cho ứng dụng Project Assistant dựa trên khung giải pháp đã đề xuất. Tham khảo cấu trúc code mẫu tại thư mục `references/anonymizer-solution.py` và `references/anonymizer-solution-gemini.py` để biết cách tích hợp gọi API kết hợp bộ lọc Regex.
    *   Bổ sung đầy đủ module ghi nhật ký vận hành ra file CSV để theo dõi hoạt động và kiểm toán an toàn dữ liệu.
    *   Điền đầy đủ thông tin người chịu trách nhiệm và đơn vị áp dụng trong tài liệu `action-plan-30-90-days.md` để loại bỏ hoàn toàn các placeholder.
    *   Chi tiết hóa sơ đồ Mermaid của luồng logic và viết lại System Prompt đầy đủ kèm few-shot examples và JSON Schema cụ thể trong `core-prompt-design.md`.
    *   Chuẩn bị slide thuyết trình (5-7 trang) và kịch bản demo chạy thực tế để báo cáo hội đồng trong đợt đánh giá lại.
