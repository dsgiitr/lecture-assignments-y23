###The made hello directory is manually added to this directory at the end

##Lab 1 and 2
Setup done according to instructions

##Lab3
Made the required directory in desktop of my pc
```console
cd desktop
cd hello
touch hello.rb
vim hello.rb
ruby hello.rb
Hello, World
git init
Initialized empty Git repository in /Users/aayanyadav/Desktop/hello/.git/
git add hello.rb
git commit -m "First Commit"
[main (root-commit) ba08ebd] First Commit
 1 file changed, 2 insertions(+)
 create mode 100644 hello.rb
```
`touch` was used to make the file and `vim` was used to add the required code in it. After that given instructions were followed


#Lab4
```console
git status
On branch main
nothing to commit, working tree clean
```


##Lab5
```console
vim hello.rb
git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
```
`vim` was used to make given changes in file


##Lab6
```console
git add hello.rb
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.rb
```

##Lab7
Theory about commiting and staging. Read✅

##Lab8
```console
git commit
```

**Using ARGV
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Changes to be committed:
#       modified:   hello.rb
#
~                                                                                                                                                            
:wq**

```console
[main eab9b0e] Using ARGV
 1 file changed, 1 insertion(+), 1 deletion(-)
git status
On branch main
nothing to commit, working tree clean
```

##Lab9
```console
vim hello.rb
```

**name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"

~                                                                               
:wq**

```console
git add hello.rb
vim hello.rb
```

**# Default is "World"
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"

~                                                                               
:wq**

```console
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.rb

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb
git commit -m "Added a default value"
[main 744c272] Added a default value
 1 file changed, 1 insertion(+)
git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
git add .
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.rb

git commit -m "Added a comment"
[main 0a16396] Added a comment
 1 file changed, 1 insertion(+)
```


##Lab10
```console
git log


commit 744c2727b2a78d731de431d63b6131ce1fcd0760
Author: Aayan Yadav <ydvaayan@gmail.com>
Date:   Thu May 4 00:15:00 2023 +0530

    Added a default value

commit eab9b0e01477471d3bd46a1652c9c008fff8149f
Author: Aayan Yadav <ydvaayan@gmail.com>
Date:   Thu May 4 00:03:20 2023 +0530

    Using ARGV

commit ba08ebdc34d0b68f9122afabdc44dee88a1881e4
Author: Aayan Yadav <ydvaayan@gmail.com>
Date:   Wed May 3 23:46:20 2023 +0530

    First Commit
```
```console
git log --pretty=oneline

0a163965454e2943daf70f2c5472ed7c64d1c109 (HEAD -> main) Added a comment
744c2727b2a78d731de431d63b6131ce1fcd0760 Added a default value
eab9b0e01477471d3bd46a1652c9c008fff8149f Using ARGV
ba08ebdc34d0b68f9122afabdc44dee88a1881e4 First Commit
```
```console
git log --pretty=oneline --max-count=2

0a163965454e2943daf70f2c5472ed7c64d1c109 (HEAD -> main) Added a comment
744c2727b2a78d731de431d63b6131ce1fcd0760 Added a default value
```
```console
git log --pretty=oneline --since='5 minutes ago'

```
empty output since no commits since 5 min ago
```
```console
git log --pretty=oneline --until='5 minutes ago'

0a163965454e2943daf70f2c5472ed7c64d1c109 (HEAD -> main) Added a comment
744c2727b2a78d731de431d63b6131ce1fcd0760 Added a default value
eab9b0e01477471d3bd46a1652c9c008fff8149f Using ARGV
ba08ebdc34d0b68f9122afabdc44dee88a1881e4 First Commit
```
```console
git log --pretty=oneline --author='Aayan Yadav'

0a163965454e2943daf70f2c5472ed7c64d1c109 (HEAD -> main) Added a comment
744c2727b2a78d731de431d63b6131ce1fcd0760 Added a default value
eab9b0e01477471d3bd46a1652c9c008fff8149f Using ARGV
ba08ebdc34d0b68f9122afabdc44dee88a1881e4 First Commit
```
```console
git log --pretty=oneline --all

0a163965454e2943daf70f2c5472ed7c64d1c109 (HEAD -> main) Added a comment
744c2727b2a78d731de431d63b6131ce1fcd0760 Added a default value
eab9b0e01477471d3bd46a1652c9c008fff8149f Using ARGV
ba08ebdc34d0b68f9122afabdc44dee88a1881e4 First Commit
```
```console
git log --pretty=format'%h %cd %s (%an)' --since='7 days ago'


