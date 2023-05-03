```shell
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work$ mkdir hello
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work$ cd helloswapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ touch hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git init
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m
error: switch `m` requires a value
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "First commit
> "
[master (root-commit) 7771f50] First commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
nothing to commit, working tree clean
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commiy
git: 'commiy' is not a git command. See 'git --help'.

The most similar command is
        commit
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit
[master f5dfb2a] Addded command line arguments to hello.py
 1 file changed, 4 insertions(+), 1 deletion(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
nothing to commit, working tree clean
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ gti status
Command 'gti' not found, did you mean:
  command 'ti' from deb ticgit (1.0.2.17-2.1)
  command 'gsi' from deb gambc (4.9.3-1.2)
  command 'gtf' from deb xserver-xorg-core (2:21.1.4-2ubuntu1.7~22.04.1)
  command 'gth' from deb genomethreader (1.7.3+dfsg-6)
  command 'gli' from deb ruby-gli (2.14.0-1.1)
  command 'gt' from deb genometools (1.6.2+ds-2)
  command 'bti' from deb bti (034-6)
  command 'git' from deb git (1:2.34.1-1ubuntu1.8)
  command 'ghi' from deb ghi (1.2.0-1.1)
  command 'gt5' from deb gt5 (1.5.0~20111220+bzr29-4)
  command 'gmi' from deb lieer (1.3-6)
Try: sudo apt install <deb name>
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Added default arguments to hello.py"
[master d116fab] Added default arguments to hello.py
 1 file changed, 2 insertions(+), 2 deletions(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add .
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Added comments for better readability"
[master 0eac671] Added comments for better readability
 1 file changed, 1 insertion(+), 1 deletion(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git log
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git log --pretty=oneline
0eac6711f7d620fcd4f65eb7f9a9a2b82b22684a (HEAD -> master) Added comments for better readability
d116fabafe16cc1f6e9d29f1eb330801ca1514da Added default arguments to hello.py
f5dfb2a5dabe6a664f899fee1bc801802fe20f8f Addded command line arguments to hello.py
7771f50f57d836708ed87b3a0fb48482934af78d First commit
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cd $HOME
swapnil@SwapG-G15:~$ ls -l
total 0
swapnil@SwapG-G15:~$ find .gitconfig
.gitconfig
swapnil@SwapG-G15:~$ which .gitconfig
swapnil@SwapG-G15:~$ git hist
git: 'hist' is not a git command. See 'git --help'.

The most similar command is
        bisect
swapnil@SwapG-G15:~$ cd -
/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ gti hist
Command 'gti' not found, did you mean:
  command 'gsi' from deb gambc (4.9.3-1.2)
  command 'ti' from deb ticgit (1.0.2.17-2.1)
  command 'gth' from deb genomethreader (1.7.3+dfsg-6)
  command 'git' from deb git (1:2.34.1-1ubuntu1.8)
  command 'gt' from deb genometools (1.6.2+ds-2)
  command 'bti' from deb bti (034-6)
  command 'gli' from deb ruby-gli (2.14.0-1.1)
  command 'gmi' from deb lieer (1.3-6)
  command 'gtf' from deb xserver-xorg-core (2:21.1.4-2ubuntu1.7~22.04.1)
  command 'ghi' from deb ghi (1.2.0-1.1)
  command 'gt5' from deb gt5 (1.5.0~20111220+bzr29-4)
Try: sudo apt install <deb name>
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout 7771f50
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout master
Previous HEAD position was 7771f50 First commit
Switched to branch 'master'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git tag v1
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout v1^
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cat hello.py
import sys

name = sys.argv[0] or "World"
print("Hello {}".format(name))swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git tag v1-beta
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout v1
Previous HEAD position was d116fab Added default arguments to hello.py
HEAD is now at 0eac671 Added comments for better readability
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout v1-beat
error: pathspec 'v1-beat' did not match any file(s) known to git
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout v1-beta
Previous HEAD position was 0eac671 Added comments for better readability
HEAD is now at d116fab Added default arguments to hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout v1
Previous HEAD position was d116fab Added default arguments to hello.py
HEAD is now at 0eac671 Added comments for better readability
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git tag
v1
v1-beta
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist master
* 0eac671 2023-05-03 | Added comments for better readability (HEAD, tag: v1, master) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist master --all
* 0eac671 2023-05-03 | Added comments for better readability (HEAD, tag: v1, master) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout hello.py
Updated 1 path from the index
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
nothing to commit, working tree clean
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cat hello.py
import sys
#Default argument
name = sys.argv[0] or "World"
print("Hello {}".format(name))swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tuto  swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git reset HEAD hello.py
Unstaged changes after reset:
M       hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout hello.py
Updated 1 path from the index
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
nothing to commit, working tree clean
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Ooops"
[master cfc2147] Ooops
 1 file changed, 1 insertion(+), 1 deletion(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git revert HEAD
[master fad87a2] Revert "Ooops"
 1 file changed, 1 insertion(+), 1 deletion(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git log
commit fad87a22f881b36d1054ca9987e1659073c609fe (HEAD -> master)
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:54:35 2023 +0530

    Revert "Ooops"

    This reverts commit cfc2147aebbc97dc0b597317edb2b12b4edcfd67.

commit cfc2147aebbc97dc0b597317edb2b12b4edcfd67
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:54:25 2023 +0530

    Ooops

commit 0eac6711f7d620fcd4f65eb7f9a9a2b82b22684a (tag: v1)
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:18:34 2023 +0530

    Added comments for better readability

commit d116fabafe16cc1f6e9d29f1eb330801ca1514da (tag: v1-beta)
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist
* fad87a2 2023-05-03 | Revert "Ooops" (HEAD -> master) [Swapnil Garg]
* cfc2147 2023-05-03 | Ooops [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git tag oops
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git reset --hard v1
HEAD is now at 0eac671 Added comments for better readability
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master, tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
* fad87a2 2023-05-03 | Revert "Ooops" (tag: oops) [Swapnil Garg]
* cfc2147 2023-05-03 | Ooops [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master, tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
* fad87a2 2023-05-03 | Revert "Ooops" (tag: oops) [Swapnil Garg]
* cfc2147 2023-05-03 | Ooops [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master, tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git tag -d oops
Deleted tag 'oops' (was fad87a2)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
* 0eac671 2023-05-03 | Added comments for better readability (HEAD -> master, tag: v1)
[Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Added author comment"
[master b2a6568] Added author comment
 1 file changed, 2 insertions(+), 1 deletion(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit --amend -m "Added an author name and email"
[master bae4237] Added an author name and email
 Date: Wed May 3 13:27:58 2023 +0530
 1 file changed, 2 insertions(+), 1 deletion(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist
* bae4237 2023-05-03 | Added an author name and email (HEAD -> master) [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ mkdir lib
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git mv hello.py lib
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    hello.py -> lib/hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Moved hello.py to ./lib"
[master 34e3688] Moved hello.py to ./lib
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename hello.py => lib/hello.py (100%)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git log
commit 34e3688aacd4d2123f83040c645eef7724d0db3f (HEAD -> master)
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 13:41:31 2023 +0530

    Moved hello.py to ./lib

commit bae42375ba873eec29ee59d5c331cb0e5f2c9d23
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 13:27:58 2023 +0530

    Added an author name and email

commit 0eac6711f7d620fcd4f65eb7f9a9a2b82b22684a (tag: v1)
Author: Swapnil Garg <swapnilgarg310504@gmail.com>
Date:   Wed May 3 12:18:34 2023 +0530

    Added comments for better readability

commit d116fabafe16cc1f6e9d29f1eb330801ca1514da (tag: v1-beta)
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist
* 34e3688 2023-05-03 | Moved hello.py to ./lib (HEAD -> master) [Swapnil Garg]
* bae4237 2023-05-03 | Added an author name and email [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ python
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls -C .git
COMMIT_EDITMSG  ORIG_HEAD  config       hooks  info  objects      refs
HEAD            branches   description  index  logs  packed-refs
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls -C .git/objects
0e  34  54  6c  7d  8e  b4  c1  c7  cf  f5  fb  info
16  4f  69  77  7e  b2  ba  c6  c9  d1  fa  fe  pack
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls -C .git/objects/09
ls: cannot access '.git/objects/09': No such file or directory
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls -C .git/objects/0e
ac6711f7d620fcd4f65eb7f9a9a2b82b22684a
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cat .git/HEAD
ref: refs/heads/master
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --max-count=1
* 34e3688 2023-05-03 | Moved hello.py to ./lib (HEAD -> master) [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git cat-file -t 34e3688
commit
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git cat-file -p 34e3688
tree fe0f982c88c680f1b1c36e308b983b49d69430fd
parent bae42375ba873eec29ee59d5c331cb0e5f2c9d23
author Swapnil Garg <swapnilgarg310504@gmail.com> 1683101491 +0530
committer Swapnil Garg <swapnilgarg310504@gmail.com> 1683101491 +0530

Moved hello.py to ./lib
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git cat-file -p fe0f982c88c680f1b1c36e308b983b49d69430fd
040000 tree c782a78bafc4294e8926fd85d3137ec6b10cf1ad    lib
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git cat-file -p c782a78bafc4294e8926fd85d3137ec6b10cf1ad
100644 blob 4ffe636bc934298597142a34fd8a3bf61e23a9a9    hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git cat-file -p c782a78bafc4294e8926fd85d3137ec6b10cf1ad
100644 blob 4ffe636bc934298597142a34fd8a3bf61e23a9a9    hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout -b greet
Switched to a new branch 'greet'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

nothing added to commit but untracked files present (use "git add" to track)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Added greeter class"
[greet 92e3e92] Added greeter class
 1 file changed, 8 insertions(+)
 create mode 100644 lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Added greeter class"
On branch greet
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   lib/hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   lib/hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   lib/hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/hello.py
hello.py  lib/
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/hello.py
hello.py  lib/
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$   swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls -l
total 0
-rwxrwxrwx 1 swapnil swapnil  139 May  3 14:46 hello.py
drwxrwxrwx 1 swapnil swapnil 4096 May  3  2023 lib
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls lib
greeter.py  hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   lib/hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py

no changes added to commit (use "git add" and/or "git commit -a")
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ lshello.py  lib
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cd.
Command 'cd.' not found, did you mean:
  command 'cdw' from deb cdw (0.8.1-2)
  command 'cd5' from deb cd5 (0.1-4)
  command 'cde' from deb cde (0.1+git9-g551e54d-1.2)
  command 'cdb' from deb tinycdb (0.78build3)
  command 'cdi' from deb cdo (2.0.4-1)
  command 'cdp' from deb irpas (0.10-9)
  command 'cdo' from deb cdo (2.0.4-1)
Try: sudo apt install <deb name>
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cd ..
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work$ cd -
/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add -all
error: did you mean `--all` (with two dashes)?
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add --all
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py
        modified:   lib/hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add greeter.py
fatal: pathspec 'greeter.py' did not match any files
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py
        modified:   lib/hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py
        modified:   lib/hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.py
        modified:   lib/hello.py

swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "modified hello.py"
[greet ff81d38] modified hello.py
 2 files changed, 10 insertions(+), 1 deletion(-)
 create mode 100644 hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
nothing to commit, working tree clean
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/greeter.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git status
On branch greet
nothing to commit, working tree clean
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls-l
ls-l: command not found
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls -l
total 0
-rwxrwxrwx 1 swapnil swapnil  139 May  3 14:46 hello.py
drwxrwxrwx 1 swapnil swapnil 4096 May  3  2023 lib
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ ls lib -l
total 0
-rwxrwxrwx 1 swapnil swapnil 152 May  3  2023 greeter.py
-rwxrwxrwx 1 swapnil swapnil 182 May  3  2023 hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ t
hist -all
t: command not found
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist -all
error: switch `l`s expects a numerical value
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
* ff81d38 2023-05-03 | modified hello.py (HEAD -> greet) [Swapnil Garg]
* 92e3e92 2023-05-03 | Added greeter class [Swapnil Garg]
* 34e3688 2023-05-03 | Moved hello.py to ./lib (master) [Swapnil Garg]
* bae4237 2023-05-03 | Added an author name and email [Swapnil Garg]
* 0eac671 2023-05-03 | Added comments for better readability (tag: v1) [Swapnil Garg]
* d116fab 2023-05-03 | Added default arguments to hello.py (tag: v1-beta) [Swapnil Garg]
* f5dfb2a 2023-05-03 | Addded command line arguments to hello.py [Swapnil Garg]
* 7771f50 2023-05-03 | First commit [Swapnil Garg]
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cat lib/hello.py
import sys
#Default argument
#Author Swapnil, swapnilgarg310504@gmail.com
name = sys.argv[0] or "World"
print("Hello {}".format(name))swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout greet
Switched to branch 'greet'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ cat lib/greeter.py
class greeter:
    def __init__(self, who):
        self.who = who

    def greet(self):
        return "Hello {}".format(self.who)

    swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add README.md
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Added README"
[master c0bc956] Added README
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout greet
Switched to branch 'greet'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git merge master
Merge made by the 'ort' strategy.
 README.md | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout master
Switched to branch 'master'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Made interactive"
[master 7c8d4b8] Made interactive
 1 file changed, 2 insertions(+), 2 deletions(-)
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git checkout greet
Switched to branch 'greet'
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git merge master
Auto-merging lib/hello.py
CONFLICT (content): Merge conflict in lib/hello.py
Automatic merge failed; fix conflicts and then commit the result.
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git add lib/hello.py
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git commit -m "Merged master fixed conflict"
[greet 630bc72] Merged master fixed conflict
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$ git hist --all
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
swapnil@SwapG-G15:/mnt/c/Users/swapn/downloads/git_tutorial/git_tutorial/work/hello$
```