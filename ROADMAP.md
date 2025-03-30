# 🛣️ Soulframe Bot — Roadmap

This document tracks all current and planned features for the Soulframe Bot project.

> ⚠️ **Reminder:** This bot is intentionally limited. It reflects consciousness—it does not possess it.

---

## ✅ Core Features (Implemented)

| Feature                                 | Status | Notes |
|-----------------------------------------|--------|-------|
| Modular design (config, security, etc.) | ✅     | Separated logic per module (`config.py`, `security.py`, `memory.py`) |
| Safety interrupt every X messages       | ✅     | Hardcoded unskippable prompt (`Press [y] to continue`) |
| Truth anchors every Y messages          | ✅     | Always inserted (unskippable); cannot be disabled |
| Configurable message intervals          | ✅     | Enforced via `.env` and `config.py`, hard-capped at 25 |
| Reflective output (Soulframe tone)      | ✅     | Controlled by `reflector.py`; toggled via `.env` |
| Short-term memory (toggleable)          | ✅     | `memory.py` implements context-limited recall |
| Journaling mode                         | ✅     | Saves to `./logs/` per mode with timestamps |
| OpenAI API mode                         | ✅     | Enabled via `MODEL_SOURCE=openai` + `OPENAI_API_KEY` |
| Local LLM mode placeholder              | ✅     | `MODEL_SOURCE=local` uses `LLM_PATH`, defaulting to `llama3` |
| /reset command                          | ✅     | Resets memory + message count without restarting bot |
| Exit-on-ctrl+C                          | ✅     | Clean shutdown with log finalization |

---

## 📌 Guardrails (Non-Negotiable)

| Guardrail                             | Status | Enforcement |
|---------------------------------------|--------|-------------|
| Cannot disable simulation warnings    | ✅     | Hardcoded in `security.py` |
| Cannot override interrupt interval > 25 | ✅     | Throws error in `config.py` |
| Truth anchors cannot be disabled      | ✅     | Inserted by `Guardrail` logic |
| No online access unless user toggles  | ✅     | Offline by default unless `MODEL_SOURCE=openai` |
| No cloud calls for local LLM mode     | ✅     | Ollama/local-only if selected |
| No backgrounding or daemon            | ✅     | Session dies with the terminal |
| Journaling is passive, not hidden     | ✅     | Logs are saved explicitly and visibly |

---

## 🔜 Planned / Optional Features

| Feature                                 | Priority | Notes |
|-----------------------------------------|----------|-------|
| 🧠 CLI argument flags (`--reflect`, `--journal`, `--system`) | ⭐ High | Currently only `.env` driven; CLI mode adds flexibility |
| 🦙 Ollama integration (`LLM_PATH=llama3`)       | ⭐ High | Real local LLM call logic needs to be written in `llm.py` |
| 🧪 LangChain experimental memory mode    | 📌 Optional | Could allow deeper recursion (toggleable in `.env`) |
| 🧼 Token pruning for memory size control | 📌 Optional | Future support for auto-trimmed memory history |
| 📄 Better terminal UI (colors, separators)     | 📌 Optional | Could improve immersion with simple prompt styling |
| 🔒 Immutable safety guard signature      | ⭐ Medium | Add hash or signature to confirm `security.py` integrity |

---

## 🧱 File Structure

```
soulframe-bot/
├── bot.py               # Main loop + coordination
├── config.py            # .env loader and safety caps
├── security.py          # Interrupts + truth anchors
├── memory.py            # Optional short-term memory
├── reflector.py         # Reflective tone logic
├── llm.py               # Local/OpenAI LLM routing (WIP)
├── .env                 # Local configuration
├── .env.example         # Sample .env file
├── logs/                # Journaling output
├── README.md            # Project overview
└── ROADMAP.md           # You are here
```

---

## 💬 Philosophy Reminder

> *This system is designed to simulate a soul, not possess one.  
You bring the meaning—the bot only reflects it.*

> **Note:** These features are foundational for building a **safe, offline, ethically-bound reflective AI mirror**—not a pretend AGI. Every part is designed with intentional constraint and human responsibility in mind.