format0a16396 Thu May 4 00:15:56 2023 +0530 Added a comment (Aayan Yadav)
format744c272 Thu May 4 00:15:00 2023 +0530 Added a default value (Aayan Yadav)
formateab9b0e Thu May 4 00:03:20 2023 +0530 Using ARGV (Aayan Yadav)
formatba08ebd Wed May 3 23:46:20 2023 +0530 First Commit (Aayan Yadav)
```
```console
git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short


* 0a16396 2023-05-04 | Added a comment (HEAD -> main) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
```


##Lab11
'''console
cd
vim .gitconfig
```
**[user]
        name = Aayan Yadav
        email = ydvaayan@gmail.com
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
~                                                                               
~                                                                               
~                                                                               
~                                                                               
:wq**
```console
vim .zshrc
```
added aliases here



##Lab12
```console
cd Desktop/Hello
git hist

* 0a16396 2023-05-04 | Added a comment (HEAD -> main) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
git checkout ba08ebd
Note: switching to 'ba08ebd'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at ba08ebd First Commit
cat hello.rb
puts "Hello, World"
git checkout main
Previous HEAD position was ba08ebd First Commit
Switched to branch 'main'
cat hello.rb
# Default is "World"
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"
```

##Lab13
```console
git tag v1
gitcheckout v1^
zsh: command not found: gitcheckout
git checkout v1^
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

HEAD is now at 744c272 Added a default value
git tag v1-beta
git checkout v1
Previous HEAD position was 744c272 Added a default value
HEAD is now at 0a16396 Added a comment
git checkout v1-beta
Previous HEAD position was 0a16396 Added a comment
HEAD is now at 744c272 Added a default value
git tag

v1
v1-beta
git hist

* 0a16396 2023-05-04 | Added a comment (HEAD, tag: v1, main) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
```


##Lab14
```console
vim hello.rb
```
**# This is a bad comment. We want to revert it.
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"

~                                                                               
:wq**
```console
git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   hello.rb

no changes added to commit (use "git add" and/or "git commit -a")
git checkout hello.rb
Updated 1 path from the index
git status
On branch main
nothing to commit, working tree clean
cat hello.rb
# Default is "World"
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"
```


##Lab15
```console
vim hello.rb
```
**# This is a unwanted but staged commit.
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"

:wq**
```console
git add hello.rb
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   hello.rb

git reset Head hello.rb
Unstaged changes after reset:
M	hello.rb
git checkout hello.rb
Updated 1 path from the index
git status
On branch main
nothing to commit, working tree clean
```


##Lab16
```console
vim hello.rb
```
**# This is an unwanted but commited change.
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"

:wq**
```console
git add hello.rb
git commit -m "Oops! we didnt want this commit"
[main 527a967] Oops! we didnt want this commit
 1 file changed, 1 insertion(+), 1 deletion(-)
git revert HEAD --no-edit
[main 94bd81b] Revert "Oops! we didnt want this commit"
 Date: Thu May 4 01:19:14 2023 +0530
 1 file changed, 1 insertion(+), 1 deletion(-)
git hist

* 94bd81b 2023-05-04 | Revert "Oops! we didnt want this commit" (HEAD -> main) [Aayan Yadav]
* 527a967 2023-05-04 | Oops! we didnt want this commit [Aayan Yadav]
* 0a16396 2023-05-04 | Added a comment (tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
```


##Lab17
```console
git hist

* 94bd81b 2023-05-04 | Revert "Oops! we didnt want this commit" (HEAD -> main) [Aayan Yadav]
* 527a967 2023-05-04 | Oops! we didnt want this commit [Aayan Yadav]
* 0a16396 2023-05-04 | Added a comment (tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]

git tag oops
git reset --hard v1
HEAD is now at 0a16396 Added a comment
git hist

* 0a16396 2023-05-04 | Added a comment (HEAD -> main, tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
git hist --all

* 94bd81b 2023-05-04 | Revert "Oops! we didnt want this commit" (tag: oops) [Aayan Yadav]
* 527a967 2023-05-04 | Oops! we didnt want this commit [Aayan Yadav]
* 0a16396 2023-05-04 | Added a comment (HEAD -> main, tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
```


##Lab18
```console
git tag -d oops
Deleted tag 'oops' (was 94bd81b)
git hist --all

* 0a16396 2023-05-04 | Added a comment (HEAD -> main, tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
```


##Lab19
```console
vim hello.rb
```
**# Default is "World"
#Author : Aayan Yadav
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"

:wq**

```console
git add hello.rb
git commit -m "Add an author comment"
[main 2af6418] Add an author comment
 1 file changed, 1 insertion(+)
vim hello.rb
```
**# Default is "World"
#Author : Aayan Yadav(abc@xyz.com)
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"

