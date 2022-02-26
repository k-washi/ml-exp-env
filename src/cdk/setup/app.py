#!/usr/bin/env python3
import os
import sys
import pathlib

module_path = pathlib.Path(__file__, "..", "..", "..", "..").resolve()
if module_path not in sys.path:
    sys.path.append(str(module_path))

import aws_cdk as cdk
from setup.setup_stack import SetupStack

from src.util.load_env import load_env
from src.util.conf import get_hydra_cnf


env = load_env(os.path.join(module_path, ".env"))
cfg = get_hydra_cnf(os.path.join(module_path, "src/conf"), "default")

cdk.Environment()

app = cdk.App()
SetupStack(app, cfg.name, cfg)

app.synth()
