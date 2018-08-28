from flask import Flask
import os

app = Flask(__name__)

@app.route('/hello/<username>', method=['GET'])
def hello(username):
	return username

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
