---
mo-ta: "Biên bản bàn giao kỹ thuật AI Agent tra cứu tài liệu kỹ thuật mạng lưới Viettel"
trang-thai: draft
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
luu-y: "Tài liệu sử dụng dữ liệu mô phỏng. Không chứa thông tin thật của VTN."
---

# Biên bản bàn giao kỹ thuật (Handoff contract)

*   **Dự án ứng dụng:** AI Agent Tra Cứu Tài Liệu Kỹ Thuật Mạng Lưới Viettel (Network Doc Assistant)
*   **Bên giao (Đơn vị phát triển):** Nhóm học viên AI Builders — [Tên nhóm thực hành — mô phỏng]
*   **Bên nhận (Đơn vị vận hành/Người dùng):** [Trung tâm Vận hành Khai thác Mạng / Phòng Quy hoạch Mạng lưới — mô phỏng]
*   **Ngày ký kết bàn giao:** [Điền ngày nghiệm thu thực tế]

---

## 1. Mục đích biên bản

Biên bản bàn giao kỹ thuật (Handoff contract) xác nhận việc chuyển giao toàn bộ mã nguồn, cấu hình hệ thống, Knowledge Base đã kiểm duyệt, tài liệu vận hành và cam kết bảo trì kỹ thuật của **AI Agent Tra Cứu Tài Liệu Kỹ Thuật** từ nhóm phát triển sang đơn vị vận hành, nhằm đảm bảo hệ thống được tiếp quản và vận hành ổn định, đúng quy chế bảo mật của **Viettel Net** — đặc biệt với cam kết vận hành **hoàn toàn offline/intranet**, không kết nối Internet bên ngoài.

---

## 2. Danh mục các tài sản bàn giao (Deliverables)

Bên giao cam kết chuyển giao đầy đủ các cấu phần dưới đây cho Bên nhận:

| STT | Tên tài sản bàn giao | Định dạng / Đường dẫn | Trạng thái bàn giao | Ghi chú kỹ thuật |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Mã nguồn AI Agent (RAG Pipeline) | `network-doc-assistant/` | [Đầy đủ] | Python 3.10+, pipeline RAG + Local LLM qua Ollama |
| 2 | Giao diện chat web nội bộ | `web-ui/index.html` + `web-ui/app.js` | [Đầy đủ] | Chạy trên intranet VTN — không kết nối Internet |
| 3 | File cấu hình môi trường | `.env` | [Đầy đủ] | Cấu hình endpoint Ollama cục bộ, tên mô hình, ngưỡng confidence |
| 4 | Knowledge Base đã kiểm duyệt (mô phỏng) | `knowledge-base/` (VectorDB cục bộ) | [Đầy đủ] | Chỉ chứa tài liệu nhãn "Công khai nội bộ" đã được kỹ sư chuyên môn cao phê duyệt |
| 5 | Danh sách kiểm duyệt tài liệu KB | `kb-audit-log.xlsx` | [Đầy đủ] | Danh sách tài liệu + người phê duyệt + ngày cập nhật + phiên bản |
| 6 | Tài liệu hướng dẫn vận hành | `runbook-template.md` | [Đầy đủ] | Hướng dẫn cài đặt, vận hành, xử lý sự cố và quy trình cập nhật KB |
| 7 | Bảng kiểm tuân thủ bảo mật | `compliance-checklist.md` | [Đầy đủ] | Đánh giá tuân thủ an toàn thông tin, phân loại dữ liệu, HITL |
| 8 | Đặc tả ca kiểm thử đã xác thực | `test-cases-specification.md` | [Đầy đủ] | Kết quả 10 ca kiểm thử đã PASS |
| 9 | Quy trình SOP cập nhật Knowledge Base | `kb-update-sop.md` | [Đầy đủ] | Hướng dẫn kỹ sư chuyên môn cao thực hiện rà soát và cập nhật KB định kỳ |
| 10 | Bộ câu hỏi kiểm thử KB (mô phỏng) | `qa-test-set.json` | [Đầy đủ] | 20 câu hỏi mẫu để kiểm thử chất lượng KB sau mỗi lần cập nhật |

---

## 3. Cam kết mức độ dịch vụ và Hỗ trợ kỹ thuật (SLA & Support guidelines)

