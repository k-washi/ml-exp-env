import random

import numpy as np
import torch


def set_seed(seed: int = 3407):
    """
    pytorch, numpy, randomのseedを固定する。
    Args:
        seed (int, optional): seedの値. Defaults to 3407.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    torch.use_deterministic_algorithms = True
    torch.backends.cudnn.deterministic = True  # True:再現性は上がるが、処理パフォーマンスが低下
