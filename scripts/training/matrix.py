import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

true_labels = ['Scab', 'Black Rot', 'Cedar Apple Rust', '', '', 'Powdery Mildew', '', 'Cercospora /Grey Leaf Spot',
               'Common Rust', 'Northern Leaf Blight', '', 'Black Rot', 'Esca', 'Leaf Blight', '', 'Haunglongbing',
               'Bacterial Spot', '', 'Bacterial Spot', '', 'Early Blight', 'Late Blight', '', '', '', '',
               'Powdery Mildew', 'Leaf Scorch', '', 'Bacterial Spot', '', 'Early Blight', 'Late Blight',
               'Leaf Mould', 'Septoria Leaf Spot', 'Spider Mites', 'Target Spot', 'Yellow Leaf Curl Virus',
               'Mosaic Virus', '']  # Example true labels

predicted_labels = ['Scab', 'Black Rot', 'Cedar Apple Rust', '', '', 'Powdery Mildew', '', 'Cercospora /Grey Leaf Spot',
                    'Common Rust', 'Northern Leaf Blight', '', 'Black Rot', 'Esca', 'Leaf Blight', '', 'Haunglongbing',
                    'Bacterial Spot', '', 'Bacterial Spot', '', 'Early Blight', 'Late Blight', '', '', '', '',
                    'Powdery Mildew', 'Leaf Scorch', '', 'Bacterial Spot', '', 'Early Blight', 'Late Blight',
                    'Leaf Mould', 'Septoria Leaf Spot', 'Spider Mites', 'Target Spot', 'Yellow Leaf Curl Virus',
                    'Mosaic Virus', '']  # Example predicted labels

# Compute the confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Plot the confusion matrix
classes = list(set(true_labels + predicted_labels))  # List of class labels
plt.figure(figsize=(8, 8))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=90)
plt.yticks(tick_marks, classes)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

# Append accuracy and loss values
accuracy = [0.9, 0.85, 0.92]  # List of validation accuracies for each epoch
loss = [0.3, 0.2, 0.1]  # List of validation losses for each epoch

new_accuracy = [0.88, 0.91, 0.89]  # List of new validation accuracies for each epoch
new_loss = [0.15, 0.12, 0.2]  # List of new validation losses for each epoch

epochs = range(1, len(accuracy) + 1)
new_epochs = range(len(accuracy) + 1, len(accuracy) + len(new_accuracy) + 1)
accuracy.extend(new_accuracy)
loss.extend(new_loss)

# Plot the validation diagram
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(epochs, accuracy, 'b', label='Accuracy')
plt.plot(new_epochs, new_accuracy, 'b--', label='New Accuracy')
plt.title('Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(epochs, loss, 'r', label='Loss')
plt.plot(new_epochs, new_loss, 'r--', label='New Loss')
plt.title('Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()
