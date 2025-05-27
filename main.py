import torch
import os

# Use all available CPU cores for best speed
torch.set_num_threads(os.cpu_count())

# ...rest of your main code...