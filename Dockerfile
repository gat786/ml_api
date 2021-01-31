FROM python:3.8-slim-buster

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 80

COPY ./app /app

RUN ls

CMD ["python", "-m","uvicorn","app.main:app","--host","0.0.0.0","--port","80"]