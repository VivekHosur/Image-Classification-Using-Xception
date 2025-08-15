from flask import Flask, request, render_template
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import os

app = Flask(__name__)
model = load_model('xception_custom.h5')  # Your fine-tuned model

# Your 6 classes
class_names = ['Building', 'Forest', 'Glacier', 'Mountain', 'Sea', 'Street']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    img_path = None
    if request.method == 'POST':
        img_file = request.files['img']
        if img_file:
            img_path = os.path.join('static', img_file.filename)
            img_file.save(img_path)

            img = image.load_img(img_path, target_size=(299, 299))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = x / 255.0  # Assuming you trained with rescale=1./255

            preds = model.predict(x)
            predicted_class = class_names[np.argmax(preds)]
            confidence = np.max(preds) * 100
            prediction = f"{predicted_class}"

    return render_template('index.html', prediction=prediction, img_path=img_path)

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
