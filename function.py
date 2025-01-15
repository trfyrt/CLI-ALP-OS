import os
import sys
import shutil
import random
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
        clear()
        print(xijinping)
        print(thankyou)
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
    exit: Exit from Clinese

Extra Command List:
    tree: Display directory tree
    quotes: Display most impactful Chinese Quotes
    
    ''')

    
# EXTRA COMMAND

def tree(path=".", indent=0):
    try:
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            # Tampilkan item dengan indentation
            print(" " * indent + "'--→ " + item)
            # Jika item adalah directory, rekursi ke dalamnya
            if os.path.isdir(item_path):
                tree(item_path, indent + 4)
    except Exception as e:
        print(f"Error: {e}")

def quotes():
    quotes = ['Tuntutlah ilmu sampai ke negeri China',
        '千里之行，始于足下。',
        '失败是成功之母。',
        '活到老，学到老。',
        '时间就是金钱。',
        '与其临渊羡鱼，不如退而结网。',
        '气贯长虹!',
        'Gōngxǐ fācái']
    
    print(suntzu)
    print(f'''
~ A Wise Chinese once said,
    "{random.choice(quotes)}" ~
    ''')

# def hongbao():