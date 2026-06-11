---
mo-ta: "Danh sách kiểm tra rủi ro bảo mật và tuân thủ cho use case AI Agent tra cứu tài liệu kỹ thuật mạng lưới Viettel"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Tài liệu sử dụng dữ liệu mô phỏng. Không chứa thông tin thật, PII hay dữ liệu nhạy cảm của VTN."
---

# Danh Sách Kiểm Tra Rủi Ro (Risk Checklist)

**Use Case:** AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel
**Người thực hiện rà soát:** [Tên nhóm thực hành — mô phỏng]
**Ngày rà soát:** 10/06/2026
**Phiên bản:** v1.0 — Draft

---

## 1. Mục Đích

Tài liệu này rà soát các rủi ro bảo mật thông tin và tuân thủ dữ liệu nhạy cảm (PII/bảo mật kỹ thuật) tiềm ẩn trong quá trình thiết kế, triển khai và vận hành hệ thống AI Agent tra cứu tài liệu kỹ thuật mạng lưới Viettel. Đồng thời đề xuất các **rào cản an toàn (guardrails)** tương ứng để kiểm soát từng rủi ro.

> ⚠️ **Lưu ý quan trọng:** Tất cả các kịch bản rủi ro trong tài liệu này đều là **mô phỏng giả định** để phục vụ thực hành. Tuyệt đối không sử dụng thông tin kỹ thuật thật, cấu hình mạng thật, hoặc dữ liệu nhạy cảm thật của VTN.

---

## 2. Bảng Rủi Ro Tổng Quan

| # | Mã rủi ro | Tên rủi ro | Mức độ nghiêm trọng | Xác suất xảy ra | Mức độ ưu tiên |
|---|---|---|---|---|---|
| 1 | RISK-01 | Rò rỉ tài liệu kỹ thuật mật vào Knowledge Base | Rất cao | Trung bình | 🔴 **Cao — Xử lý ngay** |
| 2 | RISK-02 | AI trả lời sai lệch thông tin kỹ thuật quan trọng | Cao | Cao | 🔴 **Cao — Xử lý ngay** |
| 3 | RISK-03 | Thông tin tài liệu bị lỗi thời, không cập nhật | Trung bình | Cao | 🟠 **Trung bình — Xử lý trước khi mở rộng** |
| 4 | RISK-04 | Câu hỏi người dùng chứa thông tin nhạy cảm bị ghi vào log | Cao | Trung bình | 🔴 **Cao — Xử lý ngay** |

---

## 3. Phân Tích Chi Tiết Từng Rủi Ro

---

### 🔴 RISK-01: Rò Rỉ Tài Liệu Kỹ Thuật Mật vào Knowledge Base

**Mô tả rủi ro:**
Tài liệu kỹ thuật mạng lưới có thể chứa thông tin cấu hình hạ tầng nhạy cảm (tần số, địa chỉ IP thiết bị nội bộ, cấu hình bảo mật). Nếu tài liệu mật được đưa vào Knowledge Base mà không qua phân loại, AI sẽ có thể trả lời (vô tình tiết lộ) thông tin này cho người dùng không có thẩm quyền.

**Kịch bản xảy ra (mô phỏng):**
> Kỹ sư X vô tình tải tài liệu cấu hình lõi mạng lên hệ thống. Người dùng Y (ở cấp quyền thấp hơn) tra cứu và nhận được thông tin cấu hình mà đáng lẽ không được phép truy cập.

**Mức độ tác động:** Nghiêm trọng — Có thể vi phạm quy chế bảo mật thông tin nội bộ của VTN và các quy định pháp lý liên quan.

**Rào cản an toàn (Guardrails):**

| # | Guardrail | Loại | Trạng thái MVP |
|---|---|---|---|
| G1.1 | **Phân loại tài liệu bắt buộc trước khi đưa vào KB:** Mỗi tài liệu phải được GÁN nhãn bảo mật (Công khai / Nội bộ / Mật) bởi người có thẩm quyền trước khi vector hóa. Chỉ tài liệu nhãn "Công khai nội bộ" mới được đưa vào Knowledge Base của MVP. | Quy trình + Kỹ thuật | ✅ Bắt buộc triển khai |
| G1.2 | **Cơ chế kiểm duyệt Knowledge Base định kỳ (KB Audit):** Hàng quý, người quản lý Knowledge Base phải rà soát toàn bộ danh sách tài liệu đang trong KB để loại bỏ tài liệu hết hạn hoặc đã được nâng cấp độ mật. | Quy trình | ✅ Bắt buộc triển khai |
| G1.3 | **Không cho phép người dùng cuối tự tải tài liệu vào KB trong MVP:** Chỉ người quản trị hệ thống (admin role) mới có quyền đưa tài liệu vào Knowledge Base. | Kỹ thuật (phân quyền) | ✅ Bắt buộc trong MVP |
| G1.4 | **Watermarking nhận dạng nguồn (Tham khảo — Giai đoạn sau MVP):** Gắn metadata nguồn gốc cho mỗi đoạn tài liệu trong KB để truy vết khi phát hiện rò rỉ. | Kỹ thuật | 🔜 Sau MVP |

