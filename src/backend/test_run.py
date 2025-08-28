from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = r"C:\Users\yashb\llama_ai_model\llama-2-7b-hf"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto"  # Automatically uses GPU if available
)

prompt = "Explain AI in simple terms."
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_length=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
