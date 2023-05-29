import torch

TG_TOKEN = ""
MODEL_DATA = 'runwayml/stable-diffusion-v1-5'
LOW_VRAM_MODE = 'true'
USE_AUTH_TOKEN = 'true'
SAFETY_CHECKER = 'true'
HEIGHT = 512
WIDTH = 512
NUM_INFERENCE_STEPS = 55
STRENTH = 0.75
GUIDANCE_SCALE = 7.5

revision = "fp16" if LOW_VRAM_MODE else None
torch_dtype = torch.float16 if LOW_VRAM_MODE else None