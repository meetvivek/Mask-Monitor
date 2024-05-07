import os
import cv2
import numpy as np
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt

# Function to load and preprocess test data
def load_and_preprocess_test_data(folder):
    data = []
    for category in categories:
        path = os.path.join(data_dir, folder, category)
        class_num = categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                resized_array = cv2.resize(img_array, (img_size, img_size))
                data.append([resized_array, class_num])
            except Exception as e:
                print(e)

    X = []
    y = []

    for features, label in data:
        X.append(features)
        y.append(label)

    X = np.array(X).reshape(-1, img_size, img_size, 1)
    X = X / 255.0  # Normalize pixel values
    return X, y


# Define constants
data_dir = "Face Mask Dataset"
categories = ["WithMask", "WithoutMask"]
img_size = 224

# Load saved model
saved_model_path = "mask_model.h5"
loaded_model = load_model(saved_model_path)

# Load and preprocess test dataset
X_test, y_test = load_and_preprocess_test_data("Test")

# Make predictions
predictions = loaded_model.predict(X_test)
predicted_labels = np.round(predictions).flatten().astype(int)

# Calculate accuracy
accuracy = accuracy_score(y_test, predicted_labels)
print(f"Test Accuracy: {accuracy}")

# Load training history
history = np.load('training_history.npy', allow_pickle=True).item()

# Plot training loss and accuracy on the same graph
plt.figure(figsize=(12, 6))

# Plot training loss in red
plt.plot(history['loss'], 'r', label='training loss')

# Plot validation loss in blue
plt.plot(history['val_loss'], 'b', label='validation loss')

# Plot training accuracy in green
plt.plot(history['accuracy'], 'g', label='training accuracy')

# Plot validation accuracy in orange
plt.plot(history['val_accuracy'], 'orange', label='validation accuracy')

plt.xlabel('# epochs')
plt.ylabel('Loss / Accuracy')
plt.legend()
plt.show()
