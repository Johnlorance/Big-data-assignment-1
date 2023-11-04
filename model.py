import pandas as pd
from sklearn.cluster import KMeans

# Load your preprocessed DataFrame (make sure to load the correct DataFrame)
# df = pd.read_csv('/app/res_dpre.csv')

# Select the columns you want to use for K-means clustering (e.g., 'Population' and 'Region_Length')
selected_columns = df[['Country_Label']]

# Set the number of clusters (k) to 3
k = 3

# Apply K-means clustering
kmeans = KMeans(n_clusters=k, random_state=0)
df['Cluster'] = kmeans.fit_predict(selected_columns)

# Count the number of records in each cluster
cluster_counts = df['Cluster'].value_counts().sort_index()

# Save the cluster counts as a text file
cluster_counts.to_csv('/app/k.txt', header=['Count'], index_label='Cluster', sep='\t')
