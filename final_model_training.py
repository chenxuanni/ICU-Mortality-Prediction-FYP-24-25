import psycopg2
print(" psycopg2 is working!")

from sqlalchemy import create_engine
import pandas as pd

# Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:733169@localhost:5432/mimiciv_v1")

# Load data
df = pd.read_sql("SELECT * FROM final_icu_model_data", con=engine)
print(df.head())

# Define label (target) and drop irrelevant/problematic columns
y = df['hospital_expire_flag']
X = df.drop(columns=[
    'subject_id', 'hadm_id', 'long_title', 'hospital_expire_flag',
    'icu_admit_time', 'icu_discharge_time'  # drop datetime columns
])

# Convert categorical variables to numerical
X = pd.get_dummies(X)

# Handle missing values (NaNs) by replacing them with 0 or use .fillna(method='ffill') if time-ordered
X = X.fillna(0)

# Continue with train/test split and model training
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))



