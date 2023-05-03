## Lab 1
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/GitTut$ git config --global user.name "Pranjal Gautam"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/GitTut$ git config --global user.email "pgautam2041@gmail.com"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/GitTut$ git config --global core.autocrlf input
rodger2041@LAPTOP-CH89DDGF:/mnt/c/GitTut$ git config --global core.safecrlf true
```
## Lab 3
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos$ mkdir hello
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos$ cd hello
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ touch hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ echo puts '"Hello, World"' | tee hel
lo.rb
puts "Hello, World"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
puts "Hello, World"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git init
Initialized empty Git repository in /mnt/c/git_repos/hello/.git/
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "First Commit"
[master (root-commit) d7e4b14] First Commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.rb
```
## Lab 4
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
nothing to commit, working tree clean
```
## Lab 5
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
```
## Lab 6
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.rb
```
## Lab 7
console
```rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Changes for a and b"
[master 7a32785] Changes for a and b
 3 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 a.rb
 create mode 100644 b.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add c.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Unrelated change to c
"
[master 4a7c21f] Unrelated change to c
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 c.rb
 ```
 ## Lab 9
``` console
 rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
# Default is "World"
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.rb

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.rb

rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Added a default value
"
[master d3feb84] Added a default value
 1 file changed, 2 insertions(+), 1 deletion(-)
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add .
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.rb

rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Added a comment"
[master 1dea6d8] Added a comment
 1 file changed, 1 insertion(+)
 ```
## Lab 10
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git log
commit 1dea6d852fccc67697b17509a556be6d0bc70362 (HEAD -> master)
Author: Pranjal Gautam <pgautam2041@gmail.com>
Date:   Fri Apr 28 23:11:37 2023 +0530

    Added a comment

commit d3feb8492c64d55f66e55cdb230ec1ff3143e0b1
Author: Pranjal Gautam <pgautam2041@gmail.com>
Date:   Fri Apr 28 23:11:10 2023 +0530

    Added a default value

commit 4a7c21f49dae9ce80d2deacff1ae40d7b277f243
Author: Pranjal Gautam <pgautam2041@gmail.com>
Date:   Fri Apr 28 22:58:26 2023 +0530

    Unrelated change to c

commit 7a327856e666d0824e43302b3380cc94e47c9d9d
Author: Pranjal Gautam <pgautam2041@gmail.com>
Date:   Fri Apr 28 22:58:03 2023 +0530

    Changes for a and b

commit d7e4b14d413063e213aef71014316c3f09627c6c
Author: Pranjal Gautam <pgautam2041@gmail.com>
Date:   Fri Apr 28 22:45:03 2023 +0530

    First Commit
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git log --pretty=oneline
1dea6d852fccc67697b17509a556be6d0bc70362 (HEAD -> master) Added a comment
d3feb8492c64d55f66e55cdb230ec1ff3143e0b1 Added a default value
4a7c21f49dae9ce80d2deacff1ae40d7b277f243 Unrelated change to c
7a327856e666d0824e43302b3380cc94e47c9d9d Changes for a and b
d7e4b14d413063e213aef71014316c3f09627c6c First Commit
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git log --pretty=oneline --max-count
=2
1dea6d852fccc67697b17509a556be6d0bc70362 (HEAD -> master) Added a comment
d3feb8492c64d55f66e55cdb230ec1ff3143e0b1 Added a default value
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git log --pretty=oneline --since='5 minutes ago'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git log --pretty=oneline --until='5
minutes ago'
1dea6d852fccc67697b17509a556be6d0bc70362 (HEAD -> master) Added a comment
d3feb8492c64d55f66e55cdb230ec1ff3143e0b1 Added a default value
4a7c21f49dae9ce80d2deacff1ae40d7b277f243 Unrelated change to c
7a327856e666d0824e43302b3380cc94e47c9d9d Changes for a and b
d7e4b14d413063e213aef71014316c3f09627c6c First Commit
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git log --pretty=oneline --author="Pranjal Gautam"
1dea6d852fccc67697b17509a556be6d0bc70362 (HEAD -> master) Added a comment
d3feb8492c64d55f66e55cdb230ec1ff3143e0b1 Added a default value
4a7c21f49dae9ce80d2deacff1ae40d7b277f243 Unrelated change to c
7a327856e666d0824e43302b3380cc94e47c9d9d Changes for a and b
d7e4b14d413063e213aef71014316c3f09627c6c First Commit
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git log --pretty=oneline --all
1dea6d852fccc67697b17509a556be6d0bc70362 (HEAD -> master) Added a comment
d3feb8492c64d55f66e55cdb230ec1ff3143e0b1 Added a default value
4a7c21f49dae9ce80d2deacff1ae40d7b277f243 Unrelated change to c
7a327856e666d0824e43302b3380cc94e47c9d9d Changes for a and b
d7e4b14d413063e213aef71014316c3f09627c6c First Commit
```
## Lab 11
```console
rodger2041@LAPTOP-CH89DDGF:~$ nano .gitconfig
rodger2041@LAPTOP-CH89DDGF:~$ cat .gitconfig
[user]
        name = Pranjal Gautam
        email = pgautam2041@gmail.com
[core]
        autocrlf = input
        safecrlf = true
[alias]
  co = checkout
  ci = commit
  st = status
  br = branch
  hist = log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
  type = cat-file -t
  dump = cat-file -p
```
## Lab 12
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist
* 1dea6d8 2023-04-28 | Added a comment (HEAD -> master) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout d7e4b14
Note: switching to 'd7e4b14'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at d7e4b14 First Commit
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
puts "Hello, World"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout master
Previous HEAD position was d7e4b14 First Commit
Switched to branch 'master'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
# Default is "World"
name = ARGV.first || "World"
puts "Hello, #{name}!"
```
## Lab 13
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git tag v1
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout v1^
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

HEAD is now at d3feb84 Added a default value
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git tag v1-beta
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout v1
Previous HEAD position was d3feb84 Added a default value
HEAD is now at 1dea6d8 Added a comment
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
# Default is "World"
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout v1-beta
Previous HEAD position was 1dea6d8 Added a comment
HEAD is now at d3feb84 Added a default value
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout master
Previous HEAD position was d3feb84 Added a default value
Switched to branch 'master'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git tag
v1
v1-beta
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist master --all
* 1dea6d8 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 14
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
#This is a bad comment. We want to revert it.
name = ARGV.first || "World"

puts "Hello,#{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout hello.rb
Updated 1 path from the index
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
nothing to commit, working tree clean
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
# Default is "World"
name = ARGV.first || "World"
puts "Hello, #{name}!"
```
## Lab 15
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
# This is an unwanted but staged comment
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.rb

rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git reset HEAD hello.rb
Unstaged changes after reset:
M       hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout hello.rb
Updated 1 path from the index
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
nothing to commit, working tree clean
```
## Lab 16
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
# This is n unwanted but commited change
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add .
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Oops, we didn't want
this commit"
[master 9775281] Oops, we didn't want this commit
 1 file changed, 1 insertion(+), 1 deletion(-)
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git revert HEAD
[master 2ad539e] Revert "Oops, we didn't want this commit"
 1 file changed, 1 insertion(+), 1 deletion(-)
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist
* 2ad539e 2023-04-29 | Revert "Oops, we didn't want this commit" (HEAD -> master) [Pranjal Gautam]
* 9775281 2023-04-29 | Oops, we didn't want this commit [Pranjal Gautam]
* 1dea6d8 2023-04-28 | Added a comment (tag: v1) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 17
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist
* 2ad539e 2023-04-29 | Revert "Oops, we didn't want this commit" (HEAD -> master) [Pranjal Gautam]
* 9775281 2023-04-29 | Oops, we didn't want this commit [Pranjal Gautam]
* 1dea6d8 2023-04-28 | Added a comment (tag: v1) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git tag oops
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git reset --hard v1
HEAD is now at 1dea6d8 Added a comment
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist
* 1dea6d8 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist -all
error: switch `l' expects a numerical value
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
* 2ad539e 2023-04-29 | Revert "Oops, we didn't want this commit" (tag: oops) [Pranjal Gautam]
* 9775281 2023-04-29 | Oops, we didn't want this commit [Pranjal Gautam]
* 1dea6d8 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 18
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git tag -d oops
Deleted tag 'oops' (was 2ad539e)
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
* 1dea6d8 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 19
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
* 1dea6d8 2023-04-28 | Added a comment (HEAD -> master, tag: v1) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat hello.rb
# Default is "World"
# Author: Jim Weirich (jim@somewhere.com)
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add .
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit --amend -m "Add an author/email comment"
[master 9922ee9] Add an author/email comment
 Date: Fri Apr 28 23:11:37 2023 +0530
 1 file changed, 2 insertions(+)
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist
* 9922ee9 2023-04-28 | Add an author/email comment (HEAD -> master) [Pranjal Gautam]
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 20
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ mkdir lib
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git mv hello.rb lib
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    hello.rb -> lib/hello.rb

rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls
a.rb  b.rb  c.rb  lib
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Moved hello.rb to lib
"
[master ff07d4a] Moved hello.rb to lib
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename hello.rb => lib/hello.rb (100%)
```
## Lab 21
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano Rakefile
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat Rakefile
#!/usr/bin/ruby -wKU

task :default => :run

task :run do
  require './lib/hello'
end
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add Rakefile
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Rakefile

rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Added a Rakefile."
[master 4e79404] Added a Rakefile.
 1 file changed, 7 insertions(+)
 create mode 100644 Rakefile
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ rake
Hello, World!
```
## Lab 22
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls -C .git
COMMIT_EDITMSG  ORIG_HEAD  config       hooks  info  objects      refs
HEAD            branches   description  index  logs  packed-refs
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls -C .git/objects
16  1d  27  2a  4a  59  60  7a  97  af  d3  d8  e6  f1  info
18  25  28  32  4e  5e  71  81  99  c5  d7  d9  ed  ff  pack
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls -C .git/objects/16
1927f37c63e8c935c4958b638fb6cb378f5958
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat .git/config
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        ignorecase = true
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs
heads  tags
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/heads
ls: cannot access '.git/heads': No such file or directory
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs/heads
master
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs/tags
v1  v1-beta
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs/tags/v1
.git/refs/tags/v1
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs/tags/v1 -a
.git/refs/tags/v1
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs
heads  tags
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs/heads
master
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ ls .git/refs/tags
v1  v1-beta
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat .git/refs/tags/v1
1dea6d852fccc67697b17509a556be6d0bc70362
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat .git/HEAD
ref: refs/heads/master
```
## Lab 23
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git cat-file -t 4e79404
commit
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git cat-file -p 4e79404
tree f17620c7f7fcfd5fe26be1b1b50bdeea97e45367
parent ff07d4a061ee264245bc8562e71cae1fc4014802
author Pranjal Gautam <pgautam2041@gmail.com> 1682714878 +0530
committer Pranjal Gautam <pgautam2041@gmail.com> 1682714878 +0530

Added a Rakefile.
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git cat-file -p f17620c7f7fcfd5fe26be1b1b50bdeea97e45367
100644 blob 28e0e9d6ea7e25f35ec64a43f569b550e8386f90    Rakefile
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    a.rb
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    b.rb
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    c.rb
040000 tree 6011e0ce0375e5c431b3a139aca51243f56635ad    lib
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git cat-file -p 6011e0ce0375e5c431b3a139aca51243f56635ad
100644 blob 161927f37c63e8c935c4958b638fb6cb378f5958    hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git cat-file -p 161927f37c63e8c935c4958b638fb6cb378f5958
# Default is "World"
# Author: Jim Weirich (jim@somewhere.com)
name = ARGV.first || "World"
puts "Hello, #{name}!"
```
## Lab 24
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout -b greet
giSwitched to a new branch 'greet'
trodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch greet
nothing to commit, working tree clean
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ touch ./lib/greeter.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano lib/greeter.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat lib/greeter.rb
class Greeter
  def initialize(who)
    @who = who
  end
  def greet
    "Hello, #{@who}"
  end
