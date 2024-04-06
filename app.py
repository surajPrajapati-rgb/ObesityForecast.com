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
            'gender':int( request.form['gender']),
            'age': float(request.form['age']),
            'height': float(request.form['height']),
            'weight': float(request.form['weight']),
            'family_history': int(request.form['family_history']),
            'favc': int(request.form['favc']),
            'fcvc': int(request.form['fcvc']),
            'ncp': int(request.form['ncp']),
            'caec': int(request.form['caec']),
            'smoke': int(request.form['smoke']),
            'ch2o': int(request.form['ch2o']),
            'scc': int(request.form['scc']),
            'faf': int(request.form['faf']),
            'tue': int(request.form['tue']),
            'calc': int(request.form['calc']),
            'mtrans': int(request.form['mtrans']),

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
