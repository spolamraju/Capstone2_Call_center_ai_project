# 🎧 Multi-Agent Call Center AI Tool (Amazon 2023/EC2 )

This project is a real-time AI dashboard designed for call center agents. It uses a **Multi-Agent Orchestration** architecture to triage customer queries and provide specialized guidance.

---
# 🤖 Agent Roster

This document defines the specialized agents used in the transcript processing pipeline.


| Agent Name | Role | Primary Responsibility | Output / KPI |
| :--- | :--- | :--- | :--- |
| **Sentiment Agent** | The Emotional Filter | Analyzes transcript to determine customer mood. | Label (Pos/Neu/Neg) & Score (1–10) |
| **Metrics Agent** | The Data Extractor | Scans text for specific business KPIs. | Main Issue, Resolution Status, Keywords |
| **Summarizer Agent** | The Executive Scribe | Condenses the conversation for management. | Concise 2-sentence summary |
| **Router** | The Traffic Controller | Directs flow based on inquiry type. | Technical vs. Billing path assignment |

## Workflow Overview
1. **Routing**: The `Router` identifies the inquiry type.
2. **Analysis**: The `Sentiment` and `Metrics` agents process the content.
3. **Synthesis**: The `Summarizer` generates the final brief for CRM logging.

## Sequence Diagram
<img width="1408" height="768" alt="image" src="https://github.com/user-attachments/assets/084dfca4-ab57-413e-98a9-51ae59145e32" />

## Architecture Diagram
<img width="1408" height="768" alt="image" src="https://github.com/user-attachments/assets/58f5423e-3175-440f-9d86-c8ea58c49ec3" />


