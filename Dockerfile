FROM python:3.8-slim-buster

WORKDIR /api

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 80

COPY main.py .

COPY model.py .

RUN ls

CMD ["python", "-m","uvicorn","main:app","--host","0.0.0.0","--port","80"]