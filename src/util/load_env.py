import dataclasses
import os
from dotenv import load_dotenv
from dataclasses import dataclass
load_dotenv(verbose=True)

@dataclass
class Env:
    neptune_api_token: str = None
    aws_access_key_id: str = None
    aws_region: str = None

def load_env(env_path):
    load_dotenv(dotenv_path=env_path)

    neptune_api_token = os.environ.get("NEPTUNE_AI_API_TOKEN")
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", "default")
    aws_region = os.environ.get("AWS_REGION")

    return Env(
        neptune_api_token=neptune_api_token,
        aws_access_key_id=aws_access_key_id,
        aws_region=aws_region
    )

if __name__ == "__main__":
    env_path = "./.env"
    print(load_env(env_path=env_path))

    