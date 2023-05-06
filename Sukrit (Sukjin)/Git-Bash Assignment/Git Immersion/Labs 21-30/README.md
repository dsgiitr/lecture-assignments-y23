### Lab 21
```console
echo '#!/usr/bin/ruby -wKU' > Rakefile
echo 'task :default => :run' >> Rakefile
echo 'task :run do' >> Rakefile
echo '  require '"'"'./lib/hello'"'" >> Rakefile
echo 'end' >> Rakefile
cat Rakefile
git add Rakefile
git commit -m "Added a Rakefile."
rake
```
### Lab 22
```console
ls -C .git
ls -C .git/objects
ls -C .git/objects/06
cat .git/config
ls .git/refs
ls .git/refs/heads
ls .git/refs/tags
cat .git/HEAD
```
### Lab 23
```console
git hist --max-count=1
git cat-file -t ae39948
git cat-file -p ae39948
git cat-file -p 0664a9b7
git cat-file -p 702b4eb6
git cat-file -p d42abf557
```
### Lab 24
This time I directly edited the files, instead of using echo
```console
touch ./lib/greeter.rb
cat ./lib/greeter.rb
git add lib/greeter.rb
git commit -m "Added the greeter class"
cat ./lib/hello.rb
git add lib/hello.rb
git commit -m "hello updated to use greeter"
cat Rakefile
git add Rakefile
git commit -m "Updated Rakefile"
```
### Lab 25
```console
git hist --all
git checkout main
cat lib/hello.rb
git checkout greet
cat lib/hello.rb
```
# Lab 26
```console
git checkout main
touch README
echo 'This is the Hello World example from the git tutorial.' > README
cat README
git add README
git commit -m "Added README"
```
### Lab 27
```console
git hist --all
```
### Lab 28
```console
git checkout greet
git merge main
git hist --all
```
### Lab 29
```console
git checkout main
cat hello.rb
git add hello.rb
git commit -m "Made interactive"
git hist --all
```
### Lab 30
```console
git checkout greet
git merge main
cat lib/hello.rb
cat lib/hello.rb
git add lib/hello.rb
git commit -m "Merged master fixed conflict."
```
