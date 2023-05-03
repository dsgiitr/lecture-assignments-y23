##Level0
```console
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
Entered password: **bandit0**


##Level0-->1
```console
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit0@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit1@bandit.labs.overthewire.org -p 2220
```
Entered password: **NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL**
`cat <filename>` prints contents of file to standard output


##Level1-->2
```console
bandit1@bandit:~$ cat < -
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
bandit1@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit2@bandit.labs.overthewire.org -p 2220
```
Entered Password : **rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi**
`cat -` read standard input so using `<` symbol the input stream to cat was set as the file named -


##Level2-->3
```console
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit2@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit3@bandit.labs.overthewire.org -p 2220
```
Entered Password: **aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG**
As the filename consists of spaces it had to be enclosed in quotes or the terminal would have taken it as 4 different arguments of cat


##Level3-->4
```console
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
bandit3@bandit:~/inhere$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit4@bandit.labs.overthewire.org -p 2220
```
Entered Password : **2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe**
by using `-a` flag with `ls` all file names which begin with . i.e. are hidden normally are displayed the ` cat .hidden` prints contents of the file


##Level4-->5
```console
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ file ./-file*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: Non-ISO extended-ASCII text, with no line terminators
bandit4@bandit:~/inhere$ cat < -file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
bandit4@bandit:~/inhere$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit5@bandit.labs.overthewire.org -p 2220
```
Entered Password : **lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR**
`file ./-file*` displays file type of all files starting with 'file' in the current directory. As only -file07 has ASCII values it is the only human readable file so it is opened with `cat < -file07` as file name starts with -


##Level5-->6 
```console
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
bandit5@bandit:~/inhere$ ls -al -R
.:
total 88
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 .
drwxr-xr-x  3 root root    4096 Apr 23 18:04 ..
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere00
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere01
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere02
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere03
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere04
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere05
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere06
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere07
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere08
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere09
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere10
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere11
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere12
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere13
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere14
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere15
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere16
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere17
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere18
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 maybehere19

./maybehere00:
total 72
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 1039 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5  551 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 9388 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 7836 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 7378 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 4802 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 6118 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 6850 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 1915 Apr 23 18:04 spaces file3

./maybehere01:
total 80
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 6028 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 8944 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5  288 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 3070 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 9641 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 3792 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 4139 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 4543 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 8834 Apr 23 18:04 spaces file3

./maybehere02:
total 68
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 3801 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 6351 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 3511 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 2577 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 4932 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 7953 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 6746 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 8488 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 2275 Apr 23 18:04 spaces file3

./maybehere03:
total 80
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5  315 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 9769 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 6595 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 8880 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 8275 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 2282 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 2190 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 3385 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 9234 Apr 23 18:04 spaces file3

./maybehere04:
total 60
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 4410 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 2440 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 2619 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 6144 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 2117 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5  142 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 5532 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 2491 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 6002 Apr 23 18:04 spaces file3

./maybehere05:
total 64
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 2346 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 3201 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 5959 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 5917 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 2572 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 4585 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5  880 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 2420 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 8585 Apr 23 18:04 spaces file3

./maybehere06:
total 64
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 5731 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 1271 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 1076 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 8976 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 3443 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 2418 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 4073 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 4251 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 8065 Apr 23 18:04 spaces file3

./maybehere07:
total 56
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 3663 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 3065 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 2488 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 1033 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 3362 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 1997 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 4130 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 9064 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 1022 Apr 23 18:04 spaces file3

./maybehere08:
total 56
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 1077 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 8169 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 3825 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5  747 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 2650 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 2217 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5  215 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 3693 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 9138 Apr 23 18:04 spaces file3

./maybehere09:
total 76
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 3628 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 6763 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5  774 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 8517 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 7961 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 3798 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 5301 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 8716 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 7569 Apr 23 18:04 spaces file3

./maybehere10:
total 56
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 1052 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 7092 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 1991 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5   99 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 1237 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 2961 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 8269 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 3570 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 2155 Apr 23 18:04 spaces file3

./maybehere11:
total 72
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 1211 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5  452 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 4559 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 2501 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 8854 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 8261 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 3147 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5  503 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 8845 Apr 23 18:04 spaces file3

./maybehere12:
total 72
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 9678 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 5815 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5  251 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 8244 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 9076 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 1022 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 2157 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 2460 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 1639 Apr 23 18:04 spaces file3

./maybehere13:
total 64
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 1359 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 5258 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 1423 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 8952 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 3014 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 6965 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 3952 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5  952 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 4389 Apr 23 18:04 spaces file3

./maybehere14:
total 60
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 4282 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 3427 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 8351 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 1503 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 3756 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 4821 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 1382 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5  871 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5  376 Apr 23 18:04 spaces file3

./maybehere15:
total 64
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 8794 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 2159 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 9499 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5  279 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 6299 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5  742 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 1623 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5   51 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 1637 Apr 23 18:04 spaces file3

./maybehere16:
total 80
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 4277 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 5426 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 5301 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 8472 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 8085 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 1148 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 9773 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 3146 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 7509 Apr 23 18:04 spaces file3

./maybehere17:
total 72
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 1133 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5  895 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 1791 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 8341 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 4422 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5 5094 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 8361 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 3387 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 6381 Apr 23 18:04 spaces file3

./maybehere18:
total 68
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 9697 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 5702 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5   77 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 2084 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 2306 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5  154 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 7334 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 6348 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 7040 Apr 23 18:04 spaces file3

./maybehere19:
total 76
drwxr-x---  2 root bandit5 4096 Apr 23 18:04 .
drwxr-x--- 22 root bandit5 4096 Apr 23 18:04 ..
-rwxr-x---  1 root bandit5 6302 Apr 23 18:04 -file1
-rwxr-x---  1 root bandit5 7209 Apr 23 18:04 .file1
-rw-r-----  1 root bandit5 5594 Apr 23 18:04 -file2
-rw-r-----  1 root bandit5 4740 Apr 23 18:04 .file2
-rwxr-x---  1 root bandit5 7965 Apr 23 18:04 -file3
-rwxr-x---  1 root bandit5  494 Apr 23 18:04 .file3
-rwxr-x---  1 root bandit5 7186 Apr 23 18:04 spaces file1
-rw-r-----  1 root bandit5 8785 Apr 23 18:04 spaces file2
-rwxr-x---  1 root bandit5 2307 Apr 23 18:04 spaces file3
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
bandit5@bandit:~/inhere$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit6@bandit.labs.overthewire.org -p 2220
```
Entered Password :**P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU**
first we enter into inhere directory by `cd inhere` then we print its contents by the `ls` command we see 20 directories in the inhere directory we list all directories and files in it with its size and permissions using `ls -al -R`, `-al` flags causes `ls` to list all files including hidden ones and `-R` flag causes listing of the contents inside the directories in current directory. Then its easy to see that there is only one file with exact size 1033 bytes named .file2 in maybehere07 directory . We print its contents using`cat ./maybehere07/.file2`


##Level6-->7
```console

