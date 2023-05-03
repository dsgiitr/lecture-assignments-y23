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
bandit6@bandit:~$ find /  -user bandit7 -size 33c -group bandit6 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
bandit6@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit7@bandit.labs.overthewire.org -p 2220
```
Entered Password : **z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S**
 `find /` searches in root recursively `-user bandit7 -size 33c -group bandit6` looks for file that is owned by user bandit7 group bandit6 and has size 33 bytes. Then we open the file name returned using `cat`


##Level7-->8
```console
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ grep 'millionth' <data.txt
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
bandit7@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit8@bandit.labs.overthewire.org -p 2220
```
Entered Password:**TESKZC0XvTetK0S9xNwm25STk5iWrBvP**
`grep millionth` finds line that contains millionth. Input stream is set to data.txt using `<`


##Level8-->9
```console
bandit8@bandit:~$ cat data.txt|sort|uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
bandit8@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit9@bandit.labs.overthewire.org -p 2220
```
Entered Password:**EN632PlfYiZbn3PhVK3XOGSlNInNE00t**
contents of data.txt is read using `cat` and the output is piped to `sort` so that duplicate lines come together as `uniq` checks for duplicacy only in adjacent lines. Output of `sort` is piped to `uniq`
, `-u` flag prints only the non duplicate line


##Level9-->10
```console
bandit9@bandit:~$ strings data.txt| grep '====='
4========== the#
========== password
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit9@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit10@bandit.labs.overthewire.org -p 2220
```
Entered Password:**G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s**
`strings.txt` finds printable strings in data.txt which is then piped in `grep '====='` which returns lines with multiple adjacent =


##Level10-->11
```console
bandit10@bandit:~$ cat data.txt|base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.

ssh bandit11@bandit.labs.overthewire.org -p 2220
```
Entered Password:**6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM**
output of `cat data.txt` is piped into `base64` which decodes the encoding using `-d` flag


##Level11-->12
```console
bandit11@bandit:~$ cat data.txt| tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit11@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit12@bandit.labs.overthewire.org -p 2220
```
Entered Password:**JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv**
contents of data.txt is read using `cat` and piped to `tr 'A-Za-z' 'N-ZA-Mn-za-m'` which rotates the contents rotated by 13, by 13 again to retrieve the password


##Level12-->13
```console
bandit12@bandit:~$ mkdir /tmp/aayan123
bandit12@bandit:~$ cp data.txt /tmp/aayan123
bandit12@bandit:~$ cd /tmp/aayan123
bandit12@bandit:/tmp/aayan123$ ls
data.txt
```
`mkdir` is used to make aayan123 directory under /tmp . `cp` is used to copy data.txt to the newly made directory.Then we go in the directory by `cd /tmp/aayan123`

```console
bandit12@bandit:/tmp/aayan123$ mv data.txt hexdump.txt
bandit12@bandit:/tmp/aayan123$ file hexdump.txt
hexdump.txt: ASCII text
bandit12@bandit:/tmp/aayan123$ xxd -r hexdump.txt > nonhex.txt
```
data.txt is renamed to hexdump.txt using `mv` command . then `xxd -r` is used to revert the hexdump back to binary and the output stream is directed to a new file named nonhex.txt

```console
bandit12@bandit:/tmp/aayan123$ file nonhex.txt
nonhex.txt: gzip compressed data, was "data2.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 581
bandit12@bandit:/tmp/aayan123$ gzip -d <nonhex.txt > decomp1.txt
bandit12@bandit:/tmp/aayan123$ file decomp1.txt
decomp1.txt: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/aayan123$ bzip2 -d <decomp1.txt > decomp2.txt
bandit12@bandit:/tmp/aayan123$ file decomp2.txt
decomp2.txt: gzip compressed data, was "data4.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/aayan123$ gzip -d <decomp2.txt > decomp3.txt
bandit12@bandit:/tmp/aayan123$ file decomp2.txt
decomp2.txt: gzip compressed data, was "data4.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/aayan123$ file decomp3.txt
decomp3.txt: POSIX tar archive (GNU)
bandit12@bandit:/tmp/aayan123$ tar xvf decomp3.txt
data5.bin
bandit12@bandit:/tmp/aayan123$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/aayan123$ tar xvf data5.bin
data6.bin
bandit12@bandit:/tmp/aayan123$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/aayan123$ bzip2 -d <data6.bin > decomp4.txt
bandit12@bandit:/tmp/aayan123$ file decomp4.txt
decomp4.txt: POSIX tar archive (GNU)
bandit12@bandit:/tmp/aayan123$ tar xvf decomp4.txt
data8.bin
bandit12@bandit:/tmp/aayan123$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/aayan123$ gzip -d <data8.bin > decomp5.txt
bandit12@bandit:/tmp/aayan123$ file decomp5.txt
decomp5.txt: ASCII text
bandit12@bandit:/tmp/aayan123$ cat decomp5.txt
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
bandit12@bandit:/tmp/aayan123$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit13@bandit.labs.overthewire.org -p 2220
```
Entered Password:**wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw**
The file's type is checked using `file` command and if its is gzip archive or bzip2 archive it is decompressed using `gzip -d` or `bzip2 -d` respectively and output stored in newfile. A tar archive is accesed by `tar xvf`. This is done until file type comes to be ASCII text. Then the file is read using `cat` to get the password


##Level13-->14
```console

bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ cat sshkey.private
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS
nXmwYckKUcUgzoVSpiNZaS0zUDypdpy2+tRH3MQa5kqN1YKjvF8RC47woOYCktsD
o3FFpGNFec9Taa3Msy+DfQQhHKZFKIL3bJDONtmrVvtYK40/yeU4aZ/HA2DQzwhe
ol1AfiEhAoGBAOnVjosBkm7sblK+n4IEwPxs8sOmhPnTDUy5WGrpSCrXOmsVIBUf
laL3ZGLx3xCIwtCnEucB9DvN2HZkupc/h6hTKUYLqXuyLD8njTrbRhLgbC9QrKrS
M1F2fSTxVqPtZDlDMwjNR04xHA/fKh8bXXyTMqOHNJTHHNhbh3McdURjAoGBANkU
1hqfnw7+aXncJ9bjysr1ZWbqOE5Nd8AFgfwaKuGTTVX2NsUQnCMWdOp+wFak40JH
PKWkJNdBG+ex0H9JNQsTK3X5PBMAS8AfX0GrKeuwKWA6erytVTqjOfLYcdp5+z9s
8DtVCxDuVsM+i4X8UqIGOlvGbtKEVokHPFXP1q/dAoGAcHg5YX7WEehCgCYTzpO+
xysX8ScM2qS6xuZ3MqUWAxUWkh7NGZvhe0sGy9iOdANzwKw7mUUFViaCMR/t54W1
GC83sOs3D7n5Mj8x3NdO8xFit7dT9a245TvaoYQ7KgmqpSg/ScKCw4c3eiLava+J
3btnJeSIU+8ZXq9XjPRpKwUCgYA7z6LiOQKxNeXH3qHXcnHok855maUj5fJNpPbY
iDkyZ8ySF8GlcFsky8Yw6fWCqfG3zDrohJ5l9JmEsBh7SadkwsZhvecQcS9t4vby
9/8X4jS0P8ibfcKS4nBP+dT81kkkg5Z5MohXBORA7VWx+ACohcDEkprsQ+w32xeD
qT1EvQKBgQDKm8ws2ByvSUVs9GjTilCajFqLJ0eVYzRPaY6f++Gv/UVfAPV4c+S0
kAWpXbv5tbkkzbS0eaLPTKgLzavXtQoTtKwrjpolHKIHUz6Wu+n4abfAIRFubOdN
/+aLoRQ0yBDRbdXMsZN/jvY44eM+xRLdRVyMmdPtP8belRi2E2aEzA==
-----END RSA PRIVATE KEY-----
bandit13@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
vim pvtkey.txt
chmod 600 pvtkey.txt
ssh -i pvtkey.txt bandit14@bandit.labs.overthewire.org
```
On `ls`ing we find sshkey.privatekey whose content is read to the output screen using `cat` which is then copied. We the `exit` the remote session . Create a file called pvtkey.txt using `vim pvtkey.txt` and save the copied contents in it. `chmod 600` removes all permissions from the file except read and write permission of owner to make it secure. We now login to bandit14 using private key stored in pvtkey.txt using `ssh -i pvtkey.txt bandit14@bandit.labs.overthewire.org`


##Level 14-->15
```console
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
bandit14@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
ssh bandit15@bandit.labs.overthewire.org -p 2220
```
We have access to shell of bandit14 so we can access password of current level stored in /etc/bandit_pass/bandit14. We access localhost on port 30000 using `nc localhost 30000` We then enter the password of current level to get the password of next level

