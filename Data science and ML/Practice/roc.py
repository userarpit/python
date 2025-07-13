from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np

# True binary labels (actual outcomes)
y_true = np.array([0, 0, 1, 1, 0, 1, 0, 1])

# Predicted probabilities of the positive class (e.g., from a logistic regression model)
# Higher score means higher probability of being positive
y_scores = np.array([0.1, 0.3, 0.4, 0.7, 0.2, 0.8, 0.6, 0.9])

# Calculate FPR, TPR, and thresholds
fpr, tpr, thresholds = roc_curve(y_true, y_scores)

print("FPR values:", fpr)
print("TPR values:", tpr)
print("Thresholds:", thresholds)

# Calculate the Area Under the Curve (AUC)
roc_auc = auc(fpr, tpr)
print("\nAUC:", roc_auc)

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()