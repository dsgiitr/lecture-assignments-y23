# Problem 3
## Lab 1 (Setup)
```console
parth_badgujar@Parth:~$ git config --global user.name "Parth Badgujar"
parth_badgujar@Parth:~$ git config --global user.email "parthbadgujar57@gmail.com"
parth_badgujar@Parth:~$ git config --global core.autocrlf input
parth_badgujar@Parth:~$ git config --global core.safecrlf true
parth_badgujar@Parth:~$ sudo apt install ruby-full
```
## Lab 2 (More Setup)
```console
$ wget http://gitimmersion.com/git_tutorial.zip
--2023-04-28 05:49:59--  http://gitimmersion.com/git_tutorial.zip
Resolving gitimmersion.com (gitimmersion.com)... 64:ff9b::b9c7:6d99, 64:ff9b::b9c7:6e99, 64:ff9b::b9c7:6f99, ...
Connecting to gitimmersion.com (gitimmersion.com)|64:ff9b::b9c7:6d99|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://gitimmersion.com/git_tutorial.zip [following]
--2023-04-28 05:49:59--  https://gitimmersion.com/git_tutorial.zip
Connecting to gitimmersion.com (gitimmersion.com)|64:ff9b::b9c7:6d99|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1082252 (1.0M) [application/zip]
Saving to: ‘git_tutorial.zip’

git_tutorial.zip                        100%[=============================================================================>]   1.03M  1.68MB/s    in 0.6s    

2023-04-28 05:50:00 (1.68 MB/s) - ‘git_tutorial.zip’ saved [1082252/1082252]
$ unzip git_tutorial.zip
```
## Lab 3 (Create a Project)
```console
$ mkdir hello
$ cd hello
#Changed directory to hello
$ echo 'puts "Hello, world"' > hello.rb
$ git init
Initialized empty Git repository in /home/parth_badgujar/Desktop/DSG Assignment/Problem 2/hello/.git/
$ git add hello.rb
$ git commit -m 'First Commit'
[master (root-commit) f03621e] First Commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.rb
```
## Lab 4 (Checking Status)
```console
$ git status
On branch master
nothing to commit, working tree clean
```
## Lab 5 (Making Changes)
```console
$ echo 'puts "Hello, #{ARGV.first}!"' > hello.rb
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
```
## Lab 6 (Staging Changes)
```console
$ git add hello.rb
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
  modified:   hello.rb
```
## Lab 7 (Staging and Committing)
```console
#Created a.rb and b.rb according to lab
$ git add a.rb
$ git add b.rb
$ git commit -m "Chages for a and b"
[master 1b79fc5] Chages for a and b
 3 files changed, 3 insertions(+), 1 deletion(-)
 create mode 100644 a.rb
 create mode 100644 b.rb
#Created c.rb
$ git add c.rb
$ git commit -m "Unrelated change to c"
[master 5d5596e] Unrelated change to c
 1 file changed, 1 insertion(+)
 create mode 100644 c.rb
```

## Lab 8 (Committing Changes)
```console

```

