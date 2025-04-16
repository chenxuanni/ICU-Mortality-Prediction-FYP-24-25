import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import TfidfVectorizer

# Database Connection
db_url = "postgresql://postgres:733169@localhost:5432/mimiciv_v1"
engine = create_engine(db_url)

# Load Data from PostgreSQL
query = "SELECT hadm_id, long_title FROM icu_vital_diagnoses"
df = pd.read_sql(query, con=engine)

# Check for missing values in long_title
df['long_title'].fillna('Unknown', inplace=True)

# Convert Text Data to TF-IDF Features
vectorizer = TfidfVectorizer(max_features=500)  # Limit to 500 most important words
tfidf_matrix = vectorizer.fit_transform(df['long_title'])

# Convert to DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Add `hadm_id` back for merging with the database
tfidf_df.insert(0, "hadm_id", df["hadm_id"])

# Rename any column that conflicts with SQL reserved words
tfidf_df.columns = [f"tfidf_{col}" if col.lower() in ["lateral"] else col for col in tfidf_df.columns]

# Save back to PostgreSQL
tfidf_df.to_sql("icu_vital_diagnoses_tfidf", con=engine, if_exists="replace", index=False)

print(" TF-IDF Features Extracted and Stored in PostgreSQL Successfully!")


