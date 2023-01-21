import os
import sys
from typing import List

COMMANDS = {
            "startapp": "Create a app with router, models and controllers",
            "serve": "Start the server" ,
            "test": "Run the tests"

            }


def generate_description_of_commands() -> None:
    """Generates the description of all the availabe commands."""
    print("python manage.py\t[COMMAND]")
    print(f'COMMANDS\t\tDESCRIPTION\n{"-"*8}\t\t{"-"*11}')
    for cmd, des in COMMANDS.items():
        print(f"{cmd}\t\t\t{des}")


def handle_commands(args: List[str]) -> None:
    """This function handles all the commands.
    Args:
        args (List[str]): List of commands
    """
    cmd = args[1]
    if cmd not in COMMANDS:
        raise Exception("Not a valid command")

    if cmd == "startapp":
        try:
            app_name = args[2]
            os.system(f"python scripts/start_app.py {app_name}")

        except IndexError:
            raise Exception("Please provide the app name")

    elif cmd == "serve":
        os.system("uvicorn src.main:app --host 0.0.0.0 --reload")
    elif cmd == "test":
        os.system("pytest")
    else:
        print("Nothing")


if __name__ == "__main__":

    # parse command line args
    args = sys.argv

    if len(args) < 2:
        generate_description_of_commands()
    else:
        handle_commands(args)