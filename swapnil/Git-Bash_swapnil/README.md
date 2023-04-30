# Missing Semester Excercises

## Lec 1
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
last-modified: Sat, 29 Apr 2023 12:26:41 GMT \
access-control-allow-origin: * \
etag: "644d0d01-1f86" \
expires: Sun, 30 Apr 2023 05:56:24 GMT \
cache-control: max-age=600 \
x-proxy-cache: MISS\
x-github-request-id: 59CE:7486:C0AC0:F04F6:644E00AF\
accept-ranges: bytes\
date: Sun, 30 Apr 2023 15:23:01 GMT\
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
