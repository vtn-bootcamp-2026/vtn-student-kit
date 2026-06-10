---
mo-ta: "Biểu mẫu đề xuất dự án một trang Use Case One Pager phục vụ báo cáo Capstone tại VTN"
trang-thai: active
phien-ban: v1.2
created-at: 2026-06-10 15:45 +07:00
updated-at: 2026-06-10 15:45 +07:00
---

# Đề xuất dự án một trang (Use case one pager)

*   **Tên dự án ứng dụng:** Hệ thống Tự động hóa Báo cáo & Phân tích Anomaly KPI NetBI (NetBI-KARA)
*   **Đơn vị đề xuất:** Phòng Vận hành Khai thác - Trung tâm Điều hành Mạng (NOC)
*   **Người đầu mối liên hệ:** Nguyễn Minh Huy
*   **Mức độ ưu tiên:** Cao
*   **Mốc thời gian dự kiến thí điểm:** Tháng 07/2026

---

## 1. Vấn đề và Nhu cầu thực tế (Problem statement)
*Mô tả ngắn gọn nỗi đau (pain point) hiện tại tại đơn vị mà giải pháp này sẽ giải quyết.*

*   **Hiện trạng:** Hàng tuần, 5 kỹ sư trực ca NOC phải đăng nhập thủ công vào hệ thống NetBI để kết xuất hơn 200 chỉ số KPI mạng lưới thuộc 6 mảng dịch vụ (Di động, cố định băng rộng, gián đoạn thông tin, CNTT, truyền tải, cơ điện). Sau đó, họ phải tính toán, phân tích và viết báo cáo đánh giá tổng hợp kèm số liệu chi tiết.
*   **Nỗi đau & Rủi ro:** 
    *   Quy trình xử lý dữ liệu và viết báo cáo thủ công tốn trung bình 24-30 giờ công mỗi tuần của 5 kỹ sư chất lượng cao.
    *   Thời gian hoàn thành báo cáo bị trễ từ 3-5 ngày so với thời điểm có số liệu, dẫn đến việc chậm trễ phát hiện sự cố chất lượng và chậm yêu cầu nhân sự chịu trách nhiệm (KPI owner) xử lý.
    *   Việc tải dữ liệu lớn lên các nền tảng AI công cộng để tóm tắt phân tích có nguy cơ rò rỉ thông tin mật về kiến trúc mạng của Viettel Net.

---

## 2. Giải pháp đề xuất (Proposed solution)
*Mô tả cách thức ứng dụng AI/Local LLM giải quyết vấn đề trên.*

*   **Giải pháp:** Phát triển công cụ tự động hóa **NetBI-KARA** chạy hoàn toàn cục bộ (offline) trên hạ tầng private cloud của Viettel Net.
*   **Cơ chế hoạt động:** 
    *   Tự động nạp file dữ liệu raw KPI (.csv/.xlsx) được tải về từ NetBI.
    *   Sử dụng mã Python phân tích nhanh để phát hiện các chỉ số vượt ngưỡng target hoặc có xu hướng suy giảm bất thường so với lịch sử 4 tuần gần nhất.
    *   Sử dụng mô hình ngôn ngữ lớn cục bộ (Local LLM **qwen3.5:7b-instruct** hoặc **gemma4:e4b** qua Ollama) để đọc bảng số liệu KPI vi phạm, tự động viết phần Nhận định chất lượng mạng bằng tiếng Việt mạch lạc, xác định chính xác các KPI suy giảm.
    *   Tự động soạn thảo sẵn email/tin nhắn cảnh báo gửi đích danh cho từng KPI owner (ví dụ: Kỹ sư phụ trách trạm Di động miền Bắc, phụ trách Truyền tải miền Trung) yêu cầu tìm nguyên nhân và đưa giải pháp khắc phục.
    *   Cung cấp giao diện Web UI cục bộ hiển thị báo cáo nháp và các dự thảo email để kỹ sư NOC kiểm duyệt và nhấn gửi (Human-in-the-loop).

---

## 3. Hiệu quả mang lại (Business value & Impact)
*Định lượng hiệu quả (thời gian, chi phí, mức độ an toàn) của dự án.*

*   **Tiết kiệm thời gian:** Giảm thời gian tổng hợp và viết báo cáo phân tích tuần từ **3-5 ngày** xuống còn **dưới 30 phút** (Năng suất phân tích tăng hơn 50 lần).
*   **Tối ưu hóa vận hành:** Phát hiện lỗi chất lượng và gửi yêu cầu khắc phục cho KPI owner ngay trong ngày, rút ngắn thời gian xử lý sự cố mạng lưới từ 3 ngày xuống dưới 12 giờ.
*   **Đảm bảo tuân thủ bảo mật:** Triển khai offline 100% trên server nội bộ của Viettel Net, không đưa số liệu mạng lưới ra Internet, đảm bảo an toàn tuyệt đối thông tin an ninh quốc gia.
*   **Chi phí:** Tận dụng hạ tầng máy chủ GPU có sẵn của NOC và các mô hình mã nguồn mở, chi phí đầu tư bằng 0 VNĐ.

---

## 4. Kiến trúc kỹ thuật và Phương án triển khai (Technical architecture)

*   **Tầng Giao diện (Client/UI):** Giao diện Web HTML/JS đơn giản chạy cục bộ giúp kỹ sư NOC tải file dữ liệu, duyệt báo cáo dự thảo và chỉnh sửa email cảnh báo.
*   **Tầng Logic (Core Engine):** Python 3.11+, Pandas xử lý dữ liệu lớn, tính toán xu hướng thống kê.
*   **Tầng Trí tuệ nhân tạo (Model):** Ollama chạy trên server GPU nội bộ, chạy mô hình `qwen3.5:7b-instruct` để phân tích chuyên sâu và soạn thảo báo cáo, email cảnh báo.
*   **Phương án tích hợp:** Chạy dưới dạng dịch vụ web nội bộ của NOC, phân quyền truy cập thông qua tài khoản AD (Active Directory) nội bộ.

---

## 5. Rủi ro và Biện pháp phòng ngừa (Risks & Defenses)

*   **Rủi ro 1: LLM diễn dịch sai xu hướng KPI hoặc sinh dữ liệu ảo (hallucination).**
    *   *Phòng ngừa:* Sử dụng Pandas để tính toán chính xác số liệu định lượng trước, sau đó đưa dữ liệu cấu trúc dạng bảng XML vào prompt để LLM chỉ có nhiệm vụ diễn giải ngôn ngữ tự nhiên từ số liệu thực tế đó.
*   **Rủi ro 2: Gửi nhầm email cảnh báo tự động khi số liệu lỗi.**
    *   *Phòng ngừa:* Áp dụng chặt chẽ cơ chế Human-in-the-loop: Kỹ sư NOC bắt buộc phải bấm nút phê duyệt từng dự thảo email trước khi hệ thống gửi đi.

---

## 6. Đề xuất kế hoạch hành động tiếp theo (Next steps)

1.  **Tuần 1:** Xây dựng module Python đọc dữ liệu NetBI và tính toán ngưỡng cảnh báo tự động.
2.  **Tuần 2:** Thiết lập prompt hệ thống cho Local LLM và chạy thử nghiệm sinh báo cáo tự động cho 10 tuần lịch sử.
3.  **Tuần 3:** Xây dựng giao diện web nội bộ và kết nối hệ thống email nội bộ để gửi cảnh báo nháp.
4.  **Tuần 4:** Đưa vào chạy thử nghiệm thực tế tại phòng trực NOC và đánh giá hiệu quả để tối ưu hóa prompt.
