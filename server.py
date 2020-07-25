from flask import Flask, render_template, url_for, request
import pickle
import numpy as np
app = Flask(__name__)

model=pickle.load(open('templates/apps/chanceoffire/model.pkl','rb'))

@app.route('/')
def index():
	return render_template('index.html');


#python applications
@app.route('/apps/chanceoffire')
def app1():
	return render_template('./apps/chanceoffire/index.html');

@app.route('/apps/chanceoffire/predict', methods=['POST', 'GET'])
def predict():
	# print(request.form)
	int_features=[int(x) for x in request.form.values()]
	final = [np.array(int_features)]
	# print(int_features)
	print(final)
	prediction = model.predict_proba(final)
	output = '{0: {1}f}'.format(prediction[0][1], 2)
	
	print(output)
	output = float(output)
	if output > 0.8:
		return render_template('./apps/chanceoffire/index.html', predValue = output*100, p='%', pred="There is a High danger of a forest fire", predType = "danger");
	elif(output < 0.8 and output > 0.3):
		return render_template('./apps/chanceoffire/index.html', predValue = output*100,p='%',  pred="There is Medium danger of a forest fire", predType="warning");
	else:
		return render_template('./apps/chanceoffire/index.html', predValue = output*100, p='%', pred="There is a Low danger of a forest fire", predType="success");

@app.route('/apps/stockpredictor')
def app2():
	return render_template('./apps/stockpredictor/index.html');

@app.route('/apps/crimestatspredictor')
def app3():
	return render_template('./apps/crimestatspredictor/index.html');


if __name__ == "__main__":
	app.run(debug=True)





# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
