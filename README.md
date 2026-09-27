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

Live demo: https://aiml3customersegmentationbyte-nezca5jbnsokundvhnrruf.streamlit.app/

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

## Customer Segment Profiles

- **Cluster 0 – Older, Mid-Income, Moderate-Spending:** 45 customers with an average age of 56.33, average income of $54.27k and average Spending Score of 49.07.

- **Cluster 1 – Younger, Mid-Income, Moderate-Spending:** 39 customers with an average age of 26.79, average income of $57.10k and average Spending Score of 48.13.

- **Cluster 2 – High-Income, Low-Spending:** 33 customers with an average age of 41.94, average income of $88.94k and average Spending Score of 16.97.

- **Cluster 3 – High-Income, High-Spending:** 39 customers with an average age of 32.69, average income of $86.54k and average Spending Score of 82.13. This is the main target segment for premium upselling.

- **Cluster 4 – Young, Lower-Income, High-Spending:** 23 customers with an average age of 25.00, average income of $25.26k and average Spending Score of 77.61.

- **Cluster 5 – Older, Lower-Income, Low-Spending:** 21 customers with an average age of 45.52, average income of $26.29k and average Spending Score of 19.38.

## Run the Project

Install the required packages:

```bash
pip install -r requirements.txt