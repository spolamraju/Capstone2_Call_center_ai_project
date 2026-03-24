# 🎧 Multi-Agent Call Center AI Tool (Amazon 2023/EC2 )

This project is a real-time AI dashboard designed for call center agents. It uses a **Multi-Agent Orchestration** architecture to triage customer queries and provide specialized guidance.


http://ec2-18-223-116-71.us-east-2.compute.amazonaws.com:8501/

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

## 🏗️ AI Call Supervisor: Professional Component Stack

| Layer | Component | Role & Functionality | Provider / Source |
| :--- | :--- | :--- | :--- |
| **Infrastructure** | AWS EC2 (RHEL 9) | Host OS providing compute, security groups, and networking. | [Amazon Web Services](https://aws.amazon.com) |
| **Web Server / UI** | Streamlit | Turns Python scripts into an interactive dashboard with tabs and metrics. | [Streamlit](https://streamlit.io) |
| **Audio Processing** | FFmpeg | System library to process and encode audio bytes for API transmission. | RHEL Repository |
| **Transcription** | OpenAI Whisper-1 | The "Ears"; converts raw audio into high-accuracy text. | [OpenAI API](https://openai.com) |
| **Orchestration** | LangGraph | The "Logic Flow"; manages state and sequence between AI agents. | [LangChain](https://www.langchain.com) |
| **Intelligence (LLM)** | GPT-4o-mini | The "Brain"; handles sentiment, KPI extraction, and summarization. | [OpenAI API](https://openai.com) |
| **Agent Logic** | Custom Python Agents | Three specialized functions: Sentiment, Metrics, and Summarizer. | Custom Code |
| **Usage Tracking** | LangChain Callbacks | Intercepts metadata to calculate real-time token counts and costs. | LangChain Community |
| **Frontend Audio** | Mic Recorder | React component bridging the browser mic to the Streamlit backend. | [streamlit-mic-recorder](https://github.com) |
| **Data Structure** | Pandas | Organizes agent outputs into structured tables and logs. | Open Source |

