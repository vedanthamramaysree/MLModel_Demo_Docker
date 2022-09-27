from transformers.pipelines import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

#downloading hugging face into local path. so that no need to download again and again when used in docker container

model.save_pretrained('./distilbart-cnn-12-6')
tokenizer.save_pretrained('./distilbart-cnn-12-6')
