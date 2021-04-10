# ml-exp-env
機械学習実験環境

# vs-codeでリモートコンテナに入る

ExtensionのREMOTE-SSHを使用すればOK!!
一旦、SSH先に入って、そこからコンテナにアクセスする。

# tensorboard

```
tensorboard --logdir <logpath> --port 18085 --host=0.0.0.0
```

# バックグラウンド処理

```
nohup <cmd>
```