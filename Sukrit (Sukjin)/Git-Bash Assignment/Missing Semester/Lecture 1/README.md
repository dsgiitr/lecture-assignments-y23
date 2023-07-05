### Question 1
Prints the currently active shell, in my case, it is '/bin/zsh'
``` console
$ echo $SHELL
```
### Question 2
Makes a directory 'missing' in the directory 'tmp'
```console
$ mkdir /tmp/missing
```
### Question 3
Using the man command for the touch command
```console
$ man touch
```
### Question 4
Creates a file called 'semester' in the 'missing' directory
```console
$ cd /tmp/missing
$ touch semester
```
### Question 5
Adds two lines, seaparately to the 'semester' file. The first commands overwrites any previously written statements and the single quotes hare used for inputting # and !,
```console
$ echo '#!/bin/sh' > semester
$ cho 'curl --head --silent https://missing.csail.mit.edu' >> semester
```
### Question 6
The command doesn't work as the execute permissions are missing for the file.
```console
$ ./semester
$ ls -l
```
### Question 7
The sh command invokes the default shell which does not require permissions, I guess. This one isn't really clearly explained anywhere, so this is only what I assume is happening.
```console
$ sh semester
```
### Question 8
Using the man command for the chmod command
```console
$ man chmod
```
### Question 9
Using the chmod command, I give myself execute permissions (700). For the other question, I believe it's because the shebang tells the system to parse the remaining parts of the program to the mentioned interpreter.
```console
$ chmod 700 semester
$ ./semester
```
### Question 10
I grep the last-modified part of the output through piping and add it to a file called last-modified.txt which gets created in the home directory.
```console
$ ./semester | grep last-modified > ~/last-modified.txt
```
### Question 11
My system is a MacOS.
