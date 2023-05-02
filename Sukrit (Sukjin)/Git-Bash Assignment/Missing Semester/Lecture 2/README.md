### Question 1
Has extra columns from the described output, but satisfies all the requirements.
```console
ls -a -s -t -l -h --color
```
### Question 2
Below is a working code for marco.sh,
```console
#!/bin/bash

Marco () {
    DIR="$(PWD)"
}

Polo() {
	cd "$DIR"
}
```
### Question 3
Below is a working code for testscript.sh,
```console
#!/bin/bash
count=0
rm stdout.txt
rm stderr.txt
touch stdout.txt
touch stderr.txt
while [[ $? -ne 0 ]];
do
    count=$((count+1))
    ./script.sh 1>> stdout.txt 2>> stderr.txt
done
echo "The script ran for a total of $count times, and its output is as follows,"
cat stdout.txt
echo "The error encountered is as follows,"
cat stderr.txt
```
A sample script to test it is as follows,
```console
#!/bin/bash
n=$(( RANDOM % 100 ))
if [[ n -eq 42 ]]; then
    echo "Something went wrong"
    >&2 echo "The error was using magic numbers"
    exit 1
fi
echo "Everything went according to plan"
```
### Question 4
The following command works on MacOS systems,
```console
find . -type f -name "*.html" -print0 | xargs -0 tar -cvzf archive.tar.gz
```
### Question 5
The first command extracts the most recently modified file while the second one lists the files in order of recency
```console
find . -type f -print0 | xargs -0 stat -f "%m %N" | sort -rn | head -1
find . -type f -print0 | xargs -0 stat -f "%m %N" | sort -rn
```
