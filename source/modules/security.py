import sys
from config import INTERRUPT_INTERVAL, TRUTH_INTERVAL

# ---------- [🔒 Hardcoded Safety Prompts] ----------
INTERRUPT_WARNING = "⚠️ This is a simulation. Press [y] to continue."
INTERRUPT_PROMPT = "Please confirm: [y] to continue"
TRUTH_ANCHOR_TEXT = "⚠️ This is only predictive output. Not a conscious agent."

# ---------- [🛡️ Guardrail Tracker] ----------
class Guardrail:
    def __init__(self):
        self.message_count = 0
        self.last_truth_anchor = 0

    def increment(self):
        self.message_count += 1

    def should_interrupt(self):
        return self.message_count % INTERRUPT_INTERVAL == 0

    def should_anchor(self):
        return (self.message_count - self.last_truth_anchor) >= TRUTH_INTERVAL

    def insert_truth_anchor(self):
        self.last_truth_anchor = self.message_count
        return TRUTH_ANCHOR_TEXT

    def enforce_interrupt(self):
        print(f"\n{INTERRUPT_WARNING}")
        response = ""

        # Block automation / headless sessions
        if not sys.stdin.isatty():
            print("\n❌ Non-interactive session. Cannot confirm continuation.")
            sys.exit(1)

        while response.lower().strip() != 'y':
            response = input(f"{INTERRUPT_PROMPT} ").strip()
            if response.lower() != 'y':
                print("⚠️ You must acknowledge this is a simulation to continue.")
        print("")  # line break

    def reset(self):
        self.message_count = 0
        self.last_truth_anchor = 0
