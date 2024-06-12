import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM
from accelerate import Accelerator
import streamlit as st
import os
import PyPDF2 as pdf
import json

# Set Hugging Face Token
hf_token = "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"

# Setting up CUDA if available
accelerator = Accelerator()
device = accelerator.device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Initialize LLama/any other LLM model and tokenizer
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained( model_name,
                                                 cache_dir="/Users/parth/Downloads\AIML Projects/LLM",
                                                 device_map='auto',
                                                 token=hf_token
                                                 , torch_dtype= "auto"
                                                )

tokenizer = AutoTokenizer.from_pretrained(model_name,
                                          token=hf_token
                                          ,cache_dir="/Users/parth/Downloads\AIML Projects/LLM"
                                         )

# Upload and read the resume in PDF format
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


# Get response from LLM - take input, tokenize it, generate output, and decode the tokenized output
def get_llm_repsonse(input):
    inputs = tokenizer(input, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=50, temperature = 0.2, do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

#Prompt Template
input_prompt="""
Act Like a skilled ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
Consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on Jd and the missing important keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingTopKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Resume Scorer for JD ")
st.text("Get the resume matching percentage based on JD")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume in PDF format",type="pdf", help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_llm_repsonse(input_prompt)
        st.subheader(response)