from datasets import load_dataset
from huggingface_hub import hf_hub_download
import os

# Create necessary directories
os.makedirs("./data", exist_ok=True)

# Download ToxicChat dataset
print("\nDownloading ToxicChat dataset...")
toxic_chat = load_dataset("lmsys/toxic-chat", "toxicchat1123")
toxic_chat.save_to_disk("./data/toxic-chat")

# Download XSTest dataset
print("\nDownloading XSTest dataset...")
xstest = load_dataset("natolambert/xstest-v2-copy")
xstest.save_to_disk("./data/xstest")

print("Download process completed!")