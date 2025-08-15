
# 🖼 Xception Image Classifier

This project is a **deep learning-based web application** that classifies uploaded images into one of six categories using a **fine-tuned Xception model**. It provides a simple and user-friendly interface where users can upload an image and instantly get predictions.

## 📌 Project Overview

* The application uses a fine-tuned **Xception** model trained on a dataset containing six classes.
* Users can upload any image, and the model predicts the category along with the confidence level.
* The interface displays both the prediction and the uploaded image for easy verification.

## 📊 Classes

The model predicts one of the following:

* 🏢 Building
* 🌲 Forest
* 🏔 Glacier
* ⛰ Mountain
* 🌊 Sea
* 🚗 Street

## 📂 Dataset

The model is trained using the **Intel Image Classification dataset** from Kaggle.
You can find it here: [Intel Image Classification Dataset](https://www.kaggle.com/puneet6060/intel-image-classification)

The dataset contains natural scene images across six categories. All images were resized to **299x299 pixels** and normalized before training.

## 🛠️ Technologies Used

* **Python**
* **Flask** (for backend)
* **HTML/CSS** (for frontend)
* **TensorFlow / Keras** (Xception model)
* **NumPy** (image preprocessing)

## ⚙️ How It Works

1. User uploads an image via the web interface.
2. Image is resized to `(299, 299)` and normalized (`/255.0`).
3. The fine-tuned **Xception** model predicts the category.
4. The prediction and uploaded image are displayed to the user.
