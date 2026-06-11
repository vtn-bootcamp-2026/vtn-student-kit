---
mo-ta: "Phiếu mô tả trường hợp sử dụng AI Agent tra cứu tài liệu thiết bị, tính năng, tham số và quy hoạch mạng lưới Viettel"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Tài liệu sử dụng dữ liệu mô phỏng. Tuyệt đối không chứa thông tin thật, PII hay dữ liệu nhạy cảm của VTN."
---

# Phiếu Mô Tả Trường Hợp Sử Dụng (Use Case One-Pager)

*   **Tên dự án ứng dụng:** AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel (Network Doc Assistant)
*   **Đơn vị đề xuất:** [Tên phòng/ban kỹ thuật — ẩn danh mô phỏng]
*   **Người đầu mối liên hệ:** [Kỹ sư Nguyễn Văn X — tên mô phỏng]
*   **Mức độ ưu tiên:** Cao
*   **Mốc thời gian dự kiến thí điểm:** Quý 3 / 2026

---

## 1. Vấn đề và Nhu cầu Thực tế (Problem Statement)

*   **Hiện trạng:** Các kỹ sư vận hành mạng (NOC/BSS) thường xuyên phải tra cứu tài liệu kỹ thuật phân tán: thông số thiết bị, hướng dẫn cấu hình, bảng tham số, quy hoạch vùng phủ — lưu trữ rải rác trên hàng trăm file PDF/Word/Excel nội bộ. Mỗi lần tra cứu có thể mất **10–20 phút** tìm kiếm thủ công.
*   **Rủi ro hiện tại:** Kỹ sư dễ tra cứu sai phiên bản tài liệu, áp dụng tham số cũ gây lỗi cấu hình thiết bị hoặc quy hoạch không tối ưu.

---

## 2. Người Dùng Chính (Primary User)

| Nhóm người dùng | Vai trò | Tần suất sử dụng dự kiến |
|---|---|---|
| Kỹ sư vận hành mạng (NOC) | Tra cứu thông số thiết bị, cấu hình sự cố | Hàng ngày (5–10 lần/ngày) |
| Kỹ sư quy hoạch mạng | Tra cứu bảng tham số quy hoạch vùng phủ | 2–3 lần/tuần |
| Chuyên viên hỗ trợ kỹ thuật (L2/L3) | Tìm kiếm hướng dẫn tính năng nâng cao | Theo yêu cầu sự cố |
| Kỹ sư tích hợp thiết bị mới | Tra cứu datasheet, thông số kỹ thuật | Theo dự án |

---

## 3. Đầu Vào Dự Kiến (Input)

| Loại đầu vào | Mô tả mô phỏng | Ghi chú |
|---|---|---|
| Câu hỏi tự nhiên (tiếng Việt) | "Thông số công suất phát tối đa của thiết bị BTS-X200 là bao nhiêu?" | Người dùng gõ trực tiếp |
| Từ khóa kỹ thuật | "tham số RACH", "quy hoạch tần số băng tần 2100 MHz" | Tìm kiếm nhanh |
| Tài liệu kỹ thuật nội bộ (mô phỏng) | File PDF/DOCX tài liệu thiết bị mạng — phiên bản giả định | Đã được vector hóa vào knowledge base |
| Bảng tham số cấu hình (mô phỏng) | File Excel chứa bảng thông số cấu hình — dữ liệu giả định | Không chứa dữ liệu thật |

> ⚠️ **Lưu ý:** Toàn bộ đầu vào trong môi trường thí điểm chỉ sử dụng **dữ liệu mô phỏng / tài liệu giả định**. Tuyệt đối không tải tài liệu kỹ thuật thật, mật, hoặc nội bộ chưa được phân loại vào hệ thống.

---

## 4. Đầu Ra Mong Muốn (Output)

| Loại đầu ra | Mô tả | Ví dụ mô phỏng |
|---|---|---|
| Trả lời câu hỏi trực tiếp | Câu trả lời ngắn gọn, có trích dẫn nguồn tài liệu | "Theo tài liệu [TL-BTS-X200-v2.1], công suất tối đa là XX dBm" |
| Tóm tắt đặc tính kỹ thuật | Danh sách thông số chính của thiết bị được hỏi | Bảng markdown hiển thị trực tiếp trong giao diện chat |
| Gợi ý cấu hình phù hợp | Đề xuất tham số dựa trên ngữ cảnh người dùng mô tả | "Với kịch bản vùng phủ đô thị, khuyến nghị sử dụng tham số ABC = XYZ" |
| Trích dẫn nguồn rõ ràng | Tên tài liệu gốc, số trang, phiên bản | [Bắt buộc hiển thị kèm mọi câu trả lời] |

---

## 5. Giá Trị Kỳ Vọng (Business Value)

| Chỉ số | Hiện trạng (ước tính mô phỏng) | Mục tiêu sau triển khai | Cơ sở đo |
|---|---|---|---|
| Thời gian tra cứu trung bình | ~15 phút/lần (tra cứu thủ công) | < 2 phút/lần | Log thời gian phiên chat |
| Tỉ lệ tra cứu đúng tài liệu | ~70% (tự tìm kiếm) | > 90% | Khảo sát người dùng |
| Số lần leo thang lên cấp trên để hỏi | ~3–5 lần/người/tuần | < 1 lần/người/tuần | Ticket hỗ trợ nội bộ |
| Mức độ hài lòng người dùng | — (chưa đo) | ≥ 4.0/5.0 | Khảo sát NPS nội bộ |