## Lab 9 (Changes, not Files)
```console
#changed hello.rb
$ git add hello.rb
#changed  hello.rb again
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.rb

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb
$ git commit -m "Added a default value"
[master bbcc511] Added a default value
 1 file changed, 3 insertions(+), 1 deletion(-)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb
no changes added to commit (use "git add" and/or "git commit -a")
$ git add .
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.rb
$ git commit -m "Added a comment"
[master e046030] Added a comment
 1 file changed, 1 insertion(+)
```
## Lab 10 (History)
```console
$ git log
commit e046030264dd871a7e2e65bb3208c68bd6058a9e (HEAD -> master)
Author: Parth Badgujar <parthbadgujar57@gmail.com>
Date:   Fri Apr 28 06:09:08 2023 +0530

    Added a comment

commit bbcc5114028e78ca94a33d95ff495e4c099e1738
Author: Parth Badgujar <parthbadgujar57@gmail.com>
Date:   Fri Apr 28 06:07:53 2023 +0530

    Added a default value

commit 5d5596eba56c02613bf1209d68590b6770349c63
Author: Parth Badgujar <parthbadgujar57@gmail.com>
Date:   Fri Apr 28 06:01:57 2023 +0530

    Unrelated change to c

commit 1b79fc54b4f4f5e82679ffb51e782932727e0cc0
Author: Parth Badgujar <parthbadgujar57@gmail.com>
Date:   Fri Apr 28 06:01:17 2023 +0530

    Chages for a and b

commit f03621e4017bccafed9edab12775f378e8aa1a28
Author: Parth Badgujar <parthbadgujar57@gmail.com>
Date:   Fri Apr 28 05:55:17 2023 +0530

    First Commit

$ git log --pretty=oneline
e046030264dd871a7e2e65bb3208c68bd6058a9e (HEAD -> master) Added a comment
bbcc5114028e78ca94a33d95ff495e4c099e1738 Added a default value
5d5596eba56c02613bf1209d68590b6770349c63 Unrelated change to c
1b79fc54b4f4f5e82679ffb51e782932727e0cc0 Chages for a and b
f03621e4017bccafed9edab12775f378e8aa1a28 First Commit

$ git log --pretty=oneline --until='5 minutes ago'
e046030264dd871a7e2e65bb3208c68bd6058a9e (HEAD -> master) Added a comment
bbcc5114028e78ca94a33d95ff495e4c099e1738 Added a default value
5d5596eba56c02613bf1209d68590b6770349c63 Unrelated change to c
1b79fc54b4f4f5e82679ffb51e782932727e0cc0 Chages for a and b
f03621e4017bccafed9edab12775f378e8aa1a28 First Commit

$ git log --pretty=oneline --max-count=2
e046030264dd871a7e2e65bb3208c68bd6058a9e (HEAD -> master) Added a comment
bbcc5114028e78ca94a33d95ff495e4c099e1738 Added a default value

$ git log --all --pretty=format:'%h %cd %s (%an)' --since='7 days ago'
e046030 Fri Apr 28 06:09:08 2023 +0530 Added a comment (Parth Badgujar)
bbcc511 Fri Apr 28 06:07:53 2023 +0530 Added a default value (Parth Badgujar)
5d5596e Fri Apr 28 06:01:57 2023 +0530 Unrelated change to c (Parth Badgujar)
1b79fc5 Fri Apr 28 06:01:17 2023 +0530 Chages for a and b (Parth Badgujar)
f03621e Fri Apr 28 05:55:17 2023 +0530 First Commit (Parth Badgujar)

$ git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
* e046030 2023-04-28 | Added a comment (HEAD -> master) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit [Parth Badgujar]

```

## Lab 11 (Aliases)
```console
$ nano $(locate .gitconfig)
#Adding shortcuts to .gitconfig
```

## Lab 12 (Getting Old Versions)
```console 
$ git hist
* e046030 2023-04-28 | Added a comment (HEAD -> master) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit [Parth Badgujar]

$ git checkout f03621e
Note: switching to 'f03621e'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at f03621e First Commit

$ cat hello.rb
puts "Hello, world"

$ git checkout master
Previous HEAD position was f03621e First Commit
Switched to branch 'master'

$ cat hello.rb
# Default is "World"
name = ARGV.first || "World"

puts "Hello, #{name}!"
```

## Lab 13 (Tagging versions)
```console
$ git tag v1
$ git checkout v1^
Note: switching to 'v1^'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at bbcc511 Added a default value
$ cat hello.rb
name = ARGV.first || "World"

puts "Hello, #{name}!"

$ git tag v1-beta
$ git tag
v1
v1-beta
$ git checkout v1
Previous HEAD position was bbcc511 Added a default value
HEAD is now at e046030 Added a comment
$ git checkout v1-beta
Previous HEAD position was e046030 Added a comment
HEAD is now at bbcc511 Added a default value
$ git checkout master
Previous HEAD position was bbcc511 Added a default value
Switched to branch 'master'


$ git hist master --all
* e046030 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit [Parth Badgujar]
```


## Lab 14 [Undoing Local Changes (before staging)]
```console
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")


$ git checkout hello.rb
Updated 1 path from the index
$ git status
On branch master
nothing to commit, working tree clean
```

## Lab 15 [Undoing Staged Changes (before committing)]

```console 
$ git add hello.rb
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.rb

$ git reset HEAD hello.rb
Unstaged changes after reset:
M	hello.rb
$ git checkout hello.rb
Updated 1 path from the index
$ git status
On branch master
nothing to commit, working tree clean
```

## Lab 16 (Undoing Committed Changes)

