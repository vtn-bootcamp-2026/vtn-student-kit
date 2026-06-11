---
mo-ta: Báo cáo đánh giá dự án Capstone của nhóm 02 - Network Doc Assistant
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 17:40 +07:00"
updated-at: "2026-06-10 17:40 +07:00"
---

# Báo cáo đánh giá dự án Capstone nhóm 02

*   **Tên dự án ứng dụng:** AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel (Network Doc Assistant)
*   **Đối tượng đánh giá:** Nhóm 02 (Nhóm thực hành Capstone)
*   **Hội đồng giám khảo:** Ban giám khảo chuyên môn Viettel Net
*   **Mốc thời gian đánh giá:** Tháng 5 năm 2026 (May 2026)

---

## 1. Kết quả kiểm tra hồ sơ bài nộp
Hội đồng giám khảo đã thực hiện rà soát các thành phần tài liệu và mã nguồn: source code trong thư mục bài nộp của nhóm 02 và ghi nhận trạng thái như sau:

| STT | Thành phần hồ sơ | Tên tệp tin | Trạng thái nộp | Đánh giá sơ bộ |
| :--- | :--- | :--- | :---: | :--- |
| 1 | Mã nguồn ứng dụng | Không tìm thấy | **Thiếu** | Không có tệp tin mã nguồn: source code Python nào được nộp trong thư mục của nhóm. |
| 2 | Phiếu mô tả dự án | `use-case-one-pager.md` | Đã nộp | Nghiệp vụ rõ ràng, mô tả chi tiết nỗi đau của kỹ sư NOC/BSS và định lượng cụ thể chỉ số KPI hiệu quả. |
| 3 | Sơ đồ luồng logic | `logical-workflow.md` | Đã nộp | Đầy đủ sơ đồ Mermaid thiết kế quy trình xử lý qua 5 tầng và chỉ định rõ ranh giới con người tham gia kiểm soát: human-in-the-loop (HITL) nghiêm ngặt. |
| 4 | Đặc tả lời nhắc cốt lõi | `core-prompt-design.md` | Đã nộp | Đặc tả lời nhắc hệ thống: system prompt phòng ngự tốt, có JSON Schema đầu ra và mô phỏng 4 ca kiểm thử playground chi tiết. |
| 5 | Bảng tự kiểm tuân thủ | `compliance-checklist.md` | Đã nộp | **Lỗi nghiêm trọng:** Nội dung giải trình hoàn toàn bị sao chép nguyên văn (copy-paste) từ dự án mẫu *Mini Tool Anonymizer* (che giấu CCCD, email, điện thoại, tệp `anonymizer-solution.py`...) thay vì dự án *Network Doc Assistant* của nhóm. |
| 6 | Lộ trình áp dụng thực tế | `action-plan-30-90-days.md` | Đã nộp | Lộ trình hành động: action plan chi tiết 30/90 ngày, phân công trách nhiệm rõ ràng và đề xuất 3 trường hợp sử dụng: use cases tiếp theo rất thực tế. |
| 7 | Đặc tả ca kiểm thử | `test-cases-specification.md` | Đã nộp | Đặc tả chi tiết 10 ca kiểm thử cho 4 nhóm tình huống (Normal, HITL, Out of scope, Security), tuy nhiên phần kết quả thực tế bị để trống do thiếu mã nguồn. |
| 8 | Biên bản bàn giao | `handoff-contract.md` | Đã nộp | Mô tả chi tiết danh mục bàn giao và các cam kết thỏa thuận mức độ dịch vụ: service level agreement (SLA) giữa nhóm phát triển và vận hành. |
| 9 | Tình huống lỗi & fallback | `failure-modes-rollback.md` | Đã nộp | Phân tích rõ 4 tình huống lỗi kỹ thuật (mất kết nối LLM, hallucination, KB lỗi thời, câu hỏi nhạy cảm) và đề xuất quy trình khôi phục: rollback runbook. |
| 10 | Hướng dẫn vận hành | `runbook-template.md` | Đã nộp | Bản hướng dẫn vận hành: runbook chi tiết các bước cài đặt offline, cấu hình biến môi trường `.env` và xử lý sự cố. |
| 11 | Tệp nhật ký vận hành | Không tìm thấy | **Thiếu** | Không nộp tệp tin nhật ký vận hành: execution log thực tế để kiểm toán rò rỉ dữ liệu nhạy cảm. |
| 12 | Bản trình bày bảo vệ | Không tìm thấy | **Thiếu** | Không nộp tệp tin bản trình bày: slide deck thuyết trình (`.pptx` hoặc `.pdf`). |

