#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
        redis.incr('hits')
        return 'Hello World! I have been seen %s times.' % redis.get('hits')

@app.route('/<float:salary>',methods=['get'])
def salary(salary):
        print(salary)
        return '接收浮点型数字参数: %f.' % salary

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)
