import sys
from ai_client import get_plan_for_task, refine_plan
from task_executor import execute_plan
from utils import print_plan, user_confirmation, prompt_for_feedback, extract_shell_commands

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent.py '<task description>'")
        sys.exit(1)

    task_description = sys.argv[1]
    print(f"Task Description: {task_description}")

    plan = get_plan_for_task(task_description)
    print_plan(plan)

    if not user_confirmation("Do you approve this plan?"):
        print("Task cancelled by user.")
        sys.exit(0)

    commands = extract_shell_commands(plan)

    for cmd in commands:
        print(f"\n[bold blue]Executing:[/bold blue] {cmd}")
        success, output = execute_plan(cmd)
        print(output)
        if not success:
            print("[red]Command failed. Stopping execution.[/red]")
            break

    if user_confirmation("Did the task complete successfully?"):
        print("Task completed successfully!")
        sys.exit(0)
    else:
        error_details = prompt_for_feedback()
        refined_plan = refine_plan(task_description, error_details)
        print("\n[bold yellow]Refined Plan:[/bold yellow]")
        print_plan(refined_plan)

        if user_confirmation("Do you approve the refined plan?"):
            new_commands = extract_shell_commands(refined_plan)
            for cmd in new_commands:
                print(f"\n[bold blue]Executing:[/bold blue] {cmd}")
                success, output = execute_plan(cmd)
                print(output)
                if not success:
                    print("[red]Command failed again. Stopping.[/red]")
                    break

            if user_confirmation("Did the refined task complete successfully?"):
                print("Task completed successfully!")
            else:
                print("Task still not successful. Please review and try again manually.")
        else:
            print("Refined plan not approved. Exiting.")

if __name__ == "__main__":
    main()
