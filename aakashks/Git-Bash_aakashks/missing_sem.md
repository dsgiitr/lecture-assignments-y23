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

