from dataclasses import dataclass
from pathlib import Path

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf

from src.params.subs import cdk as _cdk
from src.params.subs import ml as _ml
from src.params.subs import neptune as _neptune


@dataclass
class Config:
    cdk: _cdk.CdkDefaultConfig = _cdk.CdkDefaultConfig()
    ml: _ml.MLDefaultConfig = _ml.MLDefaultConfig()
    neptune: _neptune.NeptuneDefaultConfig = _neptune.NeptuneDefaultConfig()


cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)

_cdk.register_configs()
_ml.register_configs()
_neptune.register_configs()

cfg_path = Path(__file__, "..", "..", "..").resolve().joinpath("src/conf")


@hydra.main(config_path=str(cfg_path), config_name="default")
def my_app(cfg: Config) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
