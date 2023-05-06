## 0
```console
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit0@bandit:~$
```
## 1
```console
bandit1@bandit:~$ cat ./'-'
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
```
## 2
```console
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat ./"spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```
## 3
```console
bandit3@bandit:~$ ls -a
.  ..  .bash_logout  .bashrc  inhere  .profile
bandit3@bandit:~$ cat ./inhere
cat: ./inhere: Is a directory
bandit3@bandit:~$ cd ./inhere
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ ls -a -l
total 12
drwxr-xr-x 2 root    root    4096 Apr 23 18:04 .
drwxr-xr-x 3 root    root    4096 Apr 23 18:04 ..
-rw-r----- 1 bandit4 bandit3   33 Apr 23 18:04 .hidden
bandit3@bandit:~/inhere$ cat ./'.hidden'
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```
## 4
```console
bandit4@bandit:~/inhere$ find -type f | xargs file
./-file03: data
./-file06: data
./-file08: data
./-file07: ASCII text
./-file04: data
./-file00: data
./-file01: data
./-file02: data
./-file09: Non-ISO extended-ASCII text, with no line terminators
./-file05: data
bandit4@bandit:~/inhere$ cat ./'-file07'
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```
## 5
```console
bandit5@bandit:~/inhere$ man find
bandit5@bandit:~/inhere$ find -type f -size 1033b
bandit5@bandit:~/inhere$ find -type f -size b
find: Invalid argument `b' to -size
bandit5@bandit:~/inhere$ find -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```
## 6
```console
bandit6@bandit:~$ find / -type f -size 33c -user bandit7 -group bandit6 -readable
find: ‘/var/log’: Permission denied
find: ‘/var/crash’: Permission denied
find: ‘/var/spool/rsyslog’: Permission denied
find: ‘/var/spool/bandit24’: Permission denied
find: ‘/var/spool/cron/crontabs’: Permission denied
find: ‘/var/tmp’: Permission denied
find: ‘/var/lib/polkit-1’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/lib/chrony’: Permission denied
... a lot more "permission denied"s later ...
find: ‘/sys/fs/pstore’: Permission denied
find: ‘/sys/fs/bpf’: Permission denied
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```
## 7
```console
bandit7@bandit:~$ grep data.txt -e "millionth" -n
8994:millionth  TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```
## 8
```console
bandit8@bandit:~$ sort data.txt | uniq -c
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
```
## 9
```console
bandit9@bandit:~$ grep -a '==' data.txt
ep�f��x��PJ�e��]s��42��,h��GT\���A�P&����hI! ��lD��L��x�ִK}�v�JjP�գ��V���{z��7wzP����9Ū%�CIyb�q��i�&&�/C��q (�R���R���S�Q~�AD�7��F5Ď��!G8K��u�_��0�&ÓT���MK@��4=
�C��;aG��|B��s��=�~u#Cudf
�?� ��?l�eM��q��딕B�YBn�KI�ao��ٰ�     �=�ys_?^�J���========== password�#��J\9�Þ�a���q.�����zf�4��il�v�՗��Lt|����q쎢��?�诃�Hf��:�n&��4
                                    �W��Ժ�ݭ4�v�8��4mm��*�W�ll�6�����˻��m"���;=��2��I�Q��_�1BV�L��d6�T�6+ʝw�n���M�iԁ�
�#;��8���=Td��w���i�m��vq���&���N=��4�?{���%>-XUZg�5Nզ   o|ubv�hZ�h��j`�d��苺1�6�❨�����Yp���}]@�6a@��(�9],͑0��/"�j.�!����0�҂�z�3W�J"�[�j��#"q�Ա7
                                                                          d�پ/
                                                                              3Ы�=/A�S����vԕ���k�;5�(ͤãp�"]��.������
                                �Q.dPY/z���M��ȱK~3���K<���3N;��Y�J���hl���F���w8�5�o�X��<g1�========== is�c{�
�J�'Pc�����k�i��       ��
                 N��[�a-�@#=�-����ڀ��M`^��f        F��JW���8��],����c0����"��N.a����f��f�S�ӭ�
              �Ѥ|��+#��{���@_)�#T�TT�QA�3Y�ⱄg�w�f!(IG���I��M_�K��Fz�E��R�(#3���o��!��7�M�$�漸T%��{�޾��[D")l4z�z'~��6�l�D#�s�O�ݠ��)��r3���M<��h��ǥwϖ��7���
                                                                                   �3 ��8E�T$h_Y�HÁ��=M��m�9xu��z�鱍T�vL�
                                       ��8`;c�2���\���[D#
ɝ��c    �7�{��qî�Ņ�^�)A6�\���UYKPT�fXqk{~��     ܥ`�0%�Q�Xde����5�朁��O�5�3��J�d�ݜ����*D���f��C�4��U��t��*����R�+�د"�\�
؜�H]+�D���~��"��9�1t��*�b�`�K�ʫ���
                                          
                                          �٨M���t�o��<�.��"�g˘JH)��l&���=������*����R-�C�========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```
## 10
```console
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```
## 11
```console
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```
## 12
```console
bandit12@bandit:/tmp/mine123$ cat data9.bin
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```
## 13
```console
rodger2041@LAPTOP-CH89DDGF:~$ scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit13@bandit.labs.overthewire.org's password:
sshkey.private                                       100% 1679     9.6KB/s   00:00
rodger2041@LAPTOP-CH89DDGF:~$ ls -a
.              .bash_logout  .lesshst     .profile                   .viminfo
..             .bashrc       .local       .ssh                       sshkey.private
.bash_history  .gitconfig    .motd_shown  .sudo_as_admin_successful
rodger2041@LAPTOP-CH89DDGF:~$ chmod 600 sshkey.private
rodger2041@LAPTOP-CH89DDGF:~$ ssh -i ./sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```
## 14
```console
bandit14@bandit:/etc/bandit_pass$ cat bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
bandit14@bandit:/etc/bandit_pass$ ^C
bandit14@bandit:/etc/bandit_pass$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```
## 15
```console
bandit15@bandit:~$ openssl s_client -connect localhost:30001
```