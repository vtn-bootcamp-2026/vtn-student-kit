---
mo-ta: Báo cáo phân tích và làm sạch dữ liệu cảnh báo NOC (PII Sanitization & NOC Alerts Analysis Report)
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-11 10:50 +07:00
updated-at: 2026-06-11 10:50 +07:00
---

# Báo cáo phân tích và làm sạch dữ liệu cảnh báo NOC

Báo cáo này được thực hiện bởi Chuyên gia Vận hành NOC (NOC L2/L3 Specialist) nhằm xử lý, làm sạch thông tin cá nhân nhạy cảm (PII), thống kê số lượng cảnh báo theo thiết bị, và đề xuất phương án xử lý cho các cảnh báo nguy kịch đang mở (critical & open).

---

## 1. Quy trình làm sạch dữ liệu (PII Sanitization)

Để đảm bảo tuân thủ các quy định về bảo mật thông tin và an toàn dữ liệu, toàn bộ thông tin cá nhân nhạy cảm (PII) như **Họ tên**, **Số điện thoại**, và **Email** xuất hiện trong trường thông tin tóm tắt (`summary`) của cảnh báo đều được phát hiện và thay thế bằng nhãn bảo mật `[REDACTED_PII]`.

### Bảng đối chiếu minh họa làm sạch PII
Dưới đây là một số dòng log tiêu biểu từ dữ liệu đầu vào chứa thông tin nhạy cảm đã được xử lý làm sạch. Để đảm bảo an toàn tuyệt đối, thông tin nhạy cảm trong cột **Dữ liệu trước khi lọc** đã được chủ động che/làm mờ một phần bằng các ký tự ẩn (`*`).

