FROM python:3.9.10-alpine3.14

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=app/main

CMD ["python", "-m", "flask", "--app", "app/main", "run", "--debug", "--host=0.0.0.0"]