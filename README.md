# simple-FastAPI.py

FastAPIの動作をテストするためのプログラム。  

## 実行方法

```shell
# Dockerファイルをビルド
docker build -t fastapi-sample .

# Dockerコンテナを実行
docker run -it --name fastapi-sample -p 80:80 fastapi-sample
```

一行で書くなら、、、  

```shell
docker build -t fastapi-sample . && docker run -it --name fastapi-sample -p 80:80 fastapi-sample
```

<http://localhost:80>へアクセス。  

RESTfulAPIのテストは[postman](https://www.postman.com/)で♪  

## 環境構築手順

```shell
pip install -r requirements.txt
```

## 使用した画像ファイル

- [タコ](https://frame-illust.com/?p=13667)
- [スズメ](https://frame-illust.com/?p=13680)
- [キツネ](https://frame-illust.com/?p=9584)

## 参考文献

- [公式ドキュメント](https://fastapi.tiangolo.com/ja/)
