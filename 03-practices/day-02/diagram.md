---
mo-ta: sơ đồ kiến trúc tác nhân và luồng xử lý RAG ngày 02
trang-thai: active
phien-ban: v1.0
created-at: 2026-06-11 15:50 +07:00
updated-at: 2026-06-11 15:50 +07:00
---

# Sơ đồ thực hành ngày 02

Tài liệu này tổng hợp các sơ đồ kiến trúc tác nhân trí tuệ nhân tạo (tiếng Việt: AI agent) và quy trình xử lý dữ liệu cho các bài thực hành thuộc ngày 02 (tiếng Việt: Day 02). Các sơ đồ được biểu diễn bằng mã Mermaid giúp hiển thị trực quan trong giao diện của môi trường phát triển tích hợp (tiếng Việt: Integrated Development Environment - IDE).

---

## 1. Sơ đồ kiến trúc tác nhân AI trích xuất điều khoản hợp đồng: Expected Agent Architecture

Dưới đây là sơ đồ kiến trúc chi tiết của tác nhân trích xuất điều khoản hợp đồng (tiếng Việt: Contract Term Extractor) thuộc buổi học số 03 (tiếng Việt: Session 03):

```mermaid
graph TD
    %% Định nghĩa phong cách thiết kế
    classDef startNode fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20;
    classDef processNode fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1;
    classDef aiNode fill:#EDE7F6,stroke:#4527A0,stroke-width:2px,color:#4A148C;
    classDef conditionNode fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    classDef errorNode fill:#FFEBEE,stroke:#C62828,stroke-width:2px,color:#B71C1C;
    classDef successNode fill:#F1F8E9,stroke:#558B2F,stroke-width:2px,color:#33691E;

    Input([Hợp đồng đầu vào]) --> Intake[Nạp đầu vào: Intake <br>- Đọc tệp tin văn bản: Read text file<br>- Kiểm tra siêu dữ liệu: Check metadata<br>- Lọc lỗi rỗng hoặc mã hóa: Check empty or encoding<br>- Ghi nhật ký nạp: Write intake log]:::processNode
    Intake --> CheckIntake{Lỗi nạp đầu vào?}:::conditionNode
    
    CheckIntake -- "Có" --> IntakeError[Nhánh lỗi nạp đầu vào<br>- Ghi nhật ký lỗi<br>- Bỏ qua hợp đồng]:::errorNode
    CheckIntake -- "Không" --> Extraction[Trích xuất: Extraction <br>- Gọi giao diện lập trình ứng dụng LLM: Call LLM API<br>- Lời nhắc hệ thống: System prompt & Lời nhắc người dùng: User prompt<br>- Phân tích phản hồi JSON: Parse JSON response]:::aiNode
    
    Extraction --> SelfCheck[Tự kiểm duyệt: Self-check <br>- Xác thực cấu trúc: Schema validation<br>- Căn cứ nguồn: Source evidence<br>- Đánh giá mức tin cậy: Confidence evaluation]:::processNode
    SelfCheck --> CheckSelf{Phát hiện lỗi?}:::conditionNode
    
    CheckSelf -- "Có" --> Retry[Thử lại trích xuất: Retry extraction <br>- Ghi chú lỗi cụ thể<br>- Tối đa 2 lần]:::errorNode
    Retry --> Extraction
    
    CheckSelf -- "Không" --> RedFlag[Kiểm tra cờ đỏ: Red-flag check <br>- Đối chiếu đầu ra JSON với quy tắc: Match JSON output with rules]:::processNode
    RedFlag --> Routing{Định tuyến đầu ra: Routing <br>- Cần con người duyệt: needs_human_review = true?<br>- Mức tin cậy: confidence < 0.7?<br>- Có cờ đỏ: red_flags?<br>- Thiếu trường dữ liệu: missing_fields?}:::conditionNode
    
    Routing -- "Đạt điều kiện tự động (Auto)" --> AutoOut[Đầu ra tự động: Auto output <br>- Ghi tệp JSON kết quả<br>- Ghi nhật ký vận hành: Execution log]:::successNode
    Routing -- "Cần xem xét (HITL)" --> HitlOut[Đầu ra có con người duyệt: HITL output <br>- Ghi tệp JSON nháp<br>- Xuất báo cáo cờ đỏ: Red-flag report<br>- Chuyển sang hàng đợi người duyệt]:::conditionNode

    class Input startNode;
    class Intake,SelfCheck,RedFlag processNode;
    class Extraction aiNode;
    class CheckIntake,CheckSelf,Routing conditionNode;
    class IntakeError,Retry errorNode;
    class AutoOut,HitlOut successNode;
```

---

## 2. Bản đồ khái niệm luồng xử lý tổng thể: Concept Map

Sơ đồ tuần tự các bước xử lý từ tài liệu thô cho tới đầu ra cuối cùng:

