## 1.
```console
$ ls --color -t -lh
total 40K
-rw-rw-r-- 1 parth_badgujar parth_badgujar 4.2K May  1 07:41  error_log
-rw-rw-r-- 1 parth_badgujar parth_badgujar 1.1K May  1 07:41  all_htmls.zip
drwxrwxr-x 2 parth_badgujar parth_badgujar 4.0K May  1 07:40  sample_dir
-rwxrwxr-x 1 parth_badgujar parth_badgujar  254 May  1 07:40  checker
-rw-rw-r-- 1 parth_badgujar parth_badgujar  986 May  1 07:38  README.md
-rw-rw-r-- 1 parth_badgujar parth_badgujar    9 May  1 06:51 'this is another file.html'
-rw-rw-r-- 1 parth_badgujar parth_badgujar   10 May  1 06:51  sample1.html
-rwxrwxr-x 1 parth_badgujar parth_badgujar  209 Apr 30 15:46  given_script
-rwxrwxr-x 1 parth_badgujar parth_badgujar   89 Apr 30 15:34  macro.sh
```
## 2.
### macro.sh
```sh
#!/bin/sh
macro(){
    PATH_VAR=$(pwd)
    export PATH_VAR
}
polo(){
    cd "$PATH_VAR"
}
```


## 3.
>### Script given (given_script)
```bash
 #!/usr/bin/env bash
 n=$(( RANDOM % 100 ))

 if [[ n -eq 42 ]]; then
    echo "Something went wrong"
    >&2 echo "The error was using magic numbers"
    exit 1
 fi

 echo "Everything went according to plan"
```
>### Script to run the above script (checker)
```bash
#!/bin/bin bash
echo '' > error_log
count=0
while true; do
  output=$(./given_script)
  echo $output >> error_log
  ((count++))
  if [[ $output != "Everything went according to plan" ]]; then
    break
  fi
done

echo "The script was executed $count times"
```
>#### This script checks the output indefinitely until we stop getting required output at the same time logging outputs and counting the number of times it executed 

## 4. 
```console
$ find . -name "*.html" | xargs -d '\n' zip all_htmls.zip
```

