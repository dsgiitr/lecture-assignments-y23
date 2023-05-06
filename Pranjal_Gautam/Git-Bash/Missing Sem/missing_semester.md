# Exercise 1
## 1
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/Users/ASUS$ echo $SHELL
/bin/bash
```
## all else
```console
rodger2041@LAPTOP-CH89DDGF:/tmp$ mkdir missing
rodger2041@LAPTOP-CH89DDGF:/tmp$ touch ./missing/semester
rodger2041@LAPTOP-CH89DDGF:/tmp$ man tee
rodger2041@LAPTOP-CH89DDGF:/tmp$ echo '#!/bin/sh' | tee ./missing/semester
#!/bin/sh
rodger2041@LAPTOP-CH89DDGF:/tmp$ echo 'curl --head --silent https://missing.csail.mit.edu' | tee ./missing/semester -a
curl --head --silent https://missing.csail.mit.edu
rodger2041@LAPTOP-CH89DDGF:/tmp$ cd ./missing
rodger2041@LAPTOP-CH89DDGF:/tmp/missing$ ./semester
-bash: ./semester: Permission denied
rodger2041@LAPTOP-CH89DDGF:/tmp/missing$ chmod 766 ./semester
rodger2041@LAPTOP-CH89DDGF:/tmp/missing$ ./semester
HTTP/2 200
server: GitHub.com
content-type: text/html; charset=utf-8
last-modified: Sat, 29 Apr 2023 12:26:41 GMT
access-control-allow-origin: *
etag: "644d0d01-1f86"
expires: Sat, 29 Apr 2023 15:03:13 GMT
cache-control: max-age=600
x-proxy-cache: MISS
x-github-request-id: 2BBA:5FE8:1E0216:1FCE96:644D2F58
accept-ranges: bytes
date: Sun, 30 Apr 2023 18:03:56 GMT
via: 1.1 varnish
age: 0
x-served-by: cache-bom4721-BOM
x-cache: HIT
x-cache-hits: 1
x-timer: S1682877836.418600,VS0,VE288
vary: Accept-Encoding
x-fastly-request-id: 5ef8a6420bda01310f1cbfa2ed0d9fe9b948fce7
content-length: 8070

rodger2041@LAPTOP-CH89DDGF:/tmp/missing$ ls -l
total 4
-rwxrw-rw- 1 rodger2041 rodger2041 61 Apr 30 23:32 semester
rodger2041@LAPTOP-CH89DDGF:/home$ cd ~
rodger2041@LAPTOP-CH89DDGF:~$ touch last-modified.txt
rodger2041@LAPTOP-CH89DDGF:~$ cd /tmp/missing
rodger2041@LAPTOP-CH89DDGF:/tmp/missing$ ls -l | awk '{print $6 " " $7 " " $8}' > ~/last-modified.txt
rodger2041@LAPTOP-CH89DDGF:/tmp/missing$ cat ~/last-modified.txt

Apr 30 23:32
```
# Exercise 2
## 1
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/htmlcodes$ ls -a -l -h -t
total 75M
-rwxrwxrwx 1 rodger2041 rodger2041  4.3K Apr 30 02:36  archive1.tar.gz
drwxrwxrwx 1 rodger2041 rodger2041  4.0K Apr 30 02:35  .
drwxrwxrwx 1 rodger2041 rodger2041  4.0K Apr 28 22:41  ..
```
## 2
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/htmlcodes$ function marco {
> VAR1=$(pwd)
> }
rodger2041@LAPTOP-CH89DDGF:/mnt/c/htmlcodes$ function polo {
> cd $VAR1
> }
rodger2041@LAPTOP-CH89DDGF:/mnt/c/htmlcodes$ marco
rodger2041@LAPTOP-CH89DDGF:/mnt/c/htmlcodes$ cd ~
rodger2041@LAPTOP-CH89DDGF:~$ polo
rodger2041@LAPTOP-CH89DDGF:/mnt/c/htmlcodes$
```
## 3
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/gittut/Pranjal Gautam$ cat error.sh
 #!/usr/bin/env bash

 n=$(( RANDOM % 100 ))

 if [[ n -eq 42 ]]; then
    echo "Something went wrong"
    >&2 echo "The error was using magic numbers"
    exit 1
 fi

 echo "Everything went according to plan"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/gittut/Pranjal Gautam$ nano checker.sh
rodger2041@LAPTOP-CH89DDGF:/mnt/c/gittut/Pranjal Gautam$ cat checker.sh
#!/usr/bin/env bash

n=0

while [[ true ]]
do
        ((n++))
        ./error.sh >> stdout.txt 2>> stderr.txt
        if [[ $? -ne 0 ]]; then
                echo "Error detected in $n th try"
                break
        fi
done

rodger2041@LAPTOP-CH89DDGF:/mnt/c/gittut/Pranjal Gautam$ touch stderr.txt | touch stdou
t.txt
rodger2041@LAPTOP-CH89DDGF:/mnt/c/gittut/Pranjal Gautam$ ./checker.sh
Error detected in 17 th try
rodger2041@LAPTOP-CH89DDGF:/mnt/c/gittut/Pranjal Gautam$ cat stdout.txt
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Something went wrong
rodger2041@LAPTOP-CH89DDGF:/mnt/c/gittut/Pranjal Gautam$ cat stderr.txt
The error was using magic numbers
```
## 4
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/htmlcodes$ find -type f -name "*.html" | xargs tar -c
 -z -v -f archive
./about.html
./index.html
./loginpage.html
./match.html
./signup.html
./upload.html
```