---

## 6. Phạm Vi MVP — Sản Phẩm Khả Dụng Tối Thiểu (MVP Scope)

### ✅ MVP xử lý (Trong phạm vi thí điểm)

*   Tra cứu thông tin tính năng và thông số kỹ thuật thiết bị từ kho tài liệu mô phỏng.
*   Trả lời câu hỏi bằng tiếng Việt, có trích dẫn nguồn tài liệu rõ ràng.
*   Giao diện chat web đơn giản chạy nội bộ (intranet).
*   Ghi log phiên chat phi nhạy cảm (không lưu nội dung câu hỏi/trả lời đầy đủ).

### ❌ MVP CHƯA xử lý (Ngoài phạm vi — để đảm bảo an toàn)

| Chức năng bị loại | Lý do loại khỏi MVP |
|---|---|
| Truy cập tài liệu kỹ thuật mật / hạn chế | Chưa có cơ chế phân quyền tài liệu theo cấp độ bảo mật |
| Tự động cập nhật tài liệu từ hệ thống quản lý tài liệu | Rủi ro đồng bộ tài liệu sai phiên bản |
| Đưa ra khuyến nghị cấu hình cho mạng lưới đang vận hành thực tế | Rủi ro ảnh hưởng đến chất lượng mạng — phải qua phê duyệt chuyên gia |
| Tích hợp với hệ thống quản lý cấu hình mạng (NMS/EMS) | Phạm vi tích hợp phức tạp, rủi ro bảo mật cao |
| Ghi nhớ lịch sử hội thoại của người dùng lâu dài (persistent memory) | Rủi ro lưu trữ thông tin nhạy cảm trong log |

---

## 7. Kiến Trúc Kỹ Thuật Đề Xuất (Technical Architecture — Mô phỏng)

```text
+----------------------------------------------------------+
|         TẦNG GIAO DIỆN (User Interface)                  |
|  [ Giao diện Chat Web — Chạy trên Intranet VTN ]         |
+----------------------------------------------------------+
                          |
+----------------------------------------------------------+
|         TẦNG AI AGENT (RAG Pipeline)                     |
|  * Nhận câu hỏi → Tìm kiếm ngữ nghĩa (Vector Search)    |
|  * Truy xuất đoạn tài liệu liên quan nhất                |
|  * Mô hình LLM tổng hợp câu trả lời + trích dẫn nguồn   |
+----------------------------------------------------------+
                          |
+----------------------------------------------------------+
|         TẦNG KNOWLEDGE BASE (Mô phỏng)                   |
|  * Tài liệu kỹ thuật đã được vector hóa (giả định)       |
|  * Cơ sở dữ liệu vector nội bộ (VectorDB cục bộ)         |
+----------------------------------------------------------+
                          |
+----------------------------------------------------------+
|         TẦNG KIỂM DUYỆT (HITL Gate)                      |
|  * Chuyên gia kỹ thuật xác nhận câu trả lời quan trọng  |
|  * Đánh dấu câu trả lời "Cần xem xét" → Gửi chuyên gia  |
+----------------------------------------------------------+
```

---

## 8. Điểm Dừng Kiểm Duyệt Con Người (Human-in-the-Loop — HITL)

| # | Điểm kiểm duyệt | Ai kiểm duyệt | Hành động |
|---|---|---|---|
| HITL-01 | **Câu trả lời liên quan đến gợi ý cấu hình tham số mạng** | Kỹ sư cấp cao / Trưởng nhóm kỹ thuật | Phê duyệt trước khi áp dụng. AI chỉ gợi ý, không tự thực thi. |
| HITL-02 | **Câu trả lời AI có độ tin cậy thấp** (confidence score < 70%) | Chuyên viên hỗ trợ kỹ thuật | Hệ thống hiển thị cảnh báo, yêu cầu xác nhận từ người dùng. |
| HITL-03 | **Tài liệu nguồn trích dẫn không rõ ràng hoặc chưa được xác thực** | Người quản lý knowledge base | Đưa vào hàng đợi kiểm duyệt tài liệu trước khi đưa vào sản xuất. |
| HITL-04 | **Câu hỏi vượt phạm vi MVP** (liên quan mạng thật, tài liệu mật) | Người quản trị hệ thống | Từ chối trả lời và ghi log sự kiện. |

---

## 9. Kế Hoạch Hành Động Tiếp Theo (Next Steps)

1.  **Tuần 1–2:** Xây dựng knowledge base mô phỏng với tài liệu kỹ thuật giả định (không dùng tài liệu thật).
2.  **Tuần 3–4:** Phát triển pipeline RAG, tích hợp giao diện chat nội bộ.
3.  **Tuần 5–6:** Thí điểm với nhóm **05 kỹ sư nòng cốt** (dữ liệu mô phỏng), thu thập phản hồi.
4.  **Tuần 7–8:** Đánh giá kết quả, tinh chỉnh, hoàn thiện cơ chế HITL, trình phê duyệt ban lãnh đạo.

---

*Tài liệu này được tạo cho mục đích thực hành. Mọi dữ liệu, tên thiết bị, tham số đều là MÔ PHỎNG.*
