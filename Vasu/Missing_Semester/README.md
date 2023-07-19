# Missing semester Lec 1
1.
```
echo $SHELL
```

Outputs : /bin/bash

2.

```
cd /tmp
mkdir missing
```

3.

```
man touch
```

4.

```
touch semester
```

5.
```
echo '#!/bin/sh' > semester
echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
```

6.

```
./semester
```


throws the error: 
-bash: ./semester: Permission denied

7.
```
sh semester
```

Outputs:

HTTP/2 200 \
server: GitHub.com \
content-type: text/html; charset=utf-8 \
last-modified: Sat, 1 July 2023 21:30:41 GMT \
access-control-allow-origin: * \
etag: "6448ed01-1f86" \
expires: Sun, 2 July 2023 09:29:27 GMT \
cache-control: max-age=600 \
x-proxy-cache: MISS\
x-github-request-id: 59CE:6523:C0AC0:F09F6:698E0EF\
accept-ranges: bytes\
date: Sun, 2 July 2023 09:53:01 GMT\
via: 1.1 varnish\
age: 477\
x-served-by: cache-ccu830048-CCU\
x-cache: HIT\
x-cache-hits: 1\
x-timer: S1682868181.394681,VS0,VE1\
vary: Accept-Encoding\
x-fastly-request-id: dfcbb83313e213c9a1eb4017e88d2a4d928734a6\
content-length: 8070

8.
```
man chmod
```

9.
```
chmod a+x semester
```

gives all users permission to execute semester

10.
```
./semester | grep -i last-modified | cut -d' ' -f- > last-modified.txt
```
output of ./semester is searched for last-modified by grep and cut cuts it as it encounters a space until end of line. This is then output to last-modified.txt

# Missing semester Lec 2

1.
```
ls -lath --color
```
l is for long listing, a for all files, t for sorting by time and h for human-readable file sizes.

2.
```bash
marco(){
    export curr=$(pwd)
}

polo(){
    cd curr
}
```


3.
```bash
#!/usr/bin/env bash

count=0
until [[ "$?" -ne 0 ]];
do
   count=$(( count + 1 ))
   ./random.sh &> a.txt
done

echo "error returned after runs : $count"
cat a.txt
```

4.
```shell
find . -type f -name "*.html" | xargs tar -cvf file.tar
```

5.

```shell
find . -type f -print0| xargs -0 stat --format '%Y :%y %n' | sort -nr | cut -d: -f2-
```



