## lab1
checking configurations and ruby version
```
(base) somshekharsharma@MacBook-Air gitimm % git config --list
credential.helper=osxkeychain
user.name=Som Shekhar Sharma
user.email=sharmathat@gmail.com
color.ui=auto
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
core.autocrlf=input
core.safecrlf=true
alias.co=checkout
alias.ci=commit
alias.st=status
alias.br=branch
alias.hist=log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
alias.type=cat-file -t
alias.dump=cat-file -p
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=https://github.com/ReallyJaegar/lecture-assignments-y23.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
(base) somshekharsharma@MacBook-Air gitimm % ruby -v
ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin22]
```

## lab 3
```
(base) somshekharsharma@MacBook-Air hello % mkdir hello
(base) somshekharsharma@MacBook-Air hello % cd hello   
(base) somshekharsharma@MacBook-Air hello % echo 'puts "Hello, World"' |tee hello.rb
puts "Hello, World"
```
```
(base) somshekharsharma@MacBook-Air hello % git init   
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:     git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:     git branch -m <name>
Initialized empty Git repository in /Users/somshekharsharma/dsg/lecture-assignments-y23/Git-Bash/Som_Shekhar/Git-Bash_Som/gitimm/git_tutorial/work/hello/.git/
```
```
(base) somshekharsharma@MacBook-Air hello % git add hello.rb
(base) somshekharsharma@MacBook-Air hello % git commit -m "first commit"
[master (root-commit) 920bd9b] first commit
 1 file changed, 1 insertion(+)
 ```
 
 ## lab 4
 ```
 (base) somshekharsharma@MacBook-Air hello % git status
On branch master
nothing to commit, working tree clean
```

## lab 5
```
(base) somshekharsharma@MacBook-Air hello % echo 'puts "Hello, #{ARGV.first}!"' | tee hello.rb
puts "Hello, #{ARGV.first}!"
 create mode 100644 hello.rb
 
 (base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
```

## lab 6
```
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
(base) somshekharsharma@MacBook-Air hello % git add hello.rb
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    modified:   hello.rb
```

## lab 7
```
By separating staging and committing, you have the ability to easily fine tune what goes into each commit.
```
## lab 8
```
(base) somshekharsharma@MacBook-Air hello % git commit
[master 8702b24] Using ARGV
 1 file changed, 1 insertion(+), 1 deletion(-)
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
nothing to commit, working tree clean
```
```
commit message in vim
```
## lab 9
```
(base) somshekharsharma@MacBook-Air hello % vim hello.rb
(base) somshekharsharma@MacBook-Air hello % git add hello.rb
(base) somshekharsharma@MacBook-Air hello % vim hello.rb
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    modified:   hello.rb

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello.rb

(base) somshekharsharma@MacBook-Air hello % git commit -m "Added a deafult value"
[master 640e5cd] Added a deafult value
 1 file changed, 3 insertions(+), 1 deletion(-)
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
```
```
(base) somshekharsharma@MacBook-Air hello % git add .
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    modified:   hello.rb

(base) somshekharsharma@MacBook-Air hello % git commit -m " added a comment"
[master c946f20]  added a comment
 1 file changed, 1 insertion(+)
 ```
 ## lab 10
 ```
 (base) somshekharsharma@MacBook-Air hello % git log
commit c946f20bd0d4286cc23ca9de60f4e190595142c7 (HEAD -> master)
Author: Som Shekhar Sharma <sharmathat@gmail.com>
Date:   Wed May 3 11:35:06 2023 +0530

     added a comment

commit 640e5cd93860ab2ac2a9c4c065823c0a699b7720
Author: Som Shekhar Sharma <sharmathat@gmail.com>
Date:   Wed May 3 11:34:36 2023 +0530

    Added a deafult value

commit 8702b24bdbbc9c8a858c2768a983508432367205
Author: Som Shekhar Sharma <sharmathat@gmail.com>
Date:   Wed May 3 11:31:06 2023 +0530

    Using ARGV

commit 920bd9ba2e0149187ced59c653872c7726a70852
Author: Som Shekhar Sharma <sharmathat@gmail.com>
Date:   Wed May 3 11:26:20 2023 +0530

    first commit
(base) somshekharsharma@MacBook-Air hello % git log --pretty=oneline
c946f20bd0d4286cc23ca9de60f4e190595142c7 (HEAD -> master)  added a comment
640e5cd93860ab2ac2a9c4c065823c0a699b7720 Added a deafult value
8702b24bdbbc9c8a858c2768a983508432367205 Using ARGV
920bd9ba2e0149187ced59c653872c7726a70852 first commit
```
```
(base) somshekharsharma@MacBook-Air hello % git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
* c946f20 2023-05-03 |  added a comment (HEAD -> master) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
```
## lab 11
```
(base) somshekharsharma@MacBook-Air hello % cat ~/.gitconfig
[user]
    name = Som Shekhar Sharma
    email = sharmathat@gmail.com
[color]
    ui = auto
[filter "lfs"]
    smudge = git-lfs smudge -- %f
    process = git-lfs filter-process
    required = true
    clean = git-lfs clean -- %f
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
## lab 11
```
(base) somshekharsharma@MacBook-Air hello % git hist
* c946f20 2023-05-03 |  added a comment (HEAD -> master) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
```
```
(base) somshekharsharma@MacBook-Air hello % git checkout 920bd9b
Note: switching to '920bd9b'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 920bd9b first commit

