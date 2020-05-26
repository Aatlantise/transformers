#!/bin/bash/

for folder in $(ls -d boolq_copy_*)
do
	cd $folder
	export MASTER_PORT=$(shuf -i8000-9999 -n1)
	sbatch boolq_eval.scr
	cd ..
done