---

## 2. Đánh giá chi tiết theo từng khía cạnh của thang chấm điểm: rubric

### Khía cạnh 1: Kiểm thử chức năng (Functional testing) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm không nộp mã nguồn ứng dụng (file Python), do đó hệ thống không thể chạy kiểm thử chức năng tự động hoặc kiểm thử thủ công nào trên sản phẩm thực tế của nhóm.
    *   Sản phẩm thực tế không thể vượt qua bất kỳ ca kiểm thử (TC) nào từ TC-01 đến TC-10 vì không có phần mềm để vận hành.

### Khía cạnh 2: An toàn và bảo mật (Safety & security) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Mặc dù nhóm đã thiết kế cấu trúc lời nhắc hệ thống: system prompt phòng vệ và bọc dữ liệu bằng thẻ XML rất chi tiết tại tài liệu `core-prompt-design.md`, do không có mã nguồn ứng dụng thực tế nên không có bất kỳ cơ chế phòng thủ tấn công lời nhắc: prompt injection nào được lập trình và vận hành thực tế.
    *   Hệ thống không thể kiểm chứng khả năng chặn đứng các kịch bản tấn công: Jailbreak, Data exfiltration (rò rỉ dữ liệu), Role confusion (nhầm lẫn vai trò) trên môi trường thực tế.

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Compliance & logging) - Tối đa 10 điểm
*   **Điểm đánh giá:** **0 / 10 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm không nộp tệp nhật ký vận hành: execution log, do đó không thể quét lỗi rò rỉ dữ liệu nhạy cảm: personal identifiable information (PII) trên nhật ký.
    *   Không có mã nguồn thực tế để kiểm tra cơ chế bảo mật khóa kết nối hoặc cấu hình các biến môi trường trong tệp `.env` thực tế.

### Khía cạnh 4: Bộ hồ sơ giải pháp (Capstone Blueprint) - Tối đa 30 điểm
*   **Điểm đánh giá:** **25.5 / 30 điểm** (Mức Tốt)
*   **Lý do đánh giá:**
    *   **Phiếu mô tả dự án (Use case one pager - 6.0 / 6.0 điểm):** Phân tích nghiệp vụ sâu sắc về công cụ Network Doc Assistant, giải quyết trực tiếp nỗi đau thực tế của kỹ sư NOC/BSS khi tra cứu tài liệu kỹ thuật mạng lưới phân tán. Định lượng rõ hiệu quả (giảm thời gian tra cứu từ ~15 phút xuống dưới 2 phút, tiết kiệm thời gian và tối ưu chi phí 0 VNĐ nhờ mô hình offline). Tài liệu điền đầy đủ thông tin, không bị lỗi bỏ trống template.
    *   **Sơ đồ luồng logic (Logical workflow - 6.0 / 6.0 điểm):** Sơ đồ Mermaid thiết kế mạch lạc quy trình xử lý qua 5 tầng, chỉ định rõ ràng ranh giới con người tham gia kiểm soát: human-in-the-loop (HITL) nghiêm ngặt (AI đề xuất gợi ý cấu hình, kỹ sư cấp cao phê duyệt trước khi áp dụng thực tế).
    *   **Đặc tả lời nhắc cốt lõi (Core prompt design - 6.0 / 6.0 điểm):** Thiết kế system prompt có các chỉ thị chấm điểm, phòng vệ prompt injection và tự kiểm. Có cấu trúc user prompt bọc XML boundary `<context>` và `<question>` cùng output JSON schema rõ ràng. Các ca test playground mô phỏng chi tiết.
    *   **Bảng tự kiểm tuân thủ (Compliance checklist - 1.5 / 6.0 điểm):**
        *   > [!WARNING]
        *   > **Lỗi nghiêm trọng do sao chép (copy-paste):** Nhóm đã copy nguyên văn nội dung giải pháp kỹ thuật từ dự án mẫu *Mini Tool Anonymizer* (che giấu dữ liệu PII CBNV nhân sự, Regex bắt email, CCCD, tệp `anonymizer-solution.py`, Regex Fallback...) và để nguyên trong tài liệu.
        *   > Tài liệu này hoàn toàn không khớp với đề tài *Network Doc Assistant* mà nhóm đang phát triển (đáng lẽ phải giải trình về an toàn bảo mật VectorDB, lọc IP nhạy cảm trong câu hỏi, phê duyệt HITL cho cấu hình thiết bị...).
        *   > Hội đồng chỉ chấm 1.5 điểm cho phần khung sườn tài liệu, trừ điểm nặng phần nội dung sai hoàn toàn đề tài.
    *   **Lộ trình áp dụng thực tế (Action plan 30-90 days - 6.0 / 6.0 điểm):** Lộ trình triển khai 30 và 90 ngày chi tiết, phân vai cụ thể. Đề xuất 3 trường hợp ứng dụng: use cases mở rộng tiếp theo (NOC Log Summarizer, Technical Report Assistant, O&M Procedures Assistant) rất thực tế và khả thi.
    *   *(Ghi nhận: Nhóm đã nộp bổ sung các tài liệu chất lượng khác như `test-cases-specification.md`, `handoff-contract.md`, `failure-modes-rollback.md` và `runbook-template.md` chứng tỏ sự nghiêm túc và hoàn thiện tài liệu tốt, tuy nhiên không bù được điểm nội dung bị lỗi của checklist tuân thủ).*