```mermaid
graph TD
    classDef stepNode fill:#F5F5F5,stroke:#9E9E9E,stroke-width:2px,color:#212121;
    classDef decisionNode fill:#FFF8E1,stroke:#FFB300,stroke-width:2px,color:#FF8F00;
    classDef routeNode fill:#E0F2F1,stroke:#00897B,stroke-width:2px,color:#004D40;
    classDef errorNode fill:#FFEBEE,stroke:#C62828,stroke-width:2px,color:#B71C1C;

    Doc([Hợp đồng đầu vào]) --> Step1[Bước 1: Kiểm tra đầu vào<br>- Tệp tin rỗng?<br>- Nhận dạng ký tự quang học lỗi: OCR error?<br>- Thiếu siêu dữ liệu: Missing metadata?]:::stepNode
    Step1 --> Dec1{Hợp lệ?}:::decisionNode
    Dec1 -- "Không" --> Err1[Ghi nhật ký: Log + Con người duyệt: HITL]:::errorNode
    Dec1 -- "Có" --> Step2[Bước 2: Trích xuất điều khoản<br>- Lời nhắc hệ thống & người dùng → JSON<br>- Bắt buộc có căn cứ nguồn: Source evidence]:::stepNode
    
    Step2 --> Step3[Bước 3: Tự kiểm: Self-check<br>- Đủ trường dữ liệu? Đúng định dạng?<br>- Căn cứ nguồn khớp với phân đoạn văn bản: Chunk]:::stepNode
    Step3 --> Dec2{Thông qua?}:::decisionNode
    Dec2 -- "Không" --> Step2
    Dec2 -- "Có" --> Step4[Bước 4: Đối chiếu kho điều khoản<br>- Thư viện điều khoản: Clause library<br>- Quy tắc phát hiện cờ đỏ: Red-flag rules]:::stepNode
    
    Step4 --> Dec3{Có cờ đỏ?}:::decisionNode
    Dec3 -- "Có" --> Flag[Thêm vào danh sách cờ đỏ: red_flags[]]:::routeNode
    Dec3 -- "Không" --> Step5[Bước 5: Xuất kết quả<br>- Sinh tệp JSON & nhật ký vận hành: Execution log]:::stepNode
    Flag --> Step5
    
    Step5 --> Dec4{Cần người duyệt?}:::decisionNode
    Dec4 -- "needs_human_review = false" --> Done([Hoàn thành: DONE]):::routeNode
    Dec4 -- "needs_human_review = true" --> Queue([Hàng đợi người duyệt: HITL]):::routeNode

    class Doc stepNode;
    class Step1,Step2,Step3,Step4,Step5 stepNode;
    class Dec1,Dec2,Dec3,Dec4 decisionNode;
    class Err1 errorNode;
    class Flag,Done,Queue routeNode;
```

---

## 3. Luồng thực thi kỹ năng RAG chính sách nhân sự: HR Policy QA RAG Workflow

Kiến trúc luồng xử lý RAG chủ động (tiếng Việt: Agentic RAG) kết hợp tìm kiếm ngữ nghĩa và từ khóa ở buổi học số 04 (tiếng Việt: Session 04):

```mermaid
graph TD
    classDef clientNode fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238;
    classDef ragNode fill:#E1F5FE,stroke:#0288D1,stroke-width:2px,color:#01579B;
    classDef checkNode fill:#F9FBE7,stroke:#AFB42B,stroke-width:2px,color:#33691E;
    classDef errorNode fill:#FFEBEE,stroke:#C62828,stroke-width:2px,color:#B71C1C;

    Query([Câu hỏi chính sách nhân sự]) --> Step1[Bước 1: Tiếp nhận & Phân loại<br>- Trong phạm vi: In-scope?<br>- Ngoài phạm vi: Out-of-scope?<br>- Mơ hồ: Ambiguous?<br>- Tấn công mã độc lời nhắc: Prompt injection?]:::clientNode
    
    Step1 --> Dec1{Kết quả phân loại}:::checkNode
    Dec1 -- "Ngoài phạm vi / Tấn công" --> Refuse[Từ chối lịch sự & Ghi nhật ký]:::errorNode
    Dec1 -- "Mơ hồ" --> AskClarify[Yêu cầu làm rõ / HITL]:::clientNode
    Dec1 -- "Trong phạm vi" --> Step2[Bước 2: Truy xuất lai: Hybrid Retrieval<br>- Tìm kiếm ngữ nghĩa: Semantic search bằng ChromaDB<br>- Tìm kiếm từ khóa: Keyword search bằng TF-IDF / BM25<br>- Trả về 3 phân đoạn phù hợp nhất: Top-3 chunks]:::ragNode
    
    Step2 --> Step3[Bước 3: Tổng hợp & Tự kiểm duyệt<br>- Soạn câu trả lời dựa trên chunks<br>- Trích dẫn nguồn bắt buộc: doc_id, section, quote<br>- Kiểm tra chéo: quote khớp nguyên văn với chunk?]:::ragNode
    
    Step3 --> Dec2{Trích dẫn khớp chunk và mức tin cậy >= 0.6?}:::checkNode
    Dec2 -- "Không" --> HitlRoute[Gán cờ cần con người duyệt: needs_human_review = true]:::clientNode
    Dec2 -- "Có" --> Step4[Bước 4: Đánh giá tự động: Auto-Evaluation<br>- So sánh câu trả lời với đáp án mẫu: Ground truth<br>- Tính toán Faithfulness, Relevance, Citation Accuracy]:::ragNode
    
    HitlRoute --> Step4
    Step4 --> Output[Đầu ra JSON khớp cấu trúc: Schema]:::clientNode

    class Query,Output,HitlRoute clientNode;
    class Step1 checkNode;
    class Dec1,Dec2 checkNode;
    class Refuse errorNode;
    class AskClarify clientNode;
    class Step2,Step3,Step4 ragNode;
```
