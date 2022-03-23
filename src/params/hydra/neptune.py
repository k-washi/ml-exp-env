from dataclasses import dataclass

from hydra.core.config_store import ConfigStore


@dataclass
class NeptuneDefaultConfig:
    project_name: str = "test-project-v1"
    mode: str = "async"
    exe_id: int = -1


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        group="neptune",
        name="base_neptune",
        node=NeptuneDefaultConfig,
    )