**Checkpoint HITL:**
> Mỗi tài liệu mới đưa vào Knowledge Base phải được **người có thẩm quyền phê duyệt** (ký tắt trên danh sách kiểm duyệt) trước khi hệ thống tiếp nhận. Không được tự động hóa bước này trong MVP.

---

### 🔴 RISK-02: AI Trả Lời Sai Lệch Thông Tin Kỹ Thuật Quan Trọng (Hallucination)

**Mô tả rủi ro:**
Mô hình AI (LLM) có thể tạo ra câu trả lời có vẻ hợp lý nhưng thực tế sai — đặc biệt nguy hiểm khi liên quan đến tham số cấu hình mạng, ngưỡng công suất, hoặc gợi ý quy hoạch. Kỹ sư tin tưởng vào câu trả lời AI mà không kiểm chứng có thể áp dụng sai cấu hình.

**Kịch bản xảy ra (mô phỏng):**
> Kỹ sư hỏi: "Ngưỡng RSRP tối thiểu cho handover LTE là bao nhiêu?" — AI trả lời một giá trị không có trong tài liệu nguồn (hallucinate). Kỹ sư áp dụng mà không kiểm tra → gây sự cố vùng phủ.

**Mức độ tác động:** Cao — Có thể gây cấu hình sai thiết bị, ảnh hưởng đến chất lượng mạng lưới.

**Rào cản an toàn (Guardrails):**

| # | Guardrail | Loại | Trạng thái MVP |
|---|---|---|---|
| G2.1 | **Bắt buộc hiển thị trích dẫn nguồn kèm mọi câu trả lời:** Mọi câu trả lời của AI phải kèm tên tài liệu nguồn, số trang, phiên bản tài liệu. Nếu AI không tìm được nguồn trích dẫn → hiển thị cảnh báo "Không tìm thấy nguồn xác thực" thay vì bịa đặt. | Kỹ thuật (Prompt Engineering + RAG) | ✅ Bắt buộc triển khai |
| G2.2 | **Ngưỡng tin cậy (Confidence Threshold):** Nếu điểm tương đồng (cosine similarity) giữa câu hỏi và tài liệu nguồn < 0.70, hệ thống hiển thị cảnh báo màu vàng: "⚠️ Độ tin cậy thấp — Vui lòng xác nhận với tài liệu gốc". | Kỹ thuật (Vector Search) | ✅ Bắt buộc triển khai |
| G2.3 | **HITL bắt buộc cho gợi ý cấu hình/tham số:** Mọi câu trả lời liên quan đến gợi ý cấu hình mạng đều phải được kỹ sư cấp cao xem xét và phê duyệt trước khi áp dụng. AI chỉ là công cụ gợi ý — KHÔNG được phép tự thực thi hay áp dụng cấu hình. | Quy trình (HITL) | ✅ Bắt buộc triển khai |
| G2.4 | **Dán nhãn "AI-Generated — Cần xác minh" trên mọi đầu ra:** Mọi câu trả lời đều có watermark text rõ ràng nhắc nhở người dùng kiểm tra lại với tài liệu gốc. | Kỹ thuật (UI/UX) | ✅ Bắt buộc triển khai |

**Checkpoint HITL:**
> Đối với mọi gợi ý cấu hình tham số: **Kỹ sư cấp cao / Trưởng nhóm phải ký xác nhận** trên phiếu kiểm tra trước khi áp dụng vào thiết bị thực. AI chỉ được sử dụng như tài liệu tham khảo, không có giá trị quyết định.

---

### 🟠 RISK-03: Thông Tin Tài Liệu Bị Lỗi Thời — Knowledge Base Không Cập Nhật

**Mô tả rủi ro:**
Tài liệu kỹ thuật mạng lưới thường xuyên được cập nhật theo phiên bản phần mềm, phần cứng mới. Nếu Knowledge Base không được cập nhật kịp thời, AI sẽ trả lời dựa trên thông tin lỗi thời — đặc biệt nguy hiểm với thông số kỹ thuật và tham số cấu hình.

