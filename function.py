import os
import sys
import shutil
from ascii import *

def ls():
    try:
        items = os.listdir()
        for item in items:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

def pwd():
    try:
        print(os.getcwd())
    except Exception as e:
        print(f"Error: {e}")

def cd(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {os.getcwd()}")
    except Exception as e:
        print(f"Error: {e}")

def mkdir(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rmdir(directory_name):
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def touch(file_name):
    try:
        with open(file_name, 'w') as file:
            pass
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rm(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def cp(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied from '{source}' to '{destination}'.")
    except Exception as e:
        print(f"Error: {e}")

def mv(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved or renamed from '{source}' to '{destination}'.")
    except Exception as e:
        print(f"Error: {e}")

def clear():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"Error: {e}")

def exit():
    try:
        xijinping()
        print("Exiting. 谢谢, 再见!")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")

def help():
    print('''Command List:
    ls: Displays a list of files and folders in the current directory.
    pwd: Displays the current working directory.
    cd: Change working directory.
    mkdir: Create a new directory.
    rmdir: Delete directory (if empty).
    touch: Create a new empty file.
    rm: Delete files.
    cp: Copy files from one location to another.
    mv: Moving or renaming files/directories.
    help: Displays a list of existing commands and their functions..
    clear: Clearing the terminal screen.
    exit: Exit from 命令行界面!''')

    
# << EXTRA >>

def credit():
    print('Aaron Jevon Benedict Kongdoh AKA Trefy 亚伦')