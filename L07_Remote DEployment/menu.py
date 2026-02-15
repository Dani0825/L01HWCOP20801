"""
menu.py
Implements a Menu class to display options and execute Linux utilities.
"""

import os

class Menu:
    """Menu class to manage menu options and user input."""

    def __init__(self):
        """Constructor initializes an empty list of menu options."""
        self._options = []

    def addOption(self, option_text):
        """Adds a menu option to the options list."""
        self._options.append(option_text)

    def displayMenu(self):
        """Displays the menu options."""
        print("\n===== Linux Utility Menu =====")
        for index, option in enumerate(self._options, start=1):
            print(f"{index}. {option}")

    def getInput(self):
        """
        Collects user input, validates it, and executes the selected option.
        """
        while True:
            self.displayMenu()
            choice = input("\nEnter your choice (1-4 or Q to quit): ").strip()

            if choice.lower() == 'q' or choice == '4':
                print("Exiting program...")
                break

            if not choice.isdigit():
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(self._options):
                run_bash_cmd(choice)
            else:
                print("Invalid selection. Please choose a valid option.")


def run_bash_cmd(option):
    """
    Executes Linux commands based on user selection.
    Refactored to remove if/elif chains.
    """

    commands = {
        1: "free -h",
        2: "netstat -tulnp",
        3: "free -m"
    }

    command = commands.get(option)

    if command:
        os.system(command)
