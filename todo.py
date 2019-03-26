#!/usr/bin/env python3

##############
# Modules ####
##############

import argparse
import datetime
import os
from colorama import init, Fore, Back, Style
import webbrowser


# Get the operating system that the script is running on.
# nt = Windows.
operating_system = os.name

# Get current date and day.
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
day = now.strftime("%A")

#####################
# Helper functions ##
#####################


def go_to_todo_folder():
    """
    Moves you from your current working directory to the To-Do Lists folder.
    Takes operating system into account.
    """

    if operating_system == 'nt':
        current_dir = os.getcwd()
        folder = "\\todoLists"

        # Move to todoLists directory.
        os.chdir(current_dir + folder)

    # ToDo : Add linux/iOS support.
    else:
        print(Fore.RED + "Your operating system is not currently supported...")

    print(Style.RESET_ALL)


def build_new_list(file):
    """
    Builds a new list with basic title.
    """
    f = open(file, "w+")
    f.write("%s, %s\n"
            "== TO-DO LIST ==\n" % (date, day))

    f.close()

def print_list(file):
    """
    Prints out the list stored in the file given
    :param file: The list you would like to display.
    """

    # Opening file to read into command line.
    with open(file) as f:
        for line in f:
            print(Fore.BLUE + line.strip())
            print(Style.RESET_ALL)

###################
# Main functions ##
###################


def create_new_list():
    """
    This function is used for creating new To-Do lists.
    It checks if there is a folder in the current directory called 'todoLists', if there isn't it will create one.
    Once we know that directory exists we then check if a list for today's date exists in the folder, if it doesn't
    then we create one. If the file already exists then we do nothing.
    """

    # If the user is running on Windows ('nt') run the following:
    if operating_system == 'nt':

        # Creating directory for storing To-Do list if one does not already exist.
        current_dir = os.getcwd()
        folder = "\\todoLists"

        # Check if directory already exists. If it doesn't, create a new directory called 'todoLists'.
        print("Looking for %s ..." % (current_dir+folder))

        if os.path.isdir(current_dir+folder):
            print(Fore.GREEN + "FOLDER FOUND!")
            # Move to todoLists directory.
            os.chdir(current_dir+folder)

            # Check if list already exists for today in folder.
            if os.path.isfile("%s_todoList.txt" % date):
                print("List already exists...")
            else:
                print(Fore.GREEN + "Creating new list...")
                file_name = "%s_todoList.txt" % date
                open(file_name, "w+")
                build_new_list(file_name)
        else:
            print(Fore.RED + "Folder does not already exist, creating one now...")
            os.mkdir(current_dir+folder)
            # Move to todoLists directory.
            os.chdir(current_dir + folder)
            # Create new list.
            print(Fore.GREEN + "Creating new list...")
            file_name = "%s_todoList.txt" % date
            open(file_name, "w+")
            build_new_list(file_name)

    # ToDo : Add linux/iOS support.
    else:
        print(Fore.RED + "Your operating system is not currently supported...")

    print(Style.RESET_ALL)


def edit_list():
    """
    Let's you open and edit a to-do list of your choice in a basic text editor.
    """

    print("Which list would you like to edit? :")
    print(Fore.RED + "type 'quit' to exit")
    print(Style.RESET_ALL)

    # Go to the to-do list folder and print it's contents.
    go_to_todo_folder()
    current_dir = os.getcwd()
    print(current_dir, " : ")
    print(Fore.GREEN + str(os.listdir(current_dir)))
    print(Style.RESET_ALL)

    # Get file to edit from user.
    while True:
        file_to_edit = input("List to edit: ")

        # Check if what was entered is a valid file.
        exists = os.path.isfile(file_to_edit)
        if exists:
            print("Opening %s to edit..." % file_to_edit)
            # Opening text file in Notepad.
            webbrowser.open(file_to_edit)
            break
        elif file_to_edit == 'quit':
            break
        else:
            print(Fore.RED + "File entered does not exist in this directory.")
            print(Style.RESET_ALL)


