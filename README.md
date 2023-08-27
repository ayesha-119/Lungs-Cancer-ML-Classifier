# Lungs-Cancer-ML-Classifier




This repository contains an end-to-end project for lung nodule classification using multiple deep learning models and Flask for web deployment.

## Table of Contents

- [Description](#description)
- [Introduction](#introduction)
- [Why Timely Diagnosis of Lung Nodules](#why-timely-diagnosis-of-lung-nodules)
- [Models](#models)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Technologies](#technologies)
- [Why Lung Nodule Classification](#why-lung-nodule-classification)
- [Contributing](#contributing)
- [License](#license)

## Description

This project demonstrates the implementation and deployment of multiple deep-learning models for lung nodule classification. The web application allows users to upload CT scan images of lung nodules and receive predictions about the malignancy of the nodules.
## Introduction

Lung cancer is one of the most common and deadly forms of cancer worldwide. Early detection and accurate diagnosis are critical for improving patient outcomes. Timely identification of lung nodules, small abnormal growths in the lungs, is a crucial step in diagnosing lung cancer. These nodules can be benign (non-cancerous) or malignant (cancerous), and distinguishing between them is challenging.

This project addresses the need for automated lung nodule classification using deep learning techniques. By leveraging state-of-the-art deep learning models, we aim to provide medical professionals with a tool that aids in accurately and efficiently classifying lung nodules, thereby facilitating early intervention and treatment.

## Why Timely Diagnosis of Lung Nodules

The significance of timely diagnosis of lung nodules cannot be overstated. Here's why it matters:

1. **Early Detection:** Early detection of lung cancer increases the chances of successful treatment and improves patient survival rates.

2. **Personalized Treatment:** Accurate classification of lung nodules helps medical professionals tailor treatment plans based on the nodule's malignancy, leading to better outcomes for patients.

3. **Reduced Healthcare Costs:** Early diagnosis and treatment of lung nodules can reduce the need for extensive and costly interventions that might be required in advanced stages of cancer.

4. **Enhanced Patient Care:** Providing medical professionals with an efficient tool for nodule classification speeds up the diagnostic process and allows for more focused patient care.

## Models

The following models have been implemented for lung nodule classification:

- VGG16
- VGG19
- ResNet
- AlexNet
- EfficientNet

Each model has been trained on a labeled dataset to classify lung nodules as benign or malignant.

## Dataset

The [LIDC-IDRI dataset](https://paperswithcode.com/dataset/lidc-idri) has been used for training and evaluation. The LIDC-IDRI dataset is a publicly available dataset of lung CT scans containing annotations of lung nodules. It serves as a valuable resource for developing and evaluating lung nodule classification models.

## Installation

1. Clone the repository:
git clone https://github.com/ayesha-119/Lungs-Cancer-ML-Classifier

2. Navigate to the project directory:
cd Lungs-Cancer-ML-Classifier

3. Install the required dependencies:
pip install -r requirements.txt

## Usage

1. Run the Flask application:
python app.py


2. Access the web application in your browser at `http://localhost:5000`.

3. Upload a CT scan image to the application and select a model to use for prediction. Click the "Predict" button to receive a prediction for the malignancy of the lung nodule.



## Technologies

- Deep Learning: VGG16, VGG19, ResNet, AlexNet, EfficientNet
- Flask: Web application framework
- HTML/CSS/JavaScript: Frontend development
- TensorFlow/Keras: Deep learning library

## Why Lung Nodule Classification

Lung nodule classification is an essential task in medical imaging. It helps in the early detection and diagnosis of lung cancer, which is crucial for improving patient outcomes. By accurately classifying lung nodules as benign or malignant, doctors can make informed decisions about treatment plans and interventions.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

