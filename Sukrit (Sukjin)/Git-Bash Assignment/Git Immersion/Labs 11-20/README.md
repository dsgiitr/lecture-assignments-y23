### Lab 11
No commands required. The first set of aliases were updated in .gitconfig and the second set in .zshrc.
### Lab 12
main branch is the corresponding name for the master branch in my system.
```console
git hist
git checkout 4df195a
cat hello.rb
git checkout main
cat hello.rb
```
### Lab 13
```console
git v1
git checkout v1^
cat hello.rb
git tag v1-beta
git checkout v1
cat hello.rb
git checkout v1-beta
cat hello.rb
git hist main -a
```
### Lab 14
What I believe has happened is that the checkout has updated hello.rb to be the repository's version of it, i.e. without the bad comment, and since the bad comment was not committed, it now cannot be retrieved.
```console
git checkout main
echo '# This is a bad comment.  We want to revert it.' > hello.rb
echo 'name = ARGV.first || "World"' >> hello.rb
echo 'puts "Hello, #{name}!"' >> hello.rb
cat hello.rb
git status
git checkout hello.rb
git status
cat hello.rb
```
### Lab 15
For some reason, my status says to use 'git restore --staged <file>...' to unstage, but it doesn't work.
```console
echo '# This is an unwanted but staged comment' > hello.rb
echo 'name = ARGV.first || "World"' >> hello.rb
echo 'puts "Hello, #{name}!"' >> hello.rb
git add hello.rb
git status
cat hello.rb
git checkout hello.rb
cat hello.rb
git status
```

### Lab 16
```console
echo '# This is an unwanted but committed comment' > hello.rb
echo 'name = ARGV.first || "World"' >> hello.rb
echo 'puts "Hello, #{name}!"' >> hello.rb
cat hello.rb
git add hello.rb
git commit -m "Oops, we didn't want this commit"
git revert HEAD
git hist
```


### Lab 17
```console
git tag oops
git reset --hard v1
git hist
git hist --all
```

### Lab 18
```console
git tag -d oops
git hist --all
```

### Lab 19
```console
echo '# Default is World' > hello.rb
echo '# Author: Sukrit Jindal' >> hello.rb
echo 'name = ARGV.first || "World"' >> hello.rb
echo 'puts "Hello, #{name}!"' >> hello.rb
cat hello.rb
git add hello.rb
git commit -m "Added an author comment"
echo '# Default is World' > hello.rb
echo '# Author: Sukrit Jindal (sukjingitsit, sukrit_j@mfs.iitr.ac.in)' >> hello.rb
echo 'name = ARGV.first || "World"' >> hello.rb
echo 'puts "Hello, #{name}!"' >> hello.rb
cat hello.rb
git add hello.rb
git commit --amend -m "Added an author comment with e-mail ID and username"
git hist --all
```

### Lab 20
I didn't use the alternate method as it was redundant and slower than the first one.
```console
mkdir lib
git mv hello.rb lib
git status
git commit -m "Moved hello.rb to lib"
```
