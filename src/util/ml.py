import random
import numpy as np
import torch

def set_seed(seed=3407):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    
    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.deterministic = True

