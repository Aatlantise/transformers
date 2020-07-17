#!/bin/bash/

cd boolq_save
for i in 1 500 1000 1500 2000 2500 3000 3500 3537
do
        echo $folder
        echo $i
	python evaluate_heur_output.py hans_$i.txt
        mv formattedFile.txt hansres_$i.txt
done
cd ../..
done

