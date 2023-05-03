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

 

