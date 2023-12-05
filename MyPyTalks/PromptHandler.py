
import os
from openai import OpenAI
from openai import AzureOpenAI

client = None

if os.getenv("TYPE").lower() == "openai":
    client = OpenAI(api_key = os.getenv("OPENAI_KEY"))
elif os.getenv("TYPE").lower() == "azure":
    client = AzureOpenAI(
         azure_endpoint = os.getenv("ENDPOINT"),  
         api_key = os.getenv("OPENAI_KEY"),  
         api_version = os.getenv("VERSION"))
else:
    pass

def Generate(prompt):    
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),        
        messages = messages,
        temperature = 0.5, 
    )

    return response.choices[0].message.content