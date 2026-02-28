from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import joblib

app = Flask(__name__, static_folder='statics')

# loading the trained model and scaler
model  = tf.keras.models.load_model('my_model.keras')
scaler = joblib.load('scaler.pkl')

class_labels = ['Setosa', 'Versicolor', 'Virginica']


@app.route('/')
def home():
    return render_template('predict.html')


@app.route('/health')
def health():
    return jsonify({"status": "ok", "model": "iris_classifier"})


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.form
            sepal_length = float(data['sepal_length'])
            sepal_width  = float(data['sepal_width'])
            petal_length = float(data['petal_length'])
            petal_width  = float(data['petal_width'])

            # scaling the input using the same scaler used during training
            raw_input    = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            scaled_input = scaler.transform(raw_input)

            # prediction
            prediction      = model.predict(scaled_input)
            predicted_index = int(np.argmax(prediction))
            predicted_class = class_labels[predicted_index]
            confidence      = round(float(np.max(prediction)) * 100, 2)

            return jsonify({
                "predicted_class": predicted_class,
                "confidence": confidence
            })

        except Exception as e:
            return jsonify({"error": str(e)})

    elif request.method == 'GET':
        return render_template('predict.html')

    else:
        return "Unsupported HTTP method"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)