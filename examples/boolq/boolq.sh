export DATA_DIR=./boolq_data
export OUTPUT_DIR=./boolq_save
export SEED=42

#module load cuda
#module load python

python3 -m torch.distributed.launch \
    --nproc_per_node 1 run_glue.py \
    --model_type bert \
    --model_name_or_path bert-base-uncased \
    --task_name mnli \
    --do_train \
    --data_dir $DATA_DIR/ \
    --max_seq_length 128 \
    --per_gpu_train_batch_size 8 \
    --learning_rate 2e-5 \
    --num_train_epochs 3.0 \
    --output_dir $OUTPUT_DIR \
    --seed $SEED \
    --overwrite_output_dir
