import streamlit as st
import requests

st.set_page_config(
    page_title="Earnings Call Analyzer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Earnings Call Analyzer")
st.markdown("*AI-powered earnings call analysis*")

with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    **What it extracts:**
    - 📝 Summary
    - 📊 Sentiment (Positive/Neutral/Negative)
    - 💡 Key Insights (Revenue, Growth, Risks)
    """)
    
    if st.button("📋 Load Sample"):
        try:
            with open("data/data/sample_transcript.txt", "r") as f:
                st.session_state["sample_text"] = f.read()
            st.success("✅ Sample loaded!")
        except:
            st.error("⚠️ Sample file not found")

text = st.text_area(
    "📄 Paste earnings call transcript:",
    height=250,
    value=st.session_state.get("sample_text", "")
)

if st.button("🔍 Analyze", type="primary"):
    if text:
        with st.spinner("🧠 Analyzing earnings call..."):
            try:
                response = requests.post(
                    "http://localhost:8000/analyze/",
                    data={"text": text},
                    timeout=300
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.subheader("📝 Summary")
                    st.info(data.get("summary", "N/A"))
                    
                    st.subheader("📊 Sentiment")
                    sentiment = data.get("sentiment", "Neutral")
                    if "Positive" in sentiment:
                        st.success(f"✅ {sentiment}")
                    elif "Negative" in sentiment:
                        st.error(f"❌ {sentiment}")
                    else:
                        st.warning(f"⚖️ {sentiment}")
                    
                    st.subheader("💡 Key Insights")
                    st.info(data.get("insights", "N/A"))
                    
                    # Download
                    export = f"""=== EARNINGS CALL ANALYSIS ===

Summary: {data.get('summary', 'N/A')}
Sentiment: {data.get('sentiment', 'N/A')}
Insights: {data.get('insights', 'N/A')}
"""
                    st.download_button(
                        label="📥 Download Analysis",
                        data=export,
                        file_name="earnings_analysis.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"Error: {response.status_code}")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("⚠️ Please paste a transcript")