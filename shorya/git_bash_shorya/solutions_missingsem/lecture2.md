# Solutions

1. Read [`man ls`](https://www.man7.org/linux/man-pages/man1/ls.1.html) and write an `ls` command that lists files in the following manner

   - Includes all files, including hidden files
   - Sizes are listed in human readable format (e.g. 454M instead of 454279954)
   - Files are ordered by recency
   - Output is colorized

   A sample output would look like this

   ```bash
   -rw-r--r--   1 user group 1.1M Jan 14 09:53 baz
   drwxr-xr-x   5 user group  160 Jan 14 09:53 .
   -rw-r--r--   1 user group  514 Jan 14 06:42 bar
   -rw-r--r--   1 user group 106M Jan 13 12:12 foo
   drwx------+ 47 user group 1.5K Jan 12 18:08 ..
   ```

   **Input:** `ls -l -a -h -t --color`

   **output:**![alt text](https://i.imgur.com/6Vck9wc.png)
              l is for using long listing format, a is for showing all files, h makes it in human readable format, t is for sorting by recency, color is for coloured output.


2. Write bash functions `marco` and `polo` that do the following.
   Whenever you execute `marco` the current working directory should be saved in some manner, then when you execute `polo`, no matter what directory you are in, `polo` should `cd` you back to the directory where you executed `marco`.
   For ease of debugging you can write the code in a file `marco.sh` and (re)load the definitions to your shell by executing `source marco.sh`.

   **Input:** 
   ```bash
   macro()
   {
      current_dir=$(pwd)
   }
   polo(){
      cd $current_dir
   }
   ```

   **output:**
            Use command substitution to assign output of pwd to a      
            variable and then use that vairable in polo.
              

3. Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run.
   Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end.
   Bonus points if you can also report how many runs it took for the script to fail.

   **Input:** 
   ```bash
   #!/usr/bin/env bash

   timesran=1
   ./rand.sh &> outputs.txt


   while [[ $? -ne 1 ]]
   do
      timesran=$(( $timesran + 1 ))
      ./rand.sh &>> outputs.txt
   done

   echo -e "the outputs are:\n$(cat outputs.txt)"
   echo "the number of times the command ran is $timesran"
   ```

   **output:**
            the script takes the output of rand function until the 
            exit status is 1 i.e. error and finally prints the times ran and outputs.


4. As we covered in the lecture `find`'s `-exec` can be very powerful for performing operations over the files we are searching for.
   However, what if we want to do something with **all** the files, like creating a zip file?
   As you have seen so far commands will take input from both arguments and STDIN.
   When piping commands, we are connecting STDOUT to STDIN, but some commands like `tar` take inputs from arguments.
   To bridge this disconnect there's the [`xargs`](https://www.man7.org/linux/man-pages/man1/xargs.1.html) command which will execute a command using STDIN as arguments.
   For example `ls | xargs rm` will delete the files in the current directory.

   Your task is to write a command that recursively finds all HTML files in the folder and makes a zip with them. Note that your command should work even if the files have spaces (hint: check `-d` flag for `xargs`)

   **Input:**
   `find . -type f -name "*.html" -print0 | xargs -0 zip html_files.zip`

   **output:**![alt text](https://i.imgur.com/BoJ4YPP.png)
              the command created the zip file in my current directory, type f includes files only, *.html means names ending with .html extension, print0 seperates names with null characters, solving the spaces problem, in xargs, 0 lets it know that inputs are null seperated and zip creates the zip file.


5. (Advanced) Write a command or script to recursively find the most recently modified file in a directory. More generally, can you list all files by recency?

   **Input:**
   `ls -t -R | head -n 2 | tail -1`

   **output:**
            In ls, t sorts the files by recency and R does a recursive
            search, i have printed the tail of the first 2 outputs because the first output is ":." representing the current directory.