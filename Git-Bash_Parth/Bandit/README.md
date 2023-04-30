## Level 1 -> 2
```console
$ cat ./-
```
## Level 2->3
```console
$ cat spaces\ in\ this\ filename
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
#Tab complete 
```
## Level 3->4
```console
$ cd inhere/
$ ls
$ ll
total 12
drwxr-xr-x 2 root    root    4096 Apr 23 18:04 ./
drwxr-xr-x 3 root    root    4096 Apr 23 18:04 ../
-rw-r----- 1 bandit4 bandit3   33 Apr 23 18:04 .hidden
$ cat .hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```
## Level 4->5
```console
$ cd inhere
$ tail ./-file0{0..9}
==> ./-file00 <==
�Ű��Bη���b<Q�Ƞ�+V�iO�1�[5{�
==> ./-file01 <==
jmD�B�0D�tQ*��)�A���V �]Ȕl�
==> ./-file02 <==
x(�z�.T26 F8qqlY���v�FN#��'~
==> ./-file03 <==
�E�Q�"�p�
����4�}�]��G�A��u[�/9�
==> ./-file04 <==
�Mrj�S�r_E�,���G+�h|�+
�=>KQ�
==> ./-file05 <==
2��]o-p8q�츑���D�
                 .~�&ϯ"PT�I
==> ./-file06 <==
'�cwk^j�����M����;,��co�9
==> ./-file07 <==
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

==> ./-file08 <==
�׉ǰ�6=�>>�ӫ�w�<U'=�@��Z�xj
==> ./-file09 <==
�?3��[ٲN|?�G|b�G�[8�y�-�́*�
                          ��
```
## Level 5->6
```console
$ cd inhere
$ find . -type f -size 1033c 
./inhere/maybehere07/.file2
$ cat ./inhere/maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
```
## Level 6->7
```console
$ cd /
$ find . -type f -user bandit7 -group bandit6 -size 33c
find: ‘./var/log’: Permission denied
find: ‘./var/crash’: Permission denied
find: ‘./var/spool/rsyslog’: Permission denied
find: ‘./var/spool/bandit24’: Permission denied
find: ‘./var/spool/cron/crontabs’: Permission denied
find: ‘./var/tmp’: Permission denied
find: ‘./var/lib/polkit-1’: Permission denied
./var/lib/dpkg/info/bandit7.password
find: ‘./var/lib/chrony’: Permission denied
find: ‘./var/lib/apt/lists/partial’: Permission denied
find: ‘./var/lib/amazon’: Permission denied
find: ‘./var/lib/update-notifier/package-data-downloads/partial’: Permission denied
find: ‘./var/lib/snapd/void’: Permission denied
find: ‘./var/lib/snapd/cookie’: Permission denied
find: ‘./var/lib/ubuntu-advantage/apt-esm/var/lib/apt/lists/partial’: Permission denied
find: ‘./var/lib/private’: Permission denied
find: ‘./var/snap/lxd/common/lxd’: Permission denied
find: ‘./var/cache/ldconfig’: Permission denied
find: ‘./var/cache/apt/archives/partial’: Permission denied
find: ‘./var/cache/pollinate’: Permission denied
find: ‘./var/cache/private’: Permission denied
find: ‘./var/cache/apparmor/a4dd844e.0’: Permission denied
find: ‘./var/cache/apparmor/8eeb6286.0’: Permission denied
find: ‘./drifter/drifter14_src/axTLS’: Permission denied
find: ‘./home/bandit29-git’: Permission denied
find: ‘./home/drifter6/data’: Permission denied
find: ‘./home/bandit28-git’: Permission denied
find: ‘./home/drifter8/chroot’: Permission denied
find: ‘./home/ubuntu’: Permission denied
find: ‘./home/bandit5/inhere’: Permission denied
find: ‘./home/bandit27-git’: Permission denied
find: ‘./home/bandit30-git’: Permission denied
find: ‘./home/bandit31-git’: Permission denied
find: ‘./boot/efi’: Permission denied
find: ‘./proc/tty/driver’: Permission denied
find: ‘./proc/1302400/task/1302400/fdinfo/6’: No such file or directory
find: ‘./proc/1302400/fdinfo/5’: No such file or directory
find: ‘./etc/polkit-1/localauthority’: Permission denied
find: ‘./etc/ssl/private’: Permission denied
find: ‘./etc/multipath’: Permission denied
find: ‘./etc/sudoers.d’: Permission denied
find: ‘./dev/mqueue’: Permission denied
find: ‘./dev/shm’: Permission denied
find: ‘./tmp’: Permission denied
find: ‘./snap/core18/2721/etc/ssl/private’: Permission denied
find: ‘./snap/core18/2721/root’: Permission denied
find: ‘./snap/core18/2721/var/cache/ldconfig’: Permission denied
find: ‘./snap/core18/2721/var/lib/private’: Permission denied
find: ‘./snap/core20/1852/etc/ssl/private’: Permission denied
find: ‘./snap/core20/1852/root’: Permission denied
find: ‘./snap/core20/1852/var/cache/ldconfig’: Permission denied
find: ‘./snap/core20/1852/var/cache/private’: Permission denied
find: ‘./snap/core20/1852/var/lib/private’: Permission denied
find: ‘./snap/core20/1852/var/lib/snapd/void’: Permission denied
find: ‘./lost+found’: Permission denied
find: ‘./run/chrony’: Permission denied
find: ‘./run/user/11007’: Permission denied
find: ‘./run/user/11029’: Permission denied
find: ‘./run/user/11027’: Permission denied
find: ‘./run/user/11017’: Permission denied
find: ‘./run/user/11016’: Permission denied
find: ‘./run/user/11023’: Permission denied
find: ‘./run/user/11008’: Permission denied
find: ‘./run/user/11011’: Permission denied
find: ‘./run/user/11021’: Permission denied
find: ‘./run/user/11014’: Permission denied
find: ‘./run/user/8004’: Permission denied
find: ‘./run/user/11002’: Permission denied
find: ‘./run/user/11025’: Permission denied
find: ‘./run/user/11032’: Permission denied
find: ‘./run/user/11004’: Permission denied
find: ‘./run/user/11013’: Permission denied
find: ‘./run/user/11015’: Permission denied
find: ‘./run/user/11006/systemd/inaccessible/dir’: Permission denied
find: ‘./run/user/11005’: Permission denied
find: ‘./run/user/11001’: Permission denied
find: ‘./run/user/11012’: Permission denied
find: ‘./run/user/11020’: Permission denied
find: ‘./run/user/11000’: Permission denied
find: ‘./run/user/11024’: Permission denied
find: ‘./run/sudo’: Permission denied
find: ‘./run/screen/S-bandit15’: Permission denied
find: ‘./run/screen/S-bandit1’: Permission denied
find: ‘./run/screen/S-bandit23’: Permission denied
find: ‘./run/screen/S-bandit24’: Permission denied
find: ‘./run/screen/S-bandit17’: Permission denied
find: ‘./run/screen/S-bandit3’: Permission denied
find: ‘./run/screen/S-bandit20’: Permission denied
find: ‘./run/screen/S-bandit0’: Permission denied
find: ‘./run/screen/S-bandit25’: Permission denied
find: ‘./run/multipath’: Permission denied
find: ‘./run/cryptsetup’: Permission denied
find: ‘./run/lvm’: Permission denied
find: ‘./run/credentials/systemd-sysusers.service’: Permission denied
find: ‘./run/systemd/propagate’: Permission denied
find: ‘./run/systemd/unit-root’: Permission denied
find: ‘./run/systemd/inaccessible/dir’: Permission denied
find: ‘./run/lock/lvm’: Permission denied
find: ‘./root’: Permission denied
find: ‘./sys/kernel/tracing’: Permission denied
find: ‘./sys/kernel/debug’: Permission denied
find: ‘./sys/fs/pstore’: Permission denied
find: ‘./sys/fs/bpf’: Permission denied
$ cat "./var/lib/dpkg/info/bandit7.password"
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```
## Level 7->8
```console
$ ls
data.txt
$ cat data.txt | grep millionth
millionth       TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```
## Level 8->9
```console
$ sort data.txt | uniq -c | grep ' 1 ' 
      1 EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```
