from data_generation import generate_data
from data_preprocessing import preprocess_data
from model_building import build_model
from model_evaluation import evaluate_model

# Generate data for 100 Dummy products
df = generate_data(1000)
# Save to CSV
df.to_csv("DummyProducts.csv", index=False)

# Preprocess data
X_train, X_test, y_train, y_test, label_encoder = preprocess_data(df)

# Build model
model = build_model(label_encoder)

# Train model
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# Evaluate model
evaluate_model(model, X_test, y_test, history)
