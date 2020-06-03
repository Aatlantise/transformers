#!/bin/bash/

for folder in $(ls -d boolq_copy_*)
do
	cd $folder
	cd boolq_save
        for i in 500 1000 1500 2000 2500 3000 3500
        do
                echo $folder
                echo $i
                cat results_$i.txt
                echo
        done
	echo
	cd ../..
done

