# ICU Mortality Prediction using Multimodal Machine Learning

This repository contains the code and workflow for my Final Year Project (FYP) titled **“Enhancing ICU Mortality Prediction Using Multimodal Machine Learning”**.

The main objective of this project is to predict ICU mortality by combining both structured and unstructured data from the MIMIC-IV database. Structured data includes vitals and ICU stay information, while unstructured data comes from diagnosis descriptions (`long_title`).

## What this project includes:
- Extracting and cleaning structured data using SQL and Python
- Preprocessing unstructured diagnosis text using TF-IDF
- Grouping diagnosis terms into clusters using K-means
- Feature engineering using one-hot encoding and scaling
- Merging data for model training
- Building and evaluating a Random Forest model for mortality prediction

## Files in this repo

| File | Description |
|------|-------------|
| `preprocessing.py` | Cleans the `long_title` text column and saves the cleaned version |
| `generate_wordcloud.py` | Generates a word cloud from the cleaned diagnosis text |
| `tfidf_clustering.py` | Applies TF-IDF vectorisation and K-means clustering on diagnosis text |
| `feature_engineering.sql` | SQL script to one-hot encode ICU units and scale vital signs |
| `sql_queries.sql` | Contains PostgreSQL queries for extracting and joining structured tables |
| `model_training.py` | Basic model script that trains a Random Forest using cleaned data |
| `final_model_training.py` | Connects directly to PostgreSQL, handles full pipeline, and evaluates the final model |

**Note:** This repository does not include raw MIMIC-IV data. Only code and workflows are provided in line with data use guidelines.

## How to use
1. Set up PostgreSQL and load MIMIC-IV tables
2. Run `sql_queries.sql` and `feature_engineering.sql` to extract and transform data
3. Use Python scripts in the following order:
   - `preprocessing.py`
   - `generate_wordcloud.py`
   - `tfidf_clustering.py`
   - `model_training.py` or `final_model_training.py` (final version)

## Requirements
Install the following packages:

```bash
pip install pandas scikit-learn matplotlib wordcloud psycopg2 sqlalchemy
