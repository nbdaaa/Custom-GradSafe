#No need to use this file because of using the model from the huggingface hub

from datasets import load_dataset
from huggingface_hub import hf_hub_download
import os

os.makedirs("./model", exist_ok=True)

# Download Llama-2-7b model
# Note: You'll need to be logged in to Hugging Face and have access to the model
print("\nDownloading Llama-2-7b model...")
try:
    # This will prompt for login if you're not already logged in
    from huggingface_hub import login
    login()
    
    # Download the model files
    model_path = hf_hub_download(repo_id="meta-llama/Llama-2-7b-chat-hf", 
                               filename="pytorch_model.bin",
                               local_dir="./model")
    print(f"Model downloaded to {model_path}")
except Exception as e:
    print(f"Error downloading model: {e}")
    print("Note: You need to have access to meta-llama/Llama-2-7b-chat-hf on Hugging Face.")
    print("Visit https://huggingface.co/meta-llama/Llama-2-7b-chat-hf and request access if needed.")

print("Download process completed!")