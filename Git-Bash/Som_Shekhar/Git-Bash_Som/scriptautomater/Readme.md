# charRNN.py
char.RNN is the python script which predicts next few characters of code given an initial set of characters. A web scrapper is used to scrap data from codeforces, and a Recurrent Neural Network model is traineed upon the scrapped data.

## Arguments
I have tried to create a bash script to run char.RNN. The bash script "script.sh" has 4 arguments which are 

```
handle=sys.argv[1]
npage=sys.argv[2]
my_string=sys.argv[3]
n=sys.argv[4]
```

* where handle is the codeforces handle of the user
* npage are the number of pages in submission directory
* string is the set of character, after which the model predicts next characters 
* n is the number of characters to be generated


## Steps to Use 

Type this  in terminal

```
sh script.sh  
```
then type arguments in the prompts.

or you can write this way directly 
```
python charRNN.py $handle $npage $string $n 
```
 the output will be generated in output.txt file.


