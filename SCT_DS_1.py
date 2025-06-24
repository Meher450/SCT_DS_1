import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# PART 1: Load and process numeric data (e.g., Life Expectancy)
# ------------------------------

# Load dataset (Replace with your actual file path)
df = pd.read_excel("D:/LPU/Offer Letter/SCT/SCT_DS_1.xls")  # e.g., 'World_Bank_Data.csv'

# Filter out non-country rows (optional, based on 'Country Code')
df = df[df['Country Code'].str.len() == 3]

# Get list of years as strings from 1960 to 2023
years = [str(year) for year in range(1960, 2024, 10)]  # Every 10 years to avoid clutter

# Setup subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 12))
axes = axes.flatten()

for i, year in enumerate(years):
    if year in df.columns:
        data = df[year].dropna()
        axes[i].hist(data, bins=30, color='skyblue', edgecolor='black')
        axes[i].set_title(f'Population Distribution in {year}')
        axes[i].set_xlabel('Population')
        axes[i].set_ylabel('Number of Countries')

# Adjust layout
plt.tight_layout()
plt.suptitle("Population Distribution from 1960 to 2023 (Every 10 Years)", fontsize=16, y=1.02)
plt.show()

# ------------------------------
# PART 2: Bar chart for categorical variable (e.g., Gender Distribution)
# ------------------------------

# Example dummy categorical data (for gender)
gender_data = pd.DataFrame({
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Female", "Male",
               "Male", "Female", "Female", "Female", "Male", "Female"]
})

# Plot bar chart
plt.figure(figsize=(6, 4))
sns.countplot(data=gender_data, x="Gender", palette="pastel")
plt.title("Gender Distribution (Example)")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()