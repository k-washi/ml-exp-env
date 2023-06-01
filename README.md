# 環境構築

```
docker-compose build --no-cache \
    --build-arg uid=$(id -u) \
    --build-arg gid=$(id -g)
docker-compose up -d
```

reference: [Ascender](https://github.com/cvpaperchallenge/Ascender/tree/develop)

## Docker内

コンテナ内のbash起動

`docker compose exec ml-dev bash`


```
poetry install
source .venv/bin/activate
pip install -e .
```

poetryでライブラリの依存関係を管理しpipで、自前のライブラリをeditable modeでimport可能にする。

## vscode extentions install

```
./.devcontainer/vscode_extentions_install_batch.sh 
```