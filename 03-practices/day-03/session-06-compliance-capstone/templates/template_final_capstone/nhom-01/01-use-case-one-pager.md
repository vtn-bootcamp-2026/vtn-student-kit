---
mo-ta: "AI Scoring Assistant — Chấm điểm tự động theo tiêu chí cho trước: Đề xuất dự án một trang mô tả vấn đề, giải pháp, hiệu quả và kiến trúc kỹ thuật tổng quan"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 09:00 +07:00
updated-at: 2026-06-10 09:00 +07:00
---

# Đề xuất dự án một trang (Use case one pager)

*   **Tên dự án ứng dụng:** AI Scoring Assistant — Trợ lý AI chấm điểm tự động theo tiêu chí cho trước
*   **Đơn vị đề xuất:** Trung tâm Đào tạo & Phát triển Năng lực số — Viettel Net
*   **Người đầu mối liên hệ:** Nhóm 1
*   **Mức độ ưu tiên:** Cao
*   **Mốc thời gian dự kiến thí điểm:** Tháng 7/2026

---

## 1. Vấn đề và Nhu cầu thực tế (Problem statement)
*Mô tả ngắn gọn nỗi đau (pain point) hiện tại tại đơn vị mà giải pháp này sẽ giải quyết.*

*   **Hiện trạng:** Hàng kỳ, đội ngũ giảng viên / chuyên gia đánh giá tại VTN phải chấm điểm thủ công hàng chục đến hàng trăm bài nộp (báo cáo capstone, hồ sơ năng lực kỹ sư, đề xuất dự án, biên bản nghiệm thu kỹ thuật) theo bộ tiêu chí chấm đã được định nghĩa sẵn. Mỗi bài chấm mất trung bình **20–45 phút**, mỗi đợt có 50–200 bài cần xử lý trong 3–5 ngày làm việc.
*   **Rủi ro:** Chấm thủ công dễ bị sai lệch cảm tính (halo effect), thiếu nhất quán giữa các giám khảo, và không có nhật ký giải thích điểm số minh bạch. Khi nhân sự chấm bài phải dùng công cụ AI đám mây công cộng (ChatGPT, Gemini) để hỗ trợ xử lý, toàn bộ nội dung bài nộp — có thể chứa thông tin nhân sự nội bộ, dữ liệu kỹ thuật mạng viễn thông — bị gửi ra ngoài, vi phạm Quy chế bảo mật thông tin của Viettel Net và Nghị định 356/2025/NĐ-CP về Bảo vệ dữ liệu cá nhân.

---

## 2. Giải pháp đề xuất (Proposed solution)
*Mô tả cách thức ứng dụng AI/Local LLM giải quyết vấn đề trên.*

*   **Giải pháp:** Xây dựng **AI Scoring Assistant** — công cụ chạy hoàn toàn cục bộ (offline) trên hạ tầng private của VTN — tự động đọc bài nộp dạng văn bản, đối chiếu với bộ tiêu chí chấm điểm (rubric) có cấu trúc và trả về điểm số + nhận xét theo từng tiêu chí.
*   **Cơ chế hoạt động:**
    *   Người chấm nạp file bài nộp (`.txt`, `.md`, `.docx`) và file rubric tiêu chí chấm (JSON/YAML) vào hệ thống.
    *   Mô hình ngôn ngữ lớn cục bộ (**gemma4:e2b** hoặc **qwen3.5:1.5b-instruct** qua Ollama) đọc từng tiêu chí, đối chiếu bằng chứng trong bài và gán điểm theo thang đã định nghĩa.
    *   Hệ thống trả về **Score Report JSON** gồm: điểm từng tiêu chí, điểm tổng, nhận xét giải thích, danh sách bằng chứng trích dẫn.
    *   **Human-in-the-loop:** Giám khảo xem lại điểm đề xuất, điều chỉnh nếu cần, xác nhận trước khi ghi vào sổ điểm chính thức.

---

## 3. Hiệu quả mang lại (Business value & Impact)
*Định lượng hiệu quả (thời gian, chi phí, mức độ an toàn) của dự án.*

