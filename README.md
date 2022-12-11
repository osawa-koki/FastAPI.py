# simple-FastAPI.py

FastAPIの動作をテストするためのプログラム。  

## 実行方法

```shell
# Dockerファイルをビルド
docker build -t fastapi-sample .

# Dockerコンテナを実行
docker run -it --name fastapi-sample -p 8080:8000 fastapi-sample
```

<http://localhost:8080>へアクセス。  

## 環境構築手順

```shell
pip install -r requirements.txt
```
