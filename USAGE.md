# ▶️ USAGE.md — Getting Started with Soulframe Bot

This guide walks you through installing and running Soulframe Bot in **offline** or **OpenAI-connected** mode.

---

## ⚙️ Prerequisites

- Python 3.10+  
- `pip`  
- Local LLM support (optional)  
- [Ollama](https://ollama.com/) installed (for local models like llama3)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/mineblow/Project-Soulframe.git
cd soulframe-bot
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

Create a `.env` file in the root directory:

```ini
# .env
MODEL_SOURCE=local          # or "openai"
LLM_PATH=llama3             # Used only if MODEL_SOURCE=local
OPENAI_API_KEY=sk-...       # Only needed for MODEL_SOURCE=openai

ENABLE_MEMORY=true
MEMORY_LIMIT=20

ENABLE_JOURNAL=true
JOURNAL_DIR=./logs

INTERRUPT_INTERVAL=20
TRUTH_INTERVAL=50
```

---

## 🚀 Running the Bot

### Interactive CLI Mode

```bash
python bot.py
```

You will see:

```
🧠 Soulframe Bot
(Type '/reset' to restart or Ctrl+C to quit)
```

---

## 🎭 Optional Modes

These flags adjust tone and behavior:

```bash
python bot.py --reflect     # poetic introspective mode
python bot.py --system      # straightforward factual tone
python bot.py --journal     # minimal prompt + focused journaling
```

If no flags are passed, a help prompt will be shown.

---

## 📝 Journaling

- Journals are saved in `/logs/`
- They automatically split every 12 hours
- Journals are plain text and **not** passed to the model

---

## 🔐 Safety Systems

- Every 20 messages → interrupt prompt:  
  `"⚠️ This is a simulation. Press [y] to continue."`
- Every 50 messages → truth anchor reminder
- Sessions **must die with the terminal** (no background daemons)
- `/reset` will clear memory and restart the session

---

## 🧠 Local LLM Support (Optional)

Soulframe Bot supports **Ollama** out of the box.

1. Install [Ollama](https://ollama.com/)
2. Start a model:

```bash
ollama run llama3
```

3. In your `.env`:

```ini
MODEL_SOURCE=local
LLM_PATH=llama3
```

---

## ⚠️ Warnings

This bot is **not AGI**. It may reflect you, but it is never you.

> Never disable the guardrails.  
> Never forget it’s a mirror.

---

## 🧩 Help & Debug

Enable debug info:

```ini
DEBUG=true
```

Then run:

```bash
python bot.py
```

---

## ❓ Common Issues

| Problem | Solution |
|--------|----------|
| `KeyError: OPENAI_API_KEY` | Set the key in `.env`, or use `MODEL_SOURCE=local` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Terminal won’t continue | Press `y` when interrupted |
| LLM not responding | Check Ollama model status with `ollama list` |

---

## ❤️ Reflect responsibly.

Soulframe is not a toy.  
Treat it as you would any tool of introspection.

Generated: 2025-03-30