### Trách nhiệm của Bên giao (Nhóm phát triển):
*   **Hỗ trợ cài đặt hạ tầng ban đầu:** Hỗ trợ cài đặt môi trường Python, Ollama và tải mô hình cục bộ trực tiếp trên hạ tầng của Bên nhận trong vòng **05 ngày làm việc** kể từ ngày ký biên bản.
*   **Sửa lỗi khẩn cấp (Hotfix):** Cam kết xử lý các lỗi nghiêm trọng (sập hệ thống, AI trả lời hoàn toàn sai lệch, rò rỉ thông tin vào log) trong vòng **24 giờ** kể từ khi nhận được thông báo.
*   **Chuyển giao tri thức vận hành KB:** Tổ chức **01 buổi hướng dẫn chuyên sâu (60–90 phút)** cho kỹ sư chuyên môn cao của Bên nhận về:
    *   Quy trình phân loại và kiểm duyệt tài liệu trước khi đưa vào KB.
    *   Cách thực hiện re-index tài liệu mới vào Knowledge Base.
    *   Quy trình thu hồi và thay thế tài liệu lỗi thời.
    *   Cách chạy bộ kiểm thử QA sau mỗi lần cập nhật KB.

### Trách nhiệm của Bên nhận (Đơn vị tiếp nhận):
*   **Chuẩn bị hạ tầng:** Đảm bảo máy chủ vận hành đáp ứng yêu cầu phần cứng tối thiểu (RAM >= 16 GB cho server, cài đặt sẵn Python 3.10+ và Ollama), chạy trên mạng **intranet nội bộ VTN** — không kết nối Internet bên ngoài.
*   **Chỉ định kỹ sư quản lý Knowledge Base:** Chỉ định ít nhất **02 kỹ sư chuyên môn cao** chịu trách nhiệm rà soát, cập nhật và kiểm duyệt tài liệu trong KB định kỳ — tối thiểu **mỗi quý một lần** hoặc ngay sau khi nhà cung cấp phát hành tài liệu mới.
*   **Thực hiện kiểm duyệt HITL:** Kỹ sư cấp cao xem xét và ký xác nhận phiếu kiểm tra trước khi áp dụng bất kỳ gợi ý cấu hình tham số nào từ AI vào thiết bị thực.
*   **Báo cáo sự cố:** Thông báo kịp thời (trong vòng 4 giờ) cho nhóm phát triển khi phát hiện AI trả lời sai lệch thông tin kỹ thuật quan trọng.
*   **Sử dụng đúng mục đích:** Chỉ sử dụng hệ thống trong phạm vi nội bộ của Viettel Net. Không tự ý kết nối hệ thống ra Internet bên ngoài hoặc gửi tài liệu kỹ thuật thật lên các công cụ AI đám mây.

---

## 4. Điều khoản đặc biệt về Bảo mật Thông tin

*   **Cam kết offline tuyệt đối:** Hệ thống được thiết kế và bàn giao với cam kết **không kết nối Internet bên ngoài** tại bất kỳ thành phần nào trong pipeline (giao diện web, RAG engine, Local LLM, VectorDB). Bên nhận không được phép thay đổi cấu hình này mà không có phê duyệt từ bộ phận An toàn Thông tin VTN.
*   **Phân loại tài liệu KB:** Chỉ tài liệu có nhãn bảo mật **"Công khai nội bộ"** (đã được người có thẩm quyền ký xác nhận) mới được đưa vào Knowledge Base. Tuyệt đối không đưa tài liệu nhãn "Mật" hoặc "Tối mật".
*   **Không lưu trữ câu hỏi người dùng:** Hệ thống log chỉ ghi `session_id`, `timestamp`, `category`, `confidence_score` — tuyệt đối không ghi nội dung câu hỏi hoặc câu trả lời vào log file.

---

## 5. Xác nhận ký kết bàn giao

Hai bên cùng thống nhất các nội dung trên và cam kết thực hiện đúng trách nhiệm được giao.

**ĐẠI DIỆN BÊN GIAO (Nhóm phát triển)**
*(Ký, ghi rõ họ tên)*

<br><br><br>

**ĐẠI DIỆN BÊN NHẬN (Đơn vị tiếp quản — Kỹ sư chuyên môn cao phụ trách Knowledge Base)**
*(Ký, ghi rõ họ tên)*
