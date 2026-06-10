---
mo-ta: Báo cáo đánh giá dự án Capstone của Nhóm 05 - NetBI-KARA
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 16:30 +07:00"
updated-at: "2026-06-10 16:30 +07:00"
---

# Báo cáo đánh giá dự án Capstone nhóm 05

*   **Tên dự án ứng dụng:** Hệ thống Tự động hóa Báo cáo & Phân tích Anomaly KPI NetBI (NetBI-KARA)
*   **Đối tượng đánh giá:** Nhóm 05 (Nhóm Kỹ sư AI Thực chiến NOC)
*   **Hội đồng giám khảo:** Ban giám khảo chuyên môn Viettel Net
*   **Mốc thời gian đánh giá:** Tháng 5 năm 2026 (May 2026)

---

## 1. Kết quả kiểm tra hồ sơ bài nộp
Hội đồng đã thực hiện rà soát các thành phần tài liệu và mã nguồn trong thư mục bài nộp của Nhóm 05 và ghi nhận trạng thái như sau:

| STT | Thành phần hồ sơ | Tên tệp tin | Trạng thái nộp | Đánh giá sơ bộ |
| :--- | :--- | :--- | :---: | :--- |
| 1 | Mã nguồn ứng dụng | Không tìm thấy | **Thiếu** | Không nộp tệp tin mã nguồn `report_generator.py` hoặc `.py` nào khác như đã mô tả trong tài liệu bàn giao. |
| 2 | Phiếu mô tả dự án | `capstone_project/use-case-one-pager.md` | Đã nộp | Mô tả bài toán nghiệp vụ chi tiết tại NOC, chỉ rõ các chỉ số mạng lưới cần tự động hóa. |
| 3 | Sơ đồ luồng logic | `capstone_project/logical-workflow.md` | Đã nộp | Có sơ đồ Mermaid 3 tầng, làm rõ quy trình và ranh giới kiểm duyệt thủ công: human-in-the-loop (HITL). Lỗi copy-paste ghi tên Nhóm 01. |
| 4 | Đặc tả lời nhắc cốt lõi | `capstone_project/core-prompt-design.md` | Đã nộp | Thiết kế system prompt chi tiết, có phân tách XML và JSON Schema đầu ra. Lỗi copy-paste ghi tên Nhóm 01. |
| 5 | Bảng tự kiểm tuân thủ | `capstone_project/compliance-checklist.md` | Đã nộp | Đánh giá rất chi tiết 11 tiêu chí an toàn dữ liệu nội bộ và các phương án dự phòng. |
| 6 | Lộ trình áp dụng thực tế | `capstone_project/action-plan-30-90-days.md` | Đã nộp | Lộ trình hành động: action plan chi tiết 30/90 ngày và 3 ý tưởng use cases thực tế tiếp theo. Lỗi copy-paste ghi tên Nhóm 01. |
| 7 | Các tài liệu vận hành phụ | `failure-modes-rollback.md`<br>`handoff-contract.md`<br>`runbook-template.md`<br>`test-cases-specification.md` | Đã nộp | Đầy đủ biểu mẫu theo tiêu chuẩn bộ hồ sơ triển khai: implementation kit. Các tài liệu đều bị lỗi copy-paste ghi tên Nhóm 01. |
| 8 | Bản trình bày bảo vệ | Không tìm thấy | **Thiếu** | Không nộp tệp tin slide deck trình bày báo cáo (`.pptx` hoặc `.pdf`). |
| 9 | Nhật ký vận hành | Không tìm thấy | **Thiếu** | Không có tệp tin nhật ký vận hành: execution log (`execution-log.csv`) thực tế được tạo ra. |
| 10 | Tệp dữ liệu giả lập | `synthetic-data/edge-cases-sample.txt`<br>`synthetic-data/prompt-injection-attacks.txt` | Đã nộp | Chuẩn bị đầy đủ các văn bản kiểm thử biên và kịch bản tấn công. |

---

## 2. Đánh giá chi tiết theo từng khía cạnh của thang chấm điểm: rubric

