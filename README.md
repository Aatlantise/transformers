# aatlantise/transformers

This Huggingface Transformers-forked framework was used to run experiments for Junghyun Min<sup>1</sup>'s master's thesis <i>The roots and effects of heuristics in NLI and QA models</i>, produce in collaboration with Tom McCoy<sup>1</sup> and Tal Linzen<sup>2</sup>. This framework was developed on Nafise Sadat Moosavi<sup>3</sup>'s original implementation of HANS evaluation on Huggingface Transformers.

<sup>1</sup>Department of Cognitive Science, Johns Hopkins University, Baltimore, MD
<sup>2</sup>Department of Linguistics; Department of Data Science, New York University, New York, NY
<sup>3</sup>Department of Computer Science, Technische Universität Darmstadt, Darmstadt, Germany

## Training and in-distribution evaluation

We provide two tasks: natural language inference (NLI) and question answering (QA). We use the [MultiNLI](https://github.com/nyu-mll/multiNLI) and the [BoolQ](https://github.com/google-research-datasets/boolean-questions) datasets for training and in-distribution evaluation, respectively. The datasets, cached and tsv, can be found in `/examples/[task-name]/[task-name]_data`.

## Out-of-distribution evaluation

For each task, we provide an out-of-distribution evaluation set that targets three known heuristics in NLI models ([Mccoy et al. 2019b](https://www.aclweb.org/anthology/P19-1334/)). We use [Heuristics Analysis for NLI Systems](https://github.com/tommccoy1/hans) to evaluate NLI models, and its QA adaptation to evaluate QA models. The datasets are located in `/examples/[task-name]/hans/`.

## Results

We include figures for one iteration for each task for your reference, located in `/examples/[task-name]/[task-name]_save/`. `[task-name]_[step-count].txt` include in-distribution accuracy at step `[step-count]`, while `hans_[step-count].txt` and `hansres_[step-count].txt` include HANS evaluation labels and its accuracy broken down into categories and subcases.

## Running your experiments

To run your experiment, simply configure `mnli.sh` or `boolq.sh` and `mnli_finetune.scr` or `boolq_finetune.scr` with your parameters and run ```bash mnli.sh``` or ```bash boolq.sh```. Your model will be run, and at every checkpoint, the model's evaluation results will be saved.
