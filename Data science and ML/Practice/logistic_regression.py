import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from imblearn.over_sampling import SMOTE

warnings.filterwarnings("ignore")

np.random.seed(42)
num_transaction = 100000
num_fraud = 500

# generate legimate transactions
legit_amount = np.random.normal(50, 30, num_transaction - num_fraud)
legit_hour = np.random.randint(6, 22, num_transaction - num_fraud)
legit_items = np.random.randint(1, 10, num_transaction - num_fraud)
legit_fraud = np.zeros(num_transaction - num_fraud)

# generate fraud transactions
fraud_amount = np.random.normal(500, 200, num_fraud)
fraud_hour = np.random.choice(np.arange(0, 6), num_fraud)
fraud_items = np.random.randint(1, 3, num_fraud)
fraud_fraud = np.ones(num_fraud)

df_legit = pd.DataFrame(
    {
        "Amount": legit_amount,
        "Transaction_Hour": legit_hour,
        "items": legit_items,
        "Is_Fraud": legit_fraud,
    }
)

df_fraud = pd.DataFrame(
    {
        "Amount": fraud_amount,
        "Transaction_Hour": fraud_hour,
        "items": fraud_items,
        "Is_Fraud": fraud_fraud,
    }
)

# print(df_legit)
# print(df_fraud)

df = pd.concat([df_legit, df_fraud], ignore_index=True)
# print(df)

# endure amount is non-negative and hours are within bound
df["Amount"] = df["Amount"].apply(lambda x: max(0.01, x))
df["Transaction_Hour"] = df["Transaction_Hour"].apply(lambda x: int(max(0, min(23, x))))

# print(df[df['Amount'] < 0])

df = df.sample(frac=1, random_state=42).reset_index(drop=True)
print(df)

X = df[["Amount", "Transaction_Hour", "items"]]
y = df["Is_Fraud"]

# split the train and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# print(y_train.sum())
# print(y_train.shape)

print(y_train.value_counts())
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# print(y_train_resampled.value_counts())
# print(X_train_resampled)
# print(y_train_resampled)

# print(X_test.shape)
# print(y_test.shape)

model = LogisticRegression(solver="liblinear", random_state=42, C=0.1)
model.fit(X_train_resampled, y_train_resampled)
# print(model.coef_)
# print(model.intercept_)

# print(X_test)

y_pred_proba = model.predict_proba(X_test)[
    :, 1
]  # Probability of the positive class (Fraud=1)
print(y_pred_proba)

y_pred = (y_pred_proba >= 0.5).astype(int)
print(y_pred)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

# Plot Confusion Matrix
plt.figure(figsize=(6, 5))
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Predicted Legitimate (0)", "Predicted Fraud (1)"],
    yticklabels=["Actual Legitimate (0)", "Actual Fraud (1)"],
)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix for Fraud Detection")
plt.show()

new_transaction_legit = np.array([[80.0, 15, 5]]) # Amount, Transaction_Hour, Num_Items
predicted_proba_legit = model.predict_proba(new_transaction_legit)
print(predicted_proba_legit)
print(model.predict(new_transaction_legit))
