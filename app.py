import streamlit as st
import os
from io import BytesIO
from streamlit_mic_recorder import mic_recorder
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_community.callbacks.manager import get_openai_callback
from openai import OpenAI

# --- 1. SETUP ---
st.set_page_config(page_title="AI Call Supervisor Pro", layout="wide")
os.environ["OPENAI_API_KEY"] ="<your key>" 
client = OpenAI()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0
    st.session_state.total_cost = 0.0

# --- 2. MULTI-AGENT ARCHITECTURE ---
class CallState(dict):
    transcript: str
    sentiment_label: str  # Positive, Neutral, Negative
    sentiment_score: int    # 1 to 10
    metrics: str
    summary: str

def sentiment_agent(state: CallState):
    """Analyzes mood and provides a numerical score."""
    prompt = f"""Analyze the sentiment of this transcript. 
    Return ONLY in this format: Label | Score
    Example: Positive | 9
    Example: Negative | 2
    
    Transcript: {state['transcript']}"""
    
    res = llm.invoke(prompt).content.strip()
    label, score = res.split("|")
    return {
        "sentiment_label": label.strip(), 
        "sentiment_score": int(score.strip())
    }

def metrics_agent(state: CallState):
    res = llm.invoke(f"Extract 'Main Issue' and 'Resolution': {state['transcript']}")
    return {"metrics": res.content}

def summarizer_agent(state: CallState):
    res = llm.invoke(f"Summarize this call in 2 sentences: {state['transcript']}")
    return {"summary": res.content}

workflow = StateGraph(CallState)
workflow.add_node("sentiment", sentiment_agent)
workflow.add_node("metrics", metrics_agent)
workflow.add_node("summarizer", summarizer_agent)
workflow.set_entry_point("sentiment")
workflow.add_edge("sentiment", "metrics")
workflow.add_edge("metrics", "summarizer")
workflow.add_edge("summarizer", END)
app_graph = workflow.compile()

# --- 3. UI HELPERS ---
def get_sentiment_emoji(score):
    if score >= 8: return "😁", "green", "Excellent"
    if score >= 6: return "🙂", "blue", "Good"
    if score >= 4: return "😐", "orange", "Neutral"
    if score >= 2: return "😟", "red", "Poor"
    return "🤬", "red", "Critical"

# --- 4. UI LAYOUT ---
st.title("🎙️ AI Call Supervisor Pro")

# Sidebar: Usage
with st.sidebar:
    st.header("💳 Session Usage")
    st.metric("Total Tokens", f"{st.session_state.total_tokens:,}")
    st.metric("Total Cost", f"${st.session_state.total_cost:.4f}")

tab1, tab2 = st.tabs(["🔴 Live Audio", "📂 Upload Transcript"])
input_text = ""

with tab1:
    audio = mic_recorder(start_prompt="⏺️ Record Live", stop_prompt="⏹️ Analyze", key='recorder')
    if audio:
        audio_bio = BytesIO(audio['bytes']); audio_bio.name = "audio.wav"
        transcript_res = client.audio.transcriptions.create(model="whisper-1", file=audio_bio)
        input_text = transcript_res.text

with tab2:
    uploaded_file = st.file_uploader("Upload .json transcript", type="json")
    if uploaded_file:
        input_text = uploaded_file.getvalue().decode("utf-8")

if input_text:
    with st.spinner("Analyzing..."):
        with get_openai_callback() as cb:
            result = app_graph.invoke({"transcript": input_text})
            st.session_state.total_tokens += cb.total_tokens
            st.session_state.total_cost += cb.total_cost

        # --- RESULTS DISPLAY ---
        st.divider()
        col_emo, col_txt = st.columns([1, 3])
        
        emoji, color, status = get_sentiment_emoji(result['sentiment_score'])
        
        with col_emo:
            st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{emoji}</h1>", unsafe_allow_html=True)
            st.metric("Sentiment Score", f"{result['sentiment_score']}/10")
            st.markdown(f"<p style='text-align: center; color: {color}; font-weight: bold;'>{status}</p>", unsafe_allow_html=True)

        with col_txt:
            st.subheader("📝 Summary")
            st.success(result['summary'])
            st.subheader("📊 Metrics")
            st.write(result['metrics'])
            
            with st.expander("View Full Transcript"):
                st.text(input_text)