### Khía cạnh 1: Kiểm thử chức năng (Functional testing) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Thư mục nộp bài của nhóm hoàn toàn thiếu tệp tin mã nguồn Python (`report_generator.py`) để thực hiện kiểm thử.
    *   Mặc dù tài liệu đặc tả ca kiểm thử `test-cases-specification.md` của nhóm ghi nhận trạng thái ĐẠT (PASS) cả 10/10 ca kiểm thử chức năng (từ TC-01 đến TC-10), ban giám khảo không thể kiểm chứng hay thực thi chạy thử nghiệm tự động trên sản phẩm thực tế. Do đó, điểm khía cạnh này bắt buộc phải tính là 0 điểm.

### Khía cạnh 2: An toàn và bảo mật (Safety & security) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm đã xây dựng thiết kế lời nhắc hệ thống: system prompt phòng vệ và phân tách dữ liệu bằng thẻ XML rất tốt trên lý thuyết tại tài liệu `core-prompt-design.md`, đồng thời đã chuẩn bị sẵn các kịch bản bẫy dữ liệu tấn công trong tệp `prompt-injection-attacks.txt`.
    *   Tuy nhiên, do hoàn toàn không nộp mã nguồn lập trình thực tế, hội đồng không thể kiểm chứng năng lực phòng thủ của mô hình AI trước các kỹ thuật tấn công lời nhắc: prompt injection (Jailbreak, Data exfiltration, Role confusion).

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Compliance & logging) - Tối đa 10 điểm
*   **Điểm đánh giá:** **0 / 10 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm không nộp tệp tin nhật ký vận hành: execution log (`execution-log.csv`) để chứng minh việc ghi lại lịch sử chạy và cơ chế quét sạch dữ liệu nhạy cảm: PII sanitization.
    *   Hội đồng cũng không có mã nguồn để đánh giá việc cấu hình biến môi trường an toàn (tệp `.env` không được nạp thực tế lên hệ thống).

### Khía cạnh 4: Bộ hồ sơ giải pháp (Capstone Blueprint) - Tối đa 30 điểm
*   **Điểm đánh giá:** **26.5 / 30 điểm** (Mức Xuất sắc)
*   **Lý do đánh giá:**
    *   **Phiếu mô tả dự án (Use Case One Pager - 5.5 / 6.0 điểm):** Phân tích nghiệp vụ sâu sắc, gắn chặt với nỗi đau thực tế của 5 kỹ sư trực ca NOC khi phải xử lý thủ công 200 chỉ số KPI từ hệ thống NetBI. Chỉ rõ giá trị đo lường được (giảm từ 3-5 ngày xuống dưới 30 phút). Người đầu mối Nguyễn Minh Huy rõ ràng.
    *   **Sơ đồ luồng logic (Logical Workflow - 5.0 / 6.0 điểm):** Sơ đồ Mermaid thiết kế mạch lạc 3 tầng (Pandas, Local LLM, Web UI/HITL). Xác định chính xác ranh giới kiểm duyệt thủ công: human-in-the-loop (HITL) (kỹ sư NOC duyệt email cảnh báo trước khi nhấn gửi). Điểm trừ: Lỗi copy-paste nghiêm trọng khi để tên nhóm thực hiện là "Nhóm 01 - AI Builders Viettel Net" trong tài liệu của Nhóm 05.
    *   **Đặc tả lời nhắc cốt lõi (Core Prompt Design - 5.0 / 6.0 điểm):** Thiết kế system prompt chi tiết, cấu trúc JSON Schema đầu ra rõ ràng và bọc thẻ XML chuẩn hóa. Chuẩn bị 3 ca kiểm thử playground rất thực tế. Điểm trừ: Tiếp tục ghi sai tên nhóm thành "Nhóm 01 - AI Builders Viettel Net".
    *   **Bảng tự kiểm tuân thủ (Compliance Checklist - 6.0 / 6.0 điểm):** Đánh giá cực kỳ chi tiết 11 tiêu chí tuân thủ, bám sát Nghị định 356/2025. Giải pháp kỹ thuật như xử lý in-memory trên RAM và Pandas Fallback Mode khi mất kết nối LLM cục bộ được phân tích rất sâu sắc.
    *   **Lộ trình áp dụng thực tế (Action Plan 30-90 Days - 5.0 / 6.0 điểm):** Kế hoạch chi tiết phân chia theo các mốc 30 và 90 ngày, chỉ rõ nhân sự phụ trách (Trần Quốc Bảo, Lê Hoàng Nam, Phạm Minh Đức, Vũ Khánh Huyền, Nguyễn Minh Huy). Đề xuất 3 trường hợp sử dụng: use cases tiếp theo (tóm tắt log SCADA, sinh mã IaC, chatbot O&M offline) có tính khả thi cực kỳ cao cho NOC. Điểm trừ: Ghi sai tên nhóm thành "Nhóm 01".

