from function import *

while True:
    try:
        music()
        user_input = input("命令行界面> ").strip().split()
        
        command = user_input[0]
        args = user_input[1:]

        match command:
            case 'ls':
                ls()
            case 'pwd':
                pwd()
            case 'cd':
                cd(args[0])
            case 'mkdir':
                mkdir(args[0])
            case 'rmdir':
                rmdir(args[0])
            case 'touch':
                touch(args[0])
            case 'rm':
                rm(args[0])
            case 'cp':
                cp(args[0], args[1])
            case 'mv':
                mv(args[0], args[1])
            case 'clear' | 'cls':
                clear()
            case 'exit':
                exit()
            case 'help' | 'h':
                help()
            case _:
                print('Unknown command. Type help or h for available commands.')

    except Exception as e:
        print(f"Error: {e}")

    
