import os
import sys
import shutil
import random
from ascii import *

def ls():
    """Displays a list of files and folders in the current directory."""
    try:
        items = os.listdir()
        for item in items:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

def pwd():
    """Displays the current working directory."""
    try:
        print(os.getcwd())
    except Exception as e:
        print(f"Error: {e}")

def cd(path):
    """Change working directory."""
    try:
        os.chdir(path)
        print(f"Changed directory to {os.getcwd()}")
    except Exception as e:
        print(f"Error: {e}")

def mkdir(directory_name):
    """Create a new directory."""
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rmdir(directory_name):
    """Delete directory (if empty)."""
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def touch(file_name):
    """Create a new empty file."""
    try:
        with open(file_name, 'w') as file:
            pass
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rm(file_name):
    """Delete files."""
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def cp(source, destination):
    """Copy files from one location to another."""
    try:
        shutil.copy(source, destination)
        print(f"File copied from '{source}' to '{destination}'.")
    except Exception as e:
        print(f"Error: {e}")

def mv(source, destination):
    """Moving or renaming files/directories."""
    try:
        shutil.move(source, destination)
        print(f"Moved or renamed from '{source}' to '{destination}'.")
    except Exception as e:
        print(f"Error: {e}")

def clear():
    """Clearing the terminal screen."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"Error: {e}")

def exit():
    """Exit from Clinese"""
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
    tree: Display the directory structure as a tree.
    quotes: Display most impactful Chinese Quotes.
    hongbao: Gacha ampao.
    ''')

    
# EXTRA COMMAND

def tree(path=".", level=0):
    """Display the directory structure as a tree."""
    try:
        for entry in os.listdir(path):
            print("  " * level + f"|- {entry}")
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                tree(full_path, level + 1)
    except Exception as e:
        print(f"Error: {e}")

def quotes():
    """Display most impactful Chinese Quotes."""
    quotes = [
        'Tuntutlah ilmu sampai ke negeri China',
        '千里之行，始于足下。',
        '失败是成功之母。',
        '活到老，学到老。',
        '时间就是金钱。',
        '与其临渊羡鱼，不如退而结网。',
        '水滴石穿。',
        '塞翁失马，焉知非福。',
        '气贯长虹!',
        'Gōngxǐ fācái'
        ]
    suntzu(random.choice(quotes))

def hongbao():
    """Gacha ampao."""
    uang = [qr, limratus, seratus, limpul, dupul, sepuluh, zonk]
    print(random.choice(uang))