(base) somshekharsharma@MacBook-Air hello % cat hello.rb
puts "Hello, World"

```
```
(base) somshekharsharma@MacBook-Air hello % git checkout master
Previous HEAD position was 920bd9b first commit
Switched to branch 'master'
(base) somshekharsharma@MacBook-Air hello % cat hello.rb       
# Default is "World"
name = ARGV.first || "World"

puts "Hello, #{name}!"puts "Hello, #{ARGV.first}!"
```
## lab 13
```
(base) somshekharsharma@MacBook-Air hello % git tag v1
(base) somshekharsharma@MacBook-Air hello % git checkout v1^
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

HEAD is now at 640e5cd Added a deafult value
(base) somshekharsharma@MacBook-Air hello % cat hello.rb
name = ARGV.first || "World"

puts "Hello, #{name}!"puts "Hello, #{ARGV.first}!"
(base) somshekharsharma@MacBook-Air hello % git tag v1-beta
(base) somshekharsharma@MacBook-Air hello % git checkout v1
Previous HEAD position was 640e5cd Added a deafult value
HEAD is now at c946f20  added a comment
(base) somshekharsharma@MacBook-Air hello % git checkout v1-beta 
Previous HEAD position was c946f20  added a comment
HEAD is now at 640e5cd Added a deafult value
(base) somshekharsharma@MacBook-Air hello % git tag
v1
v1-beta
(base) somshekharsharma@MacBook-Air hello % git hist master --all
* c946f20 2023-05-03 |  added a comment (tag: v1, master) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value (HEAD, tag: v1-beta) [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
```
## lab 14
```
(base) somshekharsharma@MacBook-Air hello % git checkout master
Previous HEAD position was 640e5cd Added a deafult value
Switched to branch 'master'
(base) somshekharsharma@MacBook-Air hello % vim hello.rb
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
(base) somshekharsharma@MacBook-Air hello % git checkout hello.rb
Updated 1 path from the index
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
nothing to commit, working tree clean
(base) somshekharsharma@MacBook-Air hello % cat hello.rb
# Default is "World"
name = ARGV.first || "World"

puts "Hello, #{name}!"puts "Hello, #{ARGV.first}!"
(base) somshekharsharma@MacBook-Air hello % 

```
## lab 15
```
(base) somshekharsharma@MacBook-Air hello % vim hello.rb
(base) somshekharsharma@MacBook-Air hello % git add hello.rb
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    modified:   hello.rb

(base) somshekharsharma@MacBook-Air hello % git reset HEAD hello.rb
Unstaged changes after reset:
M    hello.rb
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
(base) somshekharsharma@MacBook-Air hello % git checkout hello.rb
Updated 1 path from the index
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
nothing to commit, working tree clean

```
## lab 16
```
(base) somshekharsharma@MacBook-Air hello % vim hello.rb
(base) somshekharsharma@MacBook-Air hello % git add hello.rb
(base) somshekharsharma@MacBook-Air hello % git commit -m "Oops, we dint want this commit"
[master 219b045] Oops, we dint want this commit
 1 file changed, 1 insertion(+), 1 deletion(-)
(base) somshekharsharma@MacBook-Air hello % git revert HEAD
[master b6841e3] Revert "Oops, we dint want this commit"
 1 file changed, 1 insertion(+), 1 deletion(-)
(base) somshekharsharma@MacBook-Air hello % git hist
* b6841e3 2023-05-03 | Revert "Oops, we dint want this commit" (HEAD -> master) [Som Shekhar Sharma]
* 219b045 2023-05-03 | Oops, we dint want this commit [Som Shekhar Sharma]
* c946f20 2023-05-03 |  added a comment (tag: v1) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value (tag: v1-beta) [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
```
## lab 17
```
(base) somshekharsharma@MacBook-Air hello % git tag oops
(base) somshekharsharma@MacBook-Air hello % git reset --hard v1
HEAD is now at c946f20  added a comment
(base) somshekharsharma@MacBook-Air hello % git hist
* c946f20 2023-05-03 |  added a comment (HEAD -> master, tag: v1) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value (tag: v1-beta) [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
(base) somshekharsharma@MacBook-Air hello % git hist --all
* b6841e3 2023-05-03 | Revert "Oops, we dint want this commit" (tag: oops) [Som Shekhar Sharma]
* 219b045 2023-05-03 | Oops, we dint want this commit [Som Shekhar Sharma]
* c946f20 2023-05-03 |  added a comment (HEAD -> master, tag: v1) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value (tag: v1-beta) [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
```
## lab 18
```
(base) somshekharsharma@MacBook-Air hello % git tag -d oops
Deleted tag 'oops' (was b6841e3)
(base) somshekharsharma@MacBook-Air hello % git hist --all 
* c946f20 2023-05-03 |  added a comment (HEAD -> master, tag: v1) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value (tag: v1-beta) [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
```
## lab 19
```
(base) somshekharsharma@MacBook-Air hello % vim hello.rb
(base) somshekharsharma@MacBook-Air hello % git add hello.rb
(base) somshekharsharma@MacBook-Air hello % git commit -m "Add an author comment "
[master a2f92dc] Add an author comment
 1 file changed, 1 insertion(+)
(base) somshekharsharma@MacBook-Air hello % vim hello.rb 
(base) somshekharsharma@MacBook-Air hello % git add hello.rb
(base) somshekharsharma@MacBook-Air hello % git commit --amend -m "Add an author/email comment"
[master da71cd5] Add an author/email comment
 Date: Wed May 3 12:20:07 2023 +0530
 1 file changed, 1 insertion(+)
(base) somshekharsharma@MacBook-Air hello % git hist
* da71cd5 2023-05-03 | Add an author/email comment (HEAD -> master) [Som Shekhar Sharma]
* c946f20 2023-05-03 |  added a comment (tag: v1) [Som Shekhar Sharma]
* 640e5cd 2023-05-03 | Added a deafult value (tag: v1-beta) [Som Shekhar Sharma]
* 8702b24 2023-05-03 | Using ARGV [Som Shekhar Sharma]
* 920bd9b 2023-05-03 | first commit [Som Shekhar Sharma]
(base) somshekharsharma@MacBook-Air hello % 

```
## lab 20
```
(base) somshekharsharma@MacBook-Air hello % mkdir lib
(base) somshekharsharma@MacBook-Air hello % git mv hello.rb lib 
(base) somshekharsharma@MacBook-Air hello % git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    renamed:    hello.rb -> lib/hello.rb
(base) somshekharsharma@MacBook-Air hello % git commit -m "Moved hello.rb to lib"
[master abb027e] Moved hello.rb to lib
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename hello.rb => lib/hello.rb (100%)
```

## lab 21
```




 