**Kịch bản xảy ra (mô phỏng):**
> Tài liệu phiên bản v2.0 được đưa vào KB. Sau đó nhà cung cấp phát hành bản v3.0 với thay đổi tham số quan trọng. KB không được cập nhật → AI tiếp tục trả lời theo v2.0 cũ.

**Mức độ tác động:** Trung bình — Có thể dẫn đến áp dụng tham số không tối ưu hoặc không còn áp dụng được.

**Rào cản an toàn (Guardrails):**

| # | Guardrail | Loại | Trạng thái MVP |
|---|---|---|---|
| G3.1 | **Metadata phiên bản bắt buộc cho mỗi tài liệu:** Mỗi tài liệu trong KB phải có metadata: `tên tài liệu`, `phiên bản`, `ngày cập nhật gần nhất`, `người phê duyệt`. AI hiển thị metadata này trong mỗi trích dẫn. | Kỹ thuật (Metadata) | ✅ Bắt buộc triển khai |
| G3.2 | **Cơ chế cảnh báo tài liệu cũ (Staleness Warning):** Hệ thống tự động đánh dấu tài liệu chưa được cập nhật sau 6 tháng với nhãn "⚠️ Tài liệu có thể lỗi thời — Cần xác nhận phiên bản mới nhất". | Kỹ thuật | 🟠 Khuyến nghị trước mở rộng |
| G3.3 | **Quy trình cập nhật KB định kỳ (KB Update SOP):** Xây dựng quy trình vận hành chuẩn (SOP) yêu cầu người quản lý KB rà soát và cập nhật tài liệu tối thiểu **mỗi quý một lần** hoặc khi nhà cung cấp phát hành phiên bản mới. | Quy trình | ✅ Bắt buộc triển khai |
| G3.4 | **Đường dẫn báo cáo "Tài liệu lỗi thời" cho người dùng:** Trong giao diện chat, người dùng có nút "🚩 Báo cáo thông tin có thể lỗi thời" để gửi phản hồi cho người quản lý KB. | Kỹ thuật (UI/UX) | 🔜 Sau MVP |

**Checkpoint HITL:**
> Người quản lý Knowledge Base **nhận báo cáo định kỳ mỗi tháng** về danh sách tài liệu cần rà soát cập nhật. Quyết định cập nhật hoặc loại bỏ tài liệu khỏi KB phải do **con người thực hiện**, không tự động hóa.

---

### 🔴 RISK-04: Câu Hỏi Người Dùng Chứa Thông Tin Nhạy Cảm Bị Ghi vào Log

**Mô tả rủi ro:**
Kỹ sư có thể vô tình đưa thông tin nhạy cảm vào câu hỏi chat (ví dụ: địa chỉ IP thiết bị thực tế, cấu hình đang áp dụng, tên thiết bị sản xuất). Nếu hệ thống ghi toàn bộ lịch sử chat vào log, thông tin này có thể bị thu thập trái phép.

**Kịch bản xảy ra (mô phỏng):**
> Kỹ sư gõ: "Thiết bị tại địa điểm [X] đang dùng IP 10.x.x.x, tôi muốn tra cứu cấu hình tương thích". Hệ thống ghi toàn bộ câu hỏi vào log. Log bị truy cập trái phép.

**Mức độ tác động:** Cao — Có thể tiết lộ thông tin cấu hình hạ tầng mạng thực tế, vi phạm quy chế bảo mật thông tin của VTN.

**Rào cản an toàn (Guardrails):**

