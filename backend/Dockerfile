FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Flask[async]

COPY . .

EXPOSE 5000

CMD ["python", "telebot_app.py"]