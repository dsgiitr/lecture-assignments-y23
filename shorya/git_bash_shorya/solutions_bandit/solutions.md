I was told i only needed to explain the mit lectures, so just gonna write the solutions i came up with for bandit here

**level 0**

    ssh bandit0@bandit.labs.overthewire.org -p 2220

    (input bandit0 when asked for password)

**level 1**

    pwd(to check if current directory is home)

    cat read me

    exit(ssh protocol only allows one active ssh connecction per session)

    ssh bandit1@bandit.labs.overthewire.org -p 2220

**level 2**

    cat < -

**level 3**

    cat "spaces in this filename"

**level 4**

    ls -a

    cd inhere

    ls -a

    cat .hidden

**level 5**

    ls -a

    cd inhere

    ls -a

    file ./-\*

    cat < -file07

**level 6**

    find . -type f -size 1033c ! -executable -exec file {} \; | grep -i ASCII

    cat ./maybehere07/.file2

**level 7**

    find / {-name .\*,} -user bandit7 -group bandit6 -size 33c 2>/dev/null

    cat /var/lib/dpkg/info/bandit7.password

**level 8**

    ls -a

    cat data.txt | grep -i millionth

**level 9**

    ls -a

    sort data.txt | uniq -u

**level 10**

    strings -a data.txt | grep '[[:print:]]' | grep "^=="

    (output-

    ========== password

    ========== is

    ========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

    )

**level 11**

    ls -a

    base64 -d data.txt

**level 12**

    ls -a

    cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]

**level 13**

    mkdir /tmp/shorya123

    cp data.txt /tmp/shorya123

    cd /tmp/shorya123

    file data.txt

    xxd -r data.txt data1

    mv data1 data2.gz

    gzip -d data2.gz

    file data2

    mv data2 data3.bz2

    bzip2 -d data3.bz2

    file data3

    mv data3 data4.gz

    gzip -d data4.gz

    file data4

    tar -xvf data4

    file data5.bin

    tar -xvf data5.bin

    file data6.bin

    mv data6.bin data7.bz2

    bzip2 -d data7.bz2

    file data7

    tar -xvf data7

    file data8.bin

    mv data8.bin data9.gz

    gzip -d data9.gz

    file data9

    cat data9

    (script likh deta isse acha)

**level 14**

    ls -l

    file sshkey.private

    ssh -i sshkey.private bandit14@localhost -p 2220

    cat /etc/bandit\_pass/bandit14

**level 15**

    (we don't have to login through ssh but just send the password to localhost on port 30000, to do that we need to just esthablish a tcp connection with the local host 30000)

    nc localhost 30000

    (type password when connection is esthablished)

**level 16**

    openssl s\_client -connect localhost:30001

    (submit password of current level when prompted)


