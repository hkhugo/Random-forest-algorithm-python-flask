from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the dataset
rssi_df = pd.read_csv('rssi.csv')
beacon_pos_df = pd.read_csv('beacon_pos.csv')

# Preprocess the dataset
X_train = rssi_df.values.tolist()
y_train = beacon_pos_df.values.tolist()

# Train the random forest regressor
rf = RandomForestRegressor(n_estimators=100, random_state=0)
rf.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    print("testing")
    # Get the input data from the request
    print(request.get_json())
    data = request.get_json()
    input_data = data['input_data']
    print(input_data)

    # Convert the input data into a format that can be used by the model
    X = np.array(input_data).reshape(1, -1)


    # Make a prediction using the trained model
    y_pred = rf.predict(X)

    # Return the prediction as a response
    return {'prediction': y_pred.tolist()}

if __name__ == '__main__':
    app.run(host='0.0.0.0')