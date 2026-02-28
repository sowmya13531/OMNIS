from llm_engine import call_llm
import re


def generate_report(user_input, domain, plan):

    prompt = f"""
You are a professional strategic advisor.

Domain: {domain}

User Question:
{user_input}

Planner Analysis:
{plan}

IMPORTANT INSTRUCTIONS:
- Do NOT show your reasoning process.
- Do NOT include <think> tags.
- Do NOT explain how you arrived at the answer.
- Only provide the final polished recommendation.
- Do NOT include internal reasoning or chain-of-thought.
- Provide only the final professional report.

Generate a structured professional report with:

Return in this format:

## Executive Summary
...

## Key Tradeoffs
...

## Recommendation
...

## Risk Considerations
...

## Confidence Level (0-100%)
...

Be concise, clear, and practical.
"""

    result = call_llm(
        model="qwen/qwen3-32b",
        prompt=prompt,
        max_tokens=350,
        temperature=0.4,
        fallback_model="moonshotai/kimi-k2-instruct"
    )

    if not result:
        return "Final report generation failed."

    # Remove accidental <think> blocks if model leaks them
    result = re.sub(r"<think>.*?</think>", "", result, flags=re.DOTALL)

    return result.strip()