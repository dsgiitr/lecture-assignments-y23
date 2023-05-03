## Question 1
```console
ls -al --color=always -t -h  
````
`-al` flag consists of `-a` and `-l` to list all files and directories even the hidden ones
`--color=always` makes sure output is colorized
`-t` orders files based of recency of modification
`-h` lists sizes in human readable format


## Question 2
```console
vim marco.sh
```
marco.sh opens in vim editor
press I and write the code written in marco.sh in the same folder as this file

press esc then press : type wq and enter to save the vim file
load the definitions to shell by
```console
source marco.sh
```
then enter the following command
```console
marco
```
cd into some other directory and enter
```console
polo
```
it will automatically take you to where marco was executed

#Question3 
The given code is stored in script.sh open vim editor using
```console
vim pgm.sh
```
Write the code written in pgm.sh and save it then to run the program do the following
```console
❯ sh pgm.sh
It took 136 runs to fail
Output : 
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
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Everything went according to plan
Something went wrong
Error : 
The error was using magic numbers
```
out.txt and err.txt contains output and error streams respectively of the sample run


##Question4
```console
find . -name '*.htm*' -print0|xargs -0 tar -czf htmlfiles.zip
```
`find . -name '*htm*'` finds all files recursively containing .htm in their name `-print0` delimits them by null character `xargs -0` passes the file names as arguments by seperating them with null character `tar -czf htmlfiles.zip` makes a zip file named htmlfiles


##Question5
```console
find . -type f|ls -t
```
find . -type f recursively lists all files in current directory , its output is piped into `ls` where `-t` flags orders them by recency of modification



