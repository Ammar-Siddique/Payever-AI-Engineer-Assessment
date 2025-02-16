# Payever-AI-Engineer-Assessment
# Product Classification with TensorFlow

This project demonstrates a machine learning prototype for classifying dummy products into predefined categories using TensorFlow. The framework includes dataset generation, data preprocessing, model building, training, and evaluation.

## Table of Contents
- [Introduction](#introduction)
- [Assumptions](#assumptions)
- [Features](#features)
- [Installation and Working](#installation-and-working)
- [Usage](#usage)
  - [Data Generation](#data-generation)
  - [Preprocessing](#preprocessing)
  - [Model Building and Training](#model-building-and-training)
  - [Evaluation](#evaluation)
- [Results](#results)
- [Limitations](#limitations)
- [Conclusion](#conclusion)

## Introduction
This project aims to build a prototype machine learning model to classify products into categories such as Electronics, Home, Gadgets, Clothing, Books, and Toys. It uses TensorFlow for model development, with preprocessing steps to handle text and categorical data. The project includes scripts for data generation, preprocessing, model training, and evaluation.

## Assumptions
### 1. Data Availability:
- **Sufficient Data:** It is assumed that the available dataset of randomly generated 1000 dummy products is representative and sufficient for training the model.

### 2. Model Assumptions:
- **Independence of Features:** Features are assumed to be independent of each other.
- **Stationary Data:** The underlying data distribution is assumed to be stationary over time, meaning it does not change significantly.
### 3. Evaluation Metrics:
- **Appropriateness of Metrics:** The chosen evaluation metrics (accuracy, precision, recall, F1 score) are assumed to be appropriate for assessing the model’s performance.

## Features
- **Data Generation**: Generates a synthetic dataset of products with attributes like name, description, price, and category.
- **Data Preprocessing**: Handles text tokenization and padding, label encoding, and splitting data into training and testing sets.
- **Model Building**: Constructs a neural network model using TensorFlow's Sequential API with dense layers.
- **Model Evaluation**: Evaluates the model’s performance and visualizes results with accuracy metrics and confusion matrix.

## Installation and Working
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/product-classification.git
    cd Payever-AI-Engineer-Assessment
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the Program
    ```sh
    py main.py
    ```
## Usage
### 1. Data Generation
Generate a dataset of dummy products:
- Name: Name of the product.
- Description: Description of the product.
- Price: Price of the product.
- Category: Category to which the product belongs.

### 2. Preprocessing

Data preprocessing is a crucial step to ensure the data is clean and suitable for training. The preprocessing steps include:

1. **Label Encoding**: Convert categorical labels (category) into numerical values.
1. **Tokenization and Padding**: Clean and convert text (name and description) to sequences and pad them.
1. **Data Normalization**: Normalize numerical data (price).
1. **Train-Test Split**: Split the data into training and testing sets.

### 3. Model Building and Training

The model is built using TensorFlow's Keras Sequential API. It involves defining the architecture, compiling the model, and training it on the preprocessed data.

**Model Architecture**

The model consists of the following layers:

- Input layer
- Dense layers with ReLU activation
- Output layer with softmax activation

**Training Parameters**

The training parameters include:

- **Batch size**: 32
- **Number of epochs**: 20
- **Loss function**: Sparse Categorical Cross-Entropy
- **Optimizer**: Adam

### 4. Evaluation

After training the model, it is evaluated on the test set to determine its accuracy and performance. The evaluation metrics include accuracy, precision, recall, F1-score and confusion matrix

## Results
The model achieved the following performance metrics on the validation set:

- Accuracy: 91.00%
- Precision: 93.26%
- Recall: 91.00%
- F1 Score: 91.28%

## Limitations
### 1. Data Quality and Quantity:

- **Insufficient Data:** The dataset is not be large enough to generalize well across different scenarios.
- **Imbalanced Data:** If the data is imbalanced due to being genrated randomly, the model may perform poorly on underrepresented classes.

### 2. Model Generalization:

- **Overfitting:** Achieving 100% accuracy on training data might indicate overfitting, where the model performs well on the training data but poorly on unseen data, due to overcomplexity of the model. 
- **Underfitting:** Conversely, underfitting might occur if the model is too simple to capture the underlying patterns in the random data generated.

## Conclusion

This project demonstrates how to build a product classification model using TensorFlow. The model can classify products into their respective categories based on attributes like name, description, and price.


