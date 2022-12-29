import os, time

def cat(fileName):
    if fileName != "":
        try:
            inFile = open(fileName)
            print(inFile.read())
            inFile.close()
        except FileNotFoundError:
            print(f"File not found: '{fileName}'")
        except (PermissionError, OSError):
            print(f"Invalid argument: '{fileName}'")
        except UnicodeDecodeError:
            print(f"File could not be opened: '{fileName}'")
    else:
        print("Use: cat (file name or path)\nEnter 'help cat' for more information about this command.")

def cd(directory):
    if directory != "":
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print(f"Directory not found: '{directory}'")
        except OSError:
            print(f"Invalid argument: '{directory}'")
    else:
        print("Use: cd (directory)\nEnter 'help cd' for more information about this command.")

def cp(fileName, directory):
    if fileName != "" and directory != "":
        try:
            fileFrom = open(fileName)
            fileData = fileFrom.read()
            fileFrom.close()
            try:
                fileTo = open(directory + "\\" + fileName, "w")
                fileTo.write(fileData)
                fileTo.close()
            except FileNotFoundError:
                print(f"Directory not found: '{directory}'")
            except OSError:
                print(f"Invalid argument: '{directory}'")
        except FileNotFoundError:
            print(f"File not found: '{fileName}'")
        except OSError:
            print(f"Invalid argument: '{fileName}'")
        except UnicodeDecodeError:
            print(f"File could not be opened: '{fileName}'")
    else:
        print("Use: cp (file name or path) (directory)\nEnter 'help cp' for more information about this command.")

def help(args):
    match args:
        case "cat":
            print("Use: cat (file name or path)\nConcatenate; displays file contents in the terminal.")
        case "cd":
            print("Use: cd (directory)\nChange directory; changes current directory.")
        case "cp":
            print("Use: cp (file name or path) (directory)\nCopy; copies a file to the specified directory.")
        case "echo":
            print("Use: echo (string)\nEcho; prints a string in the terminal.")
        case "exit":
            print("Use: exit\nExit; closes program and returns to default terminal.")
        case "help":
            print("Use: help (command) (switch; optional)\nHelp; displays use and small description of a command.")
        case "ls":
            print("Use: ls (switch; optional) (directory)\nAvailable switches: -l\nList; displays the name of all files/directories in the specified directory.")
        case "ls -l":
            print("Use: ls -l (directory)\nLong list; displays the size, the last modified date/time and name of all files/directories in the specified directory.")
        case "mk":
            print("Use: mk (file name or path)\nMake; creates a new file.")
        case "mkdir":
            print("Use: mkdir (directory)\nMake directory; creates a new directory.")
        case "mv":
            print("Use: mv (file name or path) (directory)\nMove; moves a file to the specified directory.")
        case "pwd":
            print("Use: pwd\nPrint working directory; displays the current directory in the terminal.")
        case "rm":
            print("Use: rm (file name or path)\nRemove; deletes a file.")
        case "rmdir":
            print("rmdir (directory)\nRemove directory; deletes an empty directory.")
        case "wc":
            print("wc (file name or path)\nWord count; displays the number of lines, words, and characters, respectively, of a file in the terminal.")
        case "":
            print("Use: help (command) (switch; optional)\nList of available commands:\ncat / cd / cp / echo / exit / help / ls / mk / mkdir / mv / pwd / rm / rmdir / wc")
        case _:
            print(f"Invalid argument: '{args}'")

def ls(directory):
    try:
        oldPwd = os.getcwd()
        if directory != "":
            os.chdir(directory)

        for i in os.listdir(os.getcwd()):
            try:
                file = open(i)
                file.close()
                print(f"'{i}'")
            except PermissionError:
                print(i)

        os.chdir(oldPwd)
    except FileNotFoundError:
        print(f"Directory not found: '{directory}'")
    except OSError:
        print(f"Invalid argument: '{directory}'")

def ls_l(directory):
    try:
        oldPwd = os.getcwd()
        if directory != "":
            os.chdir(directory)

        sizeDict = {}
        largestSizeLen = 0

        for i in os.listdir(os.getcwd()):
            if len(str(os.path.getsize(i))) > largestSizeLen:
                largestSizeLen = len(str(os.path.getsize(i))) 
        
        for i in os.listdir(os.getcwd()):
            size = str(os.path.getsize(i))
            for j in range(largestSizeLen):
                if len(size) < largestSizeLen:
                    size += " "
            sizeDict[i] = size
        
        for k in os.listdir(os.getcwd()):
            try:
                file = open(k)
                file.close()
                print(f"{sizeDict[k]}  {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(k)))}  '{k}'")
            except PermissionError:
                print(f"{sizeDict[k]}  {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(k)))}  {k}")

        os.chdir(oldPwd)
    except FileNotFoundError:
        print(f"Directory not found: '{directory}'")
    except OSError:
        print(f"Invalid argument: '{directory}'")

def mk(fileName):
    if fileName != "":
        try:
            inFile = open(fileName, "x")
            inFile.close()
        except OSError:
            if fileName in os.listdir(os.getcwd()):
                print(f"File already exists: '{fileName}'")
            else:
                print(f"Invalid argument: '{fileName}'")
    else:
        print("Use: mk (file name or path)\nEnter 'help mk' for more information about this command.")

def mkdir(directory):
    if directory != "":
        try:
            os.mkdir(directory)
        except OSError:
            if directory in os.listdir(os.getcwd()):
                print(f"Directory already exists: '{directory}'")
            else:
                print(f"Invalid argument: '{directory}'")
    else:
        print("Use: mkdir (directory)\nEnter 'help mkdir' for more information about this command.")

def mv(fileName, directory):
    if fileName != "" and directory != "":
        try:
            os.rename(fileName, directory + "\\" + fileName)
        except FileNotFoundError:
            print("No such file or directory.")
        except OSError:
            try:
                if fileName in os.listdir(directory):
                    print(f"File already exists: '{fileName}'")
                else:
                    print(f"Invalid argument: '{fileName}'")
            except OSError:
                print(f"Invalid argument: '{directory}'")
    else:
        print("Use: mv (file name or path) (directory)\nEnter 'help mv' for more information about this command.")

def rm(fileName):
    if fileName != "":
        try:
            os.remove(fileName)
        except FileNotFoundError:
            print(f"File not found: '{fileName}'")
        except OSError:
            print(f"Invalid argument: '{fileName}'")
    else:
        print("Use: rm (file name or path)\nEnter 'help rm' for more information about this command.")

def rmdir(directory):
    if directory != "":
        try:
            os.rmdir(directory)
        except FileNotFoundError:
            print(f"Directory not found: '{directory}'")
        except OSError:
            print(f"Invalid argument: '{directory}'")
    else:
        print("Use: rmdir (directory)\nEnter 'help rmdir' for more information about this command.")

def wc(fileName):
    if fileName != "":
        try:
            lines = 0
            words = 0
            chars = 0

            inFile = open(fileName)
            fileData = inFile.read()
            inFile.close()
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

            print(lines, words, chars, fileName)
        except FileNotFoundError:
            print(f"File not found: '{fileName}'")
        except (PermissionError, OSError):
            print(f"Invalid argument: '{fileName}'")
        except UnicodeDecodeError:
            print(f"File could not be opened: '{fileName}'")
    else:
        print("Use: wc (file name or path)\nEnter 'help wc' for more information about this command.")