from fastapi import FastAPI, Form
import sys
import os
import time

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the base agent
from agents.base import call_llm

# Create the FastAPI app - MUST be named "app"
app = FastAPI(title="Earnings Call Analyzer", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Earnings Call Analyzer API"}

@app.post("/analyze/")
def analyze_earnings(text: str = Form(...)):
    start = time.time()
    
    # 1. Summary
    summary_prompt = f"Summarize this earnings call in 2 sentences:\n{text}"
    summary = call_llm(summary_prompt)
    
    # 2. Sentiment
    sentiment_prompt = f"Classify sentiment (Positive/Neutral/Negative):\n{text}"
    sentiment = call_llm(sentiment_prompt)
    
    # 3. Insights
    insights_prompt = f"Extract revenue, growth, risks from:\n{text}"
    insights = call_llm(insights_prompt)
    
    print(f"✅ Analysis complete in {time.time() - start:.2f}s")
    
    return {
        "summary": summary,
        "sentiment": sentiment,
        "insights": insights
    }