import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if not isinstance(text, str):  # Ensure input is a string
        return ""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = re.sub(r'\d+', '', text)  # Remove digits
    tokens = word_tokenize(text)  # Tokenize text
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]  # Lemmatize and remove stopwords
    return ' '.join(tokens)



file_path = r"C:\Users\xuanni\physionet.org\files\mimiciv\3.1\hosp\d_icd_diagnoses.csv"
data = pd.read_csv(file_path)


if 'long_title' in data.columns:
    data = data[data['long_title'].notnull()]  # Remove rows with null values
    data['long_title_cleaned'] = data['long_title'].apply(preprocess_text)
else:
    raise KeyError("Column 'long_title' not found in the dataset.")







