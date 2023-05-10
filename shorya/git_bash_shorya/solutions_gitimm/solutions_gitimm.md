### Documentation(only imp results)

(Format-> lab no

		command

		output
)

**Lab 9(git saves instances)**

    vim hello.rb

	(changed the file in vim,first version)

	git add hello.rb

	(added first instance of file)

	vim hello.rb

	(edited the file again,creating a second version)

	git status

	On branch master

	Changes to be committed:

	(use "git restore --staged <file>..." to unstage)

			modified:   hello.rb

	Changes not staged for commit:

	(use "git add <file>..." to update what will be committed)

	(use "git restore <file>..." to discard changes in working directory)

			modified:   hello.rb

	git commit -m "Added a default value"

	(committed the first version to master)

	master 371dc04] Added a default value

	1 file changed, 2 insertions(+), 1 deletion(-)

	git status

	On branch master

	Changes not staged for commit:

	(use "git add <file>..." to update what will be committed)

	(use "git restore <file>..." to discard changes in working directory)

			modified:   hello.rb

	no changes added to commit (use "git add" and/or "git commit -a")

	git add .

	(added all the files in current branch on my local machine,adds the 2nd version)

	git status

	On branch master

	Changes to be committed:

	(use "git restore --staged <file>..." to unstage)

			modified:   hello.rb

	git commit -m "Added a comment"

	(commited the 2nd version)

	[master 372616f] Added a comment

	1 file changed, 1 insertion(+)

**lab 10(history)**

	git log

	commit 372616f5cfa0c0b747bb4deca1e3b7bfc3c1a2c0 (HEAD -> master)

	Author: shorya1835 <shoryasinghal1835@gmail.com>

	Date:   Sun Apr 29 00:42:00 2023 +0530

		Added a comment

	commit 371dc0434fefdafa90eba8db5401015d625d2ffe

	Author: shorya1835 <shoryasinghal1835@gmail.com>

	Date:   Sun Apr 29 00:36:17 2023 +0530

		Added a default value

	commit 4628639ae33efbd043cdcbb706aea2b2e83c32df

	Author: shorya1835 <shoryasinghal1835@gmail.com>

	Date:   Sun Apr 29 00:33:29 2023 +0530

		Using ARGV

	commit 4e91af0ae78557e39bed10c4024214c63b4ebd70

	Author: shorya1835 <shoryasinghal1835@gmail.com>

	Date:   Sun Apr 29 00:30:31 2023 +0530

		First Commit

	git log ---pretty=oneline

	372616f5cfa0c0b747bb4deca1e3b7bfc3c1a2c0 (HEAD -> master) Added a comment

	371dc0434fefdafa90eba8db5401015d625d2ffe Added a default value

	4628639ae33efbd043cdcbb706aea2b2e83c32df Using ARGV

	4e91af0ae78557e39bed10c4024214c63b4ebd70 First Commit

**lab 11(aliases)**

	git config --global alias.hist "log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"

	(added the alias)

	git hist

	\* 372616f 2023-04-30 | Added a comment (HEAD -> master) [shorya1835]

	\* 371dc04 2023-04-30 | Added a default value [shorya1835]

	\* 4628639 2023-04-30 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-30 | First Commit [shorya1835]

**lab 12 (getting older versions)**

	git checkout 4e91af0

	Note: switching to '4e91af0'.

	You are in 'detached HEAD' state. You can look around, make experimental

	changes and commit them, and you can discard any commits you make in this

	state without impacting any branches by switching back to a branch.

	If you want to create a new branch to retain commits you create, you may

	do so (now or later) by using -c with the switch command. Example:

	git switch -c <new-branch-name>

	Or undo this operation with:

	git switch -

	Turn off this advice by setting config variable advice.detachedHead to false

	HEAD is now at 4e91af0 First Commit

	cat hello.rb

	puts "Hello, World"

	git checkout master(takes it to the latest commit)

	Previous HEAD position was 4e91af0 First Commit

	Switched to branch 'master

	cat hello.rb

	# Default is "World"

	name = ARGV.first || "World"

	puts "Hello, #{name}!"

