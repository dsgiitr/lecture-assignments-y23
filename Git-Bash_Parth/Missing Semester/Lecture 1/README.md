## 1.
```console 
$ echo $SHELL
/bin/bash
```
## 2.
```console
$ cd /tmp/missing
```
## 4.
```console
$ touch semester
```

## 5.
```console
$ echo '#!/bin/sh' > semester
$ echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
$ cat semester 
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```
## 6.
```console
$ ./semester
bash: ./semester: Permission denied
$ ls -l
total 4
-rw-rw-r-- 1 parth_badgujar parth_badgujar 61 Apr 30 14:12 semester

#No executable permission given
```

## 7.
```console
$ sh semester
HTTP/2 200 
server: GitHub.com
content-type: text/html; charset=utf-8
last-modified: Sat, 29 Apr 2023 12:26:41 GMT
access-control-allow-origin: *
etag: "644d0d01-1f86"
expires: Sat, 29 Apr 2023 15:03:13 GMT
cache-control: max-age=600
x-proxy-cache: MISS
x-github-request-id: 2BBA:5FE8:1E0216:1FCE96:644D2F58
accept-ranges: bytes
date: Sun, 30 Apr 2023 08:45:12 GMT
via: 1.1 varnish
age: 0
x-served-by: cache-bom4720-BOM
x-cache: HIT
x-cache-hits: 1
x-timer: S1682844313.521611,VS0,VE212
vary: Accept-Encoding
x-fastly-request-id: e27895826a114e71304c66c45a5b96f669ed9017
content-length: 8070
```

## 9.
```console
$ chmod +x ./semester
#Giving executable permission 

$ ./semester
HTTP/2 200 
server: GitHub.com
content-type: text/html; charset=utf-8
last-modified: Sat, 29 Apr 2023 12:26:41 GMT
access-control-allow-origin: *
etag: "644d0d01-1f86"
expires: Sat, 29 Apr 2023 15:03:13 GMT
cache-control: max-age=600
x-proxy-cache: MISS
x-github-request-id: 2BBA:5FE8:1E0216:1FCE96:644D2F58
accept-ranges: bytes
date: Sun, 30 Apr 2023 08:48:34 GMT
via: 1.1 varnish
age: 202
x-served-by: cache-bom4735-BOM
x-cache: HIT
x-cache-hits: 1
x-timer: S1682844514.398992,VS0,VE1
vary: Accept-Encoding
x-fastly-request-id: aafc5ab376a5363b0d973b0221cfa1e94a987d4f
content-length: 8070
```

## 10.
```console
$ ./semester | grep 'last-modified' | cut --delimiter ' ' -f 2-7 > /home/parth_badgujar/last-modified.txt
```

## 11. 
### Script for showing battery capacity
```bash
#!/bin/sh
echo -n 'Battery percentage : '
echo -n `cat /sys/class/power_supply/BAT0/capacity` 
echo ' %'
```
```console
$ nano stats
#Write the above code
$ chmod +x ./stats
$ ./stats
Battery percentage : 67 %
```

