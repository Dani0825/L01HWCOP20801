"""
main.py
Public interface for running the Linux Utility Menu program.
"""

from menu import Menu

def main():
    """Main function to create and run the menu system."""
    menu = Menu()

    menu.addOption("Check available memory")
    menu.addOption("View network connections")
    menu.addOption("Display free RAM and swap")
    menu.addOption("Quit")

    menu.getInput()

if __name__ == "__main__":
    main()
