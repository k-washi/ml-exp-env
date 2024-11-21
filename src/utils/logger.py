import logging
import logging.handlers  # handlersを使用するため呼び出し必須
from pathlib import Path

_log_initialized: dict[str, logging.Logger] = {}


def get_logger(
    *,
    filename: str | None = None,
    name: str = "main",
    file_max_bytes: int = 100000,
    file_backup_count: int = 1,
    debug: bool = False,
    add_stream_handler: bool = True,
) -> logging.Logger:
    """loggerを取得.

    関数を読み込む前に実行
    Args:
        debug (bool): デバッグモードにするか?, Falseの場合、INFO
        filename (str, optional): ログのファイル出力先
        name (str, optional): ログの名前
        add_stream_handler (bool, optional): ストリーム出力
    Returns:
        logging.Logger: Logger instance.
    """
    global _log_initialized  # noqa: PLW0602
    logger = _log_initialized.get(name)
    if logger is not None:
        return logger

    log_format = "%(levelname)-8s: %(asctime)s | %(filename)-12s - %(funcName)-12s : %(lineno)-4s -- %(message)s"
    logger = logging.getLogger(name)

    # ログレベルの設定
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if add_stream_handler:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(stream_handler)

    # ログファイルに関する設定
    if filename is not None:
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.handlers.RotatingFileHandler(
            filename,
            maxBytes=file_max_bytes,
            backupCount=file_backup_count,
            mode="a+",  # 開くか、新しいテキストファイルを作って最後から更新
            encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S"))
        logger.addHandler(file_handler)

    _log_initialized[name] = logger
    return logger


if __name__ == "__main__":
    logger = get_logger(debug=False)
    logger.info("info message")
    logger.debug("debug message")
