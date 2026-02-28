import os
import requests
from dotenv import load_dotenv

# ==============================
# Load Environment Variables
# ==============================
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# ==============================
# Configuration
# ==============================
URL = "https://api.groq.com/openai/v1/chat/completions"

CALL_COUNT = 0
MAX_CALLS = 15   # Safety limit per program run

DEBUG = True     # Set False in production


# ==============================
# Core LLM Call Function
# ==============================
def call_llm(model, prompt, max_tokens=200, temperature=0.0, fallback_model=None):
    global CALL_COUNT

    if CALL_COUNT >= MAX_CALLS:
        raise Exception("🚨 Safety limit reached: Too many LLM calls.")

    CALL_COUNT += 1

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    try:
        response = requests.post(URL, headers=headers, json=data, timeout=30)

        if response.status_code != 200:
            print(f"⚠️ Error from model {model}: {response.text}")

            # Try fallback model if provided
            if fallback_model:
                print(f"🔁 Switching to fallback model: {fallback_model}")
                return call_llm(
                    model=fallback_model,
                    prompt=prompt,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
            return None

        result = response.json()
        content = result["choices"][0]["message"]["content"].strip()

        if DEBUG:
            print(f"\n🧠 Model Used: {model}")
            print(f"📊 Call Count: {CALL_COUNT}/{MAX_CALLS}\n")

        return content

    except requests.exceptions.Timeout:
        print("⏳ Request timed out.")
        return None

    except Exception as e:
        print("❌ Unexpected Error:", str(e))
        return None