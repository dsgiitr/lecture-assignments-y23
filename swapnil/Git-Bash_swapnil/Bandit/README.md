# Bandit levels

0.
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

1.

```
cat readme
```
 Outputs the password.

2.

```
cat ./-
```
Outputs the password. (- is a keyword for flags, thus we need to use ./ to indicate we are referring to a file in the pwd).

3.
```
cat spaces\ in\ this\ filename
```
Outputs the password. (\ to escapse whitespace)

4.

```
cd inhere
ls -la
cat ./.hidden
```
first we cd to inhere directory, then get list of files in "inhere", to find .hidden inside. then we print out its contents to find the password.

5.

```
cd inhere
ls -la
cat ./-file00
cat ./-file01
cat ./-file02
cat ./-file03
cat ./-file04
cat ./-file05
cat ./-file06
cat ./-file07
```

all other files print out garbage, except -file07 which gives the password.

6.

```
find -type f -size 1033c
cat ./inhere/maybehere07/.file2
```
finding file of size 1033 bytes (c stands for bytes) outputs ./inhere/maybehere07/.file2, which is our required file.

7.

```
find / -size 33c -user bandit7  -group bandit6 
cat /var/lib/dpkg/info/bandit7.password
```

Outputs the password

8.

```
grep "millionth" data.txt
```

Outputs millionth *password*.

9.

```
cat data.txt | sort | uniq -u
```
sort sorts the entries and uniq -u prints out the entry that only occurs once.(our password)

10.

```
strings data.txt | grep "=="
```
Gives out 4 entries with some == preceding them, but only 1 resembles a password.

11.

```
cat data.txt | base64 --decode
```

Outputs : The password is *password*
Basically we decoded the text in data.text using base64 program

12.

```
cat data.txt | tr a-zA-Z n-za-mN-ZA-M
```
Outputs : The password is *password*
We use ROT13 encryption to decryt this file. Since ROT13 is its on inverse, we can apply ROT13 encryption again to get decrypted file.(a-z is mapped to n-zaa-m meaning a is mapped to n, b to o and so on.)

13.

```
mkdir /tmp/swaplvl12
cp data.txt /tmp/swaplvl12
```
We proceed to use a series of decompressios (zcat, bcat and tar) to repeatedly decompresss this highly compressed file, keeping a check on the file type using file program.

14.
```
ssh bandit14@localhost -i sshkey.private
```

sshkey.private contains the ssh key to bandit14, using which we can enter the next level.

15.

```
cat /etc/bandit_pass/bandit14
```
gives us the password.

```
nc localhost 30000
```
asks for password, we enter it.

Outputs: Correct!
and gives the password for the next level.