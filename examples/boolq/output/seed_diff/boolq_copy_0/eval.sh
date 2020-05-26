export DATA_DIR=../../../boolq_data
export OUTPUT_DIR=./boolq_save

module load cuda

python -m torch.distributed.launch \
    --nproc_per_node 1 run_glue.py \
    --model_type bert \
    --model_name_or_path bert-base-uncased \
    --task_name mnli \
    --do_eval \
    --eval_all_checkopints \
    --data_dir $DATA_DIR/ \
    --max_seq_length 128 \
    --output_dir $OUTPUT_DIR \
    --overwrite_output_dir \
