from dataclasses import dataclass

from hydra.core.config_store import ConfigStore


@dataclass
class MLDefaultConfig:
    seed: int = 3407
    batch_size: int = 32
    learning_rate: float = 0.001
    optimizer: str = "AdamW"


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        group="ml",
        name="base_ml",
        node=MLDefaultConfig,
    )
