from flask import Flask
app = Flas(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

if__name__ == '__main__':
	app.run(debug=True)