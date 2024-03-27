FROM python:3.10.12

WORKDIR /usr/src/app

COPY . .

COPY .env .env

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir --upgrade python-telegram-bot

CMD ["python3", "bot.py"]
