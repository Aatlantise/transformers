export BERT_BASE_DIR=uncased_L-12_H-768_A-12
export BOOLQ_DIR=boolq
export TRAINED_CLASSIFIER=boolq_save

python run_classifier.py \
  --task_name=MNLI \
  --do_predict=true \
  --data_dir=$BOOLQ_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$TRAINED_CLASSIFIER \
  --max_seq_length=350 \
  --output_dir=boolq_save/boolq_output/