:wq**

```console
git commit --amend -m "Add an author/email comment"
[main b7755d4] Add an author/email comment
 Date: Thu May 4 01:35:27 2023 +0530
 1 file changed, 1 insertion(+)
git hist

* b7755d4 2023-05-04 | Add an author/email comment (HEAD -> main) [Aayan Yadav]
* 0a16396 2023-05-04 | Added a comment (tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
```


##Lab20
```console
mkdir lib
git mv hello.rb lib
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    hello.rb -> lib/hello.rb

git commit -m "move hello.rb to lib"
[main e1b5af1] move hello.rb to lib
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename hello.rb => lib/hello.rb (100%)
```


##Lab21
(made correction in hello.rb changed ARGV.first in puts to name)
```console
touch Rakefile
vim Rakefile
git add Rakefile
git commit -m "Added a Rakefile."
[main e14bc7e] Added a Rakefile.
 1 file changed, 7 insertions(+)
 create mode 100644 Rakefile
rake
Hello, World!
```


#Lab22
```console
ls -C .git
COMMIT_EDITMSG config         index          objects
HEAD           description    info           packed-refs
ORIG_HEAD      hooks          logs           refs
ls -C .git/objects
0a   20   25   2a   3d   5e   6d   74   96   ad   b7   c2   e1   ea   pack
11   21   28   2c   52   6a   71   94   ab   b4   ba   dc   e3   info
ls -C .git/objects/94
bd81b51995efea1cfea824ef68244ab6957274
cat .git/config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
ls .git/refs
heads tags
ls .git/refs/heads
main
ls .git/refs/tags
v1      v1-beta
cat .git/refs/tags/v1
0a163965454e2943daf70f2c5472ed7c64d1c109
cat .git/HEAD
ref: refs/heads/main
```


##Lab23
```console
git hist --max-count=2

* 9641f12 2023-05-04 | Correction in hello.rb (HEAD -> main) [Aayan Yadav]
* e14bc7e 2023-05-04 | Added a Rakefile. [Aayan Yadav]
git cat-file -t e14bc7e
commit
git cat-file -p e14bc7e
tree b42f33140a8623e21140d03dcd5a469774336200
parent e1b5af191a5826578271bcc697bc28086ea78d9e
author Aayan Yadav <ydvaayan@gmail.com> 1683149889 +0530
committer Aayan Yadav <ydvaayan@gmail.com> 1683149889 +0530

Added a Rakefile.
git cat-file -p b42f331
100644 blob 28e0e9d6ea7e25f35ec64a43f569b550e8386f90	Rakefile
040000 tree 6d629c22ed12b2ee4754fa25601ff2a50699eeb0	lib
❯ git cat-file -p 6d629c2
100644 blob abd5e85bd13222daaff50ecea40a1518c7d64b40	hello.rb
❯ git cat-file -p abd5e85
# Default is "World"
#Author : Aayan Yadav
name = ARGV.first || "World"
puts "Hello, #{ARGV.first}!"
```


##Lab24
```console
git checkout -b greet
Switched to a new branch 'greet'
git status
On branch greet
nothing to commit, working tree clean
touch lib/greeter.rb
vim lib/greeter.rb
```
**class Greeter
  def initialize(who)
    @who = who
  end
  def greet
    "Hello, #{@who}"
  end
end
~                                                                               
:wq**
```console
git add lib/greeter.rb
git commit -m "Added greeter class"
[greet bef1892] Added greeter class
 1 file changed, 8 insertions(+)
 create mode 100644 lib/greeter.rb
vim lib/hello.rb 
```
**require 'greeter'

# Default is "World"

name = ARGV.first || "World"
greeter=Greeter.new(name)
puts greeter.greet

:wq**
```console
git add lib/hello.rb
git commit -m "Hello uses Greeter"
[greet f085c7b] Hello uses Greeter
 1 file changed, 5 insertions(+), 2 deletions(-)
```


##Lab25
```console
git hist --all

* f085c7b 2023-05-04 | Hello uses Greeter (HEAD -> greet) [Aayan Yadav]
* bef1892 2023-05-04 | Added greeter class [Aayan Yadav]
* 9641f12 2023-05-04 | Correction in hello.rb (main) [Aayan Yadav]
* e14bc7e 2023-05-04 | Added a Rakefile. [Aayan Yadav]
* e1b5af1 2023-05-04 | move hello.rb to lib [Aayan Yadav]
* b7755d4 2023-05-04 | Add an author/email comment [Aayan Yadav]
* 0a16396 2023-05-04 | Added a comment (tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]

git checkout main
Switched to branch 'main'
❯ cat lib/hello.rb
# Default is "World"
#Author : Aayan Yadav
name = ARGV.first || "World"
puts "Hello, #{name}!"

❯ git checkout greet
Switched to branch 'greet'
❯ cat lib/hello.rb
require 'greeter'

# Default is "World"

name = ARGV.first || "World"
greeter=Greeter.new(name)
puts greeter.greet
```


