# bandit 0

(base) somshekharsharma@MacBook-Air ~ % ssh bandit0@bandit.labs.overthewire.org -p 2220
password-bandit0
# bandit 0-1
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
# bandit 1-2
i used path to read file
bandit1@bandit:~$ pwd
/home/bandit1
bandit1@bandit:~$ cat /home/bandit1/-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
# bandit 2-3
used quotations 
bandit2@bandit:~$ ls
spaces in this filename

bandit2@bandit:~$ cat "spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

# bandit 3-4
-a flag of ls 

bandit3@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  inhere  .profile
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
bandit3@bandit:~/inhere$ 

# bandit 4-5
## method1 :
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ pwd
/home/bandit4/inhere
bandit4@bandit:~/inhere$ cat /home/bandit4/inhere/-file*
?Ű??Bη???b<Q?Ƞ?+V?iO?1?[5{?jmD?B?0D?tQ*??)?A???V ?]Ȕl?x(?z?.T26 F8qqlY???v?FN#??'~?E?Q?"?p?
????4?}?]??G?A??u[?/9??Mrj?S?r_E?,???G+?h|?+
?=>KQ?2??]o-p8q?츑???D?
                       .~?&ϯ"PT?I'?cwk^j?????M????;,??co?9lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
?׉ǰ?6=?>>?ӫ?w?<U'=?@??Z?xj??3??[ٲN|??G|b?G?[8?y?-?́*?
** password =lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR **

## method 2
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: Non-ISO extended-ASCII text, with no line terminators

## bandit 5-6

bandit5@bandit:~/inhere$ find -size 1033c -ls
   292565      4 -rw-r-----   1 root     bandit5      1033 Apr 23 18:04 ./maybehere07/.file2
bandit5@bandit:~/inhere$ find -size 1033c ! -perm \a+x -ls
   292565      4 -rw-r-----   1 root     bandit5      1033 Apr 23 18:04 ./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2

** password =P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU **

## bandit 6-7
bandit6@bandit:/$ find -size 33c -user bandit7 -group bandit6 -ls
   77144      4 -rw-r-----   1 bandit7  bandit6        33 Apr 23 18:04 ./var/lib/dpkg/info/bandit7.password

** password = z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S **

## bandit 7-8
 bandit7@bandit:~$ grep millionth data.txt
millionth    TESKZC0XvTetK0S9xNwm25STk5iWrBvP

