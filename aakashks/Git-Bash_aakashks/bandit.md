# bandit solutions

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

0. cat readme
1. cat ./-
2. cat "spaces in this filename"
3.

```bash
ls -al
cat .hidden
```

4.

```bash
ll
find . -type f | xargs file | grep text
cat ./-file07
```

5. find . -type f -size 1033c ! -executable
6. find / -type f -size 33c ! -executable -user bandit7 -group bandit6 2>/dev/null

for this one handling error stream is very important as it was displaying errors with the required output. hence 2> :error stream, /dev/null is what prints null

7. cat data.txt | grep millionth
8. sort data.txt | uniq -u
9.  strings data.txt | grep ===
10. base64 --decode data.txt | cat
11. cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
12.

```bash
# make folder
mkdir /tmp/temp
mkdir /tmp/t11
cd /tmp/t11
cp ~/data.txt .
mv data.txt hex_dump.txt

# convert hex dump to ASCII
xxd -r hex_dump.txt > compressed.bin

# now we'll check zip type with
file filename

# and use zcat, bzcat to get tar file
# for tar file we use tar -xvf 
# after many times we get the text

zcat compressed.bin > compressed2
bzcat compressed2 > compressed3
tar -xvf compressed4
```

13. ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

14. 
cat /etc/bandit_pass/bandit14
echo fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq | nc localhost 30000

15.echo jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt | openssl s_client -connect localhost:30001 -ign_eof

password for 16 => JQttfApK4SeyHwDlI9SXGR50qclOAil1
