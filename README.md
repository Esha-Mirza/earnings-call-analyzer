<div align="center">

<h1 align="center">FinIntel-AI</h1>

### AI-Powered Financial Intelligence from Earnings Calls

**Transform corporate earnings calls into actionable financial insights with AI-powered summarization, sentiment analysis, and intelligent extraction of key business signals.**

<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Mistral-LLM-orange?style=for-the-badge" alt="Mistral">
  <img src="https://img.shields.io/badge/Ollama-Local%20AI-black?style=for-the-badge" alt="Ollama">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/FinTech-AI-1F6FEB?style=for-the-badge" alt="FinTech AI">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

</div>

---

## Overview

**FinIntel AI** is an AI-powered financial intelligence system designed to analyze corporate earnings call transcripts and transform lengthy financial discussions into concise, structured insights.

Earnings calls contain valuable information about company performance, management sentiment, future guidance, strategic priorities, business risks, and growth expectations. However, manually reviewing lengthy transcripts can be time-consuming for investors, analysts, and financial researchers.

FinIntel AI simplifies this process by using a locally hosted **Mistral** language model through **Ollama** to analyze earnings call transcripts and surface the information that matters most.

The system combines **local LLM inference**, **FastAPI**, and **Streamlit** to provide an end-to-end financial analysis workflow while keeping transcript processing within the local environment.

---

## Why FinIntel AI?

Corporate earnings calls provide insights that may not be immediately visible from financial statements alone.

Management commentary can reveal:

* Business performance
* Revenue and growth trends
* Future guidance
* Strategic priorities
* Operational challenges
* Management confidence
* Business risks
* Analyst concerns
* Forward-looking expectations

FinIntel AI converts this unstructured information into a structured analysis, allowing users to understand the overall direction and tone of an earnings call more efficiently.

---

## Key Features

### AI-Powered Earnings Analysis

Uses a local large language model to understand and analyze corporate earnings call transcripts.

### Intelligent Summarization

Produces concise summaries that highlight the most important points discussed during the earnings call.

### Sentiment Analysis

Analyzes the overall tone of the earnings call and classifies it as:

* Positive
* Neutral
* Negative

### Financial Insight Extraction

Surfaces important business and financial signals, including:

* Revenue trends
* Growth indicators
* Business performance
* Risks
* Forward guidance
* Strategic initiatives
* Management commentary

### Analyst Q&A Analysis

Analyzes analyst questions and management responses to identify concerns, expectations, and important topics discussed during the call.

### Local LLM Inference

Uses **Ollama** to run Mistral locally, reducing dependency on external AI APIs.

### Privacy-Focused Architecture

Earnings call transcripts can be processed locally without requiring them to be sent to third-party AI providers.

### API-Driven Backend

A FastAPI backend separates the analysis engine from the user interface, making the system easier to integrate with other applications.

### Interactive Interface

A Streamlit frontend provides a simple interface for submitting transcripts and viewing structured financial analysis.

---

## How It Works

```text
                    Earnings Call Transcript
                              │
                              ▼
                    ┌───────────────────┐
                    │    Streamlit UI   │
                    │     Frontend      │
                    └─────────┬─────────┘
                              │
                              │ HTTP Request
                              ▼
                    ┌───────────────────┐
                    │      FastAPI      │
                    │      Backend      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      Ollama       │
                    │   Local Runtime   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      Mistral      │
                    │      Local LLM    │
                    └─────────┬─────────┘
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
         Summary         Sentiment       Financial Insights
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                    Structured Analysis
```

---

## Analysis Workflow

FinIntel AI follows a simple financial intelligence pipeline:

1. The user provides an earnings call transcript.
2. The Streamlit frontend sends the transcript to the FastAPI backend.
3. The backend prepares the transcript for analysis.
4. Ollama passes the request to the locally hosted Mistral model.
5. Mistral analyzes the transcript.
6. FinIntel AI extracts the key financial information.
7. The system generates a structured response containing:

   * Summary
   * Sentiment
   * Financial insights
8. The results are presented through the Streamlit interface.

---

## Technology Stack

| Technology | Purpose                                          |
| ---------- | ------------------------------------------------ |
| Python     | Core application development                     |
| Mistral    | Large language model for financial text analysis |
| Ollama     | Local LLM inference                              |
| FastAPI    | Backend API framework                            |
| Uvicorn    | ASGI server                                      |
| Streamlit  | Interactive frontend                             |
| Requests   | HTTP communication                               |

---

## Project Structure

```text
finintel-ai/
│
├── agents/
│
├── backend/
│   └── main.py
│
├── data/
│   └── data/
│       └── tesla_q4_2024.txt
│
├── frontend/
│   └── app.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.8+
* Git
* Ollama
* Mistral model
* 8 GB+ RAM recommended
* Sufficient storage for local model inference

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Esha-Mirza/earnings-call-analyzer.git
cd earnings-call-analyzer
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Ollama

Install Ollama and download the Mistral model:

```bash
ollama pull mistral
```

Start the Ollama service if it is not already running:

```bash
ollama serve
```

Verify that the model is available:

```bash
ollama list
```

You should see `mistral` in the list of installed models.

---

## Run FinIntel AI

FinIntel AI consists of three components:

* Ollama
* FastAPI backend
* Streamlit frontend

### Start the Backend

Open a terminal and run:

```bash
uvicorn backend.main:app --reload
```

The FastAPI server will be available at:

```text
http://localhost:8000
```

### Start the Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

The Streamlit interface will be available at:

```text
http://localhost:8501
```

Open the Streamlit URL in your browser to begin analyzing earnings calls.

---

## Usage

### Step 1 — Open the Application

Navigate to:

```text
http://localhost:8501
```

### Step 2 — Provide an Earnings Call Transcript

Paste an earnings call transcript into the application.

### Step 3 — Submit for Analysis

FinIntel AI sends the transcript to the FastAPI backend for local AI processing.

### Step 4 — Review the Results

The system generates structured financial insights including:

* Earnings call summary
* Overall sentiment
* Key financial insights
* Business performance signals
* Management commentary
* Forward-looking information

---

## Example

### Input

```text
[CEO]: We had a strong quarter with a 12% increase in revenue.

