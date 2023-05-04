#!/bin/bash


echo "enter your codeforces handle"
read handle

echo "number of pages in your submission directory "
read npage

echo "string to be followed"
read string

echo "number of characters to be generated"
read n

python charRNN.py $handle $npage $ string $n

