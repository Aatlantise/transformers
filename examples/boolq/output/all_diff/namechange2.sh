#!/bin/bash/

for folder in $(ls -d boolq_copy_*)
do
	cd $folder
	cd boolq_save
        mv 1_boolq.txt boolq_1.txt
        mv 500_boolq.txt boolq_500.txt
        mv 1000_boolq.txt boolq_1000.txt
        mv 1500_boolq.txt boolq_1500.txt
        mv 2000_boolq.txt boolq_2000.txt
        mv 2500_boolq.txt boolq_2500.txt
        mv 3000_boolq.txt boolq_3000.txt
        mv 3500_boolq.txt boolq_3500.txt
        mv 3537_boolq.txt boolq_3537.txt
	cd ../..
done

