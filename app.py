import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal median Housing Price', 0, 500001, 200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# Create a radio button for filtering by median income level
income_level = st.sidebar.radio(
    "Select income level:",
    ('Low ', 'Medium', 'High')
)

# Filter the dataframe based on the selected income level
if income_level == 'Low (≤2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]



# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low (≤2.5)':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium (> 2.5 & < 4.5)':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] > 4.5]


# show on map
st.map(df)
# Display a subheader for the histogram
st.subheader('Median House Value')

# Create a histogram for median house value with 30 bins
fig, ax = plt.subplots(figsize=(20, 20))
ax.hist(filtered_df['median_house_value'], bins=30)

# Set title, labels, and y-axis limits
ax.set_title('Histogram of Median House Value', fontsize=16)
ax.set_xlabel('Median House Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)


# Display the histogram
st.pyplot(fig)