def view_list():
    """
    Lets you view today's To-Do list.
    """
    go_to_todo_folder()
    # Get today's To-Do list.
    todays_list = "%s_todoList.txt" % date

    # Check if there is a list that has been made today.
    exists = os.path.isfile(todays_list)
    if exists:
        print_list(todays_list)
    else:
        print(Fore.RED + "No To-Do list made for today, to make a new list use the '-n' flag.")
        print(Style.RESET_ALL)


def add_item():
    """
    Lets you add an item to today's to-do list.
    """
    go_to_todo_folder()
    # Get today's To-Do list.
    todays_list = "%s_todoList.txt" % date

    # Check if there is a list that has been made today.
    exists = os.path.isfile(todays_list)
    if exists:
        while True:
            print("What task(s) would you like to add to today's list?")
            print(Fore.RED + "type 'quit' to exit")
            print(Style.RESET_ALL)
            item = input("")

            if item != 'quit':
                print(Fore.GREEN + "---------------------------------------------------")
                # Append to today's list.
                f = open(todays_list, "a+")
                f.write("[ ] %s\n" % item)
                print(Style.RESET_ALL)
            else:
                break
    else:
        print(Fore.RED + "No To-Do list made for today, to make a new list use the '-n' flag.")
        print(Style.RESET_ALL)



def mark_off_item():
    """
    Let's you mark off a completed task.
    """
    # Get today's list.
    go_to_todo_folder()
    # Get today's To-Do list.
    todays_list = "%s_todoList.txt" % date

    # Check if there is a list that has been made today.
    exists = os.path.isfile(todays_list)
    if exists:
        while True:
            # Get the item you want to mark off.
            print("What task did you complete?")
            print_list(todays_list)
            print(Fore.RED + "type 'quit' to exit")
            print(Style.RESET_ALL)

            task = input()
            task_and_box = "[ ] %s" % task

            # Opens the file and gets all the lines from it. Then re-opens the file in write mode and re-writes the lines
            # back in until it gets to the task entered. When this tak is found it is re-written  with a cross in its box.
            if task == 'quit':
                break
            else:
                with open(todays_list, "r") as f:
                    lines = f.readlines()
                with open(todays_list, "w") as f:
                    for line in lines:
                        if line.strip("\n") != task_and_box:
                            f.write(line)
                        else:
                            print(Fore.GREEN + "--- Task Complete! ---")
                            print(task)
                            print(Style.RESET_ALL)
                            f.write("[X] %s\n" % task)
    else:
        print(Fore.RED + "No To-Do list made for today, to make a new list use the '-n' flag.")
        print(Style.RESET_ALL)


#########
# Main ##
#########


if __name__ == '__main__':
    init()  # initializing colorama module.

    #############################
    # Setting up ArgumentParser #
    #############################

    parser = argparse.ArgumentParser()
    # Group will make sure that only one of the arguments in the mutually exclusive group is present on CL.
    group = parser.add_mutually_exclusive_group()

    # Adding optional arguments.
    # 'store-true' - Action used for storing True. Makes checking the arguments parsed work for optional args.
    group.add_argument("-n", "--new", help="Create a new To-Do list.", action="store_true")
    group.add_argument("-e", "--edit", help="Edit an existing To-Do list", action="store_true")
    group.add_argument("-v", "--view", help="View todays To-Do List", action="store_true")
    group.add_argument("-a", "--add", help="Add task to today's list", action="store_true")
    group.add_argument("-m", "--mark", help="Mark off task from today's list", action="store_true")

    # Parsing arguments.
    args = parser.parse_args()

    # Checking arguments:
    if args.new:
        create_new_list()
    elif args.edit:
        edit_list()
    elif args.view:
        view_list()
    elif args.add:
        add_item()
    elif args.mark:
        mark_off_item()


