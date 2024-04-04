from flask import Flask, request, jsonify,render_template
import joblib

app = Flask(__name__)

model = joblib.load('Model/RandomForestClassifier.pkl')


@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

@app.route('/portal',methods=['GET','POST'])
def portal():
    data={}
    if request.method=="POST":
        data = {
            'gender': request.form['gender'],
            'age': int(request.form['age']),
            'height': int(request.form['height']),
            'weight': int(request.form['weight']),
            'family_history': request.form['family_history'],
            'favc': request.form['favc'],
            'fcvc': int(request.form['fcvc']),
            'ncp': int(request.form['ncp']),
            'caec': request.form['caec'],
            'smoke': request.form['smoke'],
            'ch2o': int(request.form['ch2o']),
            'scc': request.form['scc'],
            'faf': int(request.form['faf']),
            'tue': int(request.form['tue']),
            'calc': request.form['calc'],
            'mtrans': request.form['mtrans'],
            'nObeyesdad': request.form['nObeyesdad']
        }
    return render_template('portal.html', data=data)


# @app.route('/predict', methods=['GET','POST'])
# def predict():

#     data = request.json
    
#     features = [
#         float(data['age']), 
#         float(data['height']), 
#         float(data['weight']),
#         # Convert other features similarly
#     ]

    
#     features = [features] 
    
#     prediction = model.predict(features)
#     hello=''

#     return jsonify({'obesityLevel': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
