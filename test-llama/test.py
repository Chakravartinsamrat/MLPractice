import os

from langchain.llms import LlamaAPI

meta_llama_api_key = os.getenv("META_LLAMA_API_KEY")

if not meta_llama_api_key:
    raise ValueError("API key not found. Ensure META_LLAMA_API_KEY is set.")

llm = LlamaAPI(temperature=0.5, api_key=meta_llama_api_key)

text = "What is the capital of France?"

result = llm.generate(text)

print(result)