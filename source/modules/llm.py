# llm.py

import subprocess
import openai
from config import MODEL_SOURCE, OPENAI_API_KEY, LLM_PATH

def get_response(prompt: str) -> str:
    if MODEL_SOURCE == "openai":
        return call_openai(prompt)
    elif MODEL_SOURCE == "local":
        return call_ollama(prompt)
    else:
        return "[ERROR] Unknown MODEL_SOURCE. Must be 'openai' or 'local'."

def call_openai(prompt: str) -> str:
    if not OPENAI_API_KEY:
        return "[ERROR] OPENAI_API_KEY not set in .env"

    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Soulframe, a reflective and constrained AI mirror."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] OpenAI API call failed: {e}"

def call_ollama(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", LLM_PATH],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )

        if result.returncode != 0:
            return f"[ERROR] ollama failed: {result.stderr.decode()}"

        return result.stdout.decode().strip()
    except FileNotFoundError:
        return "[ERROR] ollama CLI not found. Make sure it's installed and in PATH."
    except subprocess.TimeoutExpired:
        return "[ERROR] ollama command timed out."

