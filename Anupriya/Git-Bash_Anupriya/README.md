## Problem 1
### Shell
1. Already had bash installed. Ran echo $SHELL and it said /bin/bash. 
2. Changed the directory to /tmp, created a new directory (using mkdir) called "missing".
3. Ran "man touch". Read through.
4. Changed directory to missing. Ran "touch semester". File format wasn't specified.
5. Read the link. Single quotes preserves the literal value of every character while double quotes have many restrictions so it's better to use single quotes in this case. The first line is a shebang (starting with #!). Indicates which interpreter to use when executing a script. Here it's the Bourne shell we want to use. Next one is curl (client URL), used to execute files from a server o our terminal. --head fetches headers only and --silent is to disable progress meter. Used echo to add first line using >semester and second line using >>semester to append instead of overwrite.
6. Tried executing semester as asked. Gives Permission denied error. Checked permissions using "ls -l" and here "x" is missing hence execution is disabled for user.
7. sh <filename> works cause we're "explicitly" telling the shell to use the sh command instead of letting the os execute the file. When the os tried to execute the file, it lacked the permission to do so but the sh command doesn't go to the os, rather runs the command directly.
8. Had already looked up the chmod commad while exploring shell myself. It is used to change the permissions of a file either for the user or the group and can be set to read (r), write(w) or execute(x) or a combination. 
9. By using "chmod +x semester", the file was executed succesfully. The shell knew what to do because of the "#!/bin/sh" line in the file. The shebang essentially translated the file to "/bin/sh/curl --head --silent <URL>" so we're explicitly stating to use sh command again. 
10. Created a txt file using sudo touch in home directory, switched back to missing directory and ran "./semester | grep -i last-modiified |cut --delimiter=':' -f2- | sudo tee /home/last-modified.txt". This worked and using "cat last-modified.txt" in /home gave desired output.
Using > gave permission denied error despite changing permissions. 
Using sudo su didn't work, probably because I can't figure out what the syntax should be.
11. After some exploration, in class, there's power_supply which contains BAT1 which further has several files like power_now, status and capacity. cat capacity returned the battery percentage.
Couldn't find where temperature is.

### Shell tools and scripting
1. ls --all --color --human-readable -l
where --all lists literally every entry, --color is for colorizing which is by default 'always', --human-readable for sizes and -l for long listing format.
2. touch marco.sh (to create a new .sh file)
code marco.sh (to edit it in vs code)
we can use these functions-
#!/bin/bash
marco(){
    func=$(pwd)
}
polo(){
    cd "$func"
}
then we first run source marco.sh to load definitions, run marco anything, check what $func returns (returns pwd), then change to some new directory, run polo anything, and theere will be a cd to the directory where marco was called.
3. So, understanding the given script first, it assigns a random integer less than 100, greater than or equal to 0 to a variable n. If n is equal to 42, we count that as a fail and print "Something went wrong" and echo that to $2 (second argument). Then we echo the next message and exit with a return value 1. We close the if statement with fi and echo "everything went according to plan" if n was never equal to 42.

Now we create a output.txt, make it writable and executable, and also a debugproblem.txt with -
#!/bin/env bash
count=0
while [[ "$?" -eq 0 ]];
do
count=$(( count+1 )) 
./problem.sh &> output.txt 
done
echo "error after $count runs"
cat output.txt

and make this executable too. 
We run source problem.sh to check what's happening. 
then we run debugproblem.sh. So, here we are putting count as 0. Then we run while loop, as long as "$?" is equal to 0, so n!=42, we increment count and store the output and error using &> to output.txt. Once n=42, we find $?=1 and while loop ends with the value of count as the number of successful loops i.e., till n was not 42. Output contains the output from problem.sh in that last run.

We get different outputs each time like -
error after 100 runs
Something went wrong
The error was using magic numbers

