#!/usr/bin/env python3

##############
# Modules ####
##############

import argparse
import datetime
import os
from colorama import init, Fore, Back, Style


def create_new_list():
    """
    This function is used for creating new To-Do lists.
    It checks if there is a folder in the current directory called 'todoLists', if there isn't it will create one.
    Once we know that directory exists we then check if a list for today's date exists in the folder, if it doesn't
    then we create one. If the file already exists then we do nothing.
    """
    
    # Get current date.
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")

    # If the user is running on Windows ('nt') run the following:
    if os.name == 'nt':

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
                open("%s_todoList.txt" % date, "w+")
        else:
            print(Fore.RED + "Folder does not already exist, creating one now...")
            os.mkdir(current_dir+folder)
            # Move to todoLists directory.
            os.chdir(current_dir + folder)
            # Create new list.
            print(Fore.GREEN + "Creating new list...")
            open("%s_todoList.txt" % date, "w+")

    print(Style.RESET_ALL)


def edit_list():
    print("Which list would you like to edit? :")
    print("<folder directory>")


if __name__ == '__main__':
    init()  # initializing colorama module.

    #############################
    # Setting up ArgumentParser #
    #############################

    parser = argparse.ArgumentParser()
    # Group will make sure that only one of the arguments in the mutually exclusive group is present on CL.
    group = parser.add_mutually_exclusive_group()

    # Adding optional arguments.
    # 'store-true' - Action used for storing True.
    group.add_argument("-n", "--new", help="Create a new To-Do list.", action="store_true")
    group.add_argument("-e", "--edit", help="Edit an existing To-Do list", action="store_true")

    # Parsing arguments.
    args = parser.parse_args()

    # Checking arguments:
    if args.new:
        create_new_list()
    elif args.edit:
        edit_list()


