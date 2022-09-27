# Model_Demo_Assignment2
lemay.ai


This repository includes code containerize and deploy the Huggingface model-BART, used for summarization of text. 

## BART:

<html>
<body>
<p> BART, which pre-trains a model combining Bidirectional and Auto-Regressive Transformers. BART is a denoising autoencoder built with a sequence-to-sequence model that applies to a very wide range of end tasks. Since predictions are not made auto-regressively in BERT, the effectiveness of BERT for generation tasks is less compared to BART. BART achieves new state-of-the-art results on a number of text generation tasks. Unsurprisingly, the BART model output is more fluent and grammatical in English. However, model output is also highly abstractive, with few phrases copied from the input. Hence, in this repository, we experimented with BART for the summarization of large texts from technical writings into a few lines.
</body>
</html>

## Why Summarizing is necessary for data science?

The term Data Summarization refers to presenting the summary of generated data in an easily comprehensible and informative manner. Data summarization is the first step in statistics, it is aimed at extracting useful information and general trends from the raw data.

In this repository, I have used an article written by me in medium to summarize and get a gist of it. The purpose of using this hugging face model for summarizing is to make my non-data science teams and functional experts understand what's in the technical writing, before reading it in prior. Practically, text summarization saves a lot of time and effort.


**requirements.txt**: libraries needed to create API along with versions

**run.txt**: Steps needed to run the file

**Huggingface_model_notebook.ipynb**: In this experiment, the BART model is set to summarize text to a maximum of 150 words. It is a python notebook demonstrating the model inputs and results for reference.

**Download_Huggingface_Local.py**: Pre-downloading the BART model into the local folder to load within the docker code avoiding downloading the model each time it is called in the Docker. This would save time essentially and can be re-used whenever needed.

**app.py**: This creates the API for the model.

**Docker_Container**: Docker file which creates the docker container.
