import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("final_icu_model_data.csv")
X = df.drop(columns=['subject_id', 'hadm_id', 'long_title', 'hospital_expire_flag', 'icu_admit_time', 'icu_discharge_time'])
X = pd.get_dummies(X).fillna(0)
y = df['hospital_expire_flag']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
