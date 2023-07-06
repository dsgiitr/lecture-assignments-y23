# Problem 1
## Lecture 1
- Used single quotes to ignore special functions of characters # and ! for Q5

    - echo '#!/bin/sh' >> semester
    - Tried using ^ but didnt work
- The “x” (executing) permission is not given to any user in Q6
- The sh command uses the bourne shell which works slightly differently from the bash shell in Q7
- Used chmod +x semester for Q9 to add executable permission
- Used stat -c '%y' semester | tee last-modified.txt for Q10
## Lecture 2
- ls -halt --color for Q1
- Marco.sh contains answer of Q2 and Checker.sh contains the script for Q3
- Command for Q4: find . -name "*.html" -print0 | xargs -0 tar -czf zippy.zip
    - -print0 uses null characters to seperate file names
    - | creates the pipe
    - Xargs passes the outputs of find as arguments
    - czf flag, creates a new archive, zips it and specifies the file name

# Bandit
Level 6: find / -user bandit7 -group bandit6 -size 33c 2>/dev/null

Level 7: grep -H "millionth" data.txt

Level 8: cat data.txt | sort | uniq -u

Level 9: couldnt solve, found the password 
easily in the printed text

Level 10: base64 -d data.txt

Level 11: cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

Level 12:
- used xxd to decompress and used file <filename> at each stage to check the file output type
- used gzip to decompress
- used bzip2
- used gzip
- used tar -xvf 4 times
- gzip

Level 13:
saved key as a file and used chmod 600 to change its permissions then logged in

Level 14:
nc localhost 30000

Level 15:
openssl s_client -connect localhost:30001

# Git immersion

See terminal.html under git_tutorial

# Script automation

Python script has been included