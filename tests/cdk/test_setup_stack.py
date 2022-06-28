# flake8: noqa
from pathlib import Path

import aws_cdk as core
import aws_cdk.assertions as assertions

from src.cdk.setup.setup.setup_stack import SetupStack
from src.util.conf import get_hydra_cnf

cfg_path = Path(__file__, "..", "..", "..").resolve().joinpath("src/conf")
cfg = get_hydra_cnf(str(cfg_path), "default")
