from hydra import compose, initialize_config_dir

from src.params.conf import Config


def get_hydra_cnf(config_dir: str, config_name: str) -> Config:
    """[hydraのconfを取得]

    Args:
        config_dir ([str]): [confのパス]
        config_name ([str]): [confの設定名]
    """
    with initialize_config_dir(config_dir=config_dir):
        cnf = compose(config_name=config_name)
        return cnf


if __name__ == "__main__":
    from pathlib import Path

    cfg_dir = Path(__file__, "..", "..", "..").resolve().joinpath("src/conf")
    print(cfg_dir)
    cfg = get_hydra_cnf(config_dir=str(cfg_dir), config_name="default")
    print(cfg)
