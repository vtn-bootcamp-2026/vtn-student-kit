# Sơ đồ quy trình thực thi (Execution Workflow Diagram)

Dưới đây là sơ đồ Mermaid thể hiện quy trình 4 bước của Agent Skill được định nghĩa trong [SKILL.md](file:///c:/Users/DELL/Documents/4.%20Presentations%20&%20Training/VTN/vtn-student-kit/03-practices/day-02/session-03-ai-agent-design/outputs/contract-term-extractor/SKILL.md).

```mermaid
flowchart TD
    Start([Kích hoạt Trigger]) --> Step1[Bước 1: Tiếp nhận & Tiền xử lý]
    
    subgraph Step1Sub [Chi tiết Bước 1 - Intake]
        Step1 --> RunIntake[Chạy: ./scripts/intake.py]
        RunIntake --> CheckIntake{Kiểm tra: File tồn tại, không rỗng,<br>độ dài tối thiểu, tỷ lệ lỗi OCR}
        CheckIntake -- Lỗi/Không đạt --> HITL1[Báo cáo & Ghi log - HITL]
        HITL1 --> EndProcess([Kết thúc / Cần con người xử lý])
    end

    CheckIntake -- Đạt --> Step2[Bước 2: Trích xuất thông tin - Extraction]

    subgraph Step2Sub [Chi tiết Bước 2 - Extraction]
        Step2 --> ExtractData[Trích xuất dựa trên:<br>./schemas/contract-term.schema.json]
        ExtractData --> CheckKB[Đối chiếu với kho mẫu:<br>./kb/clause-library.md]
        CheckKB --> GenerateJSON[Tạo JSON kết quả với source_evidence nguyên văn]
    end

    GenerateJSON --> Step3[Bước 3: Tự kiểm soát chất lượng - Self-check]

    subgraph Step3Sub [Chi tiết Bước 3 - Self-check]
        Step3 --> RunValidator[Chạy: ./scripts/validator.py]
        RunValidator --> ValidateFuzzy{Thực hiện:<br>1. Fuzzy match bằng chứng nguồn<br>2. Hiệu chỉnh confidence<br>3. Kiểm tra các trường bắt buộc}
        ValidateFuzzy --> CheckConfidence{Có lỗi hoặc confidence < 0.7?}
        CheckConfidence -- Đúng --> SetReviewFlag[Gán needs_human_review = true]
        CheckConfidence -- Sai --> Step4[Bước 4: Phát hiện cờ đỏ & Định tuyến]
    end

    SetReviewFlag --> Step4

    subgraph Step4Sub [Chi tiết Bước 4 - Routing]
        Step4 --> RunRouter[Chạy: ./scripts/router.py]
        RunRouter --> MatchRules[Đối chiếu quy tắc rủi ro:<br>./kb/red-flag-rules.md]
        MatchRules --> ActionRouter[Thực hiện:<br>1. Ghi nhật ký CSV<br>2. Xuất báo cáo cờ đỏ<br>3. Định tuyến ca khó sang HITL]
    end

    ActionRouter --> End([Hoàn thành quy trình])
```