```console
$ git add hello.rb
$ git commit -m "Didn't want this commit"
[master 5e62d80] Didn't want this commit
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git revert HEAD
[master 2067e76] Revert "Didn't want this commit"
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git hist
* 2067e76 2023-04-28 | Revert "Didn't want this commit" (HEAD -> master) [Parth Badgujar]
* 5e62d80 2023-04-28 | Didn't want this commit [Parth Badgujar]
* e046030 2023-04-28 | Added a comment (tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
```

## Lab 17 (Removing Commits from a Branch)

```console
$ git hist
* 2067e76 2023-04-28 | Revert "Didn't want this commit" (HEAD -> master) [Parth Badgujar]
* 5e62d80 2023-04-28 | Didn't want this commit [Parth Badgujar]
* e046030 2023-04-28 | Added a comment (tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
$ git tag oops
$ git reset --hard v1
HEAD is now at e046030 Added a comment
$ git hist
* e046030 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
$ git hist --all
* 2067e76 2023-04-28 | Revert "Didn't want this commit" (tag: oops) [Parth Badgujar]
* 5e62d80 2023-04-28 | Didn't want this commit [Parth Badgujar]
* e046030 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
```

## Lab 18 (Remove the oops tag)
```console
$ git tag -d oops
Deleted tag 'oops' (was 2067e76)
$ git hist --all
* e046030 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
```

## Lab 19 (Amending Commits)
```console
$ git add hello.rb
$ git commit -m "Add an author comment"
[master 9785942] Add an author comment
 1 file changed, 1 insertion(+)
$ git add hello.rb
$ git commit --amend -m "Add an author/email comment"
[master e7ddc80] Add an author/email comment
 Date: Fri Apr 28 08:29:14 2023 +0530
 1 file changed, 1 insertion(+)

$ git hist
* e7ddc80 2023-04-28 | Add an author/email comment (HEAD -> master) [Parth Badgujar]
* e046030 2023-04-28 | Added a comment (tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
```

## Lab 20 (Moving Files)
```console
$ mkdir lib
$ git mv hello.rb lib/hello.rb
$ git commit -m "Moved hello.rb to lib"
[master 073ac20] Moved hello.rb to lib
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename hello.rb => lib/hello.rb (100%)
```

## Lab 21 (More Structure)
```console
$ sudo gem install rake
[sudo] password for parth_badgujar: 
Successfully installed rake-13.0.6
Parsing documentation for rake-13.0.6
Done installing documentation for rake after 0 seconds
1 gem installed
$ git add Rakefile
$ git commit -m "Added a Rakefile"
[master 610ccb0] Added a Rakefile
 1 file changed, 7 insertions(+)
 create mode 100644 Rakefile
$ rake
Hello, World!
```

## Lab 22 (Git Internals: The .git directory)
```console
$ ls .git
branches  COMMIT_EDITMSG  config  description  HEAD  hooks  index  info  logs  objects  ORIG_HEAD  packed-refs  refs
$ ls -C .git/objects
07  12  16  17  18  1b  1d  20  2c  43  4d  59  5d  5e  61  69  6c  8e  90  96  97  9a  9d  bb  c8  d5  e0  e7  e8  f0  f3  fa  info  pack
$ ls -C .git/objects/07
3ac2045fa58c6fc0259d17a4cce642ffe546e8
$ cat .git/config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true

$ ls .git/refs/heads
master
$ ls .git/refs/tags
v0  v1  v1-beta  v2
$ cat .git/refs/tags/v1
e046030264dd871a7e2e65bb3208c68bd6058a9e


$ cat .git/HEAD
ref: refs/heads/master
```

## Lab 23 (Git Internals: Working directly with Git Objects)
```console
$ git hist
* 610ccb0 2023-04-28 | Added a Rakefile (HEAD -> master) [Parth Badgujar]
* 073ac20 2023-04-28 | Moved hello.rb to lib [Parth Badgujar]
* e7ddc80 2023-04-28 | Add an author/email comment (tag: v2) [Parth Badgujar]
* e046030 2023-04-28 | Added a comment (tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
$ git cat-file -t 610ccb0
commit
$ git cat-file -p 610ccb0
tree 438e67d10f2ea2f65d28115d23348843f2b0a22f
parent 073ac2045fa58c6fc0259d17a4cce642ffe546e8
author Parth Badgujar <parthbadgujar57@gmail.com> 1682653044 +0530
committer Parth Badgujar <parthbadgujar57@gmail.com> 1682653044 +0530

Added a Rakefile
$ git cat-file -p 438e67d
100644 blob 2c6d56e928587e058273c28ed488f3f17f6be08f	Rakefile
100644 blob e877167765e0d9f323dea8661ac0cee1c7e9fa9d	a.rb
100644 blob c85d2955dd875c955121cc09795f55d7b78b4e01	b.rb
100644 blob 12b953fdaf5ad32aa1aa5fe7845460818d172c6c	c.rb
040000 tree 966437bc15529cba3b3fce55a1326f78d08104a3	lib
$ git cat-file -p 2c6d56e
#!/usr/bin/ruby -wKU

task :default => :run

task :run do
  require './lib/hello'
end
$ git cat-file -p 966437
100644 blob fabafbda10f1b5d2d607aa8336342ad25f5e31ae	hello.rb
```

