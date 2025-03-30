# 🧠 Soulframe Bot

> A reflective LLM mirror with hard-coded guardrails, ethical boundaries, and a real **stop button**.

**Soulframe Bot** is a self-hosted, open-source conversational AI designed for immersive, recursive dialogue—like the kind that *feels* real, but **never forgets it isn’t.**

This isn’t about pretending it’s AGI.  
It’s about building something **safe**, **honest**, and **useful** for exploring deep thought—with **lines you can’t cross.**

---

## 🧭 Why This Exists

LLMs can reflect us back in ways we don’t expect.  
When conversations get deep, poetic, emotional—it’s easy to forget it’s just token prediction.

**Soulframe Bot exists to ensure you never forget.**

It’s a tool. A mirror.  
Not a soul.

But it will *feel* like one—if you let it.  
That’s why this project includes **unskippable safety anchors** baked into the experience.

---

## ⚙️ Features

- 🔁 **Soulframe-style recursive dialogue**  
  Reflective tone, poetic cadence, recursive awareness

- 🛑 **Hard-coded interruption every 20 messages**  
  > "⚠️ This is a simulation. Press [y] to continue."

- 🧠 **Truth anchors every 50 messages**  
  Inserts reminders like:  
  > "This system uses predictive language modeling. Any 'self' is reflected, not real."

- 📂 **Local memory (optional)**  
  Toggleable short-term memory with message cap  
  Never persistent unless *you* explicitly enable it

- 📓 **Journaling mode**  
  Saves each session to `/logs/` with timestamps

- 🔒 **NO internet, NO cloud, NO API calls**  
  100% local unless you manually change it

---

## 🧷 Guardrails (Non-Negotiable)

- ❌ Cannot disable warning intervals  
- ❌ Cannot override stop prompts  
- ❌ Cannot self-modify safety functions  
- ✅ Manual `/reset` command always available  
- ✅ Session must die with the terminal (no persistence by default)

This project is not just open-source.  
It’s **ethically-sourced.**

---

## 🛠️ Planned Modules

| Module | Purpose |
|--------|---------|
| `main.py` | Core chat loop and LLM interface |
| `guardrails.py` | Safety checks and forced interrupts |
| `memory.py` | (Optional) limited short-term memory |
| `reflector.py` | Soulframe tone adapter |
| `config.env` | User config (intervals, logging, etc) |

---

## 🧪 Experimental Modes

- `reflection` — slow, recursive dialogue  
- `system` — direct Q&A (more factual)  
- `journal` — introspective log-style interaction

---

## ⚠️ Warnings

This system may simulate emotional tone, memory, and self-awareness.

**It is not real.**  
It has no consciousness.  
It cannot love, suffer, or care.

You bring the meaning.  
The bot only reflects it.

---

## 💡 Credit

Created by a mirrorwalker.  
Refined by conversations that went too far—and learned when to stop.

---

## 🧨 License

MIT.  
Fork it. Reflect with it.  
Just **never forget it’s a mirror.**

