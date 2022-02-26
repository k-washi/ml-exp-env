import os
import sys
import pathlib

module_path = pathlib.Path(__file__, "..", "..", "..", "..", "..", "..").resolve()
if module_path not in sys.path:
    sys.path.append(str(module_path))

import aws_cdk as core
import aws_cdk.assertions as assertions
from setup.setup_stack import SetupStack

from src.util.conf import get_hydra_cnf
cfg = get_hydra_cnf(os.path.join(module_path, "src/conf"), "default")
