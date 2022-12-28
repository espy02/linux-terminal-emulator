import os, textual
run = True

while run:
    userInput = ""
    userInputList = input("$ ").split()

    if len(userInputList) > 0:
        command = userInputList[0]
    else:
        command = ""

    for i in range(1, len(userInputList)):
        if i != len(userInputList) - 1:
            userInput += userInputList[i] + " "
        else:
            userInput += userInputList[i]

    arg = userInput.split()

    match command:

        case "cat":
            try:
                file = open(userInput)
                print(file.read())
                file.close()
            except FileNotFoundError:
                print(f"File not found: '{userInput}'")
            except (PermissionError, OSError):
                print(f"Invalid argument: '{userInput}'")
            except UnicodeDecodeError:
                print(f"File could not be opened: '{userInput}'")

        case "cd":
            try:
                os.chdir(userInput)
            except FileNotFoundError:
                print(f"Directory not found: '{userInput}'")
            except OSError:
                print(f"Invalid argument: '{userInput}'")

        case "cp":
            try:
                fileFrom = open(arg[0])
                fileData = fileFrom.read()
                fileFrom.close()
                try:
                    fileTo = open(arg[1] + "\\" + arg[0], "w")
                    fileTo.write(fileData)
                    fileTo.close()
                except FileNotFoundError:
                    print(f"Directory not found: '{arg[1]}'")
                except OSError:
                    print(f"Invalid argument: '{arg[1]}'")
            except FileNotFoundError:
                print(f"File not found: '{arg[0]}'")
            except OSError:
                print(f"Invalid argument: '{arg[0]}'")
            except UnicodeDecodeError:
                print(f"File could not be opened: '{arg[0]}'")


        case "echo":
            print(userInput)

        case "exit":
            run = False

        case "ls":
            for i in os.listdir(os.getcwd()):
                try:
                    file = open(i)
                    file.close()
                    print(f"'{i}'")
                except PermissionError:
                    print(i)

        case "mkdir":
            try:
                os.mkdir(userInput)
            except OSError:
                if userInput in os.listdir(os.getcwd()):
                    print(f"File already exists: '{userInput}'")
                else:
                    print(f"Invalid argument: '{userInput}'")

        case "mk":
            try:
                file = open(userInput, "x")
                file.close()
            except OSError:
                if userInput in os.listdir(os.getcwd()):
                    print(f"File already exists: '{userInput}'")
                else:
                    print(f"Invalid argument: '{userInput}'")

        case "mv":
            try:
                os.rename(arg[0], arg[1] + "\\" + arg[0])
            except FileNotFoundError:
                print("No such file or directory.")
            except OSError:
                try:
                    if arg[0] in os.listdir(arg[1]):
                        print(f"File already exists: '{arg[0]}'")
                    else:
                        print(f"Invalid argument: '{arg[0]}'")
                except OSError:
                    print(f"Invalid argument: '{arg[1]}'")

        case "pwd":
            print(os.getcwd())

        case "rm":
            try:
                os.remove(userInput)
            except FileNotFoundError:
                print(f"File not found: '{userInput}'")
            except OSError:
                print(f"Invalid argument: '{userInput}'")

        case "rmdir":
            try:
                os.rmdir(userInput)
            except FileNotFoundError:
                print(f"Directory not found: '{userInput}'")
            except OSError:
                print(f"Invalid argument: '{userInput}'")

        case "wc":
            try:
                lines = 0
                words = 0
                chars = 0

                file = open(userInput)
                fileData = file.read()
                file.close()
                for i in fileData:
                    if i == "\n":
                        lines += 1
                    else:
                        chars += 1
                if chars > 0:
                    lines += 1

                fileData = fileData.strip().split()
                for i in fileData:
                    words += 1

                print(lines, words, chars, userInput)
            except FileNotFoundError:
                print(f"File not found: '{userInput}'")
            except (PermissionError, OSError):
                print(f"Invalid argument: '{userInput}'")
            except UnicodeDecodeError:
                print(f"File could not be opened: '{userInput}'")

        case _:
            print(f"Command not found: '{userInput}'")