**lab 13(tagging versions)**

	git tag v1

	(tagged current version)

	git checkout v1~1

	Note: switching to 'v1~1'.

	You are in 'detached HEAD' state. You can look around, make experimental

	changes and commit them, and you can discard any commits you make in this

	state without impacting any branches by switching back to a branch.

	If you want to create a new branch to retain commits you create, you may

	do so (now or later) by using -c with the switch command. Example:

	git switch -c <new-branch-name>

	Or undo this operation with:

	git switch -

	Turn off this advice by setting config variable advice.detachedHead to false

	HEAD is now at 371dc04 Added a default value


	git tag v1-beta

	(tagged the parent of v1(third commit))

	git checkout v1

	Previous HEAD position was 371dc04 Added a default value

	HEAD is now at 372616f Added a comment

	git checkout v1-beta

	Previous HEAD position was 372616f Added a comment

	HEAD is now at 371dc04 Added a default value

	git tag

	v1

	v1-beta

	git hist master -all

	\* 372616f 2023-04-29 | Added a comment (tag: v1, master) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (HEAD, tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

**lab 14**

	git status

	On branch master

	Changes not staged for commit:

	(use "git add <file>..." to update what will be committed)

	(use "git restore <file>..." to discard changes in working directory)

			modified:   hello.rb

	no changes added to commit (use "git add" and/or "git commit -a")


	git checkout hello.rb

	Updated 1 path from the index

	git status

	On branch master

	nothing to commit, working tree clean

**lab 15**

	git status

	On branch master

	Changes to be committed:

	(use "git restore --staged <file>..." to unstage)

			modified:   hello.rb

	git restore --staged hello.rb

	git status

	On branch master

	Changes not staged for commit:

	(use "git add <file>..." to update what will be committed)

	(use "git restore <file>..." to discard changes in working directory)

			modified:   hello.rb

	no changes added to commit (use "git add" and/or "git commit -a")

	git checkout hello.rb

	Updated 1 path from the index

**lab 16**

	git add hello.rb

	git commit -m "Oops, we didn't want this commit"

	[master 935ac84] Oops, we didn't want this commit

	1 file changed, 1 insertion(+), 1 deletion(-)

	git revert HEAD

	[master 2d9c2ba] Revert "Oops, we didn't want this commit"

	 1 file changed, 1 insertion(+), 1 deletion(-)

	git hist

	\* 2d9c2ba 2023-04-29 | Revert "Oops, we didn't want this commit" (HEAD -> master) [shorya1835]

	\* 935ac84 2023-04-29 | Oops, we didn't want this commit [shorya1835]

	\* 372616f 2023-04-29 | Added a comment (tag: v1) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

**lab 17**

	git tag oops

	git reset --hard v1

	HEAD is now at 372616f Added a comment

	git hist

	\* 372616f 2023-04-29 | Added a comment (HEAD -> master, tag: v1) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

	git hist --all

	\* 2d9c2ba 2023-04-29 | Revert "Oops, we didn't want this commit" (tag: oops) [shorya1835]

	\* 935ac84 2023-04-29 | Oops, we didn't want this commit [shorya1835]

	\* 372616f 2023-04-29 | Added a comment (HEAD -> master, tag: v1) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

**lab 18**

	git tag -d oops

	Deleted tag 'oops' (was 2d9c2ba)

	git hist --all

	\* 372616f 2023-04-29 | Added a comment (HEAD -> master, tag: v1) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

**lab 19**

	git commit  -m "Add an author commit"

	[master cbe7338] Add an author commit

	 1 file changed, 2 insertions(+), 1 deletion(-)

	git commit --amend -m "Add an author/email comment"

	[master 865ad92] Add an author/email comment

	Date: Sun Apr 29 14:53:11 2023 +0530

	 1 file changed, 2 insertions(+), 1 deletion(-)

	git hist

	\* 865ad92 2023-04-29 | Add an author/email comment (HEAD -> master) [shorya1835]

	\* 372616f 2023-04-29 | Added a comment (tag: v1) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

**lab 20**

	mkdir lib

	git mv hello.rb lib

	git status

	On branch master

	Changes to be committed:

	(use "git restore --staged <file>..." to unstage)

			renamed:    hello.rb -> lib/hello.rb

	git commit -m "Moved hello.rb to lib"

	[master f501dd9] Moved hello.rb to lib

	 1 file changed, 0 insertions(+), 0 deletions(-)

	 rename hello.rb => lib/hello.rb (100%)

**lab 23**

	git cat-file -t f501dd9

	commit

	git cat-file -p f501dd9

	tree 2a25d9d6f632333a1abcfde35d2a423a8b94a4c1

	parent 865ad92a83317db5f3bfd3a645ce8856ec6cd63b

	author shorya1835 <shoryasinghal1835@gmail.com> 1682846961 +0530

	committer shorya1835 <shoryasinghal1835@gmail.com> 1682846961 +0530

	Moved hello.rb to lib


	git dump 2a25d9d6f632333a1abcfde35d2a423a8b94a4c1

	040000 tree 79ef99d4a0bd2d25b3539cd9da9379d23e95d5e3    lib

	git dump 79ef99d4a0bd2d25b3539cd9da9379d23e95d5e3

	100644 blob 038cb6096119ad0dc3fd039002c9d70b14d4f5f9    hello.rb

	git dump 038cb6096119ad0dc3fd039002c9d70b14d4f5f9

	# Default is World

	# Author: shorya1835(shoryasinghal1835@gmail.com)

	name = ARGV.first || "World"

	puts "Hello, #{name}!"

**lab 24**

	git checkout -b greet

	Switched to a new branch 'greet'

	git status

	On branch greet

	nothing to commit, working tree clean

	git commit -m "Added greeter class"

	[greet a66413a] Added greeter class

	 1 file changed, 9 insertions(+)

	create mode 100644 lib/greeter.rb	

	git commit -m "Hello uses Greeter"

	[greet 037195a] Hello uses Greeter

	 1 file changed, 5 insertions(+), 2 deletions(-)



**lab 25**

	git checkout master

	Switched to branch 'master'

	git checkout greet

	Switched to branch 'greet'

**lab 26**

	git checkout master

	Switched to branch 'master'

	git add README.md

	git commit -m "Added README"

	[master f37c8ef] Added README

	 1 file changed, 1 insertion(+)

	 create mode 100644 README.md

**lab 27**

	git hist --all

	\* f37c8ef 2023-04-29 | Added README (HEAD -> master) [shorya1835]

	| \* 037195a 2023-04-29 | Hello uses Greeter (greet) [shorya1835]

	| \* a66413a 2023-04-29 | Added greeter class [shorya1835]

	|/

	\* f501dd9 2023-04-29 | Moved hello.rb to lib [shorya1835]

	\* 865ad92 2023-04-29 | Add an author/email comment [shorya1835]

	\* 372616f 2023-04-29 | Added a comment (tag: v1) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

**lab 28**

	git checkout greet

	Switched to branch 'greet'

	git merge master

	Merge made by the 'ort' strategy.

	 README.md | 1 +

	 1 file changed, 1 insertion(+)

	 create mode 100644 README.md	



	git hist --all

	\*   470019a 2023-04-29 | Merge branch 'master' into greet (HEAD -> greet) [shorya1835]

	|\

	| \* f37c8ef 2023-04-29 | Added README (master) [shorya1835]

	\* | 037195a 2023-04-29 | Hello uses Greeter [shorya1835]

	\* | a66413a 2023-04-29 | Added greeter class [shorya1835]

	|/

	\* f501dd9 2023-04-29 | Moved hello.rb to lib [shorya1835]

	\* 865ad92 2023-04-29 | Add an author/email comment [shorya1835]

	\* 372616f 2023-04-29 | Added a comment (tag: v1) [shorya1835]

	\* 371dc04 2023-04-29 | Added a default value (tag: v1-beta) [shorya1835]

	\* 4628639 2023-04-29 | Using ARGV [shorya1835]

	\* 4e91af0 2023-04-29 | First Commit [shorya1835]

**lab 29**

	git checkout master

	Switched to branch 'master'

	git commit -m "Made interactive"

	[master 66ba8f2] Made interactive

	 1 file changed, 4 insertions(+), 4 deletions(-)

**lab 30**

	git checkout greet

	Switched to branch 'greet'

	git merge master

	Auto-merging lib/hello.rb

	CONFLICT (content): Merge conflict in lib/hello.rb

	Automatic merge failed; fix conflicts and then commit the result.

	cat lib/hello.rb

	<<<<<<< HEAD

	require 'greeter'

	# Default is World

	name = ARGV.first || "World"

	greeter = Greeter.new(name)

	puts greeter.greet

	=======

	puts "What's your name"

	my\_name = gets.strip

	puts "Hello, #{my\_name}!"

	>>>>>>> master

	git add lib/hello.rb

	git commit -m "Merged master fixed conflict"

	[greet 6380da4] Merged master fixed conflict

	git merge master

Already up to date.