4. We first created a bunch of html files in working directory -
touch sample{1,2,3,4,5}.html 
as well as a newzip.tar.gz file.
Then ran this command to check files-
find . -type f -name "*.html" 
The output is a list of html files seperated by a new line.
Final command to create zip -
find . -type f -name "*.html" | xargs -d '\n' tar -czf newzip.tar.gz
Now ls contains the newzip.tar.gz with the html files.

5. We know that ls has  flag -t which gives the lists files by newest first.
So this command -
find . -type f | ls -t

## Problem 2
Level 0

1. Ran the following command after searching -
ssh bandit0@bandit.labs.overthewire.org -p 2220
2. password : bandit0

### Level 0 -> 1

1. ls
2. cat readme
3. Logged out using Ctrl+d
4. Logged in again using -
ssh bandit1@bandit.labs.overthewire.org -p 2220
5. password : same as copied from cat readme

### Level 1 -> 2

1. Read about dashed filename
2. Used "cat < -" to open it and get pw.
3. Logged out and loggin in again (same process as before)

### Level 2 -> 3

1. Used cat 'spaces in this filename'
2. Logged out and loggin in again (same process as before)

### Level 3 -> 4

1. cd inhere and used ls -al to see hidden file
2. Used cat .hidden 
3. Logged out and loggin in again (same process as before)

### Level 4 -> 5

1. cat each file. -file07 has the pw, OR 
1. use ls to see filenames.
2. use file -- -file* to see the file type of each file, only -file07 has ASCII. Also, -- makes sure file doesn't confuse the filenames for an option
3. Logged out and loggin in again (same process as before)

### Level 5 -> 6

1. Not sure about how to get human readable file but using
find . -type f -size 1033c ! -executable g
gave only one file path. Using cat, gave pw.
2. Logged out and loggin in again (same process as before)

### Level 6 -> 7

1. Tried -
cd /
find . -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
2. Got a filepath, used cat to obtain it
3. Logged out and loggin in again (same process as before)

### Level 7 -> 8

1. Ran cat data.txt | grep millionth
2. Logged out and loggin in again (same process as before)

### Level 8 -> 9

1. uniq only checks or duplicates in adjacent lines
2. Ran cat data.txt | sort | uniq -u data.txt
3. Logged out and loggin in again (same process as before)

### Level 9 -> 10

1. using strings to get human readable strings and piping that to grep to find string with "=" characters preceding it-
strings data.txt | grep ======
2. Logged out and loggin in again (same process as before)

### Level 10 -> 11

1. base64 -d data.txt
2. Logged out and loggin in again (same process as before)

### Level 11 -> 12

1. using translate (tr) -
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
2. Logged out and loggin in again (same process as before)

### Level 12 -> 13

1. Ran the following -
cd /
mkdir /tmp/myname123
cp data.txt /tmp/myname123
cd /tmp/myname123
cat data.txt
xxd -r data.txt > data01
file data01
gzip -d -c data01 > data02
file data02
bzip2 -d -c data02 > data03
file data03
gzip -d -c data03 > data04
file data04
tar -xf data04
cat data04
file data5.bin
tar -xf data5.bin
cat data5.bin
file data6.bin
bzip2 -d -c data6.bin >data07
file data07
tar -xf data07
cat data07
file data8.bin
gzip -d -c data8.bin > data09
file data09
cat data09

Basically we had a highly compressed file which had to be decompressed several times, storing into a new file after decompressing and checking other files it contained, then decompressing those too until we got an ASCII text file.

2. Logged out and loggin in again (same process as before)

### Level 13 -> 14

1. ls 
We see a sshkey.private
2. using command specific or using private key to login on port 2220-
ssh -i bandit14@localhost -p 2220

### Level 14 -> 15

1. The pw is in /etc/bandit_pass/bandit14, we cat it.
2. using telnet and entering copied password when prompted-
telnet localhost 30000
3. Logged into level 15 using the pw obtained from above and command below, worked!
ssh bandit15@bandit.labs.overthewire.org -p 2220




