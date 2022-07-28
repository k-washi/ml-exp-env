import os
from hydra import compose, initialize_config_dir, initialize
from omegaconf import OmegaConf

def get_hydra_cnf(config_dir: str, config_name: str) -> OmegaConf:
    """[hydraのconfを取得]

    Args:
        config_dir ([str]): [confのパス]
        config_name ([str]): [confの設定名]
    """
    config_dir = os.path.abspath(config_dir)
    with initialize_config_dir(version_base=None, config_dir=config_dir):
        cfg = compose(config_name=config_name)
        #dict_to_config = Config(cfg_dict)  # type: ignore
        #cfg: OmegaConf = OmegaConf.structured(dict_to_config)
        return cfg


if __name__ == "__main__":
    from pathlib import Path

    cfg_dir = Path(__file__, "..", "..", "..").resolve().joinpath("src/conf")
    print(cfg_dir)
    cfg = get_hydra_cnf(config_dir=str(cfg_dir), config_name="config")
    print(cfg)
    print(cfg.ml.seed)