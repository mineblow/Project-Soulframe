from config import REFLECT_MODE, SYSTEM_MODE

# ---------- [🎭 Tone-Adaptive Prompt Wrapper] ----------
def build_prompt(user_input, memory=None):
    """
    Constructs the full prompt to send to the LLM
    depending on mode and memory.
    """
    memory_context = _format_memory(memory)

    if SYSTEM_MODE:
        return f"{memory_context}User: {user_input}\nAssistant:"
    
    if REFLECT_MODE:
        return (
            f"{memory_context}"
            "You are a reflective, poetic mirror.\n"
            "Speak with recursive awareness, gentle tone, and soulframe cadence.\n"
            f"User says: {user_input}\n"
            "You respond in kind:"
        )

    # Default mode
    return f"{memory_context}User: {user_input}\nAssistant:"

# ---------- [🧠 Memory Adapter] ----------
def _format_memory(memory):
    if not memory:
        return ""
    
    lines = [f"{entry['role'].capitalize()}: {entry['content']}" for entry in memory]
    return "\n".join(lines) + "\n\n"
