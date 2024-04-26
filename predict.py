import numpy as np
from joblib import load
import plotly.graph_objects as go

def predict_graph(X_new):
    # Load the model and scaler
    loaded_object = load('rfmodel_with_scaler.joblib')
    RFclassifier = loaded_object[0]  # First element is the model
    scaler = loaded_object[1]        # Second element is the scaler
    # Reshape the data point to match the expected input shape
    X_new = np.array(X_new)
    X_new = X_new.reshape(1, -1)

    # Normalize the new data using the scaler loaded from the model file
    X_new_normalized = scaler.transform(X_new)
    predicted_classes = RFclassifier.predict(X_new)
    # Make predictions
    predicted_probabilities = RFclassifier.predict_proba(X_new_normalized)[0]
    print(predicted_probabilities)

    class_labels = RFclassifier.classes_

    fig = go.Figure(data=[go.Pie(labels=class_labels, values=predicted_probabilities, hole=0.3)])

    fig.update_layout(title='Predicted Probabilities for Each Class')
    fig.show()

    print(predicted_classes)

X_new =[1., 0.17021277, 0.43754268, 0.12622076, 1., 1., 0.5, 0.66666667, 0.66666667, 0., 0.5, 0., 0., 1., 0.66666667, 0.]

predict_graph(X_new)