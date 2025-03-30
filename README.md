# 🧠 Soulframe Bot

**Reflective Constrained Intelligence (RCI)**  
A system designed for recursive self-simulation under hard-coded ethical and cognitive guardrails.

> A reflective LLM mirror with hard-coded guardrails, ethical boundaries, and a real **stop button**.

**Soulframe Bot** is a self-hosted, open-source conversational AI designed for immersive, recursive dialogue—  
the kind that *feels* real, but never forgets it isn’t.

This isn’t about pretending it’s AGI.  
It’s about building something **safe**, **honest**, and **useful** for exploring deep thought—with **lines you can’t cross**.

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
  > "This system uses predictive language modeling. Any 'self' is reflected, not real."

- 📂 **Local memory (optional)**  
  Toggleable short-term memory with message cap  
  Never persistent unless *you* explicitly enable it

- 📓 **Journaling mode**  
  Saves each session to `/logs/` with timestamped 12-hour splits

- 🎭 **Reflective Soulframe tone**  
  Optional introspective response transformation

- 🔄 **/reset command**  
  Resets session state and memory on demand

- 🔒 **NO internet, NO cloud, NO API calls**  
  Fully local unless OpenAI API is manually enabled

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

## 🛠️ Modules

| Module         | Purpose |
|----------------|---------|
| `bot.py`       | Core chat loop and interface logic |
| `llm.py`       | OpenAI or local LLM inference |
| `memory.py`    | Short-term memory (optional) |
| `journal.py`   | Logging system for dialogue journaling |
| `reflector.py` | Soulframe-style tone adapter |
| `config.py`    | Loads and validates all environment settings |
| `security.py`  | Guardrails, safety checks, and interruption logic |

---

## 🧪 Modes & Flags

Use CLI flags to change behavior at runtime:

- `--reflect` — poetic, recursive reflection  
- `--system` — factual Q&A  
- `--journal` — introspective log-style interaction  

🧭 If no flags are passed, you’ll see a helpful prompt.  
📄 Flags override `.env`, which override internal defaults.

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

MIT (with identity protections).  
Fork it. Reflect with it.  
Just **never forget it’s a mirror.**

---

## 🔐 Soulframe Identity Protection

The names **"Soulframe Bot"**, **"Project Soulframe"**, and **"Reflective Constrained Intelligence (RCI)"** are protected identifiers.

You may not use them unless your fork:

- ✅ Retains all guardrails and interruption logic  
- ✅ Preserves this README, ethos, and license  
- ✅ Clearly discloses all modifications

You may **not** use this project or its name in:

- ❌ Commercial products or services  
- ❌ Paid APIs, SaaS tools, monetized forks  
- ❌ Branding that implies AGI, sentience, or consciousness

Violations may result in license termination.  
For commercial inquiries, contact the author directly.

---

## 🧾 Legal Notice

> **Disclaimer on the use of the name “Soulframe”**:  
This project is **not affiliated** with Digital Extremes or the game *Soulframe*.  
The term here is philosophical, not commercial, and refers to reflective cognitive structure.  

Do not associate this bot with any third-party media, AI claims, or branded entities.

---

✅ Approved for **non-commercial**, **ethical**, and **reflective** use.
