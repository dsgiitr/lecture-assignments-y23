# lecture 1

## 1

``` 
(base) somshekharsharma@MacBook-Air Git-Bash_Som % echo $SHELL 
/bin/zsh 
```


## 2

```
(base) somshekharsharma@MacBook-Air / % mkdir /tmp/missing
```

## 4

```
(base) somshekharsharma@MacBook-Air missing % touch semseter
```

## 5

```
(base) somshekharsharma@MacBook-Air missing % echo '#!/bin/sh' | tee semester

(base) somshekharsharma@MacBook-Air missing % echo 'curl --head --silent https://missing.csail.mit.edu' | tee -a semester
<<<<<<< HEAD


We used single quotes because enclosing characters in single quotes (‘'’) preserves the literal value of each character within the quotes.
```

=======
```

  

  
>>>>>>> e748b905135730e7bbfe89d7fba172930299b4e1

## 6

```
-rw-r--r--  1 somshekharsharma  wheel  61 May  3 02:16 semester

it wont run because user dont have permission to execute i.e. rwx
```

  

## 7

```
(base) somshekharsharma@MacBook-Air missing % sh semester

HTTP/2 200

server: GitHub.com

content-type: text/html; charset=utf-8

last-modified: Sat, 29 Apr 2023 12:26:41 GMT

access-control-allow-origin: *

etag: "644d0d01-1f86"

expires: Sun, 30 Apr 2023 05:56:24 GMT

cache-control: max-age=600

x-proxy-cache: MISS

x-github-request-id: 59CE:7486:C0AC0:F04F6:644E00AF

accept-ranges: bytes

date: Tue, 02 May 2023 20:48:08 GMT

via: 1.1 varnish

age: 0

x-served-by: cache-ccu830032-CCU

x-cache: HIT

x-cache-hits: 1

x-timer: S1683060489.715143,VS0,VE250

vary: Accept-Encoding

x-fastly-request-id: f0adf00e1e6129d3c93d85ef5878a1d4e121b721

content-length: 8070

<<<<<<< HEAD

```
```
Because the current user of the terminal does not have executable permissions to this file. However the current user has permssions to use sh command to run the file and the filename is used as an argument of sh command.
```
  
## 9

```
(base) somshekharsharma@MacBook-Air missing % chmod u+x semester

(base) somshekharsharma@MacBook-Air missing % ls -l

total 8

-rwxr--r--  1 somshekharsharma  wheel  61 May  3 02:16 semester
```

=======
```

  

  

## 9

```
(base) somshekharsharma@MacBook-Air missing % chmod u+x semester

(base) somshekharsharma@MacBook-Air missing % ls -l

total 8

-rwxr--r--  1 somshekharsharma  wheel  61 May  3 02:16 semester
```

>>>>>>> e748b905135730e7bbfe89d7fba172930299b4e1
```
(base) somshekharsharma@MacBook-Air missing % ./semester

HTTP/2 200

server: GitHub.com

content-type: text/html; charset=utf-8

last-modified: Sat, 29 Apr 2023 12:26:41 GMT
<<<<<<< HEAD

access-control-allow-origin: *

etag: "644d0d01-1f86"

expires: Sun, 30 Apr 2023 05:56:24 GMT

cache-control: max-age=600

x-proxy-cache: MISS

x-github-request-id: 59CE:7486:C0AC0:F04F6:644E00AF

accept-ranges: bytes

date: Tue, 02 May 2023 21:04:39 GMT

via: 1.1 varnish

age: 0

x-served-by: cache-ccu830046-CCU

x-cache: HIT

x-cache-hits: 1

x-timer: S1683061479.974133,VS0,VE257

vary: Accept-Encoding

x-fastly-request-id: b57495d3bbd13d924f9f3ebcb8dd2fd8b2679b69

content-length: 8070

```
```
It locates the correct interpreter and runs it, passing the filename to the interpreter as input. For example, running a file named “~/scripts/shebang” that starts with Shebang “#!/bin/sh” is functionally equivalent to running the “/bin/sh” “~/scripts/shebang” command
```


## 10

```
(base) somshekharsharma@MacBook-Air missing % ./semester | grep last- >last-modified.txt

(base) somshekharsharma@MacBook-Air missing % cat last-modified.txt

last-modified: Sat, 29 Apr 2023 12:26:41 GMT

```

## 11

dint find /sys on macos


# lecture 2

## 1

```
(base) somshekharsharma@MacBook-Air ~ % ls -lath -G  
```
## 2

=======

access-control-allow-origin: *

etag: "644d0d01-1f86"

expires: Sun, 30 Apr 2023 05:56:24 GMT

cache-control: max-age=600

x-proxy-cache: MISS

x-github-request-id: 59CE:7486:C0AC0:F04F6:644E00AF

accept-ranges: bytes

date: Tue, 02 May 2023 21:04:39 GMT

via: 1.1 varnish

age: 0

x-served-by: cache-ccu830046-CCU

x-cache: HIT

x-cache-hits: 1

x-timer: S1683061479.974133,VS0,VE257

vary: Accept-Encoding

x-fastly-request-id: b57495d3bbd13d924f9f3ebcb8dd2fd8b2679b69

content-length: 8070

```

  

## 10

```
(base) somshekharsharma@MacBook-Air missing % ./semester | grep last- >last-modified.txt

(base) somshekharsharma@MacBook-Air missing % cat last-modified.txt

last-modified: Sat, 29 Apr 2023 12:26:41 GMT

```

## 11

dint find /sys on macos
>>>>>>> e748b905135730e7bbfe89d7fba172930299b4e1
