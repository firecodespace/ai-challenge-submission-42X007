from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import torch
from pathlib import Path

app = FastAPI()

def path_to_posix_str(path: Path) -> str:
    return path.resolve().as_posix()

MODEL_PATH = Path(r"C:\Users\yashb\llama_ai_model\llama-2-7b-chat-hf")
ADAPTERS_DIR = Path(r"C:\Users\yashb\llama_ai_model\.llama\adapters")

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

print(f"Loading base model from: {path_to_posix_str(MODEL_PATH)}")
print(f"Base model path exists: {MODEL_PATH.exists()}")
print(f"Adapters directory exists: {ADAPTERS_DIR.exists()}")

tokenizer = AutoTokenizer.from_pretrained(
    path_to_posix_str(MODEL_PATH),
    local_files_only=True
)
model = AutoModelForCausalLM.from_pretrained(
    path_to_posix_str(MODEL_PATH),
    quantization_config=bnb_config,
    device_map="auto",
    local_files_only=True
)
model.eval()

active_adapter = None

class MessageIn(BaseModel):
    message: str
    adapter: str = None

class MessageOut(BaseModel):
    response: str

def load_adapter(adapter_name: str):
    global model, active_adapter
    adapter_path = ADAPTERS_DIR / adapter_name
    if not adapter_path.exists():
        raise RuntimeError(f"Adapter '{adapter_name}' not found at {adapter_path}")
    print(f"Loading adapter: {adapter_name}")
    loaded_model = PeftModel.from_pretrained(model, path_to_posix_str(adapter_path))
    loaded_model.eval()
    active_adapter = adapter_name
    return loaded_model

@app.post("/message", response_model=MessageOut)
async def generate_message(req: MessageIn):
    global model, active_adapter

    if req.adapter:
        if req.adapter != active_adapter:
            try:
                model = load_adapter(req.adapter)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
    else:
        if active_adapter:
            print(f"Unloading adapter {active_adapter}, reverting to base model")
            model = AutoModelForCausalLM.from_pretrained(
                path_to_posix_str(MODEL_PATH),
                quantization_config=bnb_config,
                device_map="auto",
                local_files_only=True
            )
            model.eval()
            active_adapter = None

    input_ids = tokenizer(req.message, return_tensors="pt").input_ids.to(model.device)
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=128)
    response_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return {"response": response_text}
