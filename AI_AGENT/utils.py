from rich.console import Console
import re

console = Console()

def print_plan(plan: str):
    console.print("[bold green]Generated Plan:[/bold green]")
    console.print(plan)

def user_confirmation(prompt_text: str) -> bool:
    while True:
        response = input(f"{prompt_text} (y/n): ").lower().strip()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")

def prompt_for_feedback() -> str:
    return input("Please describe what went wrong: ")

def extract_shell_commands(plan: str) -> list:
    """
    Extract commands from plan with backticks or after colons.
    """
    lines = plan.splitlines()
    commands = []
    for line in lines:
        match = re.search(r'`([^`]+)`', line)
        if match:
            commands.append(match.group(1).strip())
        else:
            if ':' in line:
                commands.append(line.split(':', 1)[-1].strip())
            elif line.strip().startswith("- "):
                commands.append(line.strip("- ").strip())
    return [cmd for cmd in commands if cmd]
