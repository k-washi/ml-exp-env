from hydra import compose, initialize_config_dir


def get_hydra_cnf(config_dir, config_name):
    """[hydraのconfを取得]

    Args:
        config_dir ([str]): [confのパス]
        config_name ([str]): [confの設定名]
    """
    with initialize_config_dir(config_dir=config_dir):
        cnf = compose(config_name=config_name)
        return cnf
