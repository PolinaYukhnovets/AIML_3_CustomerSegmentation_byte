import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Segmentation Dashboard")

st.write(
    "This dashboard uses K-Means clustering to group customers "
    "based on their age, annual income and spending behaviour."
)

df = pd.read_csv("data/Mall_Customers.csv")

features = df[[
    "Age",
    "Annual Income (k$)",
    "Spending Score (1-100)"
]]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=6, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(features_scaled)

cluster_profiles = df.groupby("Cluster").agg(
    Customers=("CustomerID", "count"),
    Average_Age=("Age", "mean"),
    Average_Income=("Annual Income (k$)", "mean"),
    Average_Spending_Score=("Spending Score (1-100)", "mean")
).round(2)

whale_cluster = cluster_profiles["Average_Spending_Score"].idxmax()
whale_profile = cluster_profiles.loc[whale_cluster]

st.subheader("Customer Segments")

col1, col2, col3 = st.columns(3)

col1.metric("Customers", len(df))
col2.metric("Number of Clusters", 6)
col3.metric("Highest-Spending Segment", f"Cluster {whale_cluster}")

st.dataframe(cluster_profiles, use_container_width=True)

st.subheader("Customer Cluster Visualisation")

fig, ax = plt.subplots(figsize=(9, 6))

scatter = ax.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    c=df["Cluster"],
    cmap="viridis",
    s=60
)

ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score (1-100)")
ax.set_title("Customer Segments")

fig.colorbar(scatter, ax=ax, label="Cluster")

st.pyplot(fig)

st.subheader("Highest-Spending Customer Segment")

st.success(f"Cluster {whale_cluster} has the highest average spending score.")

col1, col2, col3 = st.columns(3)

col1.metric("Average Age", f"{whale_profile['Average_Age']:.2f}")
col2.metric("Average Income", f"${whale_profile['Average_Income']:.2f}k")
col3.metric(
    "Average Spending Score",
    f"{whale_profile['Average_Spending_Score']:.2f}/100"
)

st.subheader("Targeted Marketing Brief")

st.write(
    f"Cluster {whale_cluster} contains customers with high annual income "
    "and the highest average spending score in the dataset."
)

st.markdown("""
**Recommended Actions:**

1. Promote premium and higher-value products to this customer segment.
2. Offer loyalty rewards and exclusive discounts to encourage repeat purchases.
3. Create personalised marketing campaigns based on the group's high spending behaviour.
""")

