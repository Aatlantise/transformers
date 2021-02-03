# aatlantise/transformers

This Huggingface Transformers-forked framework was used to run experiments for Junghyun Min<sup>1</sup>'s master's thesis <i>The roots and effects of heuristics in NLI and QA models</i>, produce in collaboration with Tom McCoy<sup>1</sup> and Tal Linzen<sup>2</sup>. This framework was developed on Nafise Sadat Moosavi<sup>3</sup>'s original implementation of HANS evaluation on Huggingface Transformers.

<sup>1</sup>Department of Cognitive Science, Johns Hopkins University, Baltimore, MD

<sup>2</sup>Department of Linguistics; Department of Data Science, New York University, New York, NY

<sup>3</sup>Department of Computer Science, Technische Universität Darmstadt, Darmstadt, Germany


## Setting up the experiment enviornment

Please run setup.py and `pip -r install requirements.txt` to setup the necessary tools and packages.

### Running the experiments on Docker

We recommened that you take advantage of the PyTorch Docker image provided by Huggingface, located at `docker/transformers-pytorch-gpu`. If you are new to Docker, you're in luck because I was as well 24 hours ago.
We walk through the Docker setup and installation in this section.
First, download the repository. The Docker image needs to be in the root directory of the repository.

`mkdir transformers && cd transformers`

`git clone https://www.github.com/aatlantise/transformers`

`cp docker/transformer-pytorch-gpu/Dockerfile ./`

Then, we build an image. We will name the image `transformers-docker`.

`docker build . -t transofmers-docker`

Now, for our convenivnce, we create a shared drive before creating the container. We name it `roots-effects`.

`mkdir ~/container-data`

`docker run -it --name roots-effects -v ~/container-data:/data transformers-docker`

In the perchance that you need to specify a GPU in a multiGPU machine or server:

`docker run -e NVIDIA_VISIBLE_DEVICES=[GPU-number] -it -P --name [container-name] -v [shared-drive-local-path]:[shared-drive-container-path] [image name]`

You are in the container! Now let's finish the setup.:

`cd transformers`

`pip install -e . && pip install -r experiments/requirements.txt`

You're ready to run your experiments! If you run into a versioning / GPU problem while running jobs, it is likely a PyTorch issue. Visit [pytorch.org](https://www.pytorch.org) and install what is appropriate for your device and ocontainer.


## Training and in-distribution evaluation

We provide two tasks: natural language inference (NLI) and question answering (QA). We use the [MultiNLI](https://github.com/nyu-mll/multiNLI) and the [BoolQ](https://github.com/google-research-datasets/boolean-questions) datasets for training and in-distribution evaluation, respectively. The datasets, cached and tsv, can be found in `/examples/[task-name]/[task-name]_data`.

## Out-of-distribution evaluation

For each task, we provide an out-of-distribution evaluation set that targets three known heuristics in NLI models ([Mccoy et al. 2019b](https://www.aclweb.org/anthology/P19-1334/)). We use [Heuristics Analysis for NLI Systems](https://github.com/tommccoy1/hans) to evaluate NLI models, and its QA adaptation QA-HANS to evaluate QA models. The datasets are located in `/examples/[task-name]/hans/`.

## Results

We include figures for one iteration for each task for your reference, located in `/examples/[task-name]/[task-name]_save/`. `[task-name]_[step-count].txt` include in-distribution accuracy at step `[step-count]`, while `hans_[step-count].txt` and `hansres_[step-count].txt` include HANS evaluation labels and its accuracy broken down into categories and subcases.

## Running your experiments

To run your experiment, simply configure `mnli.sh` or `boolq.sh` with your parameters and run ```bash mnli.sh``` or ```bash boolq.sh```. Your model will be run, and at every checkpoint, the model's evaluation results will be saved.

If your GPU environment uses Slurm, feel free to use the `mnli_finetune.scr` or `boolq_finetune.scr` scripts.


If you have any questions, please feel free to contact us at jmin10@jhu.edu, tom.mccoy@jhu.edu, and linzen@nyu.edu.
