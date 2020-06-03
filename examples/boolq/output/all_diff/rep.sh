#!/bin/bash

#repeat runnings
for folder in $(ls -d boolq_copy_*)
do
	cd $folder
	export MASTER_PORT=$(shuf -i8000-9999 -n1)
        echo $MASTER_PORT
        sbatch boolq_finetune.scr
	cd ..
done
