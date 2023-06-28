## Question 1
```console
echo $SHELL
```
**/bin/zsh**
This implies I am running a Zsh shell which is among the right shells

## Question 2
```console
cd /tmp
mkdir missing
```
Using cd /tmp we open tmp directory in root directory
Then by using mkdir we make a directory named missing inside tmp

## Question 3
```console
man touch
```
We use this command to open man page for touch command to understand how to make a file using touch . We press q to exit the man page

## Question 4
```console
cd missing
touch semester
```
First we enter the missing directory using cd missing
Then by touch semester we make file named semester in the current directory that is 'missing'

## Question 5
```console
echo '#!/bin/sh' > semester
echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
```
We echo the required string and then change the output stream to semester file using >
In second line we use >> to append the string so that it doesn’t overwrite the earlier string
We use single quotes as ! retains its special meaning in double quotes 

## Question 6
```console
./semester
```
**zsh: permission denied: ./semester**
Cant execute semester file as ls -l shows that file doesn’t have execution permission

## Question 7
```console
sh semester
```
The above command runs and gives below output

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
date: Sat, 29 Apr 2023 20:18:12 GMT
via: 1.1 varnish
age: 0
x-served-by: cache-bom4733-BOM
x-cache: HIT
x-cache-hits: 1
x-timer: S1682799492.215578,VS0,VE282
vary: Accept-Encoding
x-fastly-request-id: 07011ee9d36134ac41f08fcb62ca46a07d6a160f
content-length: 8070

## Question 8
```console
man chmod
```
Opens man page for chmod

## Question 9
```console
chmod u+x /tmp/missing/semester
```
Gives the user execute permission making it possible for  ./semester to run in shell

## Question 10
```console
./semester|grep 'last-modified' > ~/last-modified.txt
```
./semester runs the semester file the output is fed into grep using pipe symbol grep 'last-modified' finds line containing 'last-modified' from the output of ./semester and the output stream of grep is redirected to last-modified.txt in home directory by using > ~/last-modified.txt







