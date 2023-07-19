FROM python:latest

# Копирование исходного кода автотестов в образ
COPY . .
RUN pip3 install -r requirements.txt


# Запуск автотестов
CMD pytest /tests