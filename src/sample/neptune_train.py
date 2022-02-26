import os
import sys
import pathlib

module_path = pathlib.Path(__file__, "..", "..", "..").resolve()
if module_path not in sys.path:
    sys.path.append(str(module_path))

import neptune.new as neptune

from src.util.load_env import load_env
from src.util.conf import get_hydra_cnf

env = load_env(os.path.join(module_path, ".env"))
cfg = get_hydra_cnf(os.path.join(module_path, "src/conf"), "default")


cfg.exe_id = 100

print(cfg)
description = "サンプル実験用"
tags = ["sample", "model_v2"]
tracker = neptune.init(
    project=cfg.neptune.project_name,
    name=f"train_sample_{cfg.exe_id:05}",
    api_token=env.neptune_api_token,
    mode=cfg.neptune.mode,
    description=description,
    tags = tags,
    source_files=[]
)

params = cfg.ml
ROUND = 1
tracker["params"] = cfg.ml

for e in range(10):
    tracker["train/loss"].log(0.8 ** e)
    tracker["eval/loss"].log(0.90 ** e)

tracker["test/loss"].log(0.3556)

tracker.stop()