## Level 9->10ROT13
```console
$ strings data.txt | grep '=='
4========== the#
========== password
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
```
## Level 10->11
```console
$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
$ cat data.txt  | base64 -d 
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```
## Level 11->12
```console
$ ls
data.txt
$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
```
```
Output after using cyberchef ROT13 decoder
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```
## Level 12->13
```console

$ mkdir /tmp/name1

$ cd /tmp/name1

$ cp /home/bandit12/data.txt data.txt

$ ls
data.txt

$ xxd -r data.txt new_file

$ file new_file
new_file: gzip compressed data, was "data2.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 581

$ gzip -d new_file
gzip: new_file: unknown suffix -- ignored

$ ls
data.txt  new_file

$ mv new_file new_file.gz

$ gzip -d new_file.gz

$ ls
data.txt  new_file

$ file new_file 
new_file: bzip2 compressed data, block size = 900k

$ bzip2 new_file

$ ls
data.txt  new_file.bz2

$ bzip2 -d new_file.bz2

$ ls
data.txt  new_file

$ bzip2 -d new_file
bzip2: Can't guess original name for new_file -- using new_file.out

$ mv new_file file.bz2
mv: cannot stat 'new_file': No such file or directory

$ ls
data.txt  new_file.out

$ file new_file.out 
new_file.out: gzip compressed data, was "data4.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 20480

$ mv new_file.out file.gzip

$ mv new_file.gzip file.gz
mv: cannot stat 'new_file.gzip': No such file or directory

$ mv file.gzip file.gz

$ ls
data.txt  file.gz

$ gzip -d file.gz 

$ ls
data.txt  file

$ file filw
filw: cannot open `filw' (No such file or directory)

