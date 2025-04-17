# 実行環境の構築

## Docker環境の準備

Dockerfileをビルド

```bash
docker compose build \
    --build-arg uid=$(id -u) \
    --build-arg gid=$(id -g)
```

コンテナを起動

```bash
docker compose up -d
```

## 環境の構築

準備した環境に、pythonの実行環境を構築する


実行に必要なライブラリのインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

uv sync --no-dev
```

※開発環境も含めてインストールする場合は、`uv sync`を実行


### pytorchについて
[Using uv with PyTorch](https://docs.astral.sh/uv/guides/integration/pytorch/#using-a-pytorch-index)

以下のエラーが発生する場合

```bash
ImportError: libcusparseLt.so.0: cannot open shared object file: No such file or directory
```

```bash
bash ./setup/install.sh
rm cusparselt-local-repo*
```

### pathの設定

pythonのライブラリ読み込みに必要なパスを`PYTHONPATH`に設定

一時的な環境なら以下のコマンドを実行

```bash
export PYTHONPATH="$PWD:$PYTHONPATH"
```

シェル立ち上げごとに設定したい場合は以下のコマンドを実行

```bash
echo "export PYTHONPATH="$PWD:$PYTHONPATH"" >>  ~/.bashrc

source ~/.bashrc
```

# pythonを実行する場合

pythonを実行する仮想環境をアクティベート

```bash
source .venv/bin/activate
```

もし、commitをする場合も、アクティベートする必要がある。


# 開発コマンド

依存関係の確認

```
uv tree
```

インストール済みのパッケージの確認

```
uv pip freeze
```

# pre-commit

インストール

```bash
uv run pre-commit install
```
