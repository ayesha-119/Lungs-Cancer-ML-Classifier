from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
#from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
#CORS(app)
model = load_model('Seq3cnn.h5', compile=False)  # Load your trained model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        uploaded_image = request.files['image']
        if uploaded_image.filename == '':
            return jsonify({'error': 'No image selected'})

        try:
            img = image.load_img(BytesIO(uploaded_image.read()), target_size=(128, 128))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
        except Exception as img_error:
            return jsonify({'error': f'Error processing image: {str(img_error)}'})

        try:
            prediction = model.predict(img_array)[0][0]
        except Exception as model_error:
            return jsonify({'error': f'Error making prediction: {str(model_error)}'})

        if prediction > 0.5:
            result = 'Malignant'
        else:
            result = 'Benign'
        print("Prediction result:", result)

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True)
