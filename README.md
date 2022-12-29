# linux-terminal-emulator
An emulator of Linux's terminal, using Python 3.11.

## Usage
Simply change your directory inside the terminal to a folder with the following files:

- `terminal.py`
- `functions.py`

and execute the program with the command `python terminal.py`.

![img01](https://i.imgur.com/s4rrkeT.png)

This emulator contains the following commands from the Linux terminal:

- `cat (file name or path)` - Concatenate; displays file contents in the terminal.
- `cd (directory)` - Change directory; changes current directory.
- `cp (file name or path) (directory)` - Copy; copies a file to the specified directory.
- `echo (string)` - Echo; prints a string in the terminal.
- `exit` - Exit; closes program and returns to default terminal.
- `help (command) (switch; optional)` - Help; displays use and small description of a command.
- `ls (switch; optional) (directory)` - List; displays the name of all files/directories in the specified directory.
- `mk (file name or path)` - Make; creates a new file. This command isn't available in the Linux terminal, but since `mkdir`, `rm` and `rmdir` exist, I thought I might as well include it as well.
- `mkdir (directory)` - Make directory; creates a new directory.
- `mv (file name or path) (directory)` - Move; moves a file to the specified directory.
- `pwd` - Print working directory; displays the current directory in the terminal.
- `rm (file name or path)` - Remove; deletes a file.
- `rmdir (directory)` - Remove directory; deletes an empty directory.
- `wc (file name or path)` - Word count; displays the number of lines, words, and characters, respectively, of a file in the terminal.

Switches:
- `ls -l (directory)` - Long list; displays the size, the last modified date/time and name of all files/directories in the specified directory.

This program also includes exception handling for issues such as files/directories that do not exist/already exist, files that cannot be opened, and use of invalid characters (e.g. ':').

![img02](https://i.imgur.com/3E8K5Hb.png)

## Known issues

- `cp` can only copy a file that can be opened and edited.
- `cp`, `mv` and `ls -l` will not work if the destination directory has a blank space somewhere.
- `ls -l` might not display the correct size of a folder.

## For a better experience in Windows:
- Create a shortcut of the Windows terminal;
- Right click and go to properties;
- In the `Target` text box, enter the following:
- `%windir%\system32\cmd.exe /k cd (directory) & python terminal.py`
- Once you open this shortcut, the Windows terminal will change the current directory to the one specified, and will start Linux Terminal Emulator at the same time.
