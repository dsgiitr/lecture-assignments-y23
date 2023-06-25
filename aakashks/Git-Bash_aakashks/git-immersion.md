```bash
aks ~/git_tutorial
$ cd work/

aks ~/git_tutorial/work
$ mkdir hello

aks ~/git_tutorial/work
$ cd hello

aks ~/git_tutorial/work/hello
$ git init

aks ~/git_tutorial/work/hello (master)
$ touch hello.py

aks ~/git_tutorial/work/hello (master)
$ vim hello.py

aks ~/git_tutorial/work/hello (master)
$ git add hello.py
fatal: LF would be replaced by CRLF in hello.py

aks ~/git_tutorial/work/hello (master)
$ git config --global core.safecrlf warn

aks ~/git_tutorial/work/hello (master)
$ git add hello.py
warning: in the working copy of 'hello.py', LF will be replaced by CRLF the next time Git touches it

aks ~/git_tutorial/work/hello (master)
$ git commit -m "first commit"
[master (root-commit) 8b084ab] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
nothing to commit, working tree clean

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")

aks ~/git_tutorial/work/hello (master)
$

aks ~/git_tutorial/work/hello (master)
$ git add hello.py
warning: in the working copy of 'hello.py', LF will be replaced by CRLF the next time Git touches it

aks ~/git_tutorial/work/hello (master)
$ rm hello.py

aks ~/git_tutorial/work/hello (master)
$ touch hello.py

aks ~/git_tutorial/work/hello (master)
$ git add hello.py

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py


aks ~/git_tutorial/work/hello (master)
$ git commit
hint: Waiting for your editor to close the file... "C:\Softwares\Microsoft VS Code\Code.exe" --wait: line 1: C:\Softwares\Microsoft VS Code\Code.exe: No such file or directory
error: There was a problem with the editor '"C:\Softwares\Microsoft VS Code\Code.exe" --wait'.
Please supply the message using either -m or -F option.

aks ~/git_tutorial/work/hello (master)
$ git commit
hint: Waiting for your editor to close the file... "C:\Softwares\Microsoft VS Code\Code.exe" --wait: line 1: C:\Softwares\Microsoft VS Code\Code.exe: No such file or directory
error: There was a problem with the editor '"C:\Softwares\Microsoft VS Code\Code.exe" --wait'.
Please supply the message using either -m or -F option.

aks ~/git_tutorial/work/hello (master)
$ nano --version
 GNU nano, version 7.0
 (C) 2022 the Free Software Foundation and various contributors
 Compiled options: --enable-utf8

aks ~/git_tutorial/work/hello (master)
$ git config core.editor "nano"

aks ~/git_tutorial/work/hello (master)
$ git commit
[master dcfb54d] fixed CRLF issue didn't use Vim (which was the reason)
 1 file changed, 1 insertion(+), 1 deletion(-)

aks ~/git_tutorial/work/hello (master)
$ emacsclient
bash: emacsclient: command not found

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
nothing to commit, working tree clean


aks ~/git_tutorial/work/hello (master)
$ git hist
* ffb9efe 2023-05-02 | Added a comment (HEAD -> master) [aakashks]
* e6c326a 2023-05-02 | Added a default value [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git checkout 8b084ab
Note: switching to '8b084ab'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 8b084ab first commit

aks ~/git_tutorial/work/hello ((8b084ab...))
$ cat hello.py
print('hello world')

aks ~/git_tutorial/work/hello ((8b084ab...))
$ git checkout master
Previous HEAD position was 8b084ab first commit
Switched to branch 'master'

aks ~/git_tutorial/work/hello (master)
$ cat hello.py
import sys

# Default is "World"
name = "World" if len(sys.argv)==1 else sys.argv[1]

print(f'Hello, {name}!')
aks ~/git_tutorial/work/hello (master)
$ git tag v1

aks ~/git_tutorial/work/hello (master)
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

HEAD is now at e6c326a Added a default value

aks ~/git_tutorial/work/hello ((e6c326a...))
$ cat hello.py
import sys

name = "World" if len(sys.argv)==1 else sys.argv[1]

print(f'Hello, {name}!')
aks ~/git_tutorial/work/hello ((e6c326a...))
$ git tag v1-beta

aks ~/git_tutorial/work/hello ((v1-beta))
$ git checkout v1
Previous HEAD position was e6c326a Added a default value
HEAD is now at ffb9efe Added a comment

aks ~/git_tutorial/work/hello ((v1))
$ git checkout v1-beta
Previous HEAD position was ffb9efe Added a comment
HEAD is now at e6c326a Added a default value

aks ~/git_tutorial/work/hello ((v1-beta))
$ git tag
v1
v1-beta

aks ~/git_tutorial/work/hello ((v1-beta))
$ git hist master --all
* ffb9efe 2023-05-02 | Added a comment (tag: v1, master) [aakashks]
* e6c326a 2023-05-02 | Added a default value (HEAD, tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello ((v1-beta))
$ git checkout master
Previous HEAD position was e6c326a Added a default value
Switched to branch 'master'

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.py

no changes added to commit (use "git add" and/or "git commit -a")

aks ~/git_tutorial/work/hello (master)
$ git restore hello.py

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
nothing to commit, working tree clean

aks ~/git_tutorial/work/hello (master)
$ cat hello.py
import sys

# Default is "World"
name = "World" if len(sys.argv)==1 else sys.argv[1]

print(f'Hello, {name}!')
aks ~/git_tutorial/work/hello (master)
$


aks ~/git_tutorial/work/hello (master)
$ git add hello.py

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.py


aks ~/git_tutorial/work/hello (master)
$ git restore --staged hello.py

aks ~/git_tutorial/work/hello (master)
$ git checkout hello.py
Updated 1 path from the index

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
nothing to commit, working tree clean

aks ~/git_tutorial/work/hello (master)
$ git add hello.py

aks ~/git_tutorial/work/hello (master)
$ git commit -m "Oops, we didn't want this commit"
[master eb7f05b] Oops, we didn't want this commit
 1 file changed, 1 insertion(+), 1 deletion(-)

aks ~/git_tutorial/work/hello (master)
$ git reflog
eb7f05b (HEAD -> master) HEAD@{0}: commit: Oops, we didn't want this commit
ffb9efe (tag: v1) HEAD@{1}: checkout: moving from e6c326af6f1ec5a9809b5421686cf1beffa01860 to master
e6c326a (tag: v1-beta) HEAD@{2}: checkout: moving from ffb9efeb1222e907a60bb1d154bacf42db9256ba to v1-beta
ffb9efe (tag: v1) HEAD@{3}: checkout: moving from e6c326af6f1ec5a9809b5421686cf1beffa01860 to v1
e6c326a (tag: v1-beta) HEAD@{4}: checkout: moving from master to v1^
ffb9efe (tag: v1) HEAD@{5}: checkout: moving from 8b084ab5e1ea1483263125b8d628fe0f199d27f1 to master
8b084ab HEAD@{6}: checkout: moving from master to 8b084ab
ffb9efe (tag: v1) HEAD@{7}: commit: Added a comment
e6c326a (tag: v1-beta) HEAD@{8}: commit: Added a default value
dcfb54d HEAD@{9}: commit: fixed CRLF issue
8b084ab HEAD@{10}: commit (initial): first commit

aks ~/git_tutorial/work/hello (master)
$ git revert HEAD
[master e5eb51a] Revert "Oops, we didn't want this commit"
 1 file changed, 1 insertion(+), 1 deletion(-)

aks ~/git_tutorial/work/hello (master)
$ git hist
* e5eb51a 2023-05-03 | Revert "Oops, we didn't want this commit" (HEAD -> master) [aakashks]
* eb7f05b 2023-05-03 | Oops, we didn't want this commit [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git tag oops

aks ~/git_tutorial/work/hello (master)
$ git reflog
e5eb51a (HEAD -> master, tag: oops) HEAD@{0}: revert: Revert "Oops, we didn't want this commit"
eb7f05b HEAD@{1}: commit: Oops, we didn't want this commit
ffb9efe (tag: v1) HEAD@{2}: checkout: moving from e6c326af6f1ec5a9809b5421686cf1beffa01860 to master
e6c326a (tag: v1-beta) HEAD@{3}: checkout: moving from ffb9efeb1222e907a60bb1d154bacf42db9256ba to v1-beta
ffb9efe (tag: v1) HEAD@{4}: checkout: moving from e6c326af6f1ec5a9809b5421686cf1beffa01860 to v1
e6c326a (tag: v1-beta) HEAD@{5}: checkout: moving from master to v1^
ffb9efe (tag: v1) HEAD@{6}: checkout: moving from 8b084ab5e1ea1483263125b8d628fe0f199d27f1 to master
8b084ab HEAD@{7}: checkout: moving from master to 8b084ab
ffb9efe (tag: v1) HEAD@{8}: commit: Added a comment
e6c326a (tag: v1-beta) HEAD@{9}: commit: Added a default value
dcfb54d HEAD@{10}: commit: fixed CRLF issue
8b084ab HEAD@{11}: commit (initial): first commit

aks ~/git_tutorial/work/hello (master)
$ git reset --hard v1
HEAD is now at ffb9efe Added a comment

aks ~/git_tutorial/work/hello (master)
$ git hist
* ffb9efe 2023-05-02 | Added a comment (HEAD -> master, tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git hist --all
* e5eb51a 2023-05-03 | Revert "Oops, we didn't want this commit" (tag: oops) [aakashks]
* eb7f05b 2023-05-03 | Oops, we didn't want this commit [aakashks]
* ffb9efe 2023-05-02 | Added a comment (HEAD -> master, tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git tag -d oops
Deleted tag 'oops' (was e5eb51a)

aks ~/git_tutorial/work/hello (master)
$ git hist --all
* ffb9efe 2023-05-02 | Added a comment (HEAD -> master, tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git add hello.py

aks ~/git_tutorial/work/hello (master)
$ git commit -m "add an author comment"
[master 440a1c9] add an author comment
 1 file changed, 1 insertion(+)

aks ~/git_tutorial/work/hello (master)
$ git add hello.py

aks ~/git_tutorial/work/hello (master)
$ git commit --amend -m "Add author/email comment"
[master 30ba952] Add author/email comment
 Date: Wed May 3 12:35:12 2023 +0530
 1 file changed, 1 insertion(+)

aks ~/git_tutorial/work/hello (master)
$ git hist
* 30ba952 2023-05-03 | Add author/email comment (HEAD -> master) [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git log
commit 30ba9528d0ee1c2dbe04db216df8a5432a999da6 (HEAD -> master)
Author: aakashks <114357454+aakashks@users.noreply.github.com>
Date:   Wed May 3 12:35:12 2023 +0530

    Add author/email comment

commit ffb9efeb1222e907a60bb1d154bacf42db9256ba (tag: v1)
Author: aakashks <114357454+aakashks@users.noreply.github.com>
Date:   Tue May 2 23:50:06 2023 +0530

    Added a comment

commit e6c326af6f1ec5a9809b5421686cf1beffa01860 (tag: v1-beta)
Author: aakashks <114357454+aakashks@users.noreply.github.com>
Date:   Tue May 2 23:49:08 2023 +0530

    Added a default value

commit dcfb54d9753d2027fcd1a8b8d0e520eedafea90a
Author: aakashks <114357454+aakashks@users.noreply.github.com>
Date:   Tue May 2 22:27:25 2023 +0530

    fixed CRLF issue
    didn't use Vim (which was the reason)

commit 8b084ab5e1ea1483263125b8d628fe0f199d27f1
Author: aakashks <114357454+aakashks@users.noreply.github.com>
Date:   Tue May 2 17:35:05 2023 +0530

    first commit

aks ~/git_tutorial/work/hello (master)
$ mkdir lib

aks ~/git_tutorial/work/hello (master)
$ git mv hello.py lib

aks ~/git_tutorial/work/hello (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    hello.py -> lib/hello.py


aks ~/git_tutorial/work/hello (master)
$ git commit -m "Moved hello.py to lib"
[master dddb219] Moved hello.py to lib
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename hello.py => lib/hello.py (100%)

aks ~/git_tutorial/work/hello (master)
$ ls -C .git
COMMIT_EDITMSG  description  hooks/  info/  objects/   packed-refs
config          HEAD         index   logs/  ORIG_HEAD  refs/

aks ~/git_tutorial/work/hello (master)
$ ls -C .git/objects/
0b/  24/  44/  72/  79/  8b/  b0/  be/  c8/  dd/  e6/  ed/  fe/  info/
1c/  30/  48/  75/  7b/  9a/  b7/  c1/  dc/  e5/  eb/  f4/  ff/  pack/

aks ~/git_tutorial/work/hello (master)
$ ls -C .git/objects/0b
22a851ca4343f463ecc250179f8552b3551408

aks ~/git_tutorial/work/hello (master)
$ cat .git/config
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        ignorecase = true
        editor = nano
[alias]
  co = checkout
  ci = commit
  st = status
  br = branch
  hist = log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
  type = cat-file -t
  dump = cat-file -p
aks ~/git_tutorial/work/hello (master)
$ ls .git/refs/
heads/  tags/

aks ~/git_tutorial/work/hello (master)
$ ls .git/refs/heads/
master

aks ~/git_tutorial/work/hello (master)
$ ls .git/refs/tags/
v1  v1-beta

aks ~/git_tutorial/work/hello (master)
$ cat .git/refs/tags/v1
ffb9efeb1222e907a60bb1d154bacf42db9256ba

aks ~/git_tutorial/work/hello (master)
$ cat .git/HEAD
ref: refs/heads/master

aks ~/git_tutorial/work/hello (master)
$ git hist --max-count=1
* dddb219 2023-05-03 | Moved hello.py to lib (HEAD -> master) [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git cat-file -t dddb219
commit

aks ~/git_tutorial/work/hello (master)
$ git cat-file -p dddb219
tree 48e5a58f91d7c074a5418f37bd21d5928e57094b
parent 30ba9528d0ee1c2dbe04db216df8a5432a999da6
author aakashks <114357454+aakashks@users.noreply.github.com> 1683097839 +0530
committer aakashks <114357454+aakashks@users.noreply.github.com> 1683097839 +0530

Moved hello.py to lib

aks ~/git_tutorial/work/hello (master)
$ git hist
* dddb219 2023-05-03 | Moved hello.py to lib (HEAD -> master) [aakashks]
* 30ba952 2023-05-03 | Add author/email comment [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git cat-file -p 48e5a58f91d7c074a5418f37bd21d5928e57094b
040000 tree b01b1a1b8a8fb7bc0431190075399748331d981a    lib

aks ~/git_tutorial/work/hello (master)
$ git cat-file -p b01b1a1b8a8fb7bc0431190075399748331d981a
100644 blob beab0445092483a354afe792719f9dd9f7f85ccc    hello.py

aks ~/git_tutorial/work/hello (master)
$ git cat-file -p beab0445092483a354afe792719f9dd9f7f85ccc
import sys

# Default is "World"
# Author: Jim Weirich (jim@gamil.com)
name = "World" if len(sys.argv)==1 else sys.argv[1]

print(f'Hello, {name}!')
aks ~/git_tutorial/work/hello (master)
$ git checkout -b greet
Switched to a new branch 'greet'

aks ~/git_tutorial/work/hello (greet)
$ git status
On branch greet
nothing to commit, working tree clean

aks ~/git_tutorial/work/hello (greet)
$ cd lib/

aks ~/git_tutorial/work/hello/lib (greet)
$ touch greeter.py

aks ~/git_tutorial/work/hello/lib (greet)
$ nano greeter.py

aks ~/git_tutorial/work/hello/lib (greet)
$ cd ..

aks ~/git_tutorial/work/hello (greet)
$ git add .
warning: in the working copy of 'lib/greeter.py', LF will be replaced by CRLF the next time Git touches it

aks ~/git_tutorial/work/hello (greet)
$ git commit -m "Added greeter class"
[greet c325ccf] Added greeter class
 1 file changed, 6 insertions(+)
 create mode 100644 lib/greeter.py

aks ~/git_tutorial/work/hello (greet)
$ git add .
warning: in the working copy of 'lib/greeter.py', LF will be replaced by CRLF the next time Git touches it

aks ~/git_tutorial/work/hello (greet)
$ git add .

aks ~/git_tutorial/work/hello (greet)
$ git commit -m "Hello uses Greeter"
[greet f62f430] Hello uses Greeter
 2 files changed, 4 insertions(+), 2 deletions(-)

aks ~/git_tutorial/work/hello (greet)
$ git hist
* f62f430 2023-05-03 | Hello uses Greeter (HEAD -> greet) [aakashks]
* c325ccf 2023-05-03 | Added greeter class [aakashks]
* dddb219 2023-05-03 | Moved hello.py to lib (master) [aakashks]
* 30ba952 2023-05-03 | Add author/email comment [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (greet)
$ git checkout master
Switched to branch 'master'

aks ~/git_tutorial/work/hello (master)
$ cat lib/hello.py
import sys

# Default is "World"
# Author: Jim Weirich (jim@gamil.com)
name = "World" if len(sys.argv)==1 else sys.argv[1]

print(f'Hello, {name}!')
aks ~/git_tutorial/work/hello (master)
$ git checkout greet
Switched to branch 'greet'

aks ~/git_tutorial/work/hello (greet)
$ cat lib/hello.py
import sys
from greeter import Greeter

# Default is "World"
# Author: Jim Weirich (jim@gamil.com)
name = "World" if len(sys.argv)==1 else sys.argv[1]

greeter = Greeter(name)
print(greeter.greet)
aks ~/git_tutorial/work/hello (greet)
$ git checkout master
Switched to branch 'master'

aks ~/git_tutorial/work/hello (master)
$ git add README.md

aks ~/git_tutorial/work/hello (master)
$ git commit -m "Added README"
[master 75fa565] Added README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

aks ~/git_tutorial/work/hello (master)
$ git hist --all
* 75fa565 2023-05-03 | Added README (HEAD -> master) [aakashks]
| * f62f430 2023-05-03 | Hello uses Greeter (greet) [aakashks]
| * c325ccf 2023-05-03 | Added greeter class [aakashks]
|/
* dddb219 2023-05-03 | Moved hello.py to lib [aakashks]
* 30ba952 2023-05-03 | Add author/email comment [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git checkout greet
Switched to branch 'greet'

aks ~/git_tutorial/work/hello (greet)
$ git merge master
Merge made by the 'ort' strategy.
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

aks ~/git_tutorial/work/hello (greet)
$ git hist --all
*   a8308a1 2023-05-03 | Merge branch 'master' into greet (HEAD -> greet) [aakashks]
|\
| * 75fa565 2023-05-03 | Added README (master) [aakashks]
* | f62f430 2023-05-03 | Hello uses Greeter [aakashks]
* | c325ccf 2023-05-03 | Added greeter class [aakashks]
|/
* dddb219 2023-05-03 | Moved hello.py to lib [aakashks]
* 30ba952 2023-05-03 | Add author/email comment [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (greet)
$ git hist --all
*   a8308a1 2023-05-03 | Merge branch 'master' into greet (HEAD -> greet) [aakashks]
|\
| * 75fa565 2023-05-03 | Added README (master) [aakashks]
* | f62f430 2023-05-03 | Hello uses Greeter [aakashks]
* | c325ccf 2023-05-03 | Added greeter class [aakashks]
|/
* dddb219 2023-05-03 | Moved hello.py to lib [aakashks]
* 30ba952 2023-05-03 | Add author/email comment [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (greet)
$ git checkout master
Switched to branch 'master'

aks ~/git_tutorial/work/hello (master)
$ git add lib/hello.py

aks ~/git_tutorial/work/hello (master)
$ git commit -m "Made interactive"
[master 4e235ae] Made interactive
 1 file changed, 2 insertions(+), 6 deletions(-)

aks ~/git_tutorial/work/hello (master)
$ git hist --all
* 4e235ae 2023-05-03 | Made interactive (HEAD -> master) [aakashks]
| *   a8308a1 2023-05-03 | Merge branch 'master' into greet (greet) [aakashks]
| |\
| |/
|/|
* | 75fa565 2023-05-03 | Added README [aakashks]
| * f62f430 2023-05-03 | Hello uses Greeter [aakashks]
| * c325ccf 2023-05-03 | Added greeter class [aakashks]
|/
* dddb219 2023-05-03 | Moved hello.py to lib [aakashks]
* 30ba952 2023-05-03 | Add author/email comment [aakashks]
* ffb9efe 2023-05-02 | Added a comment (tag: v1) [aakashks]
* e6c326a 2023-05-02 | Added a default value (tag: v1-beta) [aakashks]
* dcfb54d 2023-05-02 | fixed CRLF issue didn't use Vim (which was the reason) [aakashks]
* 8b084ab 2023-05-02 | first commit [aakashks]

aks ~/git_tutorial/work/hello (master)
$ git checkout greet
Switched to branch 'greet'

aks ~/git_tutorial/work/hello (greet)
$ git merge master
Auto-merging lib/hello.py
CONFLICT (content): Merge conflict in lib/hello.py
Automatic merge failed; fix conflicts and then commit the result.

aks ~/git_tutorial/work/hello (greet|MERGING)
$ cat lib/hello.py
<<<<<<< HEAD
import sys
from greeter import Greeter

# Default is "World"
# Author: Jim Weirich (jim@gamil.com)
name = "World" if len(sys.argv)==1 else sys.argv[1]

greeter = Greeter(name)
print(greeter.greet)
=======
my_name = input("What's your name")

print(f"Hello, {my_name}!")
>>>>>>> master

aks ~/git_tutorial/work/hello (greet|MERGING)
$ git add lib/

aks ~/git_tutorial/work/hello (greet|MERGING)
$ git commit -m "Merged master fixed conflict."
[greet e6c66bf] Merged master fixed conflict.

aks ~/git_tutorial/work/hello (greet)
$
```