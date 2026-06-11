---
mo-ta: "Phiếu mô tả trường hợp sử dụng AI Agent tra cứu tài liệu thiết bị, tính năng, tham số và quy hoạch mạng lưới Viettel"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Tài liệu sử dụng dữ liệu mô phỏng. Tuyệt đối không chứa thông tin thật, PII hay dữ liệu nhạy cảm của VTN."
---

# Đề xuất dự án một trang (Use case one pager)

*   **Tên dự án ứng dụng:** AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel (Network Doc Assistant)
*   **Đơn vị đề xuất:** [Tên phòng/ban kỹ thuật — ẩn danh mô phỏng]
*   **Người đầu mối liên hệ:** [Kỹ sư phụ trách — tên mô phỏng]
*   **Mức độ ưu tiên:** Cao
*   **Mốc thời gian dự kiến thí điểm:** Quý 3 / 2026

---

## 1. Vấn đề và Nhu cầu thực tế (Problem statement)
*Mô tả ngắn gọn nỗi đau (pain point) hiện tại tại đơn vị mà giải pháp này sẽ giải quyết.*

*   **Hiện trạng:** Các kỹ sư vận hành mạng (NOC/BSS) và kỹ sư quy hoạch thường xuyên phải tra cứu tài liệu kỹ thuật phân tán: thông số thiết bị, hướng dẫn cấu hình, bảng tham số, quy hoạch vùng phủ — lưu trữ rải rác trên hàng trăm file PDF/Word/Excel nội bộ. Mỗi lần tra cứu có thể mất **10–20 phút** tìm kiếm thủ công.
*   **Rủi ro:** Kỹ sư dễ tra cứu sai phiên bản tài liệu, áp dụng tham số cũ gây lỗi cấu hình thiết bị hoặc quy hoạch không tối ưu. Nếu gửi tài liệu kỹ thuật nội bộ lên các công cụ AI đám mây công cộng (như ChatGPT) để tra cứu sẽ vi phạm quy chế bảo mật thông tin nội bộ của Viettel Net.

---

## 2. Giải pháp đề xuất (Proposed solution)
*Mô tả cách thức ứng dụng AI/Local LLM giải quyết vấn đề trên.*

*   **Giải pháp:** Phát triển và triển khai **AI Agent Tra Cứu Tài Liệu** (Network Doc Assistant) chạy hoàn toàn cục bộ (offline/intranet) trên hạ tầng private của VTN.
*   **Cơ chế hoạt động:**
    *   Người dùng đặt câu hỏi bằng tiếng Việt tự nhiên qua giao diện chat web nội bộ.
    *   Hệ thống tìm kiếm ngữ nghĩa (Vector Search - RAG) trong kho tài liệu kỹ thuật đã được kiểm duyệt và vector hóa.
    *   Mô hình ngôn ngữ lớn **cục bộ** (chạy qua Ollama — không kết nối Internet) tổng hợp câu trả lời có trích dẫn nguồn tài liệu rõ ràng.
    *   Cơ chế cảnh báo tin cậy thấp (confidence threshold) và vòng lặp kiểm duyệt của con người (HITL) trước khi áp dụng bất kỳ gợi ý cấu hình nào.
    *   Định kỳ, các **kỹ sư chuyên môn cao** rà soát, xác nhận và cập nhật tài liệu trong Knowledge Base.

---

## 3. Hiệu quả mang lại (Business value & Impact)
*Định lượng hiệu quả (thời gian, chi phí, mức độ an toàn) của dự án.*

