# Solutions to Missing semester problems

## lecture 1

```bash
cd /tmp
mkdir missing
cd missing
touch semester
echo '#!/bin/sh' > semester
echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
sh semester
chmod +x semester
./semester
./semester | grep -i last-modified | cut -d' ' -f2- > last-modified.txt
```

x permission not allowed for anybody
hence file not executing

now we use the shell interpreter program (sh) to run the bash script

because it is mentioned after shebang the program which needs to be run for this file (it's path /bin/sh is mentioned)

### To check the battery level (in WSL)

```bash
cd /sys/class/power_supply/BAT1
cat capacity
```

## lecture 2

1. ls -al -h -t --color=auto

2. 
```bash
#!/bin/sh
marco() {
   export MARCO=$(pwd)
}

polo() {
   cd "$MARCO"
}
```

3. 

```bash
#!/usr/bin/env bash

count=0
rm output.txt error.txt
while true; 
do
    count=$((count+1))
    if ./script.sh >> output.txt 2>> error.txt ; then
        echo "Run #$count: Script succeeded"
    else
        echo "Run #$count: Script failed"
        cat output.txt
        cat error.txt
        echo "It took $count runs to fail"
        exit 1
    fi
done
```

4. find . -type f -name "*.html" -print0 | xargs -0 tar -czf zipped.tar.gz