end

rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano lib/hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat lib/hello.rb
require 'greeter'

# Default is "World"
# Author: Jim Weirich (jim@somewhere.com)
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano Rakefile
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat Rakefile
#!/usr/bin/ruby -wKU

task :default => :run

task :run do
  ruby '-Ilib', 'lib/hello.rb'
end
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add Rakefile
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Updated Rakefile"
[greet 6c1236a] Updated Rakefile
 1 file changed, 1 insertion(+), 1 deletion(-)
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add lib/greeter.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Added a greeter class"
[greet 416dc2c] Added a greeter class
 1 file changed, 9 insertions(+)
 create mode 100644 lib/greeter.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add .
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git status
On branch greet
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   lib/hello.rb

rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "hello.rb requires gre
eter class"
[greet 446e6e7] hello.rb requires greeter class
 1 file changed, 2 insertions(+)
```
## Lab 25
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
* 446e6e7 2023-04-29 | hello.rb requires greeter class (HEAD -> greet) [Pranjal Gautam]
* 416dc2c 2023-04-29 | Added a greeter class [Pranjal Gautam]
* 6c1236a 2023-04-29 | Updated Rakefile [Pranjal Gautam]
* 4e79404 2023-04-29 | Added a Rakefile. (master) [Pranjal Gautam]
* ff07d4a 2023-04-29 | Moved hello.rb to lib [Pranjal Gautam]
* 9922ee9 2023-04-28 | Add an author/email comment [Pranjal Gautam]
| * 1dea6d8 2023-04-28 | Added a comment (tag: v1) [Pranjal Gautam]
|/
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout master
Switched to branch 'master'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat lib/hello.rb
# Default is "World"
# Author: Jim Weirich (jim@somewhere.com)
name = ARGV.first || "World"
puts "Hello, #{name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout greet
Switched to branch 'greet'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat lib/hello.rb
require 'greeter'

# Default is "World"
# Author: Jim Weirich (jim@somewhere.com)
name = ARGV.first || "World"
puts "Hello, #{name}!"
```
## Lab 26
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout master
Switched to branch 'master'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ touch README.txt
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano README.txt
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add README.txt
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Added README"
[master 2b23e22] Added README
 1 file changed, 1 insertion(+)
 create mode 100644 README.txt