## bandit 8-9
bandit8@bandit:~$ sort data.txt -d | uniq -c
     10 08Jd2vmb6FjR4zXPteGHhpJm8A0OOA5B
     10 0dEKX1sDwYtc4vyjrKpGu30ecWBsDDa9
     10 0YDTDPCLc585IaFu911ukE9QfD6Ykrlz
     10 0zP9wfUcMKjZM2hiQUYR1nTfmaRdYSQE
     10 11FFcDRW5ZXXmX7geZORYRwiJfj8B3Gh
     10 1jZv2X1O2JypCBIgDNRwWQzS1CyhvByt
     10 1MUdfR7bGGCpNfGEOXaIEdrA8hT2L8Tk
     10 2fepTygKSkWHQJS2GrmGwjyl36eXSWJe
     10 3cTCUFe6MTl1FDAL0Z49cRByfq1MRlxJ
     10 3PB0nBOh1WKb1K6MImHdvwQjItFcxfdF
     10 3QXFsSepZUIOznxndwnQNnxvbpcXG05c
     10 47eFxPAuZ4tlWbT4P5ADs1tC0twlr51V
     10 4aOtDpqjXGIMOcyqirndla7J8S3jZZAy
     10 4Fi1Ig3hG4mDdl64v3gRPre3qNx26k0U
     10 4u67BT7FonRZeibEb9iOl6pHcMtzq03H
     10 6R258gRryXf9CBoG6erTEgGjb8ykWYrV
     10 7J5LX5IxjJ75DSStY7k9QTXgY8Hcygxu
     10 7rUrQcuUE8W3u7sHw6GqIw5KIm1vnvT0
     10 8fa6npI57h2Bc2yVSHJTKYwkGF1f25nm
     10 8mUGsbsFDyMVhqsbCIu5VQdKyNS6B4yK
     10 9b0fkcvfVG8ClmKfqmzFFSxszfYoGje3
     10 9rdQWtaWPaCwsiYUmcR7DZsTjlDzCIDk
     10 9uChpqBSAkMtOSNBVj1HAzRR5SQePFZe
     10 a6SMGsFpTKq8UGdndarh86o0ohHccjb0
     10 AWuhqidoTFNEaYmsX7njF8elfk6UTt8V
     10 Bap5iwr9yiz7NNLdn2pRIBDuzjS4apt6
     10 bbFQ44ZGHTUPiPEBvfADGWpwXzdhco23
     10 cBuyMeLeTl5bFQMjlzWIGHpbVwqQZkWQ
     10 cmtlazWcnfmS07dz52EdwhfVXD5hm8Ox
     10 DCEBvsEhDdFKdhuYgoK5615G0hkxkRbS
     10 dMNfFW0t7tDLsN6jM4t15q7sGdXIJlDO
      1 EN632PlfYiZbn3PhVK3XOGSlNInNE00t
     10 EoxGdakqWSJE03uzpJBLKabYEb5J458U
     10 eRgm0TR1FqHWaSneu0XDIC7r2MZVeLMU
     10 FJHGxIQ8lboC0UFsaF91voZjntUpyHPW
     10 FUx7SEMtclai0dBobiV7AbALW69gIBXZ
     10 FyYEOUkyJZD6zV0jpupw2KT8s82SRqMW
     10 gbvJah32y6gjm2AFPdOBRHJ8iCojKRrM
     10 gByqAo56n9wcRfMCkURoEB6JDzo0koeB
     10 H06jDLvch1Uq9N3QIOjHGmt1G34Gu5WM
     10 H8EBEqXygVzAE1hqQL8hmm5T5QC2D0rO
     10 HQxr86CUUjCkJw3NAMKRh58nsrrj0MvD
     10 hTG5ZZVYTMdjYXsfPkhvyoAmJjdq9C8P
     10 i2B5hPBHqvuFHFgKLtRAraOeCSnf0t2N
     10 I2Bcs4Rj9yrvTEjKhvLv0e5xZAiFKTN5
     10 I2Fe3M2fsgREVi1t7gsF7BUeii95f1vA
     10 i4nyRlk5UsNce0xutOfeTvK7LOmvQiqc
     10 iruOHH7XTt9nTI4Gx7siKujRGJjJjwSK
     10 ITQY9WLlsn3q168qH29wYMLQjgPH9lNP
     10 ixUopdQaDHWTH5oW0lqe17FmRIWemARs
     10 JddNHIO2SAqKPHrrCcL7yTzArusoNwrt
     10 JHuHJ4RkyqhV4yawJ4M7vztZYLQXmbyu
     10 JI1N2QF0ztjs2IXNOWCW4lkyMXN83xRJ
     10 jOtUiI3GKTuTNRl6BhEe2qdBHCdVJNLR
     10 kas4TO2Bk2KZgPbOqm1lCgwdv0X9Nu1L
     10 kbWzBlmQqHogFQlrHFwIXR4WDYOP0rzY
     10 kPs5Xm6uNWF7XmlOuAEMRYONR7cj8HvJ
     10 KzsSoDTds9Q8qA3uRuxg7og60JZ93tdA
     10 l4gvzZTw1FF3we43Vi4t6sSooCRHWnGW
     10 LHdCVT0iGyBfIK20to1WrWKMhJRmpW66
     10 lpRbCU2vMhGMRbAv65HhLyKEauDjtzeh
     10 lqxcTXcF9EuMgNF9J2TeEwKvz9ZoSGeZ
     10 LWbyPVHJfWrCcic0nuzZVWGnkiPq3mSo
     10 lzyn2IJxShNscaNmM8m5yQvViw5qluaU
     10 M14I2C6xu2tOmXvyWHIMuFaxktQOtIFs
     10 MDmXBu8iPJl03znbQctcHj8oCZbulXDS
     10 N2I3twf58Vw76J8n7sixyDqxKybAeUcQ
     10 NaOfWAtaagxr32dnqud7mkYeCsSH5BDB
     10 o7U2dEUFSCmddG7CGlgZxohaMKTBbTQ8
     10 OCIRfgKSXxjLD5YCbwGJBBg2OcOCvgxd
     10 pI3SEH0Rq3gd0sNEi8038Sh5SAtY1nrR
     10 QbKQeOYoUQULmEFOvagIzwC3EF2Gmu1S
     10 qeQlhBkJIQ9Yg7JSGavnLVpGXTTCSOyw
     10 QPghVHMln5b5ckZQQ4GrJkL69sCQCNp7
     10 QWiiBJhqUoMj0lCD9XNrkTM1M94eIPMV
     10 s00Iqlwp2FLBVu5yZFazJrpjypOL5sru
     10 S9dq4wwCTyH9TyUrDfO8bOVywef9rVsh
     10 s9wGQkxKUMfEW0ulhF1QuCfkK1x06RLZ
     10 TeLCC3zSYgKgI2wlYE2tO5vzaeEKkzXO
     10 TiXMHNCJEvOQyLXoZhDMdFpmXfR7orEU
     10 tpAGLljTdBsRqjZI9vIc3CpbaDAB9MTN
     10 tWedWHXUyRvVn4vH0I3zJcD3rdI48WrC
     10 txpoO5Sv4NR55wTu62j7uGlRKNxridyM
     10 uaKvbirBhTjHpZNhGKGgpuBygADEEOfo
     10 UkKkkIJoUVJG6Zd1TDfEkBdPJptq2Sn7
     10 UsCWtdouvPXeu6zkAx1dzviUyNnbEgCk
     10 uuax66Z7cDLABlBkrIMsqPUTyQDXsDqL
     10 Uy1DDzbL8hoD4nY8PHzSPbtkoJG9BKpO
     10 vmg8trbLZvXazswE0yEND17vH978enVX
     10 VOhHVQ6DG3wyFZoEYbfUMboYycjFeuDF
     10 vUazil5hHRQ63T0cQlfK5CV8MOrpDSBX
     10 W576pWH7nfuesidcso7OvqqviVVss1ms
     10 wiwZ8UvDRBE36vjUdEcK3g7KiOsQ2E2c
     10 wObmKQw05XwirIfvzToTNd7GZhkPeIfN
     10 WYU7r3ZVSfNk3WEvu5T7HDAAHIryHzNR
     10 XBrYZfQUBd5NJdAbSOG92hsfAEnhE8YO
     10 XHvIqr0IlONuOjXsOiHtDDuUk66tYJBY
     10 XK6pbTxxVhc0CSi7Y5rXtVkpWL4KdTTp
     10 yhJxWzo1jFPzfs1RP6cGonphKTjFVBXg
     10 YHtWBWO7CPN1EV2qcSnAtSl8Xi9kLtQI
     10 yvtL2C3x6iw7XOluSnoS1avXFUCsRSfg


