FROM python:3.10.12

WORKDIR /usr/src/app

COPY . .

COPY .env .env

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "bot.py"]
