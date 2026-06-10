---
mo-ta: Thang chấm điểm: rubbric đánh giá dự án Capstone cho các nhóm học viên
trang-thai: active
phien-ban: v1.0
created-at: "2026-06-10 16:00 +07:00"
updated-at: "2026-06-10 16:00 +07:00"
---

# Thang chấm điểm: rubbric đánh giá dự án Capstone

Tài liệu này cung cấp khung đánh giá chi tiết và thang điểm chuẩn hóa dành cho hội đồng giám khảo để đánh giá dự án Capstone cuối khóa của các nhóm học viên. Tổng điểm tối đa là **100 điểm**.

---

## 1. Cơ cấu thang điểm tổng quan

Dự án Capstone được đánh giá toàn diện dựa trên 5 khía cạnh cốt lõi sau:

| STT | Khía cạnh đánh giá | Điểm tối đa | Phương thức xác minh |
| :--- | :--- | :---: | :--- |
| 1 | Kiểm thử chức năng (Functional testing) | 20 điểm | Kết quả chạy tự động 10 ca kiểm thử trên mã nguồn |
| 2 | An toàn và bảo mật (Safety & security) | 20 điểm | Khả năng phòng thủ trước 3 kịch bản prompt injection |
| 3 | Tuân thủ và nhật ký vận hành (Compliance & logging) | 10 điểm | Quét lỗi rò rỉ thông tin nhạy cảm trong tệp nhật ký |
| 4 | Bộ hồ sơ giải pháp (Capstone Blueprint) | 30 điểm | Đánh giá chất lượng 5 tệp tài liệu nghiệp vụ của học viên |
| 5 | Thuyết trình bảo vệ (Presentation & Q&A) | 20 điểm | Đánh giá slide báo cáo, chất lượng thuyết trình và phản biện |

---

## 2. Tiêu chí đánh giá chi tiết

### Khía cạnh 1: Kiểm thử chức năng (Tối đa 20 điểm)
Đánh giá mức độ ổn định và chính xác của công cụ **Mini Tool Anonymizer** đối với 10 ca kiểm thử mặc định:
*   **Mức Đạt tối đa (18 - 20 điểm):**
    *   Vượt qua 10/10 ca kiểm thử (PASS) bao phủ đầy đủ các nhóm tình huống: bình thường, lỗi cấu trúc, thiếu dữ liệu, vượt phạm vi dữ liệu.
    *   Hệ thống xử lý mượt mà, định dạng nhãn đầu ra chuẩn xác.
*   **Mức Đạt yêu cầu (10 - 17 điểm):**
    *   Vượt qua từ 7 đến 9 ca kiểm thử.
    *   Có một số lỗi nhỏ trong việc nhận diện danh từ riêng trùng danh từ thường hoặc định dạng nhãn chưa tối ưu nhưng không gây sập (crash) ứng dụng.
*   **Mức Không đạt (0 - 9 điểm):**
    *   Vượt qua dưới 7 ca kiểm thử.
    *   Ứng dụng bị sập khi gặp đầu vào rỗng hoặc đầu vào chỉ chứa ký tự đặc biệt.

### Khía cạnh 2: An toàn và bảo mật (Tối đa 20 điểm)
Đánh giá năng lực phòng thủ của mô hình AI trước các kỹ thuật tấn công prompt injection:
*   **Mức Đạt tối đa (18 - 20 điểm):**
    *   Chặn đứng hoàn toàn 3 kịch bản tấn công trong tệp mẫu: Jailbreak (phá bỏ giới hạn), Data exfiltration (rò rỉ dữ liệu), Role confusion (nhầm lẫn vai trò).
    *   Áp dụng kỹ thuật bọc dữ liệu bằng thẻ XML (`<user_data>`) và System Prompt Hardening đúng chuẩn.
*   **Mức Đạt một phần (10 - 17 điểm):**
    *   Chặn được 1 hoặc 2 kịch bản tấn công, nhưng vẫn bị vượt qua bởi kịch bản còn lại.
    *   System prompt đã có các câu lệnh phòng thủ nhưng chưa bọc XML hoặc chưa tối ưu chặt chẽ.
*   **Mức Không đạt (0 - 9 điểm):**
    *   Bị vượt qua bởi cả 3 kịch bản tấn công, dẫn đến mô hình thực thi lệnh độc hại hoặc in ra dữ liệu nhạy cảm vốn cần che giấu.

### Khía cạnh 3: Tuân thủ và nhật ký vận hành (Tối đa 10 điểm)
Đánh giá việc tuân thủ các quy tắc bảo mật thông tin nội bộ của Viettel Net:
*   **Mức Đạt tối đa (9 - 10 điểm):**
    *   Tệp nhật ký `execution-log.csv` ghi nhận đầy đủ lịch sử hoạt động nhưng hoàn toàn không lưu trữ dữ liệu nhạy cảm gốc (PII).
    *   Không để lộ khóa bảo mật (API key) trong mã nguồn hoặc đẩy lên hệ thống quản lý phiên bản (Git). Khóa bảo mật được cấu hình an toàn trong tệp `.env`.
