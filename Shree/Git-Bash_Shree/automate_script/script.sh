#!/bin/sh

echo "enter polynomial degree:"
read degree

echo "enter number of training points:"
read n

python regression.py $n $degree