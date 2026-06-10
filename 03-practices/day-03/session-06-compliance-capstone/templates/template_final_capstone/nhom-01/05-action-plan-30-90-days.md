---
mo-ta: "AI Scoring Assistant — Chấm điểm tự động theo tiêu chí cho trước: Lộ trình 30/90 ngày triển khai thí điểm, chuẩn hóa quy trình và 03 use case mở rộng"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 09:00 +07:00
updated-at: 2026-06-10 09:00 +07:00
---

# Kế hoạch hành động 30/90 ngày áp dụng AI tại đơn vị (Action Plan)

*   **Tên nhóm thực hiện:** Nhóm 1
*   **Đơn vị áp dụng:** Trung tâm Đào tạo & Phát triển Năng lực số — Viettel Net
*   **Người chịu trách nhiệm chính:** Học viên Capstone (Nhóm trưởng)
*   **Phiên bản tài liệu:** v1.0

---

## 1. Mục tiêu kế hoạch hành động

Bản kế hoạch này thiết lập lộ trình cụ thể để đưa **AI Scoring Assistant** từ sản phẩm capstone vào vận hành thực tế tại Trung tâm Đào tạo VTN trong hai giai đoạn:

*   **30 ngày đầu (07/07 – 05/08/2026):** Thử nghiệm thực tế với đợt chấm điểm Bootcamp lần 2, thu thập phản hồi giám khảo, tinh chỉnh rubric và prompt.
*   **90 ngày tiếp theo (06/08 – 03/11/2026):** Chuẩn hóa thành quy trình chấm điểm chính thức, mở rộng sang các loại bài đánh giá khác tại VTN.

---

## 2. Lộ trình hành động chi tiết (Milestone Roadmaps)

### Giai đoạn 30 ngày đầu: Thử nghiệm và Tích hợp nhanh (07/07 – 05/08/2026)
*Mục tiêu: Chấm thử thực tế 30–50 bài capstone, kiểm chứng độ chính xác, thu thập phản hồi giám khảo.*

*   - [ ] **Mốc 1 (07/07 – 16/07 — Ngày 1–10): Hoàn thiện cài đặt hạ tầng và rubric chuẩn**
    *   *Nội dung:*
        *   Cài đặt Python 3.10+, Ollama và tải mô hình `gemma4:e2b` tại 2 máy trạm của giám khảo nội bộ.
        *   Hoàn thiện file `rubric-capstone-2026.json` với đủ 5 tiêu chí, ví dụ few-shot cho từng tiêu chí.
        *   Viết `README.md` hướng dẫn cài đặt và sử dụng dành cho người không có nền kỹ thuật.
    *   *Người chịu trách nhiệm:* Học viên Capstone (kỹ thuật) + Chuyên gia đào tạo (nội dung rubric)
    *   *Tiêu chí hoàn thành:* Chạy thử thành công 3 bài mẫu trên cả 2 máy trạm.

*   - [ ] **Mốc 2 (17/07 – 26/07 — Ngày 11–20): Chấm song song (Parallel Testing)**
    *   *Nội dung:*
        *   Chọn 30 bài capstone nộp gần nhất, chấm đồng thời: AI Scoring Assistant vs. giám khảo thủ công độc lập.
        *   Ghi nhận: thời gian chấm, điểm AI vs. điểm giám khảo, tỷ lệ tiêu chí AI gán đúng.
        *   Xác định các tiêu chí mà AI chấm lệch > 2 điểm để ưu tiên cải thiện few-shot.
    *   *Người chịu trách nhiệm:* 2 giám khảo nội bộ
    *   *Tiêu chí hoàn thành:* Tỷ lệ độ lệch điểm trung bình AI vs. người < 10% tổng điểm.

*   - [ ] **Mốc 3 (27/07 – 05/08 — Ngày 21–30): Đánh giá vòng 1 và Hoàn thiện tài liệu**
    *   *Nội dung:*
        *   Phân tích dữ liệu từ Mốc 2, tổng kết loại lỗi phổ biến nhất của AI.
        *   Cập nhật few-shot examples trong rubric cho các tiêu chí chấm lệch nhiều.
        *   Hoàn thiện tài liệu vận hành: hướng dẫn nạp file, giải thích kết quả, xử lý lỗi thường gặp.
    *   *Người chịu trách nhiệm:* Học viên Capstone
    *   *Tiêu chí hoàn thành:* Score report được 3 giám khảo nhận xét là "đủ tin tưởng để làm cơ sở duyệt".

---

### Giai đoạn 90 ngày tiếp theo: Chuẩn hóa và Mở rộng (06/08 – 03/11/2026)
*Mục tiêu: Tích hợp vào quy trình chính thức, đào tạo nhân sự mới, mở rộng sang loại bài đánh giá khác.*

