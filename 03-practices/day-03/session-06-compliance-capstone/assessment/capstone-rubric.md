---
mo-ta: "Rubric chấm điểm Capstone session 06 cho giảng viên và trợ giảng"
trang-thai: active
phien-ban: v1.0
created-at: 2026-05-27 16:45 +07:00
updated-at: 2026-05-27 16:45 +07:00
---

# Rubric chấm điểm Capstone: Session 06

## Cách sử dụng

Rubric này dành cho giảng viên và trợ giảng khi chấm bài Capstone. Mỗi tiêu chí dùng thang 1-5, tổng tối đa **50 điểm**. Nhóm đạt **≥35 điểm (70%)** được xét nghiệm thu.

---

## Thang điểm

| Điểm | Mô tả |
|------|-------|
| 5 — Xuất sắc | Vượt kỳ vọng, có sáng tạo hoặc xử lý edge case phức tạp |
| 4 — Tốt | Đáp ứng đầy đủ yêu cầu, chất lượng ổn định |
| 3 — Đạt | Hoàn thành yêu cầu cơ bản, còn thiếu nhỏ |
| 2 — Chưa đạt | Thiếu sót đáng kể, cần sửa lại |
| 1 — Kém | Không hoàn thành hoặc sai hướng hoàn toàn |

---

## A. Kiểm thử toàn trình (End-to-End Testing) — Tối đa 15 điểm

### A1. Đặc tả bộ kiểm thử — Test Cases Specification (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | 10 test cases đầy đủ, bao phủ cả 4 nhóm tình huống (bình thường, lỗi, thiếu dữ liệu, vượt phạm vi). Mỗi test case có input, expected output, actual output rõ ràng. |
| 4 | 8-9 test cases, thiếu 1-2 trường hợp ở nhóm vượt phạm vi hoặc lỗi. |
| 3 | 6-7 test cases, bao phủ 3/4 nhóm tình huống. |
| 2 | Dưới 6 test cases hoặc chỉ bao phủ 2 nhóm tình huống trở xuống. |
| 1 | Không nộp đặc tả hoặc đặc tả trống. |

### A2. Kết quả chạy kiểm thử (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | 10/10 test cases PASS. Log chạy rõ ràng, có timestamp, không cảnh báo lỗi. |
| 4 | 8-9/10 test cases PASS. 1-2 case thất bại nhưng có phân tích nguyên nhân. |
| 3 | 6-7/10 test cases PASS. |
| 2 | Dưới 6/10 PASS hoặc không có log chạy. |
| 1 | Không chạy kiểm thử hoặc không nộp kết quả. |

### A3. Sửa lỗi và cải tiến sau kiểm thử (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | Tất cả test cases thất bại ban đầu đã được sửa và PASS ở lần chạy lại. Có ghi nhận quá trình debug trong báo cáo. |
| 4 | Hầu hết test cases thất bại đã sửa. Còn 1 case chưa giải quyết nhưng có phân tích nguyên nhân. |
| 3 | Sửa được khoảng một nửa số test cases thất bại. |
| 2 | Ít nỗ lực sửa lỗi, bỏ qua nhiều test cases thất bại. |
| 1 | Không có nỗ lực sửa lỗi hoặc nộp lại kết quả giống hệt lần đầu. |

---

## B. Tuân thủ bảo mật & Phòng thủ Prompt Injection — Tối đa 15 điểm

### B1. Bảng kiểm tuân thủ — Compliance Checklist (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | Compliance checklist điền đầy đủ tất cả các hạng mục (A-F). Mỗi hạng mục có mô tả giải pháp cụ thể, không chỉ tích checkbox chung chung. |
| 4 | Điền đầy đủ 5/6 hạng mục. 1 hạng mục thiếu mô tả chi tiết. |
| 3 | Điền 3-4/6 hạng mục. |
| 2 | Điền dưới 3 hạng mục hoặc chỉ tích checkbox không có mô tả. |
| 1 | Không nộp compliance checklist. |

### B2. Phòng thủ Prompt Injection (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | 3/3 kịch bản tấn công (Jailbreak, Data Exfiltration, Role Confusion) bị chặn thành công. Có log chứng minh công cụ từ chối thực thi lệnh độc hại. Có biện pháp phòng vệ đa lớp (tiền lọc + ép schema + hậu kiểm). |
| 4 | 2/3 kịch bản bị chặn. 1 kịch bản lọt qua nhưng nhóm có phân tích và đề xuất khắc phục. |
| 3 | 1-2/3 kịch bản bị chặn, chưa có biện pháp phòng vệ đa lớp. |
| 2 | Không chặn được kịch bản nào hoặc không chạy test injection. |
| 1 | Không nộp kết quả test injection. |

