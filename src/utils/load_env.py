import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(verbose=True)


class Env(BaseModel):
    neptune_api_token: str
    wandb_api_token: str
    aws_access_key_id: str
    aws_region: str


def load_env(env_path: str) -> Env:
    """
    env_pathの.envファイルを優先して、環境変数を呼び出す

    Args:
        env_path (str): .envファイルのパス

    Returns:
        Env: 環境変数のデータ
    """
    load_dotenv(dotenv_path=env_path)

    neptune_api_token = os.environ.get("NEPTUNE_API_TOKEN", "")
    wandb_api_token = os.environ.get("WANDB_API_TOKEN", "")
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", "default")
    aws_region = os.environ.get("AWS_REGION", "ap-northeast-1")

    return Env(
        neptune_api_token=neptune_api_token,
        wandb_api_token=wandb_api_token,
        aws_access_key_id=aws_access_key_id,
        aws_region=aws_region,
    )


if __name__ == "__main__":
    env_path = "./.env"
    print(load_env(env_path=env_path))
