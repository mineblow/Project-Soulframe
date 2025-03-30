# cli.py

import argparse

def parse_cli_args():
    parser = argparse.ArgumentParser(
        description="🧠 Soulframe Bot - Reflective AI Simulation"
    )

    parser.add_argument("--reflect", action="store_true", help="Enable Soulframe reflective tone")
    parser.add_argument("--journal", action="store_true", help="Log conversation to /logs/")
    parser.add_argument("--system", action="store_true", help="Use system prompt tone (factual)")
    parser.add_argument("--help", action="store_true", help="Show help message")

    args = parser.parse_args()
    return {
        "reflect": args.reflect,
        "journal": args.journal,
        "system": args.system,
        "help": args.help
    }
