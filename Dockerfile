FROM python:3.9-buster

EXPOSE 80
WORKDIR /src
COPY . .

RUN pip install -r requirements.txt

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