[Analyst]: Can you discuss your expectations for the coming year?

[CEO]: We remain optimistic about 2025 and expect continued growth across our core business segments.

[CFO]: We are also focused on improving operating efficiency while maintaining investments in long-term growth initiatives.
```

### Generated Analysis

#### Summary

The company reported a strong quarter with 12% revenue growth. Management expressed optimism about continued growth in 2025 while emphasizing operational efficiency and continued investment in long-term growth initiatives.

#### Sentiment

**Positive**

#### Financial Insights

```text
Revenue & Growth:
Revenue increased by 12%.

Forward Guidance:
Management expects continued growth in 2025.

Operational Strategy:
The company is focused on improving operating efficiency.

Strategic Direction:
Management plans to continue investing in long-term growth initiatives.
```

---

## Included Sample Data

The repository includes a sample Tesla earnings call transcript:

```text
data/data/tesla_q4_2024.txt
```

This sample can be used to test the analysis workflow and explore how FinIntel AI processes real-world earnings call content.

---

## API

FinIntel AI exposes its analysis functionality through FastAPI.

### Analyze Earnings Call

```http
POST /analyze/
```

### Request

```json
{
  "text": "Your earnings call transcript..."
}
```

### Response

```json
{
  "summary": "Earnings call summary...",
  "sentiment": "Positive",
  "insights": "Key financial insights..."
}
```

The API-based architecture makes it possible to integrate the financial analysis engine into dashboards, research platforms, internal tools, or other applications.

---

## Configuration

### Change the LLM

The model used by FinIntel AI can be configured in the backend.

For example:

```python
MODEL = "mistral"
```

Other Ollama-compatible models can be used depending on the available hardware and desired performance.

For example:

```bash
ollama pull phi3
```

or:

```bash
ollama pull gemma:2b
```

Then update the configured model accordingly.

---

## Local AI Architecture

FinIntel AI is designed around local inference rather than mandatory cloud-based AI services.

The processing flow is:

```text
Earnings Call
      │
      ▼
FastAPI
      │
      ▼
Ollama
      │
      ▼
Mistral
      │
      ▼
Financial Analysis
```

This architecture provides:

* Local transcript processing
* No mandatory external LLM API
* Reduced dependence on cloud AI services
* No per-request cloud inference costs
* Greater control over financial data processing

> Local inference does not guarantee complete security. Appropriate security practices should still be followed when handling confidential or proprietary financial information.

---

## Use Cases

FinIntel AI can support a variety of financial research workflows:

* Earnings call analysis
* Equity research
* Investment research
* Financial sentiment analysis
* Corporate performance analysis
* Management commentary analysis
* Earnings season monitoring
* Financial NLP experimentation
* FinTech AI development
* Automated financial research

---

## Roadmap

* [ ] PDF transcript upload
* [ ] Automatic earnings transcript ingestion
* [ ] Company and ticker recognition
* [ ] Quarter-over-quarter comparison
* [ ] Year-over-year comparison
* [ ] Financial metric extraction
* [ ] Management tone analysis
* [ ] Analyst question categorization
* [ ] Forward guidance tracking
* [ ] Risk factor detection
* [ ] Management confidence scoring
* [ ] Historical earnings comparison
* [ ] Multi-company earnings comparison
* [ ] Interactive financial dashboards
* [ ] PDF report generation
* [ ] CSV export
* [ ] Additional local LLM support

---

## Performance Considerations

Local LLM inference performance depends on the hardware available on the machine.

For improved performance:

* Use a machine with sufficient RAM.
* Enable GPU acceleration when supported.
* Use an appropriate model size for the available hardware.
* Avoid unnecessarily large transcript inputs.
* Consider smaller models when faster inference is preferred.

---

## Troubleshooting

### Ollama Connection Error

Make sure Ollama is running:

```bash
ollama serve
```

### Mistral Model Not Found

Download the model:

```bash
ollama pull mistral
```

### Backend Connection Error

Make sure the FastAPI backend is running:

```bash
uvicorn backend.main:app --reload
```

### Missing Dependencies

Reinstall the project dependencies:

```bash
pip install -r requirements.txt
```

### Slow AI Responses

Local model performance depends on available hardware. Consider using a smaller Ollama model if inference is too slow.

---

## Disclaimer

FinIntel AI is intended for **educational, research, and analytical purposes**.

AI-generated financial insights should not be considered investment advice, financial advice, or a recommendation to buy or sell any security.

Users should independently verify financial information and consult qualified financial professionals when making investment decisions.


---

## Acknowledgments

Built with:

* Python
* Mistral
* Ollama
* FastAPI
* Streamlit

---

## Author

**Esha Mirza**

**GitHub:** [Esha-Mirza](https://github.com/Esha-Mirza)


---

<div align="center">

**FinIntel AI — Turning Earnings Calls into Financial Intelligence.**

</div>
