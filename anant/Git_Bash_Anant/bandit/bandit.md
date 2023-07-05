#### bandit 0
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
cat readme
```
#### bandit 1
```
cat ./-
cat < -
```
#### bandit 2
```
 cat "spaces in this filename"
 cat spaces\ in\ this\ filename
 ```
#### bandit 3
```
cd inhere
ls -la
cat .hidden
```
#### bandit 4
```
cd inhere
cat ./-file07
```
#### bandit 5
```
find . -type f -size 1033c
stat ./maybehere07/.file2
cat ./maybehere07/.file2
```
#### bandit 6
```
cd ../../..
find -type f -size 33c -user bandit7 -group bandit6
./var/lib/dpkg/info/bandit7.password
```
#### bandit 7
```
grep data.txt "millionth"
```
#### bandit 8
```
cat data.txt | sort | uniq -c
correct has a 1 next to it
```
#### bandit 9
```
strings data.txt | grep "======"
```
#### bandit 10
 ```
base64 -d data.txt
 ```
#### bandit 11
```
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
#### bandit 12
```
mkdir /tmp/anant12
cp data.txt /tmp/anant12/data.txt
cd /tmp/anant12
```
**going from hexdump to binary**
```
 xxd -r data.txt pass
 file pass
```
**file is a gzib file**
```
 mv pass pass.gz
 gzip -d pass.gz
 file pass 
 ```
  **this is a bzip2 file**
  ```
 mv pass pass.bz
 bzip2 -d pass.bz
 file pass
 mv pass pass.gz
 gzip -d pass.gz
 file pass 
 ```
  **this is a tar file**
  ```
 tar -xvf pass
 file data5.bin
 ```
**these are reperated mutiple times till the file has ascii**
#### bandit 13
```
 cat sshkey.private
 ```
**copy the key,exit the server**
```
 echo 'key' > private.key
 chmod 700 sshkey.private
 ssh bandit14@bandit.labs.overthewire.org -i sshkey.private
 ```
#### bandit 14
```
 nc 127.0.0.1 30000
 ```
#### bandit 15 
```
 openssl s_client -connect localhost:30001
 ```

