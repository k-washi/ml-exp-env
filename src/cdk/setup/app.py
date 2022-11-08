#!/usr/bin/env python3
import os
import pathlib

import aws_cdk as cdk

from setup.setup_stack import SetupStack
from src.util.conf import get_hydra_cnf
from src.util.load_env import load_env

module_path = pathlib.Path(__file__, "..", "..", "..", "..").resolve()
env = load_env(os.path.join(module_path, ".env"))
cfg = get_hydra_cnf(os.path.join(module_path, "src/conf"), "config")

cdk.Environment()

app = cdk.App()
SetupStack(app, cfg.cdk.name, cfg.cdk)

app.synth()
