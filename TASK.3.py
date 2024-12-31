#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset 
data = pd.read_csv('AccidentsBig .csv')
data
# Display dataset
print("Dataset Information:")
print(data.info())
print(data.head())

# Checking missing values
print("\nMissing Values:")
print(data.isnull().sum())

# data preprocessing (ensure your data variable is defined)
road_condition_counts = data['Road_Surface_Conditions'].value_counts()


# In[26]:


# Map numerical values to alternative road surface condition names
road_condition_mapping = {
    1: 'Smooth & Dry',
    2: 'Wet & Slippery',
    3: 'Snow-Covered',
    4: 'Icy & Dangerous',
    5: 'Mud-Covered',
    6: 'Flooded Roads',
    7: 'Oily Surface',
    8: 'Unknown/Other'
}

# Replace numerical values with descriptive names
data['Road_Surface_Conditions'] = data['Road_Surface_Conditions'].replace(road_condition_mapping)

# Data preprocessing (ensure your data variable is defined)
road_condition_counts = data['Road_Surface_Conditions'].value_counts()

# Barplot
plt.figure(figsize=(14, 8))  # Increased figure size for better readability
sorted_counts = road_condition_counts.sort_values(ascending=False)  # Sort for clarity

sns.barplot(x=sorted_counts.index, y=sorted_counts.values, palette='coolwarm')

# Data labels
for i, value in enumerate(sorted_counts.values):
    plt.text(i, value + 0.02 * max(sorted_counts.values), f'{value}', ha='center', fontsize=10)

# Title and labels
plt.title('Number of Accidents by Road Surface Condition', fontsize=16, weight='bold')
plt.xlabel('Road Surface Condition', fontsize=14)
plt.ylabel('Number of Accidents', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=12)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot
plt.tight_layout()
plt.show()


# In[27]:


# Map numerical values to weather condition names
weather_mapping = {
    1: 'Clear',
    2: 'Cloudy',
    3: 'Rainy',
    4: 'Snowy',
    5: 'Foggy',
    6: 'Windy',
    7: 'Stormy',
    8: 'Hail',
    9: 'Other'
}

# Replace numerical values with descriptive names
data['Weather_Conditions'] = data['Weather_Conditions'].replace(weather_mapping)

# Count occurrences and calculate percentages
weather_counts = data['Weather_Conditions'].value_counts()
weather_percentages = (weather_counts / weather_counts.sum()) * 100

# Sort values for clarity
sorted_counts = weather_counts.sort_values(ascending=False)
sorted_percentages = weather_percentages.loc[sorted_counts.index]

# Create the barplot
plt.figure(figsize=(12, 7))
sns.barplot(x=sorted_counts.index, y=sorted_counts.values, palette='Blues_d')

# Add data labels for counts
for i, (count, pct) in enumerate(zip(sorted_counts.values, sorted_percentages.values)):
    plt.text(i, count + 0.02 * max(sorted_counts.values), f'{count} ({pct:.1f}%)', 
             ha='center', fontsize=10)

# Add title and axis labels
plt.title('Impact of Weather Conditions on Accidents', fontsize=16, weight='bold')
plt.xlabel('Weather Conditions', fontsize=14)
plt.ylabel('Number of Accidents', fontsize=14)

# Improve axis readability
plt.xticks(rotation=45, fontsize=12)

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Optimize plot layout
plt.tight_layout()

# Final plot
plt.show()


# # Time Parsing and Data Cleaning for Accident Data :
# This code snippet performs the following steps :
# 1 Explicit Time Parsing:
# 2 Identifying Invalid Time Entries:
# 3 Dropping Invalid Entries:
# 4 Extracting Hour:
# 5 Final Data checking 

# In[31]:


# Explicitly specify the format for parsing the 'Time' column
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M', errors='coerce')

# Check for rows where parsing failed
invalid_times = data[data['Time'].isna()]
print("Rows with invalid time values:")
print(invalid_times)

# Drop rows with invalid time values (optional)
data = data.dropna(subset=['Time'])

# Extract the hour (assuming 'Time' is now valid)
data['hour'] = data['Time'].dt.hour

# Final check
print("Data after cleaning:")
print(data.head())
print(data['Time'].unique())


# In[37]:


hourly_accidents = data['hour'].value_counts().sort_index()
sns.set(style="whitegrid", palette="muted")
plt.figure(figsize=(12, 7))

sns.lineplot(x=hourly_accidents.index, y=hourly_accidents.values, marker='o', color='darkblue', linewidth=2.5)
plt.title('Accidents by Hour of the Day', fontsize=18, fontweight='bold', color='darkslategray')
plt.xlabel('Hour of the Day', fontsize=14, fontweight='bold', color='dimgray')
plt.ylabel('Number of Accidents', fontsize=14, fontweight='bold', color='dimgray')

# Add data labels
for i, value in enumerate(hourly_accidents.values):
    plt.text(hourly_accidents.index[i], value + 1, str(value), ha='center', va='bottom', fontsize=12, color='darkblue')

plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Improve axis and tick marks
plt.xticks(fontsize=12, rotation=45, ha='right')
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()


# In[ ]:




