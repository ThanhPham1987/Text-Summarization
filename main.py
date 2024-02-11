from fastapi import FastAPI
from typing import Optional
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Initialize the summarizer

checkpoint = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer.save_pretrained("model/")
model.save_pretrained("model/")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

app = FastAPI(
    root_path="/txtapp-service"
)


@app.get("/Text_Summarization")
async def text_summarization(Text: Optional[str] = None):
    results = {"Mlops": [{"Author": "DrissDo"}]}
    if Text:
        # Use the summarizer to summarize the text
        summary = summarizer(Text, max_length=130, min_length=30, do_sample=False)
        results.update({"Text Summarization ": summary})
    return results