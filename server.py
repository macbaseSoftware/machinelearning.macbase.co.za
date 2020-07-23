from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html');


#python applications
@app.route('/apps/chanceoffire')
def app1():
	return render_template('./apps/chanceoffire/index.html');

@app.route('/apps/stockpredictor')
def app2():
	return render_template('./apps/stockpredictor/index.html');

@app.route('/apps/crimestatspredictor')
def app3():
	return render_template('./apps/crimestatspredictor/index.html');


if __name__ == "__main__":
	app.run(debug=True)