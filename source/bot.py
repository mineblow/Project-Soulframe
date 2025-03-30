# bot.py
import os
import sys
from datetime import datetime

from config import (
    MODEL_SOURCE, ENABLE_MEMORY, ENABLE_JOURNAL,
    REFLECT_MODE, SYSTEM_MODE, JOURNAL_MODE
)
from llm import get_response
from reflector import build_prompt
from security import Guardrail
from memory import Memory
from journal import Journal

# ---------- [🌱 Init] ----------
guard = Guardrail()
memory = Memory() if ENABLE_MEMORY else None
journal = Journal() if ENABLE_JOURNAL else None

print("🧠 Soulframe Bot\n(Type '/reset' to restart or Ctrl+C to quit)\n")

# Determine session mode for journal naming
if ENABLE_JOURNAL:
    mode = "reflect" if REFLECT_MODE else "system" if SYSTEM_MODE else "journal"
    journal.set_mode(mode)

# ---------- [💬 Main Loop] ----------
try:
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "/reset":
            print("🔄 Session reset.\n")
            guard.reset()
            if memory:
                memory.reset()
            if journal:
                journal.new_session()
            continue

        if not user_input:
            continue

        guard.increment()

        # ⛔ Safety interrupt
        if guard.should_interrupt():
            guard.enforce_interrupt()

        # ⚓ Truth anchor
        if guard.should_anchor():
            anchor = guard.insert_truth_anchor()
            print(f"\n{anchor}\n")
            if journal:
                journal.append("system", anchor)

        # 🧠 Build prompt
        context = memory.get_context() if memory else None
        prompt = build_prompt(user_input, context)

        # 🤖 Get model output
        raw_response = get_response(prompt)
        response = raw_response.strip()

        # 💬 Reflective tone if enabled
        if REFLECT_MODE:
            response = build_prompt(response, None, bot=True)

        print(f"\nSoulframe: {response}\n")

        if memory:
            memory.append(user_input, response)
        if journal:
            journal.append("user", user_input)
            journal.append("bot", response)

except KeyboardInterrupt:
    print("\n👋 Goodbye.")
    if journal:
        journal.close()
    sys.exit(0)
