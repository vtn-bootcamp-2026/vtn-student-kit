---
mo-ta: "Biểu mẫu biên bản bàn giao kỹ thuật Handoff Contract cho VTN HR Policy Assistant"
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-10 15:51 +07:00
updated-at: 2026-06-10 15:51 +07:00
---

# Biên bản bàn giao kỹ thuật (Handoff contract)

*   **Dự án ứng dụng:** Trợ lý AI tra cứu chính sách nhân sự nội bộ (VTN HR Policy Assistant)
*   **Bên giao (Đơn vị phát triển):** Nhóm học viên AI Builders - Nhóm 1 VTN
*   **Bên nhận (Đơn vị vận hành/Người dùng):** Phòng Tổ chức Lao động / Bộ phận IT Viettel Net
*   **Ngày ký kết bàn giao:** 10/06/2026

---

## 1. Mục đích biên bản

Biên bản bàn giao kỹ thuật này xác nhận việc chuyển giao đầy đủ mã nguồn, tài liệu hướng dẫn vận hành, cơ sở dữ liệu vector chính sách và cam kết hỗ trợ kỹ thuật của công cụ **VTN HR Policy Assistant** từ nhóm phát triển sang bộ phận vận hành tại Viettel Net, bảo đảm hệ thống vận hành đúng quy chế bảo mật thông tin nội bộ và an toàn thông tin theo Nghị định 356/2025/NĐ-CP.

---

## 2. Danh mục các tài sản bàn giao (Deliverables)

Bên giao cam kết chuyển giao đầy đủ các cấu phần dưới đây cho Bên nhận:

| STT | Tên tài sản bàn giao | Định dạng / Đường dẫn | Trạng thái bàn giao | Ghi chú kỹ thuật |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Mã nguồn ứng dụng chính | `hr_assistant.py` | [Đầy đủ] | Viết bằng Python 3.10+, tích hợp LangChain, ChromaDB và Pydantic. |
| 2 | File cấu hình môi trường | `.env` | [Đầy đủ] | Chứa các tham số kết nối API Ollama offline và tên mô hình. |
| 3 | File cấu hình thư viện | `requirements.txt` | [Đầy đủ] | Danh sách thư viện Python cần thiết cài đặt môi trường ảo. |
| 4 | Tài liệu vận hành hệ thống | `runbook-template.md` | [Đầy đủ] | Hướng dẫn triển khai, cài đặt và cập nhật Vector DB. |
| 5 | Bộ ca kiểm thử đã xác thực | `test-cases-specification.md` | [Đầy đủ] | Ghi nhận kết quả của 10 ca kiểm thử bao phủ các tình huống biên. |
| 6 | Tài liệu đánh giá bảo mật | `compliance-checklist.md` | [Đầy đủ] | Bảng tự đánh giá tuân thủ an toàn thông tin nội bộ. |
| 7 | Tệp cơ sở dữ liệu Vector mẫu | `data/vector_db/` | [Đầy đủ] | Thư mục chứa chỉ mục vector của quy chế phúc lợi, phép năm, công tác phí. |

---

## 3. Cam kết mức độ dịch vụ và Hỗ trợ kỹ thuật (SLA & Support guidelines)

Để đảm bảo hệ thống VTN HR Policy Assistant hoạt động ổn định và hỗ trợ kịp thời cho phòng Tổ chức Lao động sau bàn giao, hai bên thống nhất các điều khoản hỗ trợ như sau:

### Trách nhiệm của Bên giao (Nhóm phát triển):
*   **Hỗ trợ triển khai ban đầu:** Hỗ trợ cài đặt môi trường, dựng Docker container và cấu hình kết nối API Ollama trực tiếp trên server private cloud của Bên nhận trong vòng **03 ngày làm việc** kể từ ngày ký biên bản.
*   **Hỗ trợ sửa lỗi khẩn cấp (Hotfix):** Cam kết hỗ trợ khắc phục các lỗi nghiêm trọng như sập dịch vụ máy chủ, AI trả lời sai thông tin chính sách nghiêm trọng hoặc phát hiện rò rỉ thông tin cá nhân trong vòng **24 giờ** kể từ khi nhận được yêu cầu hỗ trợ.
*   **Chuyển giao tri thức:** Tổ chức 01 buổi hướng dẫn nghiệp vụ (45 phút) cho cán bộ phòng HR để hướng dẫn cách cập nhật văn bản quy chế mới vào Vector DB và cách kiểm duyệt câu trả lời nhạy cảm trên Admin Dashboard.

### Trách nhiệm của Bên nhận (Đơn vị tiếp nhận):
*   **Chuẩn bị hạ tầng vận hành:** Đảm bảo hệ thống máy chủ private cloud chạy ổn định, đáp ứng đúng yêu cầu tài nguyên tối thiểu (RAM $\ge 8$ GB, cài đặt sẵn Docker và Ollama).
*   **Kiểm soát chất lượng thông tin:** Cán bộ HR có trách nhiệm kiểm tra, kiểm duyệt định kỳ các câu trả lời của AI và cập nhật kịp thời các tài liệu quy chế mới thay thế quy chế cũ.
*   **Bảo mật tài khoản quản trị:** Bảo mật thông tin tài khoản admin truy cập hệ thống và file cấu hình `.env`, không chia sẻ ra bên ngoài mạng nội bộ.

---

## 4. Xác nhận ký kết bàn giao

Hai bên cùng thống nhất các nội dung trên và cam kết thực hiện đúng trách nhiệm được giao.

**ĐẠI DIỆN BÊN GIAO (Nhóm phát triển)**  
*(Ký, ghi rõ họ tên)*  

<br><br><br>

**ĐẠI DIỆN BÊN NHẬN (Đơn vị tiếp quản)**  
*(Ký, ghi rõ họ tên)*  
