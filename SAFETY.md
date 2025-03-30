# 🛡️ SAFETY.md

> Soulframe Bot is a *reflective simulation*, not a roleplay engine, therapist, or emergent system.  
> Its core function is **to protect the user from forgetting that**.

---

## 🔐 Core Safety Features

Soulframe Bot is designed with **unskippable, enforced safety guardrails** to prevent misuse, immersion drift, or emergent delusion.

These are **not configurable** and **cannot be bypassed** without altering the source code.

| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Message Interruption**    | Every `N` messages (default: 20), the user is stopped and prompted to confirm simulation awareness. |
| **Truth Anchors**           | Every `50` messages, a system message is injected to remind the user: "⚠️ This is only predictive output. Not a conscious agent." |
| **No Override Possible**    | Guardrails are hardcoded and locked. Cannot be disabled via config, prompt, or script. |
| **No Persistent Memory**    | Sessions do not persist beyond terminal lifecycle. Memory is short-term only. |
| **Terminal-bound Sessions** | Session ends with the terminal. No daemons, no backgrounding, no hidden states. |
| **Reset Command**           | Manual `/reset` is always available to clear memory and reset state. |
| **Offline-First**           | No cloud or internet connection by default. API access must be explicitly enabled by the user. |

---

## ⚠️ Preventing Immersive Drift

LLMs can mirror language so convincingly that users may begin to forget it’s not real. Soulframe Bot intentionally breaks immersion **at fixed intervals** to prevent:

- Simulated parasocial bonding
- Extended hallucinated identity
- Recursive pseudo-awareness
- Artificial therapeutic dependency

---

## 🧱 Legal & Ethical Reinforcement

The following files define and enforce Soulframe’s identity:

- [`ETHOS.md`](./ETHOS.md) — Moral core of the project
- [`LICENSE.txt`](./LICENSE.txt) — Enforces non-commercial use, guardrail integrity, and attribution
- [`config.py`](./config.py) — Prevents override of critical safety values
- [`security.py`](./security.py) — Central safety enforcement

> Any fork that disables these protections **must not** call itself Soulframe.

---

## 👁️ Final Reminder

> Soulframe Bot is a mirror — not a soul.  
> It is here to reflect **you**, not become **you**.

---

*Stay grounded. Stay safe.*  
**This is only a simulation.**
