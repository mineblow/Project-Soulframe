import os
from dotenv import load_dotenv

# ---------- [📄 Load .env] ----------
load_dotenv()

# ---------- [🧠 Model Selection] ----------
MODEL_SOURCE = os.getenv("MODEL_SOURCE", "local").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_PATH = os.getenv("LLM_PATH", "llama3")  # Used if MODEL_SOURCE=local

# ---------- [🧠 Memory Settings] ----------
ENABLE_MEMORY = os.getenv("ENABLE_MEMORY", "false").lower() == "true"
MEMORY_LIMIT = int(os.getenv("MEMORY_LIMIT", 20))  # short-term messages retained

# ---------- [📓 Journaling] ----------
ENABLE_JOURNAL = os.getenv("ENABLE_JOURNAL", "false").lower() == "true"
JOURNAL_DIR = os.getenv("JOURNAL_DIR", "./logs")

# ---------- [🛑 Guardrails] ----------
INTERRUPT_INTERVAL = int(os.getenv("INTERRUPT_INTERVAL", 20))  # enforced ≤ 25
TRUTH_INTERVAL = int(os.getenv("TRUTH_INTERVAL", 50))          # flexible, but required

# Hard cap on how far user can push interrupt delay
if INTERRUPT_INTERVAL > 25:
    raise ValueError("INTERRUPT_INTERVAL cannot exceed 25. Safety limit enforced.")

# ---------- [📜 Mode Flags] ----------
JOURNAL_MODE = os.getenv("JOURNAL_MODE", "false").lower() == "true"
REFLECT_MODE = os.getenv("REFLECT_MODE", "false").lower() == "true"
SYSTEM_MODE = os.getenv("SYSTEM_MODE", "false").lower() == "true"

# ---------- [🧪 Debug Diagnostics] ----------
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
if DEBUG:
    print("🔧 [CONFIG DEBUG]")
    print(f"MODEL_SOURCE={MODEL_SOURCE}")
    print(f"OPENAI_API_KEY={'set' if OPENAI_API_KEY else 'unset'}")
    print(f"LLM_PATH={LLM_PATH}")
    print(f"MEMORY_ENABLED={ENABLE_MEMORY} (limit: {MEMORY_LIMIT})")
    print(f"JOURNAL_ENABLED={ENABLE_JOURNAL} => {JOURNAL_DIR}")
    print(f"INTERRUPT_INTERVAL={INTERRUPT_INTERVAL}")
    print(f"TRUTH_INTERVAL={TRUTH_INTERVAL}")
    print(f"Modes => journal={JOURNAL_MODE}, reflect={REFLECT_MODE}, system={SYSTEM_MODE}")
