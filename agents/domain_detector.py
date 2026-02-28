from llm_engine import call_llm

def detect_domain(user_input):

    prompt = f"""
Classify the following question into ONE domain only:
- Career
- Finance
- Education
- Business
- Personal
- Technology

Question:
{user_input}

Return only the domain name.
"""

    result = call_llm(
        model="groq/compound-mini",
        prompt=prompt,
        max_tokens=10,
        temperature=0,
        fallback_model="moonshotai/kimi-k2-instruct"
    )

    if not result:
        return "Unknown"

    return result.strip()