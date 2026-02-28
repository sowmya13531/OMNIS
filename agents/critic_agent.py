from llm_engine import call_llm
import re


def critique_and_improve(user_input, domain, plan, report):

    prompt = f"""
You are an expert AI critic reviewing a strategic recommendation.

Domain: {domain}

Original User Question:
{user_input}

Planner Analysis:
{plan}

Initial Recommendation Report:
{report}

Your task:

1. Identify weaknesses in the reasoning.
2. Detect missing risks or assumptions.
3. Check for bias or overconfidence.
4. Improve clarity and structure.

IMPORTANT:
- Do NOT explain your reasoning process.
- Do NOT use <think> tags.
- Output ONLY the improved final recommendation.


Return a refined, stronger version of the recommendation.
"""

    result = call_llm(
        model="moonshotai/kimi-k2-instruct",
        prompt=prompt,
        max_tokens=350,
        temperature=0.3,
        fallback_model="qwen/qwen3-32b"
    )

    if not result:
        return report  # fallback to original if critique fails

    # Remove accidental reasoning tags
    result = re.sub(r"<think>.*?</think>", "", result, flags=re.DOTALL)

    return result.strip()