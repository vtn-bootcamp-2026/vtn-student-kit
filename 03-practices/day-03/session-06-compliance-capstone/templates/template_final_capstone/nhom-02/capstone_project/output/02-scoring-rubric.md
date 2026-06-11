---
mo-ta: "Bảng chấm điểm sơ bộ (Scoring Rubric) cho use case AI Agent tra cứu tài liệu kỹ thuật mạng lưới Viettel"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Điểm số là ước lượng sơ bộ phục vụ thực hành. Không phản ánh đánh giá chính thức của VTN."
---

# Bảng Chấm Điểm Sơ Bộ (Scoring Rubric)

**Use Case:** AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel
**Người đánh giá:** [Tên mô phỏng — Nhóm thực hành]
**Ngày đánh giá:** 10/06/2026
**Phiên bản:** v1.0 — Draft

---

## 1. Thang Chấm Điểm Tổng Quan

Mỗi tiêu chí được chấm trên thang **0–20 điểm**, tổng cộng **5 tiêu chí = 100 điểm**.

| Mức điểm | Ý nghĩa |
|---|---|
| 18–20 | Xuất sắc — Đáp ứng hoàn toàn, rủi ro rất thấp |
| 14–17 | Tốt — Đáp ứng phần lớn, rủi ro có thể kiểm soát |
| 10–13 | Trung bình — Đáp ứng một phần, cần cải thiện trước khi triển khai |
| 5–9  | Yếu — Đáp ứng ít, cần xem xét lại thiết kế |
| 0–4  | Không đạt — Không nên triển khai ở trạng thái hiện tại |

---

## 2. Bảng Điểm Chi Tiết

### Tiêu chí 1: Tính Khả Thi của Dữ Liệu (Data Feasibility)

**Câu hỏi đánh giá:** Dữ liệu đầu vào đã có sẵn, có thể truy cập, có cấu trúc để xây dựng Knowledge Base chưa?

| Hạng mục con | Mức độ đáp ứng | Điểm con |
|---|---|---|
| Tài liệu kỹ thuật đã được tập trung hóa | Một phần (còn phân tán) | 3/5 |
| Định dạng tài liệu có thể xử lý tự động (PDF, DOCX) | Phần lớn có thể xử lý | 4/5 |
| Chất lượng / độ chính xác của tài liệu nguồn | Chưa đánh giá đầy đủ | 3/5 |
| Cơ chế cập nhật tài liệu định kỳ | Chưa có quy trình rõ ràng | 2/5 |

**→ Điểm Tiêu chí 1: 12/20**

**Nhận xét:**
> Tài liệu kỹ thuật hiện còn phân tán ở nhiều nguồn (hệ thống quản lý tài liệu, email, ổ đĩa chia sẻ). Chưa có quy trình cập nhật tự động khi tài liệu thay đổi. Đây là **rủi ro lớn nhất** của use case — nếu Knowledge Base lỗi thời, AI sẽ trả lời sai. Cần đầu tư vào cơ chế quản lý vòng đời tài liệu trước khi triển khai.

---

### Tiêu chí 2: Mức Độ Lặp Lại (Task Repetitiveness)

**Câu hỏi đánh giá:** Nhiệm vụ tra cứu tài liệu có lặp đi lặp lại đủ nhiều để AI mang lại giá trị rõ ràng không?

| Hạng mục con | Mức độ đáp ứng | Điểm con |
|---|---|---|
| Tần suất tra cứu tài liệu hàng ngày | Cao (5–15 lần/ngày/kỹ sư) | 5/5 |
| Mẫu câu hỏi có tính lặp lại cao | Cao (~60–70% câu hỏi tương tự nhau) | 4/5 |
| Quy trình tra cứu hiện tại có thể chuẩn hóa | Trung bình (cần nghiên cứu thêm) | 3/5 |
| Số lượng người dùng tiềm năng | Trung bình (ước tính ~50–200 kỹ sư) | 5/5 |

**→ Điểm Tiêu chí 2: 17/20**

**Nhận xét:**
> Use case có mức độ lặp lại rất cao — tra cứu tài liệu kỹ thuật là nhu cầu hàng ngày của kỹ sư vận hành và quy hoạch mạng. Đây là **điểm mạnh nhất** của bài toán, tạo cơ sở tốt để AI mang lại giá trị tiết kiệm thời gian đáng kể và nhân rộng trong tổ chức.

---

### Tiêu chí 3: Khả Năng Đo Lường (Measurability)

**Câu hỏi đánh giá:** Có thể đo lường được hiệu quả của AI một cách rõ ràng và khách quan không?

| Hạng mục con | Mức độ đáp ứng | Điểm con |
|---|---|---|
| Định nghĩa KPI rõ ràng (thời gian, độ chính xác) | Có, nhưng cần baseline hiện tại | 3/5 |
| Cơ chế thu thập dữ liệu đo lường | Chưa có hệ thống log/phản hồi | 2/5 |
| Khả năng so sánh trước–sau (A/B) | Trung bình (cần nhóm đối chứng) | 3/5 |
| Thang đánh giá chất lượng câu trả lời AI | Chưa xây dựng rubric đánh giá chất lượng | 2/5 |

**→ Điểm Tiêu chí 3: 10/20**

**Nhận xét:**
> Khả năng đo lường hiện còn yếu do thiếu dữ liệu baseline (thời gian tra cứu thực tế hiện tại chưa được ghi nhận). Cần thiết kế bộ KPI cụ thể và cơ chế ghi log phi nhạy cảm ngay từ đầu thí điểm để đảm bảo có dữ liệu đánh giá sau này.

