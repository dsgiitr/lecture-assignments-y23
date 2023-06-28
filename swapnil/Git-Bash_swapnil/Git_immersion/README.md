# Git-Immersion
### Labs 1-2 
Just setup, done easily

### Lab 3
```shell
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work$ mkdir hello
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work$ cd hello
swapnil@SwapG-G15$ touch hello.py
swapnil@SwapG-G15$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello/.git/
swapnil@SwapG-G15$ git add hello.py
swapnil@SwapG-G15$ git commit -m "First commit"
[master (root-commit) 7771f50] First commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
```

### Lab 4
```shell
swapnil@SwapG-G15$ git status
On branch master
nothing to commit, working tree clean
```
### Lab 5
```shell
swapnil@SwapG-G15$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
```

### Lab 6
```shell
swapnil@SwapG-G15$ git add hello.py
swapnil@SwapG-G15$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py
```
### Lab 8
```shell
swapnil@SwapG-G15$ git commit
[master f5dfb2a] Addded command line arguments to hello.py
 1 file changed, 4 insertions(+), 1 deletion(-)
swapnil@SwapG-G15$ git status
On branch master
nothing to commit, working tree clean
```
### Lab 9
```shell
swapnil@SwapG-G15$ git add hello.py
swapnil@SwapG-G15$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

swapnil@SwapG-G15$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

swapnil@SwapG-G15$ git commit -m "Added default arguments to hello.py"
[master d116fab] Added default arguments to hello.py
 1 file changed, 2 insertions(+), 2 deletions(-)
swapnil@SwapG-G15$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15$ git add .
swapnil@SwapG-G15$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

swapnil@SwapG-G15$ git commit -m "Added comments for better readability"
[master 0eac671] Added comments for better readability
 1 file changed, 1 insertion(+), 1 deletion(-)
```
### Lab 10 
```shell
swapnil@SwapG-G15$ git log
commit 0eac6711f7d620fcd4f65eb7f9a9a2b82b22684a (HEAD -> master)
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:18:34 2023 +0530

    Added comments for better readability

commit d116fabafe16cc1f6e9d29f1eb330801ca1514da
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:17:22 2023 +0530

    Added default arguments to hello.py

commit f5dfb2a5dabe6a664f899fee1bc801802fe20f8f
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:14:23 2023 +0530

    Addded command line arguments to hello.py

commit 7771f50f57d836708ed87b3a0fb48482934af78d
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:09:41 2023 +0530

    First commit
swapnil@SwapG-G15$ git log --pretty=oneline
0eac6711f7d620fcd4f65eb7f9a9a2b82b22684a (HEAD -> master) Added comments for better readability
d116fabafe16cc1f6e9d29f1eb330801ca1514da Added default arguments to hello.py
f5dfb2a5dabe6a664f899fee1bc801802fe20f8f Addded command line arguments to hello.py
7771f50f57d836708ed87b3a0fb48482934af78d First commit
```
### Lab 11
Added aliases to git config file.
### Lab 12
```shell
swapnil@SwapG-G15$ git hist
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15$ git checkout 7771f50
Note: switching to '7771f50'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 7771f50 First commit
swapnil@SwapG-G15$ git checkout master
Previous HEAD position was 7771f50 First commit
Switched to branch 'master'
```
### Lab 13
```shell
swapnil@SwapG-G15$ git tag v1
swapnil@SwapG-G15$ git checkout v1^
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

HEAD is now at d116fab Added default arguments to hello.py
swapnil@SwapG-G15$ cat hello.py
import sys

name = sys.argv[0] or "World"
print("Hello {}".format(name))swapnil

swapnil@SwapG-G15$ git tag v1-beta
swapnil@SwapG-G15$ git checkout v1
Previous HEAD position was d116fab Added default arguments to hello.py
HEAD is now at 0eac671 Added comments for better readability
swapnil@SwapG-G15$ git checkout v1-beat
error: pathspec 'v1-beat' did not match any file(s) known to git
swapnil@SwapG-G15$ git checkout v1-beta
Previous HEAD position was 0eac671 Added comments for better readability
HEAD is now at d116fab Added default arguments to hello.py
swapnil@SwapG-G15$ git checkout v1
Previous HEAD position was d116fab Added default arguments to hello.py
HEAD is now at 0eac671 Added comments for better readability
swapnil@SwapG-G15$ git tag
v1
v1-beta

swapnil@SwapG-G15$ git hist master --all
* 0eac671 2023-05-03 | Added comments for better readability (HEAD, tag: v1, master) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```
### Lab 14
```shell
swapnil@SwapG-G15$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15$ git checkout hello.py
Updated 1 path from the index
swapnil@SwapG-G15$ git status
On branch master
nothing to commit, working tree clean
swapnil@SwapG-G15$ cat hello.py
import sys
#Default argument
name = sys.argv[0] or "World"
print("Hello {}".format(name))
```
### Lab 15 
```shell
swapnil@SwapG-G15$ git add hello.py
swapnil@SwapG-G15$ git reset HEAD hello.py
Unstaged changes after reset:
M       hello.py
swapnil@SwapG-G15$ git checkout hello.py
Updated 1 path from the index
swapnil@SwapG-G15$ git status
On branch master
nothing to commit, working tree clean
```
### Lab 16
```shell
swapnil@SwapG-G15$ git add hello.py
swapnil@SwapG-G15$ git commit -m "Ooops"
[master cfc2147] Ooops
 1 file changed, 1 insertion(+), 1 deletion(-)
swapnil@SwapG-G15$ git revert HEAD
[master fad87a2] Revert "Ooops"
 1 file changed, 1 insertion(+), 1 deletion(-)

swapnil@SwapG-G15$ git hist
* fad87a2 2023-05-03 | Revert "Ooops" (HEAD -> master) [Swapnil Garg]
* cfc2147 2023-05-03 | Ooops [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```
### Lab 17
```shell
swapnil@SwapG-G15$ git tag oops
swapnil@SwapG-G15$ git reset --hard v1
HEAD is now at 0eac671 Added comments for better readability
swapnil@SwapG-G15$ git hist
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master, tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15$ git hist --all
* fad87a2 2023-05-03 | Revert "Ooops" (tag: oops) [Swapnil Garg]
* cfc2147 2023-05-03 | Ooops [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master, tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```
### Lab 18
```shell
swapnil@SwapG-G15$ git tag -d oops
Deleted tag 'oops' (was fad87a2)
swapnil@SwapG-G15$ git hist --all
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master, tag: v1)
[Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```
### Lab 19
```shell
swapnil@SwapG-G15$ git add hello.py
swapnil@SwapG-G15$ git commit -m "Added author comment"
[master b2a6568] Added author comment
 1 file changed, 2 insertions(+), 1 deletion(-)
swapnil@SwapG-G15$ git add hello.py
swapnil@SwapG-G15$ git commit --amend -m "Added an author name and email"
[master bae4237] Added an author name and email
 Date: Wed May 3 13:27:58 2023 +0530
 1 file changed, 2 insertions(+), 1 deletion(-)
swapnil@SwapG-G15$ git hist
* bae4237 2023-05-03 | Added an author name and email (HEAD -> master) [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```
### Lab 20
```shell
swapnil@SwapG-G15$ mkdir lib
swapnil@SwapG-G15$ git mv hello.py lib
swapnil@SwapG-G15$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    hello.py -> lib/hello.py
swapnil@SwapG-G15$ git commit -m "Moved hello.py to ./lib"
[master 34e3688] Moved hello.py to ./lib
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename hello.py => lib/hello.py (100%)
```
### Lab 21
Skipped adding rakefile, I am substituting Ruby with Python, so couldn't figure out how to make another file to run a python script from the terminal(shebang + chmod -x is what i know) 
what exact file i add doesn't matter anyways :/ 
### Lab 22
```shell
swapnil@SwapG-G15$ ls -C .git
COMMIT_EDITMSG  ORIG_HEAD  config       hooks  info  objects      refs
HEAD            branches   description  index  logs  packed-refs
swapnil@SwapG-G15$ ls -C .git/objects
0e  34  54  6c  7d  8e  b4  c1  c7  cf  f5  fb  info
16  4f  69  77  7e  b2  ba  c6  c9  d1  fa  fe  pack
swapnil@SwapG-G15$ ls -C .git/objects/09
ls: cannot access '.git/objects/09': No such file or directory
swapnil@SwapG-G15$ ls -C .git/objects/0e
ac6711f7d620fcd4f65eb7f9a9a2b82b22684a
swapnil@SwapG-G15$ cat .git/HEAD
ref: refs/heads/master
```
### Lab 23
```shell
swapnil@SwapG-G15$ git hist --max-count=1
* 34e3688 2023-05-03 | Moved hello.py to ./lib (HEAD -> master) [Swapnil Garg]
swapnil@SwapG-G15$ git cat-file -t 34e3688
commit
swapnil@SwapG-G15$ git cat-file -p 34e3688
tree fe0f982c88c680f1b1c36e308b983b49d69430fd
parent bae42375ba873eec29ee59d5c331cb0e5f2c9d23
author Swapnil Garg <swapnilgarg310504@gmail.com> 1683101491 +0530
committer Swapnil Garg <swapnilgarg310504@gmail.com> 1683101491 +0530

Moved hello.py to ./lib
swapnil@SwapG-G15$ git cat-file -p fe0f982c88c680f1b1c36e308b983b49d69430fd
040000 tree c782a78bafc4294e8926fd85d3137ec6b10cf1ad    lib
swapnil@SwapG-G15$ git cat-file -p c782a78bafc4294e8926fd85d3137ec6b10cf1ad
100644 blob 4ffe636bc934298597142a34fd8a3bf61e23a9a9    hello.py
swapnil@SwapG-G15$ git cat-file -p c782a78bafc4294e8926fd85d3137ec6b10cf1ad
100644 blob 4ffe636bc934298597142a34fd8a3bf61e23a9a9    hello.py
```
### Lab 24
```shell
swapnil@SwapG-G15$ git checkout -b greet
Switched to a new branch 'greet'
swapnil@SwapG-G15$ git status
On branch greet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

nothing added to commit but untracked files present (use "git add" to track)
swapnil@SwapG-G15$ git add lib/greeter.py
swapnil@SwapG-G15$ git commit -m "Added greeter class"
[greet 92e3e92] Added greeter class
 1 file changed, 8 insertions(+)
 create mode 100644 lib/greeter.py
swapnil@SwapG-G15$ git add lib/hello.py
swapnil@SwapG-G15$ git status
On branch greet
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py
        modified:   lib/hello.py

swapnil@SwapG-G15$ git commit -m "modified hello.py"
[greet ff81d38] modified hello.py
 2 files changed, 10 insertions(+), 1 deletion(-)
 create mode 100644 hello.py
```
### Lab 25
```shell 
swapnil@SwapG-G15$ git hist --all
* ff81d38 2023-05-03 | modified hello.py (HEAD -> greet) [Swapnil Garg]
* 92e3e92 2023-05-03 | Added greeter class [Swapnil Garg]
* 34e3688 2023-05-03 | Moved hello.py to ./lib (master) [Swapnil Garg]
* bae4237 2023-05-03 | Added an author name and email [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15$ cat lib/hello.py
import sys
#Default argument
#Author Swapnil, swapnilgarg310504@gmail.com
name = sys.argv[0] or "World"
print("Hello {}".format(name))swapnil@SwapG-G15$
swapnil@SwapG-G15$ git checkout greet
Switched to branch 'greet'
swapnil@SwapG-G15$ cat lib/greeter.py
class greeter:
    def __init__(self, who):
        self.who = who

    def greet(self):
        return "Hello {}".format(self.who)

```
### Lab 26
```shell
swapnil@SwapG-G15$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15$ git add README.md
swapnil@SwapG-G15$ git commit -m "Added README"
[master c0bc956] Added README
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```
### Lab 27
```shell
swapnil@SwapG-G15$ git hist --all
* c0bc956 2023-05-03 | Added README (HEAD -> master) [Swapnil Garg]
| * ff81d38 2023-05-03 | modified hello.py (greet) [Swapnil Garg]
| * 92e3e92 2023-05-03 | Added greeter class [Swapnil Garg]
|/
* 34e3688 2023-05-03 | Moved hello.py to ./lib [Swapnil Garg]
* bae4237 2023-05-03 | Added an author name and email [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```

