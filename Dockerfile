FROM python:3.11-bullseye
EXPOSE 80
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
