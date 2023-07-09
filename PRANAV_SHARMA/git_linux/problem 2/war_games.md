lvl-0:cat readme

lvl-1:ls -alps
	cat ./-

lvl-2:ls -alps
	cat "spaces in this filename"

lvl-3:cd inhere
	ls -alps
	cat .hidden

lvl-4:cd inhere
	find . -type f | xargs file
	cat ./-file07

lvl-5:cd inhere
	find . -type f -size 1033c
	cat ./maybehere07/.file2

lvl-6:find / -user bandit7 -group bandit6 -size 33c
	cat /var/lib/dpkg/info/bandit7.password
	
lvl-7:grep millionth data.txt

lvl-8:sort data.txt | uniq -u

lvl-9:strings data.txt

lvl-10:cat data.txt
	 echo VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg== | base64 -d

lvl-11:cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
	 
lvl-12:tar -xf ab.txt
	gzip -d <ab.txt> data.txt
	bzip2 -d <data.txt> ab.txt
used them repeatedly

lvl 13: ls
	  ssh bandit14@localhost -i sshkey.private -p 2220
	  cat /etc/bandit_pass/bandit14

lvl 14:ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
	  nc localhost 30000
	 fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

lvl 15:jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt