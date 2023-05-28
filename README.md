# 環境構築

```
docker-compose up -d
```

## Docker内

```
poetry install
pip install -e .
```

poetryでライブラリの依存関係を管理しpipで、自前のライブラリをeditable modeでimport可能にする。

## vscode extentions install

```
./.devcontainer/vscode_extentions_install_batch.sh 
```