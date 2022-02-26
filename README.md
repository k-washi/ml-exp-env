# ml-exp-env
機械学習実験環境

# 環境変数など

.envに記載する

```
# naptune.ai実験管理用
NEPTUNE_AI_API_TOKEN=xxx
```

# AWS周りの環境設定

- awsのクレデンシャル設定

```
aws configure
```

- aws cdkを使用する (データをs3で管理する場合など)

```
cd src/cdk/setup
cdk synth
cdk bootstrap
```

- 必要だった権限について

```
IAMFullAccess
AmazonEC2ContainerRegistryFullAccess
AmazonS3FullAccess
AmazonSSMFullAccess
AWSCloudFormationFullAccess
AWSLambda_FullAccess
```

適宜、修正、追加を行ってください。

- 新しいスタックを作成する場合

```
cdk init setup --language=python
```

# test

```
python -m pytest
```

# Docker

 CUDAによりpytorchのインストール方法が異なるので、適宜[公式](https://pytorch.org/)を参照し、インストールしてください。

```
docker-compose -f docker-compose-cpu.yml up -d
```

でコンテナを作成し、VS Codeの`ms-vscode-remote.remote-containers`から開発環境に入る

# gpu周り

もし、`docker-compose-gpu.yml`における以下の設定で上手くいかない場合

```
    deploy:
      resources:
        reservations:
          devices:
          - driver: nvidia
            capabilities: [gpu]
```

以下に変更する。

```
runtime: nvidia
```

# ローカル環境で仮想環境の作成

```
python -m venv .venv
```

```
source .venv/bin/activate
```

```
deactivate
```

versoinを変更したい場合、最初にpythonのバージョンを変更する。
```
pyenv local 3.8.0
```

# vscode extensionの設定

1. view/command palletを開き、shellからcodeをインストール
2. 新しいshellを開く
3. 以下のコマンド実行 (権限は与えておく)

```
./.devcontainer/vscode_extentions_install_batch.sh
```