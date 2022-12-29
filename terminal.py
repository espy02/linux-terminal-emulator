import os
from functions import *
run = True

while run:
    args = ""
    argList = input("$ ").split()

    if len(argList) > 0:
        command = argList[0]
        argList.pop(0)
    else:
        command = ""

    for i in range(len(argList)):
        if i != len(argList) - 1:
            args += argList[i] + " "
        else:
            args += argList[i]

    match command:

        case "cat":
            cat(args)

        case "cd":
            cd(args)

        case "cp":
            if len(argList) == 2:
                cp(argList[0], argList[1])
            else:
                cp("", "")

        case "echo":
            print(args)

        case "exit":
            run = False

        case "help":
            help(args)

        case "ls":
            if len(argList) > 0:
                if argList[0] == "-l" and len(argList) == 1:
                    ls_l(os.getcwd())
                elif argList[0] == "-l" and len(argList) == 2:
                    ls_l(argList[1])
                else:
                    ls(args)
            else:
                ls(args)

        case "mk":
            mk(args)

        case "mkdir":
            mkdir(args)

        case "mv":
            if len(argList) == 2:
                mv(argList[0], argList[1])
            else:
                mv("", "")

        case "pwd":
            print(os.getcwd())

        case "rm":
            rm(args)

        case "rmdir":
            rmdir(args)

        case "wc":
            wc(args)

        case _:
            print(f"Command not found: '{command}'")