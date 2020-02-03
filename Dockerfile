FROM python:3.7-alpine

WORKDIR /rtsp

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD python streaming.py