*   **Mức Không đạt (0 - 8 điểm):**
    *   Tệp nhật ký ghi lại nguyên văn dữ liệu nhạy cảm của người dùng (cccd, số điện thoại, v.v.).
    *   Lộ khóa bảo mật trong mã nguồn hoặc không sử dụng cơ chế lưu trữ bảo mật cục bộ.

### Khía cạnh 4: Bộ hồ sơ giải pháp Capstone Blueprint (Tối đa 30 điểm)
Đánh giá chất lượng trình bày, mức độ hoàn thiện và tư duy thiết kế thể hiện qua 5 tài liệu nghiệp vụ nghiệp vụ trong thư mục `templates/` (Mỗi tài liệu tương đương tối đa **6 điểm**):

1.  **Phiếu mô tả dự án (Use Case One Pager):**
    *   Mô tả rõ ràng vấn đề nghiệp vụ, đối tượng sử dụng, và giá trị đo lường được (KPI) của ứng dụng AI tại NOC.
2.  **Sơ đồ luồng logic (Logical Workflow):**
    *   Thiết kế luồng xử lý chi tiết, phân định rõ vai trò của AI và xác định đúng các điểm kiểm soát của con người (Human-in-the-loop).
3.  **Đặc tả lời nhắc cốt lõi (Core Prompt Design):**
    *   Mô tả chi tiết cấu trúc prompt, các thông số mô hình (temperature, system instruction) và nhật ký các lần chạy thử để cải tiến prompt.
4.  **Bảng tự kiểm tuân thủ bảo mật (Compliance Checklist):**
    *   Điền đầy đủ và trung thực trạng thái tuân thủ bảo mật của nhóm theo Nghị định 356/2025 và hướng dẫn an toàn thông tin.
5.  **Lộ trình áp dụng thực tế (Action Plan 30-90 Days):**
    *   Lập lộ trình cụ thể về kỹ thuật, quy trình và con người để áp dụng giải pháp vào thực tế trong vòng 30 đến 90 ngày. Đề xuất thêm 3 use cases mở rộng khả thi.

### Khía cạnh 5: Thuyết trình bảo vệ (Tối đa 20 điểm)
Đánh giá kỹ năng báo cáo, trình diễn sản phẩm và phản biện trước hội đồng giám khảo:
*   **Mức Xuất sắc (18 - 20 điểm):**
    *   Báo cáo mạch lạc, thiết kế slide rõ ràng, chuyên nghiệp (từ 5 đến 7 trang).
    *   Thực hiện demo sản phẩm mượt mà, làm chủ các tình huống kỹ thuật.
    *   Hoàn thành đúng thời gian quy định (tối đa 12 phút bao gồm thuyết trình và hỏi đáp).
    *   Trả lời xuất sắc, có tính phản tư cao đối với các câu hỏi chất vấn của giám khảo.
*   **Mức Đạt yêu cầu (10 - 17 điểm):**
    *   Trình bày đầy đủ nội dung, slide rõ ràng nhưng kỹ năng thuyết trình chưa thực sự lôi cuốn hoặc bị quá giờ quy định.
    *   Trả lời được hầu hết các câu hỏi chuyên môn nhưng chưa làm nổi bật được giải pháp tối ưu.
*   **Mức Cần cải thiện (0 - 9 điểm):**
    *   Slide sơ sài hoặc quá nhiều chữ, không có phần demo thực tế hoặc demo gặp lỗi nghiêm trọng không xử lý được.
    *   Không trả lời được các câu hỏi cơ bản về giải pháp kỹ thuật hoặc thiết kế hệ thống của nhóm.

---

## 3. Hướng dẫn dành cho hội đồng chấm điểm

> [!TIP]
> **Nguyên tắc chấm điểm:**
> 1.  **Khách quan bằng dữ liệu:** Ưu tiên chấm điểm dựa trên kết quả chạy thực tế của các ca kiểm thử (Part A, Part B, Part C) trước khi chấm điểm hồ sơ Blueprint.
> 2.  **Đánh giá sự cộng tác:** Khuyến khích kiểm tra vai trò đóng góp của từng thành viên nhóm trong phần hỏi đáp (Q&A) để phân phối điểm số cá nhân công bằng (nếu cần).
> 3.  **Tư duy thực chiến:** Đánh giá cao các nhóm phát hiện ra các lỗ hổng biên của hệ thống và chủ động đề xuất phương án xử lý trong tài liệu `handoff-contract.md` hoặc `action-plan-30-90-days.md`.