### Lab 28
```shell 
swapnil@SwapG-G15$ git checkout greet
Switched to branch 'greet'
swapnil@SwapG-G15$ git merge master
Merge made by the 'ort' strategy.
 README.md | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
swapnil@SwapG-G15$ git hist --all
*   76a9a44 2023-05-03 | Merge branch 'master' into greet (HEAD -> greet) [Swapnil Garg]
|\
| * c0bc956 2023-05-03 | Added README (master) [Swapnil Garg]
* | ff81d38 2023-05-03 | modified hello.py [Swapnil Garg]
* | 92e3e92 2023-05-03 | Added greeter class [Swapnil Garg]
|/
* 34e3688 2023-05-03 | Moved hello.py to ./lib [Swapnil Garg]
* bae4237 2023-05-03 | Added an author name and email [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```

### Lab 29
```shell
swapnil@SwapG-G15$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15$ git add lib/hello.py
swapnil@SwapG-G15$ git commit -m "Made interactive"
[master 7c8d4b8] Made interactive
 1 file changed, 2 insertions(+), 2 deletions(-)
```
### Lab 30
```shell  
swapnil@SwapG-G15$ git hist --all
* 7c8d4b8 2023-05-03 | Made interactive (HEAD -> master) [Swapnil Garg]
| *   76a9a44 2023-05-03 | Merge branch 'master' into greet (greet) [Swapnil Garg]
| |\
| |/
|/|
* | c0bc956 2023-05-03 | Added README [Swapnil Garg]
| * ff81d38 2023-05-03 | modified hello.py [Swapnil Garg]
| * 92e3e92 2023-05-03 | Added greeter class [Swapnil Garg]
|/
* 34e3688 2023-05-03 | Moved hello.py to ./lib [Swapnil Garg]
* bae4237 2023-05-03 | Added an author name and email [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15$ git checkout greet
Switched to branch 'greet'
swapnil@SwapG-G15$ git merge master
Auto-merging lib/hello.py
CONFLICT (content): Merge conflict in lib/hello.py
Automatic merge failed; fix conflicts and then commit the result.
swapnil@SwapG-G15$ git add lib/hello.py
swapnil@SwapG-G15$ git commit -m "Merged master fixed conflict"
[greet 630bc72] Merged master fixed conflict
swapnil@SwapG-G15$ git hist --all
*   630bc72 2023-05-03 | Merged master fixed conflict (HEAD -> greet) [Swapnil Garg]
|\
| * 7c8d4b8 2023-05-03 | Made interactive (master) [Swapnil Garg]
* | 76a9a44 2023-05-03 | Merge branch 'master' into greet [Swapnil Garg]
|\|
| * c0bc956 2023-05-03 | Added README [Swapnil Garg]
* | ff81d38 2023-05-03 | modified hello.py [Swapnil Garg]
* | 92e3e92 2023-05-03 | Added greeter class [Swapnil Garg]
|/
* 34e3688 2023-05-03 | Moved hello.py to ./lib [Swapnil Garg]
* bae4237 2023-05-03 | Added an author name and email [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
```