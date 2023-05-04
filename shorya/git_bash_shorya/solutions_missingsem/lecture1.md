# Solutions

1.  To make sure you’re running an appropriate shell.

    **Input:** `echo $SHELL`

    **output:** `/bin/bash`
                `$SHELL` is a env variable containing the absolute pathname to the shell, so we run this command to make sure we are connected to an appropiate shell.


2. Create a new directory called `missing` under `/tmp`.

   **Input:** 
        cd tmp
        mkdir missing

   **output:** Created the missing directory 

3. Look up the `touch` program. The `man` program is your friend.

   **Input:** `man touch`

   **output:** info about how touch is used to change file timestamps but mostly used for creating files imo

4. Use `touch` to create a new file called `semester` in `missing`.

   **Input:** 
        `cd missing`
        `touch semester`

   **output:** Created the file semester inside /tmp/missing.

5. Write the following into that file, one line at a time:

   ```bash
   #!/bin/sh
   curl --head --silent https://missing.csail.mit.edu
   ```

   The first line might be tricky to get working. It's helpful to know that
   `#` starts a comment in Bash, and `!` has a special meaning even within
   double-quoted (`"`) strings. Bash treats single-quoted strings (`'`)
   differently: they will do the trick in this case. See the Bash
   [quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html)
   manual page for more information.

   **Input:** 
        `echo '!#/bin/sh' > semester`
        `echo 'curl --head --silent https://missing.csail.mit.edu' >` `semester`

   **output:** Echo gives the output of command then this outputs gets Written into semester usng `>` and the 2nd command curl or client url is used to write from the url, head helps us to show the url info and silent stops the progress bars and error messages, doesn't have much use here, since command works fine even without silent(no errors to make silent).Also the first command tells the interpreter what shell to use(born shell used here).

6. Try to execute the file, i.e. type the path to the script (`./semester`)
   into your shell and press enter. Understand why it doesn't work by
   consulting the output of `ls` (hint: look at the permission bits of the
   file).

   **Input:**
        `./semester`
        `ls -l`

   **output:** 
            `bash: ./semester: Permission denied`
            `-rw-rw-r-- 1`  
             ls shows that we don't have executable permission(x) for the file semester,so command `./semester` which is trying to execute semester doesn't work.    

7. Run the command by explicitly starting the `sh` interpreter, and giving it
   the file `semester` as the first argument, i.e. `sh semester`. Why does
   this work, while `./semester` didn't?

   **Input:** `sh semester`

   **output:**
             `HTTP/2 200`
            `....`
            `content-length: 8070`
             we have permission to use sh and we also have reading permission for semester, so all the command does is that it reads the the file semester into sh/interpreter which executes it.  
   

8. Look up the `chmod` program (e.g. use `man chmod`).

   **Input:** `man chmod`

   **output:** shows how chmod is used to change file mode bits.

9. Use `chmod` to make it possible to run the command `./semester` rather than
   having to type `sh semester`. How does your shell know that the file is
   supposed to be interpreted using `sh`? See this page on the
   [shebang](<https://en.wikipedia.org/wiki/Shebang_(Unix)>) line for more
   information.

   **Input:** `chmod +x semester`

   **output:** changes file mode bits to contain x i.e. executable bit. it knows to use sh shell becuase of the first command `!#/bin/sh`.

10. Use `|` and `>` to write the "last modified" date output by
   `semester` into a file called `last-modified.txt` in your home
   directory.

   **Input:**
         `./semester | grep -i last-modified | cut -d ':' -f2 | sudo tee /home/last-modified.txt`
   
   **output:** the first command give the output of semseter file which is then fed into the grep command which searches fo last-modified feild and returns it then cut cuts the line into 2 pieces about `:` and f2 takes the second field out of the 2 and then tee creates and writes the output into last-modified.txt.

11. Write a command that reads out your laptop battery's power level or your
    desktop machine's CPU temperature from `/sys`. Note: if you're a macOS
    user, your OS doesn't have sysfs, so you can skip this exercise.

    **Input:**`cat /sys/class/power_supply/BAT1/capacity`

    **output:** `100`
                (can't find cpu temp file in thermal directory)