| # | Guardrail | Loại | Trạng thái MVP |
|---|---|---|---|
| G4.1 | **Logging phi nhạy cảm (Sanitized Logging):** Hệ thống CHỈ ghi log: `session_id`, `timestamp`, `loại câu hỏi (category)`, `thời gian xử lý`, `mức tin cậy`, `có cần HITL không`. Tuyệt đối KHÔNG ghi nội dung câu hỏi đầy đủ hay câu trả lời vào log. | Kỹ thuật | ✅ Bắt buộc triển khai |
| G4.2 | **Thông báo hướng dẫn người dùng:** Hiển thị banner cảnh báo rõ ràng trong giao diện: "⚠️ Vui lòng KHÔNG nhập thông tin cấu hình mạng thực tế, địa chỉ IP, tên thiết bị sản xuất vào ô chat. Công cụ này CHỈ phục vụ tra cứu tài liệu." | UX / Quy trình | ✅ Bắt buộc triển khai |
| G4.3 | **Bộ lọc phát hiện thông tin nhạy cảm trong câu hỏi (PII/Sensitive Data Detector):** Hệ thống tự động quét câu hỏi đầu vào bằng Regex để phát hiện địa chỉ IP (pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`), số serial thiết bị và các mẫu nhạy cảm khác. Nếu phát hiện → hiển thị cảnh báo và yêu cầu người dùng xóa thông tin trước khi gửi. | Kỹ thuật (Input Validation) | 🟠 Khuyến nghị triển khai sớm |
| G4.4 | **Quy trình xóa lịch sử chat định kỳ:** Lịch sử phiên chat (nếu có lưu trữ tạm) phải được xóa tự động sau **24 giờ**. Không lưu trữ lịch sử chat lâu dài trong MVP. | Kỹ thuật + Quy trình | ✅ Bắt buộc triển khai |

**Checkpoint HITL:**
> Định kỳ **mỗi tháng**, người quản trị hệ thống rà soát file log để đảm bảo không có thông tin nhạy cảm bị ghi lọt. Kết quả rà soát được ghi thành biên bản kiểm tra tuân thủ (compliance audit record).

---

## 4. Ma Trận Rủi Ro Tổng Hợp

```
              Mức độ tác động
              THẤP    TRUNG BÌNH    CAO    RẤT CAO
Xác suất  ┌─────────┬─────────────┬──────┬─────────────┐
RẤT CAO   │         │             │      │             │
CAO       │         │  RISK-03    │      │             │
TRUNG BÌNH│         │             │RISK-04│  RISK-01   │
THẤP      │         │             │      │             │
          └─────────┴─────────────┴──────┴─────────────┘

RISK-02 (Hallucination): Tác động CAO × Xác suất CAO → 🔴 Ưu tiên cao nhất
```

| Mã rủi ro | Tổng mức ưu tiên | Hành động tiếp theo |
|---|---|---|
| RISK-02 | 🔴 KHẨN CẤP | Triển khai G2.1–G2.4 trước khi ra mắt MVP |
| RISK-01 | 🔴 KHẨN CẤP | Thiết lập quy trình phân loại tài liệu trước khi đưa vào KB |
| RISK-04 | 🔴 CAO | Triển khai sanitized logging và banner cảnh báo ngay từ MVP |
| RISK-03 | 🟠 TRUNG BÌNH | Xây dựng SOP cập nhật KB trước khi mở rộng quy mô |

---

## 5. Danh Sách Kiểm Tra Nhanh (Quick Checklist) — Trước Khi Thí Điểm

```
KIỂM TRA BẢO MẬT KNOWLEDGE BASE
[ ] Tất cả tài liệu trong KB đã được phân loại bảo mật
[ ] Không có tài liệu "Mật" hoặc "Tối mật" trong KB MVP
[ ] Có danh sách kiểm duyệt tài liệu được ký bởi người có thẩm quyền
[ ] Cơ chế kiểm duyệt KB định kỳ đã được thiết lập

KIỂM TRA CHỐNG HALLUCINATION
[ ] Mọi câu trả lời đều có trích dẫn nguồn tài liệu
[ ] Ngưỡng confidence threshold đã được cài đặt
[ ] Cảnh báo HITL hiển thị với câu trả lời về cấu hình tham số
[ ] Nhãn "AI-Generated — Cần xác minh" xuất hiện trên mọi đầu ra

KIỂM TRA LOGGING AN TOÀN
[ ] File log không chứa nội dung câu hỏi/trả lời đầy đủ
[ ] Banner cảnh báo "Không nhập thông tin thật" đã hiển thị
[ ] Cơ chế xóa lịch sử chat tự động sau 24h đã hoạt động
[ ] Kiểm duyệt log định kỳ đã được lên lịch

KIỂM TRA VÒNG LẶP HITL
[ ] Người/nhóm chịu trách nhiệm HITL đã được chỉ định cụ thể
[ ] Quy trình leo thang (escalation) đã được tài liệu hóa
[ ] Cơ chế phản hồi định kỳ về chất lượng AI đã thiết kế
[ ] Chưa có chức năng nào cho phép AI tự thực thi cấu hình
```

---

## 6. Tuyên Bố Trách Nhiệm

> Tài liệu này được soạn thảo cho mục đích **thực hành Capstone** trong chương trình đào tạo AI Thực chiến tại VTN. Tất cả kịch bản, tên thiết bị, tham số, địa chỉ IP và thông tin kỹ thuật trong tài liệu đều là **MÔ PHỎNG HOÀN TOÀN**. Không phản ánh cấu hình thực tế hay thông tin bảo mật thật của hệ thống mạng Viettel.

---

*Phiên bản: v1.0 — Draft | Ngày: 10/06/2026 | Phục vụ thực hành Capstone Session-06*