## Lab 24 (Creating a Branch)
```console
$ git checkout -b greet
Switched to a new branch 'greet'
$ git add lib/greeter.rb
$ git commit -m "Added a greeter class"
[greet 0193247] Added a greeter class
 1 file changed, 8 insertions(+)
 create mode 100644 lib/greeter.rb

$ git add lib/hello.rb
$ git commit -m "Hello uses Greeter"
[greet b512c4d] Hello uses Greeter
 1 file changed, 5 insertions(+), 3 deletions(-)
$ git add Rakefile
$ git commit -m "Updated Rakefile"
[greet 16ddd1b] Updated Rakefile
 1 file changed, 1 insertion(+), 1 deletion(-)
```

## Lab 25 (Navigating Branches)
```console
$ git checkout master
Switched to branch 'master'
$ cat lib/hello.rb
# Default is "World"
#Author : Parth (parth_db@ece.iitr.ac.in)
name = ARGV.first || "World"

puts "Hello, #{name}!"
$ git checkout greet
Switched to branch 'greet'
$ cat lib/hello.rb
require 'greeter'

# Default is World
name = ARGV.first || "World"

greeter = Greeter.new(name)
puts greeter.greet
```

## Lab 26 (Changes in Master)
```console
$ git add README
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   README

$ git commit -m "Added README"
[master 7acc3af] Added README
 1 file changed, 1 insertion(+)
 create mode 100644 README
```

## Lab 27 (Viewing Diverging Branches)
```console
$ git hist --all
* 7acc3af 2023-04-28 | Added README (HEAD -> master) [Parth Badgujar]
| * 16ddd1b 2023-04-28 | Updated Rakefile (greet) [Parth Badgujar]
| * b512c4d 2023-04-28 | Hello uses Greeter [Parth Badgujar]
| * 0193247 2023-04-28 | Added a greeter class [Parth Badgujar]
|/  
* 610ccb0 2023-04-28 | Added a Rakefile [Parth Badgujar]
* 073ac20 2023-04-28 | Moved hello.rb to lib [Parth Badgujar]
* e7ddc80 2023-04-28 | Add an author/email comment (tag: v2) [Parth Badgujar]
* e046030 2023-04-28 | Added a comment (tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
```
## Lab 28 (Merging)
```console
$ git checkout greet
Switched to branch 'greet'
$ git merge master
Merge made by the 'ort' strategy.
 README | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README
$ git hist --all
*   0b26605 2023-04-28 | Merge branch 'master' into greet (HEAD -> greet) [Parth Badgujar]
|\  
| * 7acc3af 2023-04-28 | Added README (master) [Parth Badgujar]
* | 16ddd1b 2023-04-28 | Updated Rakefile [Parth Badgujar]
* | b512c4d 2023-04-28 | Hello uses Greeter [Parth Badgujar]
* | 0193247 2023-04-28 | Added a greeter class [Parth Badgujar]
|/  
* 610ccb0 2023-04-28 | Added a Rakefile [Parth Badgujar]
* 073ac20 2023-04-28 | Moved hello.rb to lib [Parth Badgujar]
* e7ddc80 2023-04-28 | Add an author/email comment (tag: v2) [Parth Badgujar]
* e046030 2023-04-28 | Added a comment (tag: v1) [Parth Badgujar]
* bbcc511 2023-04-28 | Added a default value (tag: v1-beta) [Parth Badgujar]
* 5d5596e 2023-04-28 | Unrelated change to c [Parth Badgujar]
* 1b79fc5 2023-04-28 | Chages for a and b [Parth Badgujar]
* f03621e 2023-04-28 | First Commit (tag: v0) [Parth Badgujar]
```