| Mã cảnh báo | Dữ liệu trước khi lọc (Làm mờ một phần) | Dữ liệu sau khi lọc (Sanitized) |
| :--- | :--- | :--- |
| **ALERT-001** | database query latency spike in performance test [Contact: Ngu*** A (098*****21)] | database query latency spike in performance test [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-009** | RF module communication failure in lab environment [Assigned to: Ngu*** E (091*****78)] | RF module communication failure in lab environment [Assigned to: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-022** | database query latency spike in performance test [Contact: Tra*** B (tra***@vtn.com.vn)] | database query latency spike in performance test [Contact: [REDACTED_PII] ([REDACTED_PII])] |
| **ALERT-042** | spanning tree topology change detected [Operator notes: contact engineer Le*** C at le***@vtn.vn if alert persists] | spanning tree topology change detected [Operator notes: contact engineer [REDACTED_PII] at [REDACTED_PII] if alert persists] |
| **ALERT-070** | session table capacity warning (simulated) [Ticket owner: Pha*** D - px***@vtn.com.vn] | session table capacity warning (simulated) [Ticket owner: [REDACTED_PII] - [REDACTED_PII]] |

---

## 2. Thống kê số lượng cảnh báo theo loại thiết bị

Tổng số lượng cảnh báo trong tệp dữ liệu NOC là **115 cảnh báo**. Dưới đây là bảng thống kê số lượng cảnh báo phân phối theo từng loại thiết bị (`device_type`):

| Loại thiết bị (Device Type) | Số lượng cảnh báo | Tỷ lệ (%) |
| :--- | :---: | :---: |
| **Server** | 23 | 20.0% |
| **UPS** (Bộ lưu điện) | 22 | 19.1% |
| **Base-station** (Trạm thu phát sóng) | 19 | 16.5% |
| **Switch** (Thiết bị chuyển mạch) | 18 | 15.7% |
| **Firewall** (Tường lửa) | 18 | 15.7% |
| **Router** (Thiết bị định tuyến) | 15 | 13.0% |
| **Tổng cộng** | **115** | **100%** |

---

## 3. Danh sách cảnh báo nguy kịch đang mở (Critical & Open)

Hệ thống đã trích xuất được **03 cảnh báo** có mức độ nghiêm trọng là **Nguy kịch (Critical)** và hiện tại vẫn đang ở trạng thái **Đang mở (Open)**. Dưới đây là thông tin chi tiết, bản dịch nội dung lỗi và đề xuất hành động khắc phục nhanh (HITL - Human-in-the-loop):

### 🔴 ALERT-040
- **Thời gian ghi nhận**: 2026-05-01 23:56:00
- **Mã trạm (Site Code)**: TEST_SITE_034
- **Loại thiết bị**: Base-station (Trạm thu phát sóng)
- **Nội dung cảnh báo gốc**: `power backup warning in training scenario`
- **Dịch nghĩa tiếng Việt**: Cảnh báo nguồn điện dự phòng trong kịch bản diễn tập / đào tạo.
- **Hành động khắc phục đề xuất (HITL)**:
  1. Kiểm tra từ xa trạng thái của hệ thống điện dự phòng (Ắc quy/UPS/Máy phát điện) tại trạm TEST_SITE_034 để xác định mức dung lượng còn lại và điện áp đầu ra.
  2. Phối hợp với kỹ sư vận hành tại hiện trường hoặc nhân viên trực ca phòng lab để xác nhận xem đây là lỗi phần cứng nguồn thực tế hay chỉ là tín hiệu giả lập trong bài diễn tập.
  3. Nếu dung lượng ắc quy giảm dưới ngưỡng an toàn, kích hoạt nguồn điện lưới hoặc khởi động máy phát điện dự phòng để ngăn chặn việc trạm bị mất điện hoàn toàn gây gián đoạn dịch vụ.

### 🔴 ALERT-058
- **Thời gian ghi nhận**: 2026-05-01 19:41:00
- **Mã trạm (Site Code)**: TEST_SITE_013
- **Loại thiết bị**: Base-station (Trạm thu phát sóng)
- **Nội dung cảnh báo gốc**: `RF module communication failure in lab environment`
- **Dịch nghĩa tiếng Việt**: Lỗi kết nối/truyền thông của mô-đun RF (vô tuyến) trong môi trường phòng lab.
- **Hành động khắc phục đề xuất (HITL)**:
  1. Thực hiện kiểm tra ping và truy cập dòng lệnh (CLI) tới khối xử lý trung tâm (BBU) quản lý mô-đun RF bị lỗi để kiểm tra lịch sử kết nối.
  2. Thực hiện khởi động lại mềm (soft reboot) mô-đun RF từ hệ thống quản lý tập trung.
  3. Nếu không khôi phục được kết nối, cử kỹ sư trực phòng lab kiểm tra trực quan các kết nối vật lý (cáp quang/cáp đồng CPRI nối BBU và RRU), đầu nối nguồn và đèn trạng thái LED trên thiết bị phần cứng để phát hiện hư hỏng vật lý hoặc lỏng cáp.

### 🔴 ALERT-081
- **Thời gian ghi nhận**: 2026-05-01 13:48:00
- **Mã trạm (Site Code)**: TEST_SITE_020
- **Loại thiết bị**: Switch (Thiết bị chuyển mạch)
- **Nội dung cảnh báo gốc**: `high broadcast traffic detected in lab subnet`
- **Dịch nghĩa tiếng Việt**: Phát hiện lưu lượng tin quảng bá (broadcast traffic) cao bất thường trong phân đoạn mạng (subnet) phòng lab.
- **Hành động khắc phục đề xuất (HITL)**:
  1. Truy cập vào thiết bị Switch tại TEST_SITE_020 thông qua SSH, kiểm tra số liệu thống kê lưu lượng trên các cổng mạng (`show interfaces` hoặc tương đương) để định vị cổng (port) phát tán gói tin broadcast nhiều nhất.
  2. Xác định các thiết bị đầu cuối kết nối vào cổng đó để điều tra nguyên nhân (ví dụ: lỗi vòng lặp mạng - loop, lỗi card mạng của thiết bị lab, hoặc mã độc quét mạng).
  3. Tạm thời shutdown cổng bị ảnh hưởng để bảo vệ tính toàn vẹn và băng thông của toàn bộ phân đoạn mạng lab, đồng thời cấu hình Storm Control giới hạn tỷ lệ broadcast traffic trên Switch để tự động ngăn chặn các sự cố tương tự trong tương lai.
