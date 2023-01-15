FROM python:3.10.6

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN python -m pip install flask-sqlalchemy

EXPOSE 5000

CMD python ./main.py