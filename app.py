#install libraries for fast API
from fastapi import Request,FastAPI
from pydantic import BaseModel
import uvicorn

#install transformers needed for downloading hugging face model
from transformers.pipelines import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

#creating API
app = FastAPI()

# check whether the device is cpu or GPU
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
print ("Device ", torch_device)
torch.set_grad_enabled(False)

# download tokenizers
tokenizer = AutoTokenizer.from_pretrained("./distilbart-cnn-12-6")


#download pre trained distil bart model used for summarization in our case
model = AutoModelForSeq2SeqLM.from_pretrained("./distilbart-cnn-12-6").to(torch_device)
model = model.to(torch_device)

posts = [{ "text" : "High-quality data allows companies and supply chain managers to improve operational efficiencies, monitor inventory management, provide analytics information on budget, timely procurement management, and much more.According to tech research firm Gartner, it is expected that by 2025, 80% of supply chain applications will use AI in practice. “The world’s gotten too complex to try to manage some of these things on spreadsheets,” said Dwight Klappich, a Gartner analyst.This article is about how we performed quality health checks on supply chain data and applied simple programming techniques to reduce manual data-checking processes by 40%.Accurate product data is a critical feature in supply chain systems as it is the foundation of supply chain transactions and aids in faster decision-making. A weak inaccurate data point would disrupt the entire system challenging stakeholders who tend to make unreliable conclusions.We found that to large extent the characteristics of data quality are highly dependent on the input health provided to the system. Also, it is impossible for humans to manually review huge data excel files and perform quality checks.As a team of data scientists and data engineers, we provided a solution to this challenge by conducting data health checks to detect areas of risk, and data discrepancies and identified data improvement opportunities, resulting in a more stable, secure environment and high-quality data in supply chain management."}]
# define a function for summarizing
class SummaryRequest(BaseModel):
    text: str
    min_length: int
    max_length: int

def get_summary(t,tokenizer_summary,model_summary):
  txt = t['text']
  minl = t['min_length'] #75
  maxl = t['max_length'] #150
  inputs = tokenizer_summary([txt], max_length=1024,truncation=True, return_tensors='pt').to(torch_device)
  summary_ids = model_summary.generate(inputs['input_ids'], num_beams=3,num_return_sequences=1,no_repeat_ngram_size=2, min_length = minl,max_length=maxl, early_stopping=True)
  dec = [tokenizer_summary.decode(ids,skip_special_tokens=True, clean_up_tokenization_spaces=True) for ids in summary_ids]
  output = dec[0].strip()
  return {'summary':output}


#testing the API for validation
@app.get('/')
async def home():
    return {"message": "Have a nice day"}


 #API for summary to get the output
@app.post("/summary")
async def getsummary(user_request_in: SummaryRequest):
    payload = {"text":user_request_in.text,"min_length":user_request_in.min_length,"max_length":user_request_in.max_length}
    summ = get_summary(payload,tokenizer,model)
    summ["Device"]= torch_device
    return summ
