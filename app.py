import os
from rich import print as rprint

# * Functions for Text Styling (rich)
def make_text_yellow(text):
    return f"[bold yellow on black]{text}[/bold yellow on black]"

def make_text_red_underlined(text):
    return f"[bold red underline]{text}[/bold red underline]"

def make_text_bold(text):
    return f"[bold]{text}[/bold]"

def make_text_cyan_on_dark_gray_background(text):
    return f"[bold cyan on dark_gray]{text}[/bold cyan on dark_gray]"

# * Functions for Interactivity
def get_user_confirmation(prompt):
    while True:
        user_input = input(prompt + "\n(yes/no): ").strip().lower()
        if user_input in ["yes", "y"]:
            return True
        elif user_input in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no.'")


warning = "Read carefully!"
message = "This Script will remove all .git Folders in All Folders in this directory."
confirmation = "This cannot be restored. Are you sure about that?"
workingPath = os.getcwd()

user_confirmation = "Do you want to proceed?\n"

rprint()
rprint(make_text_yellow(warning))
rprint(make_text_bold(message))
rprint(make_text_red_underlined(confirmation))
rprint(make_text_cyan_on_dark_gray_background(workingPath))
rprint()
confirmation = get_user_confirmation(user_confirmation)
if confirmation:
    print("\nThese are all the folders in which .git is getting removed:\n")
else: 
    print("\nBye.\n")
