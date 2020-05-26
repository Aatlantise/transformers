#!/bin/bash/

for folder in $(ls -d boolq_copy_*)
do
	cd $folder
	cd boolq_save
        for i in 500 1000 1500 2000 2500 3000 3500
        do
	        python evaluate_heur_output.py checkpoint-$i.txt
                mv formattedFile.txt $i_results.txt
        done
	echo $folder
	#cat eval_results.txt
	#cat formattedFile.txt
	echo
	cd ../..
done