---

### Tiêu chí 4: Rủi Ro Bảo Mật (Security Risk)

**Câu hỏi đánh giá:** Use case có xử lý thông tin nhạy cảm, mật hoặc PII không? Rủi ro bảo mật ở mức nào?

| Hạng mục con | Mức độ đáp ứng | Điểm con |
|---|---|---|
| Tài liệu kỹ thuật đầu vào có chứa thông tin mật không | Có rủi ro (một số tài liệu hạn chế) | 2/5 |
| Câu hỏi người dùng có thể tiết lộ thông tin nhạy cảm | Rủi ro thấp–trung bình | 3/5 |
| Kiến trúc triển khai có bảo vệ dữ liệu không (offline/local) | Có thể thiết kế offline | 4/5 |
| Cơ chế phân quyền tài liệu theo cấp bảo mật | Chưa có — cần thiết kế | 1/5 |

**→ Điểm Tiêu chí 4: 10/20**

**Nhận xét:**
> Đây là **rủi ro cần ưu tiên xử lý**. Tài liệu kỹ thuật mạng lưới có thể chứa thông tin nhạy cảm về cấu hình hạ tầng. Cần phân loại tài liệu theo cấp độ bảo mật và chỉ đưa tài liệu **không mật** vào Knowledge Base của MVP. Phải triển khai theo mô hình offline/intranet, không dùng API đám mây công cộng.

---

### Tiêu chí 5: Sự Tham Gia của Con Người — HITL (Human-in-the-Loop)

**Câu hỏi đánh giá:** Đã thiết kế rõ ràng các điểm kiểm duyệt của con người để kiểm soát rủi ro chưa?

| Hạng mục con | Mức độ đáp ứng | Điểm con |
|---|---|---|
| Các điểm HITL được xác định rõ ràng | Có (4 điểm HITL trong One-Pager) | 4/5 |
| Quy trình leo thang (escalation) khi AI không chắc | Đã đề xuất, cần chi tiết hóa | 3/5 |
| Cơ chế phản hồi để cải thiện AI theo thời gian | Chưa thiết kế | 2/5 |
| Người chịu trách nhiệm kiểm duyệt được xác định | Chưa cụ thể hóa vai trò | 2/5 |

**→ Điểm Tiêu chí 5: 11/20**

**Nhận xét:**
> Cơ chế HITL đã được nhận thức ở mức thiết kế nhưng chưa cụ thể hóa quy trình vận hành. Cần chỉ định rõ người/nhóm chịu trách nhiệm kiểm duyệt và xây dựng quy trình phản hồi định kỳ để cải thiện chất lượng AI theo thời gian.

---

## 3. Tổng Kết Điểm

| # | Tiêu chí | Điểm đạt | Điểm tối đa | Tỉ lệ |
|---|---|---|---|---|
| 1 | Tính khả thi của dữ liệu | **12** | 20 | 60% |
| 2 | Mức độ lặp lại | **17** | 20 | 85% |
| 3 | Khả năng đo lường | **10** | 20 | 50% |
| 4 | Rủi ro bảo mật | **10** | 20 | 50% |
| 5 | Sự tham gia của con người (HITL) | **11** | 20 | 55% |
| | **TỔNG ĐIỂM** | **60** | **100** | **60%** |

---

## 4. Biểu Đồ Điểm Radar (Mô phỏng dạng văn bản)

```
Tính khả thi dữ liệu       ████████████░░░░░░░░  12/20  ★★★☆☆
Mức độ lặp lại             █████████████████░░░  17/20  ★★★★☆
Khả năng đo lường          ██████████░░░░░░░░░░  10/20  ★★★☆☆
Rủi ro bảo mật             ██████████░░░░░░░░░░  10/20  ★★★☆☆
HITL                       ███████████░░░░░░░░░  11/20  ★★★☆☆
```

---

## 5. Kết Luận & Khuyến Nghị

**→ Tổng điểm: 60/100 — Mức: TRUNG BÌNH – CÓ THỂ TIẾN HÀNH THÍ ĐIỂM CÓ ĐIỀU KIỆN**

| Mức tổng điểm | Khuyến nghị |
|---|---|
| 80–100 | ✅ Tiến hành triển khai — Rủi ro thấp |
| 60–79  | ⚠️ Thí điểm có điều kiện — Cần giải quyết các điểm yếu trước |
| 40–59  | 🔶 Cần nghiên cứu thêm — Chưa sẵn sàng triển khai |
| < 40   | ❌ Không khuyến nghị — Cần thiết kế lại |

**Điều kiện để tiến hành thí điểm:**

1. ✅ **Bắt buộc:** Phân loại và kiểm duyệt toàn bộ tài liệu đưa vào Knowledge Base (chỉ tài liệu **không mật**).
2. ✅ **Bắt buộc:** Triển khai theo kiến trúc **offline / intranet** — không dùng API đám mây công cộng.
3. ⚠️ **Khuyến nghị:** Xây dựng cơ chế ghi log phiên tra cứu (phi nhạy cảm) để có dữ liệu đo lường.
4. ⚠️ **Khuyến nghị:** Chỉ định rõ người/nhóm chịu trách nhiệm HITL và cơ chế phản hồi định kỳ.

---

*Điểm số trong bảng này là ước lượng sơ bộ phục vụ thực hành Capstone. Không phản ánh đánh giá chính thức của VTN.*
