# tfidf_clustering_and_visuals.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load cleaned data
cleaned_data = pd.read_csv("long_title_cleaned.csv")

# TF-IDF Vectorisation
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(cleaned_data['long_title'])

# K-means clustering
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(tfidf_matrix)
cleaned_data['cluster'] = clusters

# Generate word clouds for each cluster
for cluster_num in range(num_clusters):
    cluster_data = cleaned_data[cleaned_data['cluster'] == cluster_num]
    cluster_text = ' '.join(cluster_data['long_title'])

    cluster_wordcloud = WordCloud(width=800, height=400, background_color="white").generate(cluster_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(cluster_wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for Cluster {cluster_num}', fontsize=16)
    plt.show()

# Save the dataframe with cluster labels
cleaned_data.to_csv("cleaned_data_with_clusters.csv", index=False)

# Visualise cluster distribution
cluster_counts = cleaned_data['cluster'].value_counts()
print("Cluster Distribution:")
print(cluster_counts)

cluster_counts.plot(kind='bar', figsize=(8, 5))
plt.title('Distribution of Clusters', fontsize=16)
plt.xlabel('Cluster', fontsize=14)
plt.ylabel('Number of Entries', fontsize=14)
plt.show()