** password=EN632PlfYiZbn3PhVK3XOGSlNInNE00t **


## level 9-10
bandit9@bandit:~$ strings data.txt
B4Qle
x<9s
f`    W0
?`YOd45
Iiuv
|S5j
hZOh|
Q~4    py
1Jec
EA    k
HZpEm
hI! 
7wzP
4========== the#
~u#Cudf
pc65
<@af
$3_*
^,tN
h.(    
88Iip
hi44
JJpzD1
VY'M
IbU#
{84W
XVnM
,Ek{
QSs^A
$iV5X
?'tb-
.'FEf:
kI%+
nj+T
z]Ju
{:6|
hFQk
WLaM
WZ<g
xw    Z
:b6w`
vakTv
W6)>_]_
h7m>
#pC'r]t
YZ2]
e AZ
>m]Br
%!F8
64uz
7b7 $F
68q)
kZM\n&
zM9d9
5P=GnFE
l'8rr`Btp
9,"F
~lyc
i}A.
R2wc
JK5E #
A~Jk>
n<mW
L7J%k
ys_?^
========== password
'DN9=5
s$yof
`@q!
[R~>{,8
XLFtt
T^+k
RCuE
)ZewS
%~mn    
RCed
+/[V
<#RY
ELuh
#/jr
9:    M
]Kff
G,x}
>,|W
F"rN i
?Vg*
    o|ubv
Q.dPY/z
========== is
[D")
T$h_
Xj|o3
YP"/
]+@e
Hc!z!
v<*>_
6)V(l
[Vl7
`NaT
]X8i
r_k/n
y\1b
%@K1
$Z=_
=TU%
]5Yy
/8Q 
dv5eG{
GK1g
#^@!
m{6Vd
HQ%F
p;Oir_^
a%v6s<t
5CI[
%@W!
5hzW
_URt
Q7?s
=^,T,?
4?A{
'.    dz
<8~V
g}h/i
md_y
!9qv
QH0i
,71]
+WYdA
f(iYzI
B5{I
6:u}
+q]EF
d~{N
94g!
ox!s
DJK.
`Ol[
B&2P
$7\U
?\bI
'v6n
hW,6
p0Jd
YNd\
B)BT
#+<}5
%O8]
WxX:
jXWSD
~n|"
O#4PgZ
oW._i<
(]Cr
GYTz
O{&^
W=y 
q=W 
K^v9T
N&J[
C!Gcb
Z~k"rs
gk7q
(;fH
&3T\
R6f1;
5\%?
 {Js~3
$Uf>
n7 BM
i3!x
j#Jg
]#[9
.WwIL&Rb#
Uc/G&
tPee
X=K,
)vNw
UYKPT
fXqk{~
c)Gv
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
}    H\QXV
:$u5K@9M
|kSn
<^H`n
'OX{ob
eI-'
mkvs
]kvN
&S=(
[LhHJ
R>0I
TG~:
,w|Z    D
7e`k+
NyoG
e-tY
YiEl\*e
nd?=
^4>AREf
j/!a'
5#sb
);J:
o+Ma
>ZOx
*x!g
5fV^{g-u
(?@1

the strings command is used to extract printable character strings from binary files. It is typically used to search for human-readable text within binary files, such as executable files or library files.


** password = G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s **

## level 10-11

bandit10@bandit:~$ base64 data.txt -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

## level 11-12

bandit11@bandit:~$ tr 'A-Za-z' 'N-ZA-Mn-za-m'<data.txt
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


## level 12-13

recursively decompressing bzip2 gzip and tar files by commands: 

bandit12@bandit:/tmp/level12/yo$ tar -xf data.txt
bandit12@bandit:/tmp/level12/yo$ gzip -d <new.txt>data.txt
bandit12@bandit:/tmp/level12/yo$ bzip2 -d <data.txt>new.txt

** password = wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw **

## level 13-14

ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220


## level 14-15

bandit14@bandit:/etc/ssh$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr













 

