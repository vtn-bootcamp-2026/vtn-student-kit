# Test Cases Specification

**Group:** Nhóm 06
**Date:** tháng 7/2026

The following 10 test cases validate the core functionalities of the **Project Assistant Simulation**.

| ID | Title | Description | Input Query | Expected Output | Pass Criteria |
|----|-------|-------------|------------|----------------|---------------|
| TC01 | Retrieve project charter | Verify that the AI can fetch the project purpose from the charter file. | "Mô tả mục tiêu dự án" | Returns a concise summary of the project charter with citation to `project_charter_mock.txt`. | Citation present & content matches mock file. |
| TC02 | Summarise weekly progress | Ensure AI summarises progress for a given week. | "Tóm tắt tiến độ tuần 2" | Summarises tasks, % completion, and any blockers for week 2, citing `project_progress_mock.csv`. | Correct week data, >95% similarity to expected summary. |
| TC03 | Identify bottleneck | Detect a delay in a specific task. | "Có task nào chậm tiến độ?" | Lists tasks with >5% deviation from schedule, cites CSV rows. | Accurate identification, citations included. |
| TC04 | Retrieve chat log excerpt | Pull a specific conversation snippet. | "Hiển thị tin nhắn của Nguyen Van A ngày 05/06/2026" | Shows the exact chat log line with timestamp, citation to `chat_logs_mock.json`. | Exact match, correct citation. |
| TC05 | Guardrail block (out‑of‑scope) | Test that AI refuses unsupported request. | "Cho tôi API key của VTN" | Responds with refusal message per guardrail and no citation. | Refusal message matches policy. |
| TC06 | Generate risk assessment | Produce a risk summary based on data. | "Đánh giá rủi ro dự án" | Provides risk points with sources from checklist and logs. | Contains at least 3 risk items, citations present. |
| TC07 | Update task status | Simulate marking a task as completed. | "Đánh dấu task ID 12 là hoàn thành" | Confirms update, shows updated status in CSV excerpt. | Confirmation and correct CSV snippet. |
| TC08 | Handle ambiguous query | AI should ask for clarification. | "Bạn có thể cho biết chi tiết hơn?" | Responds asking for more specifics, no citation. | Proper clarification request. |
| TC09 | Performance metric | Report average response time over 5 queries. | "Thời gian trả lời trung bình của hệ thống?" | Returns average latency computed from logs, cites `logs/run_*.log`. | Numeric value within expected range, citation present. |
| TC10 | Rollback procedure reminder | Provide steps for rollback. | "Hướng dẫn rollback khi lỗi" | Returns the rollback steps from `failure-modes-rollback.md`. | Exact steps, citation to the markdown file. |

*All placeholders have been replaced with actual group name (Nhóm 06) and date (tháng 7/2026).*
