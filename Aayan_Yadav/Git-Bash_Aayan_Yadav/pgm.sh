#!usr/bin/env bash
n=1
sh script.sh >out.txt 2>err.txt
while [ $? -eq 0 ] ;
do
	n=$(($n+1))
	sh script.sh >>out.txt 2>err.txt
done
echo "It took $n runs to fail"
echo "Output : "
cat out.txt
echo "Error : "
cat err.txt
	 
