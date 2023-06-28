### Lab 1
My MacOS has a pre-installed Ruby interface.
```console
git config --global user.name "sukjingitsit"
git config --global user.email "sukrit_j@mfs.iitr.ac.in"
git config --global core.autocrlf input
git config --global core.safecrlf true
```
### Lab 2
No commands required
### Lab 3
I created the 'hello' directory within the 'work' directory of the previously downloaded tutorial file.
```console
cd ./Downloads/git_tutorial/work
mkdir hello
cd ./hello
echo 'puts "Hello, World"' > hello.rb
cat hello.rb
git init
git add hello.rb
git commit -m "First Commit"
```
### Lab 4
Initially, it showed an untracked file, namely .DS_Store which is added by MacOS. Thus, I searched on StackExchange found a way to ignore said file.
```console
git status
echo .DS_Store >> .gitignore
git add .gitignore
git commit -m '.DS_Store banished!'
git status
```
### Lab 5
```console
echo 'puts "Hello, #{ARGV.first}!"' > hello.rb
cat hello.rb
git status
```
### Lab 6
```console
git add hello.rb
git status
```
### Lab 7
No code required, it just explains how to separate commits through sequential staging and committing.
### Lab 8
I had to use the :wq command for the vi editor in my Terminal
```console
git commit
git status
```
### Lab 9
```console
echo 'name = ARGV.first || "World"' > hello.rb
echo 'puts "Hello, #{name}!"' >> hello.rb
cat hello.rb
git add hello.rb
echo '# Default is "World"' > hello.rb
echo 'name = ARGV.first || "World"' >> hello.rb
echo 'puts "Hello, #{name}!"' >> hello.rb
cat hello.rb
git status
git commit -m "Added a default value"
git status
git add .
git status
git commit -m "Added a comment"
```
### Lab 10
I have one extra commit due to the .DS_Store file
```console
git log
git log --pretty=oneline
git log --pretty=oneline --max-count=2
git log --pretty=oneline --since='5 minutes ago'
git log --pretty=oneline --until='5 minutes ago'
git log --pretty=oneline --author=<your name>
git log --pretty=oneline --all
git log --all --pretty=format:'%h %cd %s (%an)' --since='7 days ago'
git log --all --pretty=format:'%h %cd %s (%an)' --since='7 days ago' --author=sukjingitsit
git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
```
