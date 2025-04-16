# ICU Mortality Prediction using Multimodal Machine Learning

This repository contains the code and workflow for my Final Year Project (FYP) titled **“Enhancing ICU Mortality Prediction Using Multimodal Machine Learning.”**

The main goal of this project is to improve ICU mortality prediction by combining structured and unstructured data from the MIMIC-IV database. Structured data includes vitals and ICU admission records, while unstructured data comes from diagnosis descriptions (`long_title`).

---

## 🛠️ What This Project Includes
- Loading and cleaning MIMIC-IV data using SQL and Python
- Preprocessing unstructured diagnostic text
- TF-IDF vectorisation and clustering of text data
- Feature engineering including one-hot encoding and scaling
- Model training and evaluation using Random Forest
- Visualisations of diagnosis clusters and word clouds

---

## 📁 Files in This Repository

| File | Description |
|------|-------------|
| `preprocessing.py` | Cleans the `long_title` text column and saves the cleaned version |
| `tfidf_clustering.py` | Converts the cleaned text into numerical features using TF-IDF |
| `tfidf_clustering_and_visuals.py` | Performs clustering and generates word clouds and a cluster distribution bar chart |
| `feature_engineering.sql` | SQL script to create one-hot encoded columns and scale vital signs |
| `sql_queries.sql` | SQL queries to extract and join relevant MIMIC-IV tables |
| `model_training.py` | Initial model training and evaluation on processed data |
| `final_model_training.py` | Full end-to-end model pipeline: connects to PostgreSQL, trains and evaluates final model |
| `README.md` | This documentation file explaining the contents and how to run each script |

---

## How to Run This Project

1. **Set up** your PostgreSQL environment and load MIMIC-IV data
2. Run the following scripts in this order:
   - `sql_queries.sql` – Extracts data from MIMIC-IV
   - `feature_engineering.sql` – Adds and scales important features
   - `preprocessing.py` – Cleans diagnosis descriptions
   - `tfidf_clustering.py` – Converts text to TF-IDF
   - `tfidf_clustering_and_visuals.py` – Clusters diagnosis terms and shows word clouds
   - `model_training.py` – Trains a Random Forest model
   - `final_model_training.py` – Full pipeline connected to your PostgreSQL database

---

## Requirements

Install required Python packages:

```bash
pip install pandas scikit-learn matplotlib wordcloud psycopg2 sqlalchemy

This project was completed as part of my Final Year Project under the guidance of Professor Mengling 'Mornin' Feng (PhD). Special thanks to the PhysioNet team for providing access to the MIMIC-IV dataset.

Note: No raw patient data is included in this repository. Only code and processed output structures are shared in accordance with MIMIC-IV data usage guidelines.