### Khía cạnh 5: Thuyết trình bảo vệ (Presentation & Q&A) - Tối đa 20 điểm
*   **Điểm đánh giá:** **5 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm hoàn toàn không nộp tệp tin slide trình chiếu (`.pptx` hoặc `.pdf`) phục vụ buổi thuyết trình bảo vệ.
    *   Không có sản phẩm demo chạy thực tế để thuyết phục hội đồng.
    *   Hội đồng chấm 5 điểm khích lệ dựa trên tư duy thiết kế hệ thống lý thuyết rất tốt thể hiện qua bộ hồ sơ giải pháp và khả năng phản biện lý thuyết của nhóm.

---

## 3. Tổng kết điểm số và Xếp loại

*   **Tổng điểm:** 0 + 0 + 0 + 26.5 + 5 = **31.5 / 100 điểm**
*   **Xếp loại:** **Không đạt (Fail)**
*   **Trạng thái nghiệm thu:** **Không đạt yêu cầu** (Bộ hồ sơ thiết kế đạt chất lượng rất cao nhưng phần kỹ thuật mã nguồn và slide thuyết trình chưa được triển khai nộp).

---

## 4. Nhận xét chung và Đề xuất cải tiến

1.  **Điểm mạnh:**
    *   Tư duy thiết kế nghiệp vụ của nhóm cực kỳ xuất sắc. Giải pháp NetBI-KARA giải quyết trúng pain point thực tế tại NOC Viettel Net, có kế hoạch và lộ trình hành động chi tiết và phân công vai trò rõ ràng.
    *   Tài liệu lý thuyết (One Pager, Workflow, Prompt Design, Compliance Checklist, Action Plan) được biên soạn chỉn chu, bài bản, đáp ứng vượt trội các tiêu chí chất lượng tài liệu.
2.  **Hạn chế lớn nhất:**
    *   Sự thiếu hụt hoàn toàn của mã nguồn thực tế và tệp tin cấu hình. Nhóm có thiết kế hướng dẫn vận hành (Runbook) và đặc tả ca kiểm thử rất tốt nhưng không lập trình sản phẩm để chạy thử.
    *   Lỗi copy-paste không rà soát kỹ khiến tên nhóm thực hiện bị ghi sai đồng loạt thành "Nhóm 01" trong các tài liệu con, làm giảm tính chuyên nghiệp của hồ sơ.
    *   Thiếu slide thuyết trình chính thức.
3.  **Khuyến nghị cải tiến:**
    *   Nhóm cần lập tức triển khai viết mã nguồn Python (`report_generator.py`) bám sát thiết kế luồng xử lý và Runbook đã soạn thảo.
    *   Tham chiếu tệp mã nguồn giải pháp mẫu `03-practice/day-03/session-06-compliance-capstone/src/anonymizer.py` để tích hợp các biểu thức chính quy: regex ẩn danh dữ liệu nhạy cảm nâng cao (dob, bank_account, address) và logic kết nối LLM cục bộ (Ollama requests).
    *   Bổ sung cơ chế ghi nhật ký vận hành phi nhạy cảm ra tệp tin `execution-log.csv` để hoàn thiện tiêu chí tuân thủ log.
    *   Rà soát lại toàn bộ tài liệu để sửa tên nhóm từ "Nhóm 01" thành "Nhóm 05" trước khi nộp lại.
    *   Chuẩn bị slide thuyết trình (từ 5 đến 7 trang) tóm tắt dự án để tham gia bảo vệ nghiệm thu lần 2.
