# Problem 1

## Missing semester Lec 1
1.
```
echo $SHELL
```

Outputs : /bin/bash

2.

```
cd /tmp
mkdir missing
```

3.

```
man touch
```

4.

```
touch semester
```

5.
```
echo '#!/bin/sh' > semester
echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
```

6.

```
./semester
```


throws the error: 
-bash: ./semester: Permission denied

7.
```
sh semester
```

Outputs:

HTTP/2 200 \
server: GitHub.com \
content-type: text/html; charset=utf-8 \
last-modified: Sat, 29 Apr 2023 12:26:41 GMT \
access-control-allow-origin: * \
etag: "644d0d01-1f86" \
expires: Sun, 30 Apr 2023 05:56:24 GMT \
cache-control: max-age=600 \
x-proxy-cache: MISS\
x-github-request-id: 59CE:7486:C0AC0:F04F6:644E00AF\
accept-ranges: bytes\
date: Sun, 30 Apr 2023 15:23:01 GMT\
via: 1.1 varnish\
age: 477\
x-served-by: cache-ccu830048-CCU\
x-cache: HIT\
x-cache-hits: 1\
x-timer: S1682868181.394681,VS0,VE1\
vary: Accept-Encoding\
x-fastly-request-id: dfcbb83313e213c9a1eb4017e88d2a4d928734a6\
content-length: 8070

8.
```
man chmod
```

9.
```
chmod a+x semester
```

gives all users permission to execute semester

10.
```
./semester | grep -i last-modified | cut -d' ' -f- > last-modified.txt
```
output of ./semester is searched for last-modified by grep and cut cuts it as it encounters a space until end of line. This is then output to last-modified.txt



# Problem 2

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