*   **Tiết kiệm thời gian:** Giảm thời gian chấm từ **20–45 phút/bài** xuống còn **2–3 phút/bài** cho khâu xem xét và phê duyệt cuối của giám khảo (năng suất tăng ~10–15 lần). Một đợt 100 bài tiết kiệm **~30–40 giờ lao động** chuyên gia.
*   **Tăng nhất quán & minh bạch:** Điểm số được giải thích theo từng tiêu chí kèm bằng chứng trích dẫn từ bài nộp, loại bỏ hoàn toàn cảm tính chủ quan giữa các giám khảo khác nhau.
*   **Đảm bảo tuân thủ bảo mật:** Toàn bộ nội dung bài nộp được xử lý offline trên hạ tầng nội bộ, không rời khỏi mạng VTN, đáp ứng tuyệt đối Quy chế bảo mật thông tin.
*   **Chi phí đầu tư:** Sử dụng mô hình mã nguồn mở chạy local qua Ollama, chi phí bản quyền phần mềm và API = **0 VNĐ**.

---

## 4. Kiến trúc kỹ thuật và Phương án triển khai (Technical architecture)

*   **Tầng Client (Giao diện):** CLI Python tương tác, hỗ trợ nạp file bài nộp và file rubric, hiển thị kết quả điểm số có màu sắc phân loại (Đạt / Không đạt / Cần xem lại).
*   **Tầng Core (Logic):** Python 3.10+; đọc rubric từ file JSON/YAML; xây dựng prompt động theo từng tiêu chí; gọi Ollama local API; parse và validate kết quả JSON trả về bằng Pydantic.
*   **Tầng Model (AI):** Ollama Server chạy cục bộ, mô hình lượng tử hóa `gemma4:e2b` hoặc `qwen3.5:1.5b-instruct` (RAM tiêu thụ: 1.5–3 GB).
*   **Tầng Output:** Xuất Score Report dạng JSON + bản tóm tắt Markdown; ghi nhật ký vận hành phi nhạy cảm ra `scoring-log.csv`.
*   **Đóng gói:** File `.bat` / `.sh` một chạm, không yêu cầu kiến thức kỹ thuật từ người dùng cuối.

---

## 5. Rủi ro và Biện pháp phòng ngừa (Risks & Defenses)

*   **Rủi ro 1: Mô hình gán điểm thiếu chính xác với tiêu chí mơ hồ hoặc chủ quan.**
    *   *Phòng ngừa:* Yêu cầu mỗi tiêu chí trong rubric kèm theo ví dụ mẫu "đạt" và "không đạt" cụ thể (few-shot examples). Bật cờ `needs_human_review = true` khi độ tin cậy thấp.
*   **Rủi ro 2: Mô hình bị Prompt Injection qua nội dung bài nộp (bài viết cố ý nhúng lệnh thao túng AI).**
    *   *Phòng ngừa:* Đóng khung toàn bộ nội dung bài nộp trong thẻ XML `<submission>...</submission>`, áp dụng Output Schema Enforcement (Pydantic) — mọi lệnh độc hại chỉ trả về dưới dạng chuỗi trong JSON, không thực thi được.
*   **Rủi ro 3: Mất kết nối Ollama hoặc RAM không đủ trên máy trạm yếu.**
    *   *Phòng ngừa:* Fallback mode an toàn — KHÔNG tự động gán điểm bằng heuristic (vì chấm điểm là tác vụ định tính, gán máy móc dễ sai), mà đặt `score = null` + cờ `needs_human_review` cho các tiêu chí bị ảnh hưởng và chuyển sang chấm thủ công, đảm bảo không phát sinh điểm sai.

---

## 6. Đề xuất kế hoạch hành động tiếp theo (Next steps)

1.  **Tuần 1:** Hoàn thiện bộ rubric JSON mẫu cho Capstone Bootcamp và thử nghiệm với 10 bài nộp thật.
2.  **Tuần 2:** Thu thập phản hồi từ 3 giám khảo nội bộ, tinh chỉnh System Prompt và ví dụ few-shot.
3.  **Tuần 3:** Đóng gói bản hoàn thiện, bàn giao kỹ thuật cho bộ phận Đào tạo VTN.
4.  **Tuần 4:** Nghiệm thu và đề xuất mở rộng sang chấm điểm hồ sơ năng lực kỹ sư tại các trung tâm kỹ thuật.