### Khía cạnh 5: Thuyết trình bảo vệ (Presentation & Q&A) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Cần cải thiện)
*   **Lý do đánh giá:**
    *   Nhóm không chuẩn bị tệp bản trình bày: slide deck thuyết trình chính thức cho buổi báo cáo.
    *   Không có sản phẩm demo chạy thực tế để thuyết phục hội đồng giám khảo.

---

## 3. Tổng kết điểm số và Xếp loại

*   **Tổng điểm:** 0 + 0 + 0 + 25.5 + 0 = **25.5 / 100 điểm**
*   **Xếp loại:** **Không đạt (Fail)**
*   **Trạng thái nghiệm thu:** **Không đạt yêu cầu** (Thiếu hoàn toàn phần mã nguồn kỹ thuật thực thi, tệp nhật ký vận hành, bản trình bày thuyết trình và sản phẩm demo; tài liệu tuân thủ bị lỗi copy-paste sai đề tài nghiêm trọng).

---

## 4. Nhận xét chung và Đề xuất cải tiến

1.  **Điểm mạnh:**
    *   Tư duy thiết kế nghiệp vụ và giải pháp kỹ thuật của Network Doc Assistant rất xuất sắc, bám sát nỗi đau thực tế và nhu cầu tra cứu tài liệu an toàn offline của kỹ sư Viettel Net.
    *   Các tài liệu thiết kế (One Pager, Workflow, Prompt Design, Action Plan, Failure Modes, Runbook) được chuẩn bị cực kỳ chi tiết, mạch lạc và có tư duy thực chiến cao.
2.  **Hạn chế lớn nhất:**
    *   Sự thiếu hụt hoàn toàn của phần hiện thực hóa kỹ thuật. Không có mã nguồn: source code thực tế, không có tệp nhật ký vận hành: execution log, không có slide thuyết trình và không có demo sản phẩm.
    *   Lỗi thiếu cẩn thận nghiêm trọng trong khâu chuẩn bị tài liệu tuân thủ bảo mật (`compliance-checklist.md`), sao chép nguyên văn dự án mẫu khác mà không chỉnh sửa nội dung.
3.  **Khuyến nghị cải tiến:**
    *   Nhóm cần khẩn trương phát triển mã nguồn Python cho ứng dụng Network Doc Assistant sử dụng RAG pipeline (kết hợp ChromaDB/FAISS cục bộ và gọi Ollama API offline với mô hình `qwen3.5:7b-instruct` hoặc `gemma4:e2b`).
    *   Rà soát và viết lại hoàn toàn tài liệu `compliance-checklist.md` cho khớp với dự án Network Doc Assistant (nêu rõ giải pháp bảo mật dữ liệu VectorDB, cơ chế Regex chặn IP thô ở đầu vào, cơ chế bật cờ đỏ HITL khi gợi ý tham số cấu hình mạng...).
    *   Soạn thảo slide báo cáo (5-7 slides) và chuẩn bị kịch bản demo chạy thực tế trên terminal để thuyết phục hội đồng trong buổi bảo vệ tiếp theo.
