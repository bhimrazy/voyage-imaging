import os
import sys
from typing import List

def generate_description_of_start_app_command() -> None:
    """Generates the description of this command."""
    print("python start_app.py [APP_NAME]")
    print(f'Create a app with router, models and controllers inside src.')


def handle_generate_app(args: List[str]) -> None:
    """This function handles to create app.
    Args:
        args (List[str]): List of commands
    """
    try:
        app_name = args[1]
        # check if app already exists inside src
        if os.path.exists(f"src/{app_name}"):
            raise Exception(f"App with name '{app_name}' already exists")
        else:
            print(f"Creating app with name '{app_name}'")
            os.mkdir(f"src/{app_name}")

    except IndexError:
        raise Exception("Please provide the app name")


if __name__ == "__main__":

    # parse command line args
    args = sys.argv

    if len(args) < 2:
        generate_description_of_start_app_command()
    else:
        handle_generate_app(args)