import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score


def evaluate_model(model, X_test, y_test, history):
    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {accuracy:.2f}")

    # Plot the training history
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0, 1])
    plt.legend(loc='lower right')
    plt.show()

    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    print("------------------------------------------------")
    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred_classes)
    print(cm)

    acc = accuracy_score(y_test, y_pred_classes)
    print("Succes accuracy = {0:.2f} %".format(acc * 100))
    fail = 1.0 - acc
    print("Fail accuracy = {0:.2f} %".format(fail * 100))
    print("------------------------------------------------")

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.show()
