#!/bin/bash/

for folder in $(ls -d boolq_copy_*)
do
	cd $folder
	cd boolq_save
        mv 1_hans.txt hans_1.txt
        mv 500_hans.txt hans_500.txt
        mv 1000_hans.txt hans_1000.txt
        mv 1500_hans.txt hans_1500.txt
        mv 2000_hans.txt hans_2000.txt
        mv 2500_hans.txt hans_2500.txt
        mv 3000_hans.txt hans_3000.txt
        mv 3500_hans.txt hans_3500.txt
        mv 3537_hans.txt hans_3537.txt
	cd ../..
done

