# 🎧 Multi-Agent Call Center AI Tool (RHEL/EC2 Deployment)

This project is a real-time AI dashboard designed for call center agents. It uses a **Multi-Agent Orchestration** architecture to triage customer queries and provide specialized guidance.

---

## 🏗️ System Architecture

The tool is built using a **Modular Monolith** pattern on RHEL:

- **Frontend/Backend:** Streamlit (Python)
- **Orchestration:** LangGraph (Stateful Multi-Agent Graph)
- **Intelligence:** Google Gemini 1.5 Flash
- **Deployment:** AWS EC2 (RHEL 8/9)

### Component Breakdown
1. **Router Agent:** Analyzes transcript intent (Technical vs. Billing).
2. **Technical Agent:** Provides hardware/software troubleshooting.
3. **Billing Agent:** Handles policy, refunds, and accounting inquiries.
4. **State Management:** Uses Streamlit Session State to persist call logs.

---

## 📂 Source Code

### 1. Requirements (`requirements.txt`)
```text
streamlit
langgraph
langchain-google-genai
python-dotenv
