from llm_engine import call_llm

def plan_decision(user_input, domain):

    prompt = f"""
You are a strategic decision planner.

Domain: {domain}

User Question:
{user_input}

Break this into:
Provide:
1. Key decision factors
2. Comparative strengths/weaknesses
3. Risk assessment
4. Long-term projection
5. Confidence level (0–100%)

Be structured and analytical.
"""

    result = call_llm(
        model="moonshotai/kimi-k2-instruct",
        prompt=prompt,
        max_tokens=300,
        temperature=0.3,
        fallback_model="qwen/qwen3-32b"
    )

    if not result:
        return "Planning failed."

    return result