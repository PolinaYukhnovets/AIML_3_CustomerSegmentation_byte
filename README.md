# Customer Segmentation Using K-Means

The project uses K-Means clustering to group customers based on their age, annual income and spending behaviour. It also automatically identifies the customer segment with the highest average Spending Score and generates a targeted marketing brief for that group.

## Dataset

The project uses the Mall Customer Segmentation dataset from Kaggle.

The dataset contains:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

The dataset was checked for missing values and duplicate records before clustering.

## Features Used

The K-Means model uses:

- Age
- Annual Income
- Spending Score

Gender was not included in the clustering features.

## Choosing the Number of Clusters

The Elbow Method and Silhouette Score were used to compare different values of k.

The highest Silhouette Score was achieved with:

- k = 6
- Silhouette Score = 0.428

Therefore, six clusters were selected for the final model.

## Highest-Spending Segment

Cluster 3 was identified as the segment with the highest average Spending Score.

Its approximate profile is:

- Customers: 39
- Average Age: 32.69
- Average Annual Income: $86.54k
- Average Spending Score: 82.13/100

This segment is used as the target for the generated marketing recommendations.

## Marketing Recommendations

1. Promote premium and higher-value products.
2. Offer loyalty rewards and exclusive discounts.
3. Use personalised marketing campaigns and targeted offers.

## Streamlit Dashboard

A Streamlit dashboard was created to display the customer segments, cluster statistics, visualisation and targeted marketing recommendations.

## Technologies

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit
- Jupyter Notebook

## Project Structure

- `customer_segmentation.ipynb` - data analysis and K-Means clustering
- `app.py` - Streamlit dashboard
- `data/` - customer dataset
- `images/` - clustering and evaluation visualisations
- `examples/` - dataset sample, centroids, cluster profiles and marketing brief

## Run the Project

Install the required packages:

```bash
pip install -r requirements.txt