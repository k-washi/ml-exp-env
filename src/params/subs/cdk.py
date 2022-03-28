from dataclasses import dataclass

from hydra.core.config_store import ConfigStore


@dataclass
class CdkDefaultConfig:
    name: str = "ml-ops-sample"
    aws_s3_dataset_bucket: str = "ml-ops-sample-bucket"


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        group="cdk",
        name="base_cdk",
        node=CdkDefaultConfig,
    )
