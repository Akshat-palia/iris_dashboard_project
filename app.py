import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('iris')

# Title
st.title("🌸 Iris Dataset Explorer")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Sidebar filters
species = st.sidebar.multiselect("Select species", options=df["species"].unique(), default=df["species"].unique())

# Filtered dataframe
filtered_df = df[df["species"].isin(species)]

# Summary
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# Plot
st.subheader("Petal Length vs Petal Width")
fig, ax = plt.subplots()
for s in filtered_df['species'].unique():
    subset = filtered_df[filtered_df['species'] == s]
    ax.scatter(subset['petal_length'], subset['petal_width'], label=s)
ax.set_xlabel("Petal Length")
ax.set_ylabel("Petal Width")
ax.legend()
st.pyplot(fig)
