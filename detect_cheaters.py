
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/player_behavior.csv")

# Features for detection
features = ['accuracy', 'headshot_ratio', 'movement_speed', 'reaction_time', 'kdr']
X = df[features]

# Fit Isolation Forest
model = IsolationForest(contamination=0.06, random_state=42)
df['anomaly_score'] = model.fit_predict(X)

# Map results
df['detected_cheater'] = df['anomaly_score'].map({1: 0, -1: 1})

# Show confusion matrix if ground truth is available
if 'suspected' in df.columns:
    from sklearn.metrics import confusion_matrix, classification_report
    print("Classification Report (vs. Ground Truth):")
    print(classification_report(df['suspected'], df['detected_cheater']))

# Save results
df.to_csv("data/detected_cheaters.csv", index=False)

# Optional: plot distribution
sns.pairplot(df, hue='detected_cheater', vars=features)
plt.suptitle("Player Behavior Anomaly Detection", y=1.02)
plt.tight_layout()
plt.savefig("data/cheater_detection_plot.png")
plt.show()
