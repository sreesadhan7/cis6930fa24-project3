import pandas as pd

import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import os

def cluster_and_visualize(incidents_df):
    """
    Perform clustering on the incident data and visualize it.
    """
    # Preprocessing: Use Label Encoding for 'nature' field
    le = LabelEncoder()
    incidents_df['nature_encoded'] = le.fit_transform(incidents_df['nature'])

    # Clustering using K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    incidents_df['cluster'] = kmeans.fit_predict(incidents_df[['nature_encoded']])

    # Visualization 1: Scatter Plot for Clusters
    plt.figure(figsize=(10, 6))
    for cluster_id in incidents_df['cluster'].unique():
        cluster_data = incidents_df[incidents_df['cluster'] == cluster_id]
        plt.scatter(cluster_data['incident_number'], cluster_data['nature_encoded'], label=f'Cluster {cluster_id}')
    plt.title('Incident Clusters')
    plt.xlabel('Incident Number')
    plt.ylabel('Nature (Encoded)')
    plt.legend()
    scatter_plot_path = os.path.join(os.path.dirname(__file__), 'static', 'cluster_plot.png')
    if not os.path.exists(os.path.dirname(scatter_plot_path)):
        os.makedirs(os.path.dirname(scatter_plot_path))
    plt.savefig(scatter_plot_path)
    plt.close()

    # Visualization 1.1: Nature Clustering based on Counts
    nature_counts = incidents_df['nature'].value_counts().reset_index()
    nature_counts.columns = ['nature', 'count']
    nature_counts['nature_encoded'] = pd.factorize(nature_counts['nature'])[0]

    # Clustering based on nature and count
    kmeans_counts = KMeans(n_clusters=3, random_state=42)
    nature_counts['cluster'] = kmeans_counts.fit_predict(nature_counts[['nature_encoded', 'count']])

    # Scatter Plot for Nature and Count Clustering
    plt.figure(figsize=(10, 6))
    for cluster_id in nature_counts['cluster'].unique():
        cluster_data = nature_counts[nature_counts['cluster'] == cluster_id]
        plt.scatter(
            cluster_data['nature_encoded'],
            cluster_data['count'],
            label=f'Cluster {cluster_id}'
        )
    plt.title('Clustering of Incident Records (Nature and Count)')
    plt.xlabel('Nature (Encoded)')
    plt.ylabel('Count')
    plt.legend()
    nature_clustering_path = os.path.join(os.path.dirname(__file__), 'static', 'nature_clustering.png')
    plt.savefig(nature_clustering_path)
    plt.close()

    print(f"Scatter plot saved at: {scatter_plot_path}")
    print(f"Nature clustering plot saved at: {nature_clustering_path}")

    # Visualization 2: Bar Graph for Nature Counts
    nature_counts = incidents_df['nature'].value_counts()
    plt.figure(figsize=(10, 6))
    nature_counts.plot(kind='bar', color='skyblue')
    plt.title('Comparison of Incident Types')
    plt.xlabel('Incident Nature')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    bar_graph_path = os.path.join(os.path.dirname(__file__), 'static', 'bar_graph.png')
    plt.savefig(bar_graph_path)
    plt.close()

    # Visualization 3: Pie Chart for Nature Distribution
    plt.figure(figsize=(8, 8))
    nature_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Incident Nature Distribution')
    plt.ylabel('')  # Hide the 'nature' label
    pie_chart_path = os.path.join(os.path.dirname(__file__), 'static', 'pie_chart.png')
    plt.savefig(pie_chart_path)
    plt.close()

    print(f"Scatter plot saved at: {scatter_plot_path}")
    print(f"Bar graph saved at: {bar_graph_path}")
    print(f"Pie chart saved at: {pie_chart_path}")

    # Extract the status output (nature and count)
    status_output = incidents_df['nature'].value_counts().reset_index()
    status_output.columns = ['nature', 'count']

    # Return the status output DataFrame
    return status_output