$ file file
file: POSIX tar archive (GNU)

$ mv file file.tar

$ tar -xvf file.tar
data5.bin

$ ls
data5.bin  data.txt  file.tar

$ file data5.bin
data5.bin: POSIX tar archive (GNU)

$ tar -xvf data5.bin
data6.bin

$ file data6.bin 
data6.bin: bzip2 compressed data, block size = 900k

$ bzip2 -d data6.bin
bzip2: Can't guess original name for data6.bin -- using data6.bin.out

$ file data6.bin.out 
data6.bin.out: POSIX tar archive (GNU)

$ tar -xvf data6.bin.out
data8.bin

$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Sun Apr 23 18:04:23 2023, max compression, from Unix, original size modulo 2^32 49

$ gzip -d data8.bin
gzip: data8.bin: unknown suffix -- ignored

$ ls
data5.bin  data6.bin.out  data8.bin  data.txt  file.tar

$ mv data8.bin data9.bin

$ mv data9.bin data8.gz

$ gzip -d data8.gz 

$ ls
data5.bin  data6.bin.out  data8  data.txt  file.tar

$ file data8
data8: ASCII text

$ cat data8
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```

## Level 13->14
```console
$ ls
sshkey.private 
$ ssh -p 2220 -i sshkey.private bandit14@localhost
#You get to shell of bandit14
$ bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
```

## Level 14->15
```console
$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```

## Level 15->16
```console
$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Apr 26 00:56:39 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Apr 26 00:56:39 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Apr 26 00:55:39 2023 GMT; NotAfter: Apr 26 00:56:39 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEFFcfiTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwNDI2MDA1NTM5WhcNMjMwNDI2MDA1NjM5WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDp
Ku7a5QH2R4bSv0k410iSq1UOCSI4VPcsxctPdeHGvI/RVnkCYJkgubm9ultnpYew
rdlYSpJLskpoQANI/wkGhwMF9LOswUCpLCwr3gvkknU9tr92vNKPdkfLEJn1Pup+
MwKGnLZ2ZzNzC5JOu+IzHiRssfHhP9aMJaFjJwD0eEfOIh2t0cIblMFB3Gzk2FrI
uEDePfAmxXg/Qp4dgatbyM6I6rn/9UzEb5mIjw22kN5OjBp9DO+repcK5hQtJbXO
FdyK4cGz/Ds7Aoec+ifBfskEsGoQ+0dVJfs3bOcvrjfnE47TsUFsmwePkDdlk+Si
MrvhYede0UOkdsfHOPjrAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQCC
ucE91DmhCTTF+oGBHkg8SD21iJ9+5TT3hYcln9cwyOfF47MNV8Bi6zKpyE5JTTU2
gYDe8144nUyi5Yo54z2oo7mQYSAfMFl2azgRfRXEDNhfnTvPBI3tjuIgHcQXPSIP
u9vFIvHEF41wnbZjHhWPdvDidnWJP2SQ4Rxrrl1ZW3uf3YaoQV2iKpQzrUFFKUO0
PUZtjce7zSn3GpWpCJxuz0dSNf9RVW8qfIE3VRW96I9Kfhk74ozw4YOTLpLCkcMK
80iqEWsojaplcievflEAwHikjZbSib1eugNpVJIWlUEOr52Wrbi4Ib6/v5khhlBt
AUV7MeIAqxsrUfT720GY
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 46C24A424BAF054315780FB8258890F6439F6F7046DD219D52C2EE47D2001362
    Session-ID-ctx: 
    Resumption PSK: 88E9A79AEF621053179F4240344EE662439C0F6B5D7411B7D7B471CFAAD1B889826CCC888190286243020481EDE70423
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 65 99 98 87 ff 71 4a 70-7c e7 20 71 00 d7 9a 9d   e....qJp|. q....
    0010 - 19 d1 a2 8f f6 2b a6 67-94 fc 0f 09 de 85 fd 12   .....+.g........
    0020 - 37 5e 32 da 21 7b 51 f4-62 67 17 c2 d3 85 b7 0b   7^2.!{Q.bg......
    0030 - 82 8f c0 bd 8b 77 1e dd-f0 3b a9 28 f8 70 3b 01   .....w...;.(.p;.
    0040 - b8 84 5b 85 10 01 d1 c0-ff 61 5d 8f ed e7 16 ea   ..[......a].....
    0050 - 7d 53 18 f8 30 51 5b ad-96 fe 82 27 9e 94 1b bf   }S..0Q[....'....
    0060 - 95 2a d6 df 45 84 52 7b-e4 9b 35 91 e9 be 4a 5e   .*..E.R{..5...J^
    0070 - 8e bd 50 41 c4 8c d3 8f-0e 5c 39 b2 b7 d4 1e cf   ..PA.....\9.....
    0080 - aa 14 a6 b7 c7 0a 62 79-8f 0e 4d 6f a1 04 e0 ca   ......by..Mo....
    0090 - d3 dd 94 2e 73 18 47 40-de 0e 91 41 ba 31 22 33   ....s.G@...A.1"3
    00a0 - df a6 b6 a7 21 59 b5 db-09 13 98 cb 4e 7f 52 90   ....!Y......N.R.
    00b0 - 1f 31 eb 6c 3a 9b d0 a2-02 73 fc e4 c1 b5 cc 56   .1.l:....s.....V
    00c0 - 23 48 fc 81 17 65 7d 02-46 51 a3 8d a3 cc 70 e1   #H...e}.FQ....p.

    Start Time: 1682884870
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 8FBC75D40FFF6B394A063D6536BC1678357A478A75731F317F6E3BE75DC983EA
    Session-ID-ctx: 
    Resumption PSK: E1DEA5A168198E3D9AD2B65A7B5431C086C5E54EA425E4894844120146AD2F52144A58111E4C9B99D7D213D0554B28E5
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 65 99 98 87 ff 71 4a 70-7c e7 20 71 00 d7 9a 9d   e....qJp|. q....
    0010 - 28 15 33 cc 5b 7c fd 74-bd 4b aa c9 2e 97 f0 5c   (.3.[|.t.K.....\
    0020 - 5f 7d 5d f3 08 fc 4e 40-e0 00 0e b2 62 36 2b bc   _}]...N@....b6+.
    0030 - 1e b3 7b 29 cf d0 48 6e-8c 5c e7 48 6a e7 7c c9   ..{)..Hn.\.Hj.|.
    0040 - 5e dc a6 3a 3e 1f d3 5e-1f 1d 89 85 d1 23 58 f5   ^..:>..^.....#X.
    0050 - c1 c4 f2 f1 1b d0 1b 61-18 0c 23 0b fc b4 eb e2   .......a..#.....
    0060 - 11 7a a5 72 8a 47 20 4e-ef d5 98 f8 7a ef b0 a2   .z.r.G N....z...
    0070 - 0f 09 6c c4 7e 51 63 cf-c0 96 69 59 a0 42 5a f3   ..l.~Qc...iY.BZ.
    0080 - 45 99 3d fb 3b c8 5a 85-9b d2 8c c1 e1 70 07 5a   E.=.;.Z......p.Z
    0090 - 0c 40 04 ba be 52 40 57-96 22 fd 45 07 ae a7 45   .@...R@W.".E...E
    00a0 - b7 8c cf fb a1 d9 56 2b-fe fa f2 6d f8 f8 2a a4   ......V+...m..*.
    00b0 - 2c d8 d0 73 0e d5 45 59-6e 9b bc 0b 4f d0 aa 8a   ,..s..EYn...O...
    00c0 - 35 f9 7f 50 99 3f 09 2d-7c 3d 89 e5 fe b1 e4 ab   5..P.?.-|=......

    Start Time: 1682884870
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
```