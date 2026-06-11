# Logical Workflow

> **Group:** Nhóm 06
> **Date:** tháng 7/2026

```mermaid
flowchart TD
    A[Start] --> B[User submits request]
    B --> C{AI processes}
    C -->|Confidence high| D[Auto‑generate answer]
    D --> E[Present to user]
    C -->|Confidence low| F[Human‑in‑the‑loop review]
    F --> G[Human edits/approves]
    G --> E
    E --> H[End]
```

**Explanation**:
- The AI first attempts to answer the query.
- If the confidence score is above the threshold, the answer is returned directly.
- Otherwise, the request is routed to a human reviewer (PM) who validates, edits, and approves.
- All interactions are logged for audit purposes.
