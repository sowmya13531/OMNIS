# 🧠 OMNIS — Multi-Agent Decision Intelligence System

A structured AI reasoning system that transforms raw user questions into strategic, multi-layered decision analysis using a multi-agent architecture.
OMNIS leverages LLMs via the Groq API, orchestrating multiple open-source *models—groq/compound-mini*, *moonshotai/kimi-k2-instruct*, and *qwen/qwen3-32b*—to deliver multi-domain, structured, and professional decision-making insights.
## 🌍 What is OMNIS?

OMNIS (Latin for “all”) is an AI-powered decision intelligence prototype designed to simulate structured strategic thinking.
Instead of generating simple chat responses, OMNIS:
- Detects the decision domain
- Builds a structured analysis plan
- Generates a detailed reasoning repor
- Critically evaluates its own reasoning
- Produces refined executive-level output
It mimics how consulting firms and strategic advisors break down complex decisions.

## 🎯 Purpose of the Project
The goal of OMNIS is to:

- Demonstrate applied AI system architecture (not just API usage)
- Show multi-agent orchestration in production
- Implement structured reasoning workflows
- Integrate model calls with safety constraints
- Deploy a working decision intelligence interface
  
* This project was built to explore:
- AI reasoning pipelines
- Agent-based decomposition
- Decision analysis modeling
- Production-ready LLM integration
- Streamlit-based deployment

# Demo
![App Demo](omnis_demo/Screenshot%20(212).png)
![App Demo](omnis_demo/Screenshot%20(213).png)
![App Demo](omnis_demo/Screenshot%20(214).png)
![App Demo](omnis_demo/Screenshot%20(215).png)
![App Demo](omnis_demo/Screenshot%20(216).png)
![App Demo](omnis_demo/Screenshot%20(217).png)
![App Demo](omnis_demo/Screenshot%20(218).png)
![App Demo](omnis_demo/Screenshot%20(219).png)
![App Demo](omnis_demo/Screenshot%20(220).png)
![App Demo](omnis_demo/Screenshot%20(221).png)
![App Demo](omnis_demo/Screenshot%20(222).png)
![App Demo](omnis_demo/Screenshot%20(223).png)
![App Demo](omnis_demo/Screenshot%20(224).png)
![App Demo](omnis_demo/Screenshot%20(225).png)
![App Demo](omnis_demo/Screenshot%20(226).png)
![App Demo](omnis_demo/Screenshot%20(227).png)


## ⚙️ Technologies & Models Used

- Programming & Frameworks
- Python 3.11+
- Streamlit — for interactive web interface
- Requests — API calls to LLMs
- dotenv — environment variable management
- Virtual environment (venv) for dependency isolation

## AI Models (Free / Open-Source, accessed via Groq API)
OMNIS uses a multi-agent, multi-model orchestration system:
| Agent               | Model                         | Purpose                                                                  |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------ |
| Domain Detector     | `groq/compound-mini`          | Detects the decision domain (e.g., Career, Finance, Startup, Tech Stack) |
| Planning Agent      | `moonshotai/kimi-k2-instruct` | Builds structured analysis and key decision factors                      |
| Final Synthesis     | `qwen/qwen3-32b`              | Generates a detailed, executive-level decision report                    |
| Fallback / Critique | `moonshotai/kimi-k2-instruct` | Optional refinement and self-critique of outputs                         |

## ⭐ What Makes OMNIS Special?
Most AI apps are simple “prompt → response” wrappers.
*OMNIS is different*
1️⃣ Multi-Agent Architecture
The system separates responsibilities into agents:
- Domain Agent → Detects decision context (Career, Finance, Startup, etc.)
- Planning Agent → Breaks down key decision factors
- Critic Agent → Evaluates weaknesses & improves reasoning
- Final Synthesizer → Produces structured executive output
This modular design mirrors real-world decision systems.

2️⃣ Structured Reasoning Output
OMNIS produces:
- Decision framing
- Key factors
- Comparative analysis
- Risk assessment
- Strategic recommendation
- Self-critique and improvement
This goes beyond casual chat — it delivers decision intelligence.

3️⃣ LLM Safety Control
The system includes:
- API call counter limits
- Free-tier protection
- Safety stop to prevent runaway LLM calls
This demonstrates awareness of production cost control.

4️⃣ Model Orchestration via Groq API
OMNIS integrates large language models using the Groq API.
Groq provides:
- High-speed inference
- Low-latency model execution
- Access to instruction-tuned LLMs
The system routes structured prompts to Groq-hosted models and retrieves responses for agent processing.

🏗 System Architecture

User Input
↓
Streamlit Interface
↓
Domain Detection Agent
↓
Planning Agent
↓
Critic Agent
↓
Final Structured Output
↓
Rendered UI

Each agent operates independently but passes structured outputs forward.


### 🧠 How Groq API is Used (Conceptually)

OMNIS does not directly generate responses in one step.
Instead:
- Each agent constructs a structured prompt.
- The prompt is sent to Groq’s hosted model endpoint.
- The model returns structured reasoning text.
- The output is passed to the next agent.
- A call counter tracks API usage.
- If limit is exceeded → system halts for safety.
This simulates an orchestrated reasoning pipeline.

## ⚙️ How the System Works (Step-by-Step)

- User enters a decision question in the Streamlit UI.
- Domain Agent classifies the decision type.
- Planning Agent generates key analysis dimensions.
- Critic Agent reviews the logic and improves it.
- Final structured response is rendered in interface.
- Call count is displayed for transparency.

## 💻 How to Run Locally
1️⃣ Clone Repository
```
git clone https://github.com/sowmya13531/OMNIS.git
cd OMNIS
```

2️⃣ Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   (Mac/Linux)
venv\Scripts\activate      (Windows)
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Add API Key

Create a .env file:

```
GROQ_API_KEY=your_api_key_here
```

5️⃣ Run Application
*streamlit run app.py*

The interface will open in your browser.



# 👩‍💻 Author
**Sowmya Kanithi**
Built as an exploration into decision intelligence systems and multi-agent AI architecture.
