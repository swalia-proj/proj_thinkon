FROM ghcr.io/swalia-proj/secure-base:latest

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install flask

EXPOSE 5000

CMD ["python3", "app.py"]
