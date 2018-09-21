from flask import Flask
app = Flask(__name__)
@app.route('/flask')
def hello_flask(a,b):
	return a+b
@app.route('/python')
def hello_data():
	return 'Hello python'
if __name__ == '__main__':
	app.run()
