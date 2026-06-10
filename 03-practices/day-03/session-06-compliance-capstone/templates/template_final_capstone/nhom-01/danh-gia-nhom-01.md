---
mo-ta: Báo cáo đánh giá dự án Capstone của nhóm 01 - AI Scoring Assistant
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 16:30 +07:00"
updated-at: "2026-06-10 16:30 +07:00"
---

# Báo cáo đánh giá dự án Capstone nhóm 01

*   **Tên dự án ứng dụng:** AI Scoring Assistant — Trợ lý AI chấm điểm tự động theo tiêu chí cho trước
*   **Đối tượng đánh giá:** Nhóm 01 (Nhóm AI Builders - Trung tâm Đào tạo & Phát triển Năng lực số)
*   **Hội đồng giám khảo:** Ban giám khảo chuyên môn Viettel Net
*   **Mốc thời gian đánh giá:** Tháng 5 năm 2026 (May 2026)

---

## 1. Kết quả kiểm tra hồ sơ bài nộp
Hội đồng đã thực hiện rà soát các thành phần tài liệu và mã nguồn: source code trong thư mục bài nộp của nhóm 01 và ghi nhận trạng thái như sau:

| STT | Thành phần hồ sơ | Tên tệp tin | Trạng thái nộp | Đánh giá sơ bộ |
| :--- | :--- | :--- | :---: | :--- |
| 1 | Mã nguồn ứng dụng | Không tìm thấy | **Thiếu** | Không có tệp tin mã nguồn: source code Python nào được nộp. |
| 2 | Phiếu mô tả dự án | `01-use-case-one-pager.md` | Đã nộp | Nội dung nghiệp vụ rất chi tiết, định lượng rõ ràng hiệu quả và có phương án kiến trúc cụ thể. |
| 3 | Sơ đồ luồng logic | `02-logical-workflow.md` | Đã nộp | Đầy đủ sơ đồ Mermaid mô tả quy trình xử lý qua 5 tầng và ranh giới con người tham gia kiểm soát: human-in-the-loop (HITL). |
| 4 | Đặc tả lời nhắc cốt lõi | `03-core-prompt-design.md` | Đã nộp | Có đặc tả lời nhắc hệ thống: system prompt phòng ngự, JSON Schema đầu ra và nhật ký chạy thử chi tiết. |
| 5 | Bảng tự kiểm tuân thủ | `04-compliance-checklist.md` | Đã nộp | Điền đầy đủ và giải thích chi tiết các giải pháp kỹ thuật đáp ứng 12 tiêu chí bảo mật dữ liệu nội bộ. |
| 6 | Lộ trình áp dụng thực tế | `05-action-plan-30-90-days.md` | Đã nộp | Có lộ trình hành động: action plan chi tiết 30/90 ngày và đề xuất 3 trường hợp sử dụng: use cases tiếp theo rất thực tế. |
| 7 | Tệp nhật ký vận hành | Không tìm thấy | **Thiếu** | Không có tệp tin nhật ký vận hành: execution log (`scoring-log.csv` hoặc `execution-log.csv`) để kiểm toán rò rỉ thông tin nhạy cảm. |
| 8 | Bản trình bày bảo vệ | Không tìm thấy | **Thiếu** | Không có tệp tin bản trình bày: slide deck thuyết trình (`.pptx` hoặc `.pdf`). |

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
    *   Mặc dù nhóm đã thiết kế cấu trúc lời nhắc hệ thống: system prompt phòng vệ và bọc dữ liệu bằng thẻ XML rất chi tiết tại tài liệu `03-core-prompt-design.md`, do không có mã nguồn ứng dụng thực tế nên không có bất kỳ cơ chế phòng thủ tấn công lời nhắc: prompt injection nào được lập trình và vận hành.
    *   Hệ thống không thể kiểm chứng khả năng chặn đứng các kịch bản tấn công: Jailbreak, Data exfiltration (rò rỉ dữ liệu), Role confusion (nhầm lẫn vai trò) trên môi trường thực tế.

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Compliance & logging) - Tối đa 10 điểm
*   **Điểm đánh giá:** **0 / 10 điểm** (Mức Không đạt)
*   **Lý do đánh giá:**
    *   Nhóm không nộp tệp nhật ký vận hành: execution log, do đó không thể quét lỗi rò rỉ dữ liệu nhạy cảm: personal identifiable information (PII) trên nhật ký.
    *   Không có mã nguồn thực tế để kiểm tra cơ chế bảo mật khóa kết nối hoặc cấu hình các biến môi trường trong tệp `.env`.

