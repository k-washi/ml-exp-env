# ml-exp-env
機械学習実験環境

# Docker

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