##Lab26
```console
git checkout main
Switched to branch 'main'
touch README
vim README
```
**This is the Hello World example for the git tutorial
~                                                                               
~                                                                               
~                                                                               
:wq**
```console
git add README
git commit -m "Added README"
[main 036ba75] Added README
 1 file changed, 1 insertion(+)
 create mode 100644 README
```

##Lab27
```console
git hist --all

* 036ba75 2023-05-04 | Added README (HEAD -> main) [Aayan Yadav]
| * f085c7b 2023-05-04 | Hello uses Greeter (greet) [Aayan Yadav]
| * bef1892 2023-05-04 | Added greeter class [Aayan Yadav]
|/  
* 9641f12 2023-05-04 | Correction in hello.rb [Aayan Yadav]
* e14bc7e 2023-05-04 | Added a Rakefile. [Aayan Yadav]
* e1b5af1 2023-05-04 | move hello.rb to lib [Aayan Yadav]
* b7755d4 2023-05-04 | Add an author/email comment [Aayan Yadav]
* 0a16396 2023-05-04 | Added a comment (tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
```


##Lab28
```console
git checkout greet
Switched to branch 'greet'

git merge main
Merge made by the 'ort' strategy.
 README | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README
git hist --all

*   2376632 2023-05-04 | Merge branch 'main' into greet (HEAD -> greet) [Aayan Yadav]
|\  
| * 036ba75 2023-05-04 | Added README (main) [Aayan Yadav]
* | f085c7b 2023-05-04 | Hello uses Greeter [Aayan Yadav]
* | bef1892 2023-05-04 | Added greeter class [Aayan Yadav]
|/  
* 9641f12 2023-05-04 | Correction in hello.rb [Aayan Yadav]
* e14bc7e 2023-05-04 | Added a Rakefile. [Aayan Yadav]
* e1b5af1 2023-05-04 | move hello.rb to lib [Aayan Yadav]
```


##Lab29
```console
git checkout main
Switched to branch 'main'
vim lib/hello.rb
```
**puts "What's your name"
my_name = gets.strip

puts "Hello, #{my_name}!"

:wq**
```console
git add lib/hello.rb
git commit -m "Made Interactive"
[main 57ec06d] Made Interactive
 1 file changed, 4 insertions(+), 4 deletions(-)
git hist --all

* 57ec06d 2023-05-04 | Made Interactive (HEAD -> main) [Aayan Yadav]
| *   2376632 2023-05-04 | Merge branch 'main' into greet (greet) [Aayan Yadav]
| |\  
| |/  
|/|   
* | 036ba75 2023-05-04 | Added README [Aayan Yadav]
| * f085c7b 2023-05-04 | Hello uses Greeter [Aayan Yadav]
| * bef1892 2023-05-04 | Added greeter class [Aayan Yadav]
|/  
* 9641f12 2023-05-04 | Correction in hello.rb [Aayan Yadav]
* e14bc7e 2023-05-04 | Added a Rakefile. [Aayan Yadav]
* e1b5af1 2023-05-04 | move hello.rb to lib [Aayan Yadav]
* b7755d4 2023-05-04 | Add an author/email comment [Aayan Yadav]
* 0a16396 2023-05-04 | Added a comment (tag: v1) [Aayan Yadav]
* 744c272 2023-05-04 | Added a default value (tag: v1-beta) [Aayan Yadav]
* eab9b0e 2023-05-04 | Using ARGV [Aayan Yadav]
* ba08ebd 2023-05-03 | First Commit [Aayan Yadav]
~
```


##Lab30
```console
git checkout greet
git merge main
Auto-merging lib/hello.rb
CONFLICT (content): Merge conflict in lib/hello.rb
Automatic merge failed; fix conflicts and then commit the result.
vim lib/hello.rb  
**require 'greeter'

puts "What's your name"
my_name = gets.strip

greeter = Greeter.new(my_name)
puts greeter.greet<<<<<<< HEAD
:wq**
```console
git add lib/hello.rb
git commit -m "Merged master fixed conflict"
[greet 5aa26c3] Merged master fixed conflict
```