*   **Tiết kiệm thời gian:** Giảm thời gian tra cứu từ **~15 phút/lần** xuống còn dưới **2 phút/lần** (Năng suất tăng 7 lần) cho đối tượng kỹ sư vận hành và quy hoạch mạng.
*   **Đảm bảo tuân thủ bảo mật:** Triển khai offline 100% trên hạ tầng nội bộ VTN, tuyệt đối không truyền tài liệu kỹ thuật ra các API đám mây công cộng.
*   **Tăng độ chính xác tra cứu:** Câu trả lời luôn kèm trích dẫn tên tài liệu, số trang, phiên bản — giảm nguy cơ áp dụng thông số lỗi thời hoặc sai tài liệu.
*   **Tối ưu chi phí:** Sử dụng mô hình cục bộ mã nguồn mở, chạy trên hạ tầng có sẵn của VTN — chi phí bản quyền API bên ngoài bằng **0 VNĐ**.

---

## 4. Kiến trúc kỹ thuật và Phương án triển khai (Technical architecture)

*   **Tầng Client (Giao diện):** Giao diện chat web (HTML/JS) chạy trên intranet VTN — kỹ sư truy cập qua trình duyệt nội bộ.
*   **Tầng AI Agent (RAG Pipeline):** Nhận câu hỏi → Tìm kiếm ngữ nghĩa trong VectorDB cục bộ → Local LLM tổng hợp câu trả lời có trích dẫn nguồn.
*   **Tầng Knowledge Base:** Tài liệu kỹ thuật đã được phân loại bảo mật, kiểm duyệt bởi kỹ sư chuyên môn cao và vector hóa vào cơ sở dữ liệu vector nội bộ.
*   **Tầng Mô hình (AI):** Mô hình ngôn ngữ lớn cục bộ chạy qua **Ollama** (không kết nối Internet), sử dụng phần cứng có sẵn của VTN.
*   **Tầng Kiểm duyệt (HITL):** Cảnh báo độ tin cậy thấp → Kỹ sư chuyên môn cao phê duyệt trước khi áp dụng bất kỳ gợi ý cấu hình nào.

---

## 5. Rủi ro và Biện pháp phòng ngừa (Risks & Defenses)

*   **Rủi ro 1: AI trả lời sai lệch thông tin kỹ thuật (Hallucination).**
    *   *Phòng ngừa:* Bắt buộc hiển thị trích dẫn nguồn tài liệu kèm mọi câu trả lời; ngưỡng tin cậy (confidence threshold) < 70% hiển thị cảnh báo; HITL bắt buộc cho mọi gợi ý cấu hình tham số.
*   **Rủi ro 2: Tài liệu trong Knowledge Base lỗi thời.**
    *   *Phòng ngừa:* Kỹ sư chuyên môn cao rà soát và cập nhật tài liệu định kỳ (ít nhất hàng quý); metadata phiên bản hiển thị rõ trên mỗi trích dẫn; cảnh báo tài liệu cũ (staleness warning) sau 6 tháng không cập nhật.
*   **Rủi ro 3: Tài liệu kỹ thuật mật bị đưa vào Knowledge Base.**
    *   *Phòng ngừa:* Mọi tài liệu đưa vào KB phải qua phân loại bảo mật và phê duyệt bởi người có thẩm quyền; chỉ tài liệu nhãn "Công khai nội bộ" được đưa vào MVP.

---

## 6. Đề xuất kế hoạch hành động tiếp theo (Next steps)

1.  **Tuần 1–2:** Phân loại, kiểm duyệt và vector hóa bộ tài liệu kỹ thuật mô phỏng (không dùng tài liệu thật trong thí điểm nội bộ).
2.  **Tuần 3–4:** Phát triển pipeline RAG + giao diện chat web + cơ chế HITL và cảnh báo tin cậy.
3.  **Tuần 5–6:** Thí điểm với nhóm **05 kỹ sư nòng cốt**, thu thập phản hồi thực tế.
4.  **Tuần 7–8:** Đánh giá kết quả, tinh chỉnh, hoàn thiện quy trình kiểm duyệt KB định kỳ, trình phê duyệt ban lãnh đạo để mở rộng quy mô.

---

*Tài liệu này được tạo cho mục đích thực hành Capstone. Mọi tên thiết bị, tham số, câu hỏi mẫu đều là MÔ PHỎNG.*
