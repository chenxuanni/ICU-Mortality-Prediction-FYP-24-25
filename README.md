# ICU Mortality Prediction using Multimodal Machine Learning

This repository contains the codes and workflow for my Final Year Project (FYP) titled **“Enhancing ICU Mortality Prediction Using Multimodal Machine Learning”**.

The main aim of this project is to improve the prediction of ICU mortality by using both structured and unstructured data from the MIMIC-IV database. Structured data includes vitals and patient stay information, while unstructured data refers to diagnosis descriptions (`long_title`).

## What I did
- Loaded MIMIC-IV data into PostgreSQL for better data management
- Cleaned and prepared structured data (e.g., vital signs, ICU stay)
- Preprocessed the unstructured diagnosis text using TF-IDF
- Used K-means clustering to group diagnosis terms into meaningful themes
- Merged both datasets using `hadm_id` as the key
- Trained a Random Forest model to predict ICU mortality
- Evaluated the model using accuracy, precision, recall, and F1-score

## Files in this repo
| File | Description |
|------|-------------|
| `preprocessing.py` | Code for cleaning structured and unstructured data |
| `tfidf_clustering.py` | Converts text to TF-IDF and applies K-means clustering |
| `model_training.py` | Random Forest model training and evaluation |
| `sql_queries.sql` | SQL queries used to extract and join tables from PostgreSQL |
| `outputs/` | Folder with word cloud images and feature importance chart |

**Note**: No actual patient data is included in this repo. Only code and sample structures are provided.

## How to run
1. Set up a PostgreSQL database and load relevant MIMIC-IV tables
2. Edit the database connection string in the scripts
3. Run the scripts in order:
   - `preprocessing.py`
   - `tfidf_clustering.py`
   - `model_training.py`

## Acknowledgement
This project is part of my final year work under the guidance of **Mengling 'Mornin' Feng (PhD)**. I would also like to thank the team behind MIMIC-IV for providing access to such a useful dataset.

