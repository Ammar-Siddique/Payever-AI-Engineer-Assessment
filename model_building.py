from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense


def build_model(label_encoder):
    model = Sequential([
        Embedding(input_dim=100, output_dim=16, input_length=10),
        GlobalAveragePooling1D(),
        Dense(16, activation='relu'),
        Dense(len(label_encoder.classes_), activation='softmax')
    ])
    # Compile the model
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    model.save('dummy_product.keras')
    return model
