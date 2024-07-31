from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np


def preprocess_data(df):
    # Encode the labels (categories)
    label_encoder = LabelEncoder()
    df['category'] = label_encoder.fit_transform(df['category'])

    # Split the data into training and testing sets
    train_data, test_data = train_test_split(
        df,
        test_size=0.2,
        random_state=42
    )

    # Tokenize the text data
    tokenizer = Tokenizer(num_words=100)
    tokenizer.fit_on_texts(train_data['description'])

    # Convert text to sequences and pad them
    X_train = tokenizer.texts_to_sequences(train_data['description'])
    X_train = pad_sequences(X_train, padding='post', maxlen=10)
    X_test = tokenizer.texts_to_sequences(test_data['description'])
    X_test = pad_sequences(X_test, padding='post', maxlen=10)

    # Convert labels to numpy arrays
    y_train = np.array(train_data['category'])
    y_test = np.array(test_data['category'])

    return X_train, X_test, y_train, y_test, label_encoder