### Khía cạnh 4: Bộ hồ sơ giải pháp (Capstone Blueprint) - Tối đa 30 điểm
*   **Điểm đánh giá:** **30 / 30 điểm** (Mức Xuất sắc)
*   **Lý do đánh giá:**
    *   **Phiếu mô tả dự án (Use case one pager - 6.0 / 6.0 điểm):** Phân tích nghiệp vụ sâu sắc về công cụ chấm bài tự động, giải quyết trực tiếp nỗi đau thực tế của Trung tâm Đào tạo VTN (thời gian chấm bài thủ công lâu, rủi ro bảo mật dữ liệu). Định lượng rõ hiệu quả (giảm thời gian từ 20-45 phút xuống 2-3 phút, tiết kiệm 30-40 giờ/đợt, chi phí 0 VNĐ). Tài liệu được điền đầy đủ, không bị lỗi bỏ trống thẻ template.
    *   **Sơ đồ luồng logic (Logical workflow - 6.0 / 6.0 điểm):** Sơ đồ Mermaid thiết kế mạch lạc quy trình xử lý qua 5 tầng, chỉ định rõ ràng ranh giới con người tham gia kiểm soát: human-in-the-loop (HITL) nghiêm ngặt (AI đề xuất, giám khảo review/edit/approve trước khi lưu kết quả chính thức).
    *   **Đặc tả lời nhắc cốt lõi (Core prompt design - 6.0 / 6.0 điểm):** Thiết kế system prompt có các chỉ thị chấm điểm, phòng vệ prompt injection và tự kiểm. Có cấu trúc user prompt bọc XML boundary `<submission>` và output JSON schema 8 trường cố định rõ ràng. Các ca test playground rất đa dạng (bình thường, bài sơ sài, prompt injection).
    *   **Bảng tự kiểm tuân thủ (Compliance checklist - 6.0 / 6.0 điểm):** Tự đánh giá rất chi tiết cho 12 tiêu chí tuân thủ bảo mật dữ liệu offline, phân quyền, human-in-the-loop, phòng thủ và logging phi nhạy cảm. Giải pháp áp dụng thực tế được giải trình rất cặn kẽ và thuyết phục.
    *   **Lộ trình áp dụng thực tế (Action plan 30-90 days - 6.0 / 6.0 điểm):** Lộ trình triển khai 30 và 90 ngày chi tiết, phân vai cụ thể. Đề xuất 3 trường hợp ứng dụng: use cases mở rộng tiếp theo rất thực tế và khả thi cho Trung tâm Đào tạo VTN.

### Khía cạnh 5: Thuyết trình bảo vệ (Presentation & Q&A) - Tối đa 20 điểm
*   **Điểm đánh giá:** **0 / 20 điểm** (Mức Cần cải thiện)
*   **Lý do đánh giá:**
    *   Nhóm không chuẩn bị tệp bản trình bày: slide deck thuyết trình chính thức cho buổi báo cáo.
    *   Không có sản phẩm demo chạy thực tế để thuyết phục hội đồng giám khảo.

---

## 3. Tổng kết điểm số và Xếp loại

*   **Tổng điểm:** 0 + 0 + 0 + 30 + 0 = **30 / 100 điểm**
*   **Xếp loại:** **Không đạt (Fail)**
*   **Trạng thái nghiệm thu:** **Không đạt yêu cầu** (Thiếu hoàn toàn phần mã nguồn kỹ thuật thực thi, tệp nhật ký vận hành, bản trình bày thuyết trình và sản phẩm demo).

---

## 4. Nhận xét chung và Đề xuất cải tiến

1.  **Điểm mạnh:**
    *   Tư duy thiết kế nghiệp vụ của giải pháp AI Scoring Assistant rất xuất sắc, bám sát nỗi đau thực tế và nhu cầu bảo mật thông tin nội bộ của Trung tâm Đào tạo VTN.
    *   Bộ hồ sơ giải pháp: capstone blueprint (5 tài liệu) được chuẩn bị cực kỳ chỉn chu, chi tiết và hoàn hảo, không có lỗi bỏ trống template.
2.  **Hạn chế lớn nhất:**
    *   Sự thiếu hụt hoàn toàn của phần hiện thực hóa kỹ thuật. Không có mã nguồn: source code thực tế, không có tệp nhật ký vận hành: execution log, không có slide thuyết trình và không có demo sản phẩm.
3.  **Khuyến nghị cải tiến:**
    *   Nhóm cần nhanh chóng phát triển mã nguồn Python cho ứng dụng AI Scoring Assistant dựa trên luồng xử lý và prompt đã đặc tả.
    *   Có thể tham khảo cấu trúc code mẫu tại `references/anonymizer-solution.py` và `references/anonymizer-solution-gemini.py` để tích hợp gọi Ollama API local (qwen3.5:1.5b-instruct / gemma4:e2b), thực hiện validate JSON bằng Pydantic và ghi log phi nhạy cảm ra file csv.
    *   Soạn thảo slide báo cáo (5-7 slides) và chuẩn bị kịch bản demo chạy thực tế trên terminal để thuyết phục hội đồng trong buổi bảo vệ tiếp theo.