```
## Lab 27
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
* 2b23e22 2023-04-29 | Added README (HEAD -> master) [Pranjal Gautam]
| * 446e6e7 2023-04-29 | hello.rb requires greeter class (greet) [Pranjal Gautam]
| * 416dc2c 2023-04-29 | Added a greeter class [Pranjal Gautam]
| * 6c1236a 2023-04-29 | Updated Rakefile [Pranjal Gautam]
|/
* 4e79404 2023-04-29 | Added a Rakefile. [Pranjal Gautam]
* ff07d4a 2023-04-29 | Moved hello.rb to lib [Pranjal Gautam]
* 9922ee9 2023-04-28 | Add an author/email comment [Pranjal Gautam]
| * 1dea6d8 2023-04-28 | Added a comment (tag: v1) [Pranjal Gautam]
|/
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 28
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout greet
Switched to branch 'greet'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git merge master
Merge made by the 'ort' strategy.
 README.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.txt
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
*   f18ca97 2023-04-29 | Merge branch 'master' into greet (HEAD -> greet) [Pranjal Gautam]
|\
| * 2b23e22 2023-04-29 | Added README (master) [Pranjal Gautam]
* | 446e6e7 2023-04-29 | hello.rb requires greeter class [Pranjal Gautam]
* | 416dc2c 2023-04-29 | Added a greeter class [Pranjal Gautam]
* | 6c1236a 2023-04-29 | Updated Rakefile [Pranjal Gautam]
|/
* 4e79404 2023-04-29 | Added a Rakefile. [Pranjal Gautam]
* ff07d4a 2023-04-29 | Moved hello.rb to lib [Pranjal Gautam]
* 9922ee9 2023-04-28 | Add an author/email comment [Pranjal Gautam]
| * 1dea6d8 2023-04-28 | Added a comment (tag: v1) [Pranjal Gautam]
|/
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 29
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout master
Switched to branch 'master'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano lib/hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat lib/hello.rb
puts "What's your name"
my_name = gets.strip

puts "Hello, #{my_name}!"
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add .
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Made interactive"
[master c61dcbb] Made interactive
 1 file changed, 4 insertions(+), 4 deletions(-)
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
* c61dcbb 2023-04-29 | Made interactive (HEAD -> master) [Pranjal Gautam]
| *   f18ca97 2023-04-29 | Merge branch 'master' into greet (greet) [Pranjal Gautam]
| |\
| |/
|/|
* | 2b23e22 2023-04-29 | Added README [Pranjal Gautam]
| * 446e6e7 2023-04-29 | hello.rb requires greeter class [Pranjal Gautam]
| * 416dc2c 2023-04-29 | Added a greeter class [Pranjal Gautam]
| * 6c1236a 2023-04-29 | Updated Rakefile [Pranjal Gautam]
|/
* 4e79404 2023-04-29 | Added a Rakefile. [Pranjal Gautam]
* ff07d4a 2023-04-29 | Moved hello.rb to lib [Pranjal Gautam]
* 9922ee9 2023-04-28 | Add an author/email comment [Pranjal Gautam]
| * 1dea6d8 2023-04-28 | Added a comment (tag: v1) [Pranjal Gautam]
|/
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```
## Lab 30
```console
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git checkout greet
Switched to branch 'greet'
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git merge master
Auto-merging lib/hello.rb
CONFLICT (content): Merge conflict in lib/hello.rb
Automatic merge failed; fix conflicts and then commit the result.
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ nano lib/hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ cat lib/hello.rb
require 'greeter'

puts "What's your name"
my_name = gets.strip

greeter = Greeter.new(my_name)
puts greeter.greet
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git add lib/hello.rb
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git commit -m "Merged master fixed c
onflict."
[greet 16df2cb] Merged master fixed conflict.
rodger2041@LAPTOP-CH89DDGF:/mnt/c/git_repos/hello$ git hist --all
*   16df2cb 2023-04-29 | Merged master fixed conflict. (HEAD -> greet) [Pranjal Gautam]
|\
| * c61dcbb 2023-04-29 | Made interactive (master) [Pranjal Gautam]
* | f18ca97 2023-04-29 | Merge branch 'master' into greet [Pranjal Gautam]
|\|
| * 2b23e22 2023-04-29 | Added README [Pranjal Gautam]
* | 446e6e7 2023-04-29 | hello.rb requires greeter class [Pranjal Gautam]
* | 416dc2c 2023-04-29 | Added a greeter class [Pranjal Gautam]
* | 6c1236a 2023-04-29 | Updated Rakefile [Pranjal Gautam]
|/
* 4e79404 2023-04-29 | Added a Rakefile. [Pranjal Gautam]
* ff07d4a 2023-04-29 | Moved hello.rb to lib [Pranjal Gautam]
* 9922ee9 2023-04-28 | Add an author/email comment [Pranjal Gautam]
| * 1dea6d8 2023-04-28 | Added a comment (tag: v1) [Pranjal Gautam]
|/
* d3feb84 2023-04-28 | Added a default value (tag: v1-beta) [Pranjal Gautam]
* 4a7c21f 2023-04-28 | Unrelated change to c [Pranjal Gautam]
* 7a32785 2023-04-28 | Changes for a and b [Pranjal Gautam]
* d7e4b14 2023-04-28 | First Commit [Pranjal Gautam]
```