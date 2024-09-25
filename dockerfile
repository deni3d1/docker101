FROM python:3.9

WORKDIR /app

RUN pip install -U Flask

COPY . .

ENV FLASK_APP=testdocker.py

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]