*   - [ ] **Mốc 4 (06/08 – 04/09 — Ngày 31–60): Đóng gói và Tích hợp quy trình chính thức**
    *   *Nội dung:*
        *   Đóng gói thành file `.bat` (Windows) / `.sh` (Mac/Linux) một chạm cho giám khảo không có nền kỹ thuật.
        *   Tích hợp vào quy trình chấm điểm chính thức của Trung tâm Đào tạo: mỗi đợt capstone dùng AI để pre-score, giám khảo chỉ cần review và approve.
        *   Tổ chức buổi training nội bộ 2 giờ hướng dẫn 5–10 giám khảo cách sử dụng.
    *   *Người chịu trách nhiệm:* Học viên Capstone + IT Hỗ trợ VTN
    *   *Tiêu chí hoàn thành:* 5 giám khảo sử dụng độc lập không cần hỗ trợ kỹ thuật.

*   - [ ] **Mốc 5 (05/09 – 19/09 — Ngày 61–75): Xây dựng quy chế vận hành và bảo mật**
    *   *Nội dung:*
        *   Soạn thảo và ban hành **Quy chế sử dụng công cụ AI chấm điểm nội bộ** (1–2 trang): phạm vi sử dụng, giới hạn, trách nhiệm của giám khảo, quy trình kháng điểm khi học viên không đồng ý.
        *   Ghi rõ trong quy chế: AI chỉ đề xuất, giám khảo là người quyết định cuối cùng.
        *   Đăng ký với bộ phận CNTT VTN để công cụ được liệt vào danh mục phần mềm nội bộ được chấp thuận.
    *   *Người chịu trách nhiệm:* Trưởng Trung tâm Đào tạo + Phòng Pháp chế VTN
    *   *Tiêu chí hoàn thành:* Quy chế được ký ban hành và gửi đến toàn bộ giám khảo.

*   - [ ] **Mốc 6 (20/09 – 03/11 — Ngày 76–90): Nghiệm thu, đánh giá hiệu quả và đề xuất mở rộng**
    *   *Nội dung:*
        *   Lập báo cáo định lượng kết quả sau 3 tháng: tổng số bài đã chấm, giờ lao động tiết kiệm được, tỷ lệ giám khảo điều chỉnh điểm AI, số lần phát hiện `INJECTION_ATTEMPT`.
        *   Trình báo cáo lên Ban Giám đốc Trung tâm Đào tạo để đề xuất nhân rộng.
        *   Đề xuất 3 use case tiếp theo (xem Mục 3).
    *   *Người chịu trách nhiệm:* Nhóm Capstone + Lãnh đạo Trung tâm Đào tạo
    *   *Tiêu chí hoàn thành:* Báo cáo được trình bày và nhận phản hồi từ Ban Giám đốc.

---

## 3. Danh mục đề xuất 03 trường hợp ứng dụng tiếp theo (Next Use Cases)

### Use case 1: Chấm điểm hồ sơ đề xuất dự án nội bộ (Project Proposal Scoring)
*   **Mục tiêu:** Tự động đánh giá các đề xuất dự án CNTT/số hóa theo bộ tiêu chí tính khả thi, ROI, mức độ ưu tiên chiến lược của VTN.
*   **Dữ liệu sử dụng:** Template đề xuất dự án chuẩn của VTN + Rubric đánh giá dự án (do Ban Chiến lược định nghĩa).
*   **Hiệu quả mong đợi:** Giảm thời gian sàng lọc hồ sơ ban đầu từ 2–3 ngày/đợt xuống còn nửa ngày, giúp Hội đồng tập trung vào phỏng vấn thay vì đọc hồ sơ thô.

### Use case 2: Đánh giá báo cáo vận hành kỹ thuật định kỳ (O&M Report Quality Scoring)
*   **Mục tiêu:** Tự động kiểm tra chất lượng các báo cáo vận hành hàng tuần/tháng của các trung tâm kỹ thuật theo checklist chuẩn (đủ mục, có số liệu, có phân tích nguyên nhân).
*   **Dữ liệu sử dụng:** Báo cáo vận hành dạng text + Checklist tiêu chuẩn chất lượng báo cáo nội bộ VTN.
*   **Hiệu quả mong đợi:** Giảm thời gian kiểm tra chất lượng báo cáo đầu vào từ 30 phút/báo cáo xuống 3 phút; tự động trả về nhận xét cụ thể cho tác giả báo cáo trong vòng 1 phút.

### Use case 3: Chấm điểm phỏng vấn kỹ thuật bằng transcript (Interview Transcript Scoring)
*   **Mục tiêu:** Sau buổi phỏng vấn kỹ thuật tuyển dụng, AI đọc transcript (bản ghi lời) và chấm điểm ứng viên theo rubric kỹ năng kỹ thuật đã định nghĩa sẵn, hỗ trợ panel phỏng vấn ra quyết định nhanh hơn.
*   **Dữ liệu sử dụng:** Transcript phỏng vấn dạng text (đã ẩn danh tên ứng viên trước khi nạp) + Rubric kỹ năng kỹ thuật (do bộ phận Tuyển dụng VTN xây dựng).
*   **Hiệu quả mong đợi:** Giảm thời gian họp thống nhất điểm phỏng vấn từ 45 phút/ứng viên xuống 10 phút; cung cấp bằng chứng trích dẫn cụ thể cho mọi quyết định tuyển/không tuyển.
