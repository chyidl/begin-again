FROM python:3.8-alpine

ADD . /code
WORKDIR /code
RUN pip install redis flask
CMD ["python", "app.py"]
