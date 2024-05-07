# Mask Monitor

Mask Monitor is a machine learning project that detects whether a person is wearing a mask or not using computer vision techniques. If a person is detected without a mask, a voice alert is triggered. Additionally, the project records data including date, time, and status (with mask or without mask) every 5 seconds, storing it in a proper format.

## Contents

- [Introduction](#introduction)
- [Key Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Contributions](#contributions)

## Introduction

With the ongoing global pandemic, wearing masks has become crucial for public health safety. The Mask Monitor project aims to automate the process of monitoring mask-wearing compliance in public places such as offices, schools, and stores.

The project utilizes a Convolutional Neural Network (CNN) trained on a dataset of images containing people with and without masks. It leverages the OpenCV library for real-time face detection and classification. When a person without a mask is detected, a voice alert is issued to remind them to wear a mask. Furthermore, the project records the time-stamped status of each detection for future analysis.

## Features

- **Real-time Mask Detection**: Utilizes computer vision techniques to detect whether a person is wearing a mask in real-time.

- **Voice Alerts**: Issues voice alerts when a person is detected without a mask, enhancing safety measures and compliance.

- **Data Recording**: Records data including date, time, and mask status every 5 seconds, storing it for future analysis.

- **Automatic Image Saving**: Saves images of detected individuals with their mask status for further reference and analysis.

- **Modular Design**: Divided into modular components for model training, mask detection, data recording, and image saving, facilitating maintenance and extensibility.


## Requirements

To run this project, you need:

- Python 3.x
- OpenCV
- NumPy
- TensorFlow
- Matplotlib
- Pandas
- pyttsx3
- Dataset : The dataset used for training and testing the Mask Monitor project is available in the `Face Mask Dataset` directory. It contains images of people with and without masks, organized into separate folders.
- Trained Model: The trained model file (`mask_model.h5`) is available in the repository. This file contains the trained neural network model for mask detection.


## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies as mentioned in the requirements section.
3. Run `main.py` to start the Mask Monitor application.
4. Ensure your camera is connected and properly configured.
5. The application will display live video with mask detection annotations.
6. Press 'q' to quit the application.

## File Descriptions

- `Train_Model.py`: This script trains the machine learning model on a dataset of images containing people with and without masks.
- `Accuracy_Test.py`: This script evaluates the trained model's accuracy on a separate test dataset and plots the training history.
- `mask_detector.py`: This module contains the FaceMaskDetector class responsible for real-time mask detection and data recording.
- `excel_handler.py`: This module handles the recording of data to an Excel file.
- `image_saver.py`: This module handles saving captured images along with their status (with or without mask).
- `main.py`: This is the main script to run the Mask Monitor application.

## Contributions

Contributions to this project are welcome and encouraged! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

Your contributions can include bug fixes, feature enhancements, documentation improvements, and more. Let's work together to make this project even better!
