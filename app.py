#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/<name>', method=['GET'])
def hello(name):
	redis.incr('hits')
	return 'hello %s, I have been seen %s times.' % (name, redis.get('hits'))

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
