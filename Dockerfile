FROM python:2.7
MAINTAINER chengtao1381 "chengt1988@qq.com"
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
