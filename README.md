# Command-Line Interface To-Do List

The idea for this basic script is to emulate my physical pen-and-paper To-Do list by creating a command-line script that
can create, store, and edit a To-Do list from the command-line.

## Key Features
* Ability to create a To-Do list which includes the following:
    * Date/Day
    * List of items
* Be able to add items to an existing To-Do list.
* Be able to cross off items on an existing list to signify task has been completed ([x]) 
* Saves lists in a folder called `ToDoLists` with following naming structure :
    `"<date>_ToDoList.txt"`

## Purpose
The point of building this script is mostly to help me learn more about the Argparse module and file handling in Python.
I will likely build on the base features further in the future with the more I learn.

## Requirements
Works on both Windows and Linux command lines.<br>
This script uses **Python 3**, and also requires the **colorama** module to be installed.<br>
Colorama can be installed using ```sudo pip install colorama```.

## Usage
```
python3 todo.py [-h] [-n | -e | -v | -a | -m]

optional arguments:
  -h, --help  show this help message and exit
  -n, --new   Create a new To-Do list.
  -e, --edit  Edit an existing To-Do list
  -v, --view  View todays To-Do List
  -a, --add   Add task to today's list
  -m, --mark  Mark off task from today's list
```
Builds a folder of To-Do Lists in the directory this script is stored in.

## Modules Used
* **argparse**  - Used for writing the command-line interface.
* **datetime** - For retrieving date/time information.
* **os** - Used for creating, reading, and writing files. os also allows you to manipulate paths and file structures
regardless of the operating system you are using to run the script.
* **colorama** - Used for outputting coloured text to the terminal.
* **webbrowser** - Used for opening text files with Notepad/Gedit when editing.
