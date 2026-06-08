# BÁO CÁO PHÂN TÍCH VÀ LÀM SẠCH DỮ LIỆU CẢNH BÁO NOC

* **Vai trò thực hiện:** Chuyên gia Vận hành NOC (NOC L2/L3 Specialist)
* **Thời gian báo cáo:** 08/06/2026
* **Nguồn dữ liệu:** [sample-noc-alerts.csv](file:///c:/Users/DELL/Documents/4.%20Presentations%20&%20Training/VTN/vtn-student-kit/03-practices/day-01/session-01-use-case-selection/synthetic-data/sample-noc-alerts.csv)
* **Trạng thái xử lý dữ liệu:** Đã hoàn thành làm sạch thông tin nhạy cảm (PII Sanitized)

---

## 1. Giới thiệu tổng quan & Quy trình làm sạch PII

Trong công tác vận hành Trung tâm Giám sát và Điều hành Mạng (NOC), các tệp nhật ký (logs) sự cố thường chứa các thông tin cá nhân nhạy cảm (PII - Personally Identifiable Information) của kỹ sư trực ca hoặc kỹ sư đối tác (như tên, số điện thoại và email liên hệ). Để tuân thủ chính sách bảo mật thông tin và an toàn dữ liệu, toàn bộ dữ liệu thô đã được xử lý lọc bỏ thông tin nhạy cảm trước khi đưa vào phân tích.

**Quy tắc làm sạch dữ liệu (Data Masking Rules):**
* **Tên người liên hệ (Contact Name):** Thay thế bằng `[REDACTED_PII]`.
* **Số điện thoại di động (Phone Number):** Thay thế bằng `[REDACTED_PII]`.
* **Thư điện tử (Email Address):** Thay thế bằng `[REDACTED_PII]`.
* Mọi cấu trúc log mang tính nghiệp vụ và các tham số kỹ thuật khác vẫn được giữ nguyên trạng để đảm bảo tính toàn vẹn trong phân tích sự cố.

---

## 2. Thống kê phân loại cảnh báo theo loại thiết bị (Device Type)

Tổng số cảnh báo ghi nhận trong hệ thống là **115 cảnh báo**. Dưới đây là bảng phân loại chi tiết theo từng loại thiết bị (`device_type`):

| Loại thiết bị (Device Type) | Số lượng cảnh báo | Tỷ lệ (%) | Đánh giá mức độ rủi ro |
| :--- | :---: | :---: | :--- |
| **Server** | 23 | 20.00% | Trung bình (Chủ yếu là cảnh báo dung lượng đĩa và tiến trình Docker) |
| **UPS (Bộ lưu điện)** | 22 | 19.13% | Cao (Ảnh hưởng trực tiếp đến nguồn điện dự phòng của trạm) |
| **Base-station (Trạm phát sóng)** | 19 | 16.52% | Cao (Nhiều cảnh báo lỗi module RF và nguồn điện dự phòng trạm) |
| **Switch (Thiết bị chuyển mạch)** | 18 | 15.65% | Trung bình (Lưu lượng broadcast cao và thay đổi cấu hình STP) |
| **Firewall (Tường lửa)** | 18 | 15.65% | Cao (Cảnh báo đầy session table và phát hiện brute force) |
| **Router (Thiết bị định tuyến)** | 15 | 13.04% | Rất Cao (Gây gián đoạn kênh truyền uplink, mất kết nối OSPF/BGP) |
| **Tổng cộng** | **115** | **100.00%** | |

---

## 3. Phân tích các cảnh báo nguy kịch (Critical) đang mở (Open)

Hệ thống đã trích xuất được **03 cảnh báo** đáp ứng đồng thời cả 2 điều kiện: mức độ nghiêm trọng **Nguy kịch (severity: critical)** và tình trạng lỗi **Chưa xử lý (status: open)**. Dưới đây là chi tiết lỗi, nội dung dịch nghĩa tiếng Việt và đề xuất hành động khắc phục nhanh (Human-in-the-loop - HITL):

### Cảnh báo 1: ALERT-040
* **Thời gian ghi nhận:** `2026-05-01 23:56:00`
* **Mã trạm (Site Code):** `TEST_SITE_034`
* **Loại thiết bị:** `Base-station` (Trạm phát sóng)
* **Nội dung cảnh báo gốc:** `power backup warning in training scenario`
* **Dịch nghĩa sự cố:** Cảnh báo lỗi nguồn điện dự phòng tại trạm trong kịch bản diễn tập (mất điện lưới và đang chạy ắc quy dự phòng).
* **Đề xuất khắc phục nhanh (HITL):**
  > [!IMPORTANT]
  > **Mức độ khẩn cấp: Cao**
  > 1. Kiểm tra khẩn cấp trạng thái điện lưới AC tại trạm qua hệ thống giám sát nguồn.
  > 2. Theo dõi dung lượng pin/ắc quy còn lại và tính toán thời gian duy trì tối đa của trạm.
  > 3. Nếu điện lưới không tự khôi phục trong vòng 15 phút tới, điều phối kỹ thuật viên địa bàn mang máy phát điện di động đến trạm để ứng cứu thông tin.

---

### Cảnh báo 2: ALERT-058
* **Thời gian ghi nhận:** `2026-05-01 19:41:00`
* **Mã trạm (Site Code):** `TEST_SITE_013`
* **Loại thiết bị:** `Base-station` (Trạm phát sóng)
* **Nội dung cảnh báo gốc:** `RF module communication failure in lab environment`
* **Dịch nghĩa sự cố:** Lỗi kết nối truyền thông của mô-đun vô tuyến (RF Module) trong môi trường phòng Lab.
* **Đề xuất khắc phục nhanh (HITL):**
  > [!IMPORTANT]
  > **Mức độ khẩn cấp: Cao**
  > 1. Thực hiện lệnh khởi động lại phần mềm (soft-reset) mô-đun RF từ xa thông qua giao diện quản trị trạm gốc.
  > 2. Đo kiểm tra công suất phản xạ vô tuyến (VSWR) để xác định xem có lỗi phần cứng hoặc hỏng đầu nối nhảy anten (jumper) hay không.
  > 3. Cử nhân sự trực lab kiểm tra kết nối cáp quang nối từ khối xử lý băng gốc (BBU) tới khối vô tuyến (RRU).

---

### Cảnh báo 3: ALERT-081
* **Thời gian ghi nhận:** `2026-05-01 13:48:00`
* **Mã trạm (Site Code):** `TEST_SITE_020`
* **Loại thiết bị:** `Switch` (Thiết bị chuyển mạch)
* **Nội dung cảnh báo gốc:** `high broadcast traffic detected in lab subnet`
* **Dịch nghĩa sự cố:** Phát hiện lưu lượng quảng bá (broadcast) tăng cao bất thường trong phân mạng lab (nguy cơ Broadcast Storm).
* **Đề xuất khắc phục nhanh (HITL):**
  > [!WARNING]
  > **Mức độ khẩn cấp: Trung bình/Cao**
  > 1. Sử dụng lệnh trên switch kiểm tra lưu lượng truyền nhận ở các cổng để xác định cổng mạng đang phát sinh lưu lượng broadcast bất thường.
  > 2. Kiểm tra log sự kiện xem có sự thay đổi cấu trúc Spanning Tree (STP) hay loop vật lý nào vừa xảy ra không.
  > 3. Cấu hình giới hạn lưu lượng quảng bá (Storm Control) trên cổng bị ảnh hưởng để ngăn chặn sự cố tràn lưu lượng làm treo toàn hệ thống mạng lab.

---

## 4. Bảng đối chiếu minh họa kết quả làm sạch dữ liệu PII

Vì cả 3 cảnh báo nguy kịch đang mở ở trên đều không chứa PII nhạy cảm, NOC L2/L3 cung cấp bảng đối chiếu minh họa dưới đây để làm rõ hiệu quả thực tế của quy trình làm sạch dữ liệu PII trên các dòng log tiêu biểu từ dữ liệu đầu vào.

*Để đảm bảo bảo mật tuyệt đối cho thông tin của nhân sự, các thông tin nhạy cảm ở cột "Dữ liệu trước khi lọc" dưới đây đã được chủ động che mờ một phần (ví dụ: `Nguyen Van A` -> `Ngu*** A`, `0987654321` -> `098*****21`, `tran.b@vtn.com.vn` -> `tr***@vtn.com.vn`):*

| Mã cảnh báo | Dữ liệu trước khi lọc (Đã che mờ một phần để bảo mật) | Dữ liệu sau khi làm sạch (Sanitized) |
| :--- | :--- | :--- |
| **ALERT-001** | database query latency spike in performance test [Contact: Ngu*** A (098*****21)] | database query latency spike in performance test [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-009** | RF module communication failure in lab environment [Assigned to: Ngu*** E (091*****78)] | RF module communication failure in lab environment [Assigned to: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-013** | high memory usage alert on training cluster [Contact: Ngu*** A (098*****21)] | high memory usage alert on training cluster [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-022** | database query latency spike in performance test [Contact: Tra*** B (tr***@vtn.com.vn)] | database query latency spike in performance test [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-025** | interface flap in synthetic log [Contact: Tra*** B (tr***@vtn.com.vn)] | interface flap in synthetic log [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-041** | swap space exhausted in sandbox environment [Contact: Ngu*** A (098*****21)] | swap space exhausted in sandbox environment [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-042** | spanning tree topology change detected [Operator notes: contact engineer Le*** C at le***@vtn.vn if alert persists] | spanning tree topology change detected [Operator notes: contact engineer [REDACTED_PII] at [REDACTED_PII] if alert persists] |
| **ALERT-045** | disk space low on simulated system drive [Contact: Ngu*** A (098*****21)] | disk space low on simulated system drive [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-061** | spanning tree topology change detected [Contact: Ngu*** A (098*****21)] | spanning tree topology change detected [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-067** | high memory usage alert on training cluster [Operator notes: contact engineer Le*** C at le***@vtn.vn if alert persists] | high memory usage alert on training cluster [Operator notes: contact engineer [REDACTED_PII] at [REDACTED_PII] if alert persists] |
| **ALERT-068** | unauthorized login attempt simulated in audit log [Contact: Tra*** B (tr***@vtn.com.vn)] | unauthorized login attempt simulated in audit log [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-070** | session table capacity warning (simulated) [Ticket owner: Pha*** D - px***@vtn.com.vn] | session table capacity warning (simulated) [Ticket owner: [REDACTED_PII] - [REDACTED_PII]] |
| **ALERT-077** | simulated brute force attack blocked on local port [Contact: Tra*** B (tr***@vtn.com.vn)] | simulated brute force attack blocked on local port [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-084** | docker daemon crash warning in test node [Contact: Tra*** B (tr***@vtn.com.vn)] | docker daemon crash warning in test node [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-085** | BGP session flapping on simulated interface [Operator notes: contact engineer Le*** C at le***@vtn.vn if alert persists] | BGP session flapping on simulated interface [Operator notes: contact engineer [REDACTED_PII] at [REDACTED_PII] if alert persists] |
| **ALERT-093** | input voltage fluctuation detected in lab [Operator notes: contact engineer Le*** C at le***@vtn.vn if alert persists] | input voltage fluctuation detected in lab [Operator notes: contact engineer [REDACTED_PII] at [REDACTED_PII] if alert persists] |
| **ALERT-095** | RF module communication failure in lab environment [Assigned to: Ngu*** E (091*****78)] | RF module communication failure in lab environment [Assigned to: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-096** | high load capacity warning on bench unit [Operator notes: contact engineer Le*** C at le***@vtn.vn if alert persists] | high load capacity warning on bench unit [Operator notes: contact engineer [REDACTED_PII] at [REDACTED_PII] if alert persists] |
| **ALERT-102** | unauthorized login attempt simulated in audit log [Contact: Ngu*** A (098*****21)] | unauthorized login attempt simulated in audit log [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-109** | input voltage fluctuation detected in lab [Contact: Ngu*** A (098*****21)] | input voltage fluctuation detected in lab [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-110** | RF module communication failure in lab environment [Operator notes: contact engineer Le*** C at le***@vtn.vn if alert persists] | RF module communication failure in lab environment [Operator notes: contact engineer [REDACTED_PII] at [REDACTED_PII] if alert persists] |
| **ALERT-115** | power backup warning in training scenario [Ticket owner: Pha*** D - px***@vtn.com.vn] | power backup warning in training scenario [Ticket owner: [REDACTED_PII] - [REDACTED_PII]] |

---

## 5. Kết luận & Khuyến nghị

1. Quy trình làm sạch dữ liệu tự động đã hoạt động chính xác 100%, loại bỏ toàn bộ dữ liệu PII trong log mà không làm ảnh hưởng đến cấu trúc kỹ thuật của thông điệp lỗi.
2. Thiết bị loại **Server**, **UPS**, và **Base-station** chiếm tỷ trọng cảnh báo cao nhất (tổng cộng hơn 55% lượng cảnh báo). Đề xuất lên kế hoạch bảo dưỡng định kỳ hệ thống ắc quy dự phòng (UPS) và tối ưu hóa hệ thống máy chủ để giảm thiểu cảnh báo ảo.
3. Đối với 3 sự cố **Critical & Open** (ALERT-040, ALERT-058, ALERT-081), đề nghị Trực ca NOC L2/L3 tiến hành xử lý gấp theo quy trình khắc phục nhanh (HITL) đã nêu ở Mục 3 nhằm ngăn ngừa nguy cơ gián đoạn dịch vụ diện rộng.
