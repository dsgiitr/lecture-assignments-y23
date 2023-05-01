## 1.
```console
$ ls --color -t -lh

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

