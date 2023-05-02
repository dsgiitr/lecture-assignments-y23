### Level 0
```console
$ ssh bandit0@bandit.labs.overthewire.org -p 2220
```
### Level 0 -> 1 (NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL)
```console
$ ls
$ cat readme
$ exit
```
### Level 1 -> 2 (rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi)
```console
$ ssh bandit1@bandit.labs.overthewire.org -p 2220
$ ls
$ cat ./-
$ exit
```
### Level 2 -> 3 (aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG)
```console
$ ssh bandit2@bandit.labs.overthewire.org -p 2220
$ ls
$ cat "spaces in this filename"
$ exit
```
### Level 3 -> 4 (2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe)
```console
$ ssh bandit3@bandit.labs.overthewire.org -p 2220
$ ls -a
$ cd ./inhere
$ ls -a
$ cat .hidden
$ exit
```
### Level 4 -> 5 (lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR)
```console
$ ssh bandit4@bandit.labs.overthewire.org -p 2220
$ ls -a
$ cd inhere
$ ls -a
$ file ./*
$ cat ./-file07
$ exit
```
### Level 5 -> 6 (P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU)
```console
$ ssh bandit5@bandit.labs.overthewire.org -p 2220
$ ls -a
$ cd inhere
$ ls --human-readable -rf | find -size 1033c ! -executable
$ cat ./maybehere07/.file2
$ exit
```
### Level 6 -> 7 (z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S)
```console
$ ssh bandit6@bandit.labs.overthewire.org -p 2220
$ ls -a
$ find / -user bandit7 -group bandit6 -size 33c
$ cat /var/lib/dpkg/info/bandit7.password
$ exit
```
### Level 7 -> 8 (TESKZC0XvTetK0S9xNwm25STk5iWrBvP)
```console
$ ssh bandit7@bandit.labs.overthewire.org -p 2220
$ ls -a
$ cat data.txt | grep millionth
$ exit
```
### Level 8 -> 9 (EN632PlfYiZbn3PhVK3XOGSlNInNE00t)
```console
$ ssh bandit8@bandit.labs.overthewire.org -p 2220
$ ls -a
$ cat data.txt | sort | uniq -u
$ exit
```
### Level 9 -> 10 (G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s)
```console
$ ssh bandit9@bandit.labs.overthewire.org -p 2220
$ ls -a
$  strings data.txt | grep '=='
$ exit
```
### Level 10 -> 11 (6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM)
```console
$ ssh bandit10@bandit.labs.overthewire.org -p 2220
$ ls -a
$ base64 data.txt -d
$ exit
```
### Level 11 -> 12 (JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv)
```console
$ ssh bandit11@bandit.labs.overthewire.org -p 2220
$ ls -a
$ cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
$ exit
```
### Level 12 -> 13 (wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw)
```console
$ ssh bandit12@bandit.labs.overthewire.org -p 2220
$ ls -a
$ mkdir /tmp/dsgsukjin
$ cp data.txt /tmp/dsgsukjin
$ cd /tmp/dsgsukjin
$ xxd -r data.txt revdata
$ file revdata
$ mv revdata datagz.gz
$ gzip -d datagz.gz
$ file datagz
$ mv datagz databz.bz2
$ bzip2 -d databz.bz2
$ file databz
$ mv databz data1gz.gz
$ gzip -d data1gz.gz
$ file data1gz
$ tar -xvf data1gz
$ file data5.bin
$ tar -xvf data5.bin
$ file data6.bin
$ mv data6.bin data1bz.bz2
$ bzip2 -d data1bz.bz2
$ file data1bz
$ tar -xvf data1bz
$ file data8.bin
$ mv data8.bin data2gz.gz
$ file data2gz
$ cat data2gz
$ exit
```
### Level 13 -> 14 (fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq)
```console
$ ssh bandit13@bandit.labs.overthewire.org -p 2220
$ ls -a
$ ssh bandit14@localhost -i sshkey.private -p 2220
$ cat /etc/bandit_pass/bandit14
```
### Level 14 -> 15 (jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt)
```console
$ telnet localhost 30000
$ exit
```
### Level 15 -> 16 ()
```console
$ ssh bandit15@bandit.labs.overthewire.org -p 2220
$ openssl s_client -connect localhost:30001 -ign_eof
$ exit
```
