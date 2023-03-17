FROM python:3.10.10-alpine

ADD tinder_bot.py ./tinder_bot.py

RUN pip install requirements.txt

CMD ["python", "./tinder_bot.py"