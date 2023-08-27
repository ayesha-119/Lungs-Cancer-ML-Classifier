function predict() {
    const fileInput = document.getElementById('image-input');
    const errorMessage = document.getElementById('error-message');
    const imagePreview = document.getElementById('image-preview');
    const predictionResult = document.getElementById('prediction-result');

    errorMessage.textContent = '';
    predictionResult.textContent = '';
    imagePreview.innerHTML = '';

    const file = fileInput.files[0];

    if (!file) {
        errorMessage.textContent = 'Please select a CT scan image first.';
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    const img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    img.alt = 'Selected Image';
    imagePreview.appendChild(img);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(result => {
        console.log('Result:', result);
        if (result.error) {
            predictionResult.textContent = `Error: ${result.error}`;
        } else {
            predictionResult.textContent = `Prediction: ${result.prediction}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        predictionResult.textContent = 'An error occurred while processing the image.';
    });
}
