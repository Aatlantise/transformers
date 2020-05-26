export HANS_DIR=./hans
export MODEL_PATH=./boolq_save

module load cuda

python -m torch.distributed.launch \
    --nproc_per_node 1 run_glue.py \
    --model_type bert \
    --model_name_or_path $MODEL_PATH \
    --task_name mnli \
    --do_eval \
    --data_dir $HANS_DIR/ \
    --max_seq_length 128 \
    --output_dir $MODEL_PATH \
    --overwrite_output_dir \
