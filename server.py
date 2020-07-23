from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html');


#python applications
@app.route('/apps/chanceoffire')
def chanceoffire():
	return render_template('./apps/chanceoffire/index.html');

if __name__ == "__main__":
	app.run(debug=True)