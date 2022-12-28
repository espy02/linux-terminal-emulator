# linux-terminal-emulator
Linux Terminal Emulator, powered by Python

## Usage
Simply change your directory inside the terminal to a folder with `terminal.py` and execute the program with the command `python terminal.py`.

![img01](https://i.imgur.com/s4rrkeT.png)

This emulator contains the following commands from the Linux terminal:

- `cat (filename)` - Concatenate; prints file contents in the terminal.
- `cd (directory)` - Change directory; changes current directory.
- `cp (filename) (directoruy)` - Copy; copies a file to another directory.
- `echo (input)` - Echo; prints the input in the terminal.
- `exit` - Exit; closes program and returns to default terminal.
- `ls` - List; prints the names of all files/directories in current directory.
- `mkdir (directory)` - Make directory; creates a new directory.
- `mv (filename) (directory)` - Move; moves a file to another directory. 
- `pwd` - Print working directory; prints the current directory.
- `rm (filename)` - Remove; deletes a file.
- `rmdir (directory)` - Remove directory; deletes an empty directory.
- `wc (filename)` - Word count; prints the number of lines, words, and characters, respectively, of a file in the terminal.
- `mk (filename)` - Make; creates a new file. This command isn't available in the Linux terminal, but since `mkdir`, `rm` and `rmdir` exist, I thought I might as well include it as well.

This program also includes exception handling for issues such as files/directories that do not exist/already exist, files that cannot be opened, and use of invalid characters (e.g. ':').

![img02](https://i.imgur.com/dXADwKr.png)

## Known issues

- `cp` can only copy a file that can be opened and edited. This is due the fact it uses Python's file handling function.

## Future features:

- A few more commands;
- Switches for a few commands (such as `ls -l`);
- Documentation
