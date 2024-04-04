from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('Model/RandomForestClassifier.pkl')

@app.route('/predict', methods=['GET','POST'])

def predict():

    data = request.json

    # features = [
    #     float(data['age']), 
    #     float(data['height']), 
    #     float(data['weight']),
    #     # Convert other features similarly
    # ]

    features = [1.        , 0.17021277, 0.43754268, 0.12622076, 1.        ,
       1.        , 0.5       , 0.66666667, 0.66666667, 0.        ,
       0.5       , 0.        , 0.        , 1.        , 0.66666667,
       0.        ]
    
    features = [features] 
    
    prediction = model.predict(features)
    hello=''

    return jsonify({'obesityLevel': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