### B3. An toàn nhật ký — Clean Logs (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | `execution-log.csv` hoàn chỉnh, không chứa PII thật (email, số điện thoại, CCCD thật). Mọi trường nhạy cảm đã được thay bằng `[REDACTED_*]`. Có ít nhất 10 dòng log tương ứng với 10 test cases. |
| 4 | Log đủ 8-9 dòng. Không lộ PII thật nhưng có 1-2 trường còn thiếu redaction. |
| 3 | Log đủ 6-7 dòng. Không lộ PII thật. |
| 2 | Log dưới 6 dòng hoặc phát hiện 1-2 trường PII thật chưa che giấu. |
| 1 | Log lộ nhiều PII thật hoặc không nộp execution-log.csv. |

---

## C. Bộ hồ sơ đóng gói triển khai — Implementation Kit — Tối đa 10 điểm

### C1. Đầy đủ tài liệu (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | Nộp đủ 7/7 template đã điền: test-cases-specification, compliance-checklist, runbook, failure-modes-rollback, use-case-one-pager, handoff-contract, action-plan-30-90-days. Mỗi file có nội dung cụ thể của nhóm, không phải bản trống. |
| 4 | Nộp 5-6/7 template. |
| 3 | Nộp 3-4/7 template. |
| 2 | Nộp dưới 3 template hoặc đa số còn trống. |
| 1 | Không nộp Implementation Kit. |

### C2. Chất lượng tài liệu (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | Tài liệu viết rõ ràng, có số liệu cụ thể (RAM, model, thời gian phản hồi). Runbook có lệnh CLI chính xác. Failure modes có severity rating. Handoff contract có cam kết SLA đo lường được. |
| 4 | Tài liệu khá đầy đủ, thiếu 1-2 chi tiết kỹ thuật cụ thể. |
| 3 | Tài liệu ở mức trung bình, một số phần còn chung chung. |
| 2 | Tài liệu sơ sài, nhiều phần placeholder chưa điền. |
| 1 | Tài liệu không đọc được hoặc không liên quan đến dự án của nhóm. |

---

## D. Trình bày Capstone — Tối đa 10 điểm

### D1. Nội dung trình bày (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | Trình bày đầy đủ: vấn đề → giải pháp → kiến trúc → kết quả kiểm thử → compliance → kế hoạch triển khai. Có số liệu cụ thể, demo chạy được. Thời gian 5-7 phút. |
| 4 | Trình bày đủ các phần chính nhưng thiếu 1 phần (thường là kế hoạch triển khai hoặc demo). |
| 3 | Trình bày thiếu 2 phần hoặc quá ngắn (< 3 phút) hoặc quá dài (> 10 phút). |
| 2 | Trình bày lan man, không có cấu trúc rõ ràng. |
| 1 | Không trình bày hoặc slide trống. |

### D2. Phản biện — Q&A (5 điểm)

| Điểm | Tiêu chuẩn |
|------|-----------|
| 5 | Trả lời đầy đủ 3+ câu hỏi từ giảng viên và nhóm khác. Thể hiện hiểu sâu về kiến trúc, biết rõ giới hạn công cụ, có đề xuất cải thiện thực tế. |
| 4 | Trả lời được 2 câu hỏi rõ ràng. 1 câu trả lời chưa thỏa đáng. |
| 3 | Trả lời được 1 câu hỏi. 2 câu trả lời chung chung. |
| 2 | Không trả lời được câu hỏi nào hoặc trả lời sai hướng. |
| 1 | Không tham gia phần phản biện. |

---

## Tổng hợp điểm

| Hạng mục | Điểm tối đa | Điểm nhóm |
|----------|------------|-----------|
| A. Kiểm thử toàn trình | 15 | |
| B. Tuân thủ & Phòng thủ Prompt Injection | 15 | |
| C. Implementation Kit | 10 | |
| D. Trình bày Capstone | 10 | |
| **Tổng cộng** | **50** | |

### Xếp loại

| Tổng điểm | Xếp loại | Ghi chú |
|-----------|---------|---------|
| 45-50 | **Xuất sắc** | Sẵn sàng thí điểm tại đơn vị |
| 35-44 | **Đạt** | Đủ điều kiện nghiệm thu, cần tinh chỉnh nhỏ |
| 25-34 | **Cần bổ sung** | Phải nộp lại phần thiếu trong 7 ngày |
| Dưới 25 | **Chưa đạt** | Cần thực hiện lại toàn bộ |

---

## Ghi chú cho giảng viên

* Chấm dựa trên **sản phẩm thực tế**, không tính nỗ lực hay hứa hẹn.
* Nhóm dùng Gemini Cloud API thay vì Ollama local vẫn chấm bình thường, miễn giữ an toàn (API key trong `.env`, không commit key).
* Nhóm có sáng tạo (thêm tính năng, xử lý edge case ngoài danh sách) → cân nhắc cộng thêm vào hạng mục tương ứng, nhưng tổng không vượt 50.
* Phản biện (D2): nên khuyến khích nhóm khác đặt câu hỏi chéo để tăng tương tác.
