#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the CSV file
df = pd.read_csv("WellDates.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows missing date or depth
df = df.dropna(subset=['Date', 'Depth To Water (Decimal Feet)'])

# Extract year from date
df['Year'] = df['Date'].dt.year

# Group by year and calculate average depth
yearly_avg = df.groupby('Year')['Depth To Water (Decimal Feet)'].mean()

# Get the 10 years with the highest (deepest) average depth
top_10 = yearly_avg.sort_values(ascending=False).head(10)

# PRINT the results instead of saving
print("📊 Top 10 Years with Highest Average Depth to Water (ft):")
print(top_10)



# In[2]:


import pandas as pd

# Load the CSV
df = pd.read_csv("WellDates.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows missing date or depth
df = df.dropna(subset=['Date', 'Depth To Water (Decimal Feet)'])

# Extract the year
df['Year'] = df['Date'].dt.year

# Group by year and calculate average depth
yearly_avg = df.groupby('Year')['Depth To Water (Decimal Feet)'].mean()

# Force pandas to display ALL rows (important part!)
pd.set_option('display.max_rows', None)

# Print all years and averages
print("📈 Average Depth to Water for Each Year:")
print(yearly_avg)



# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("WellDates.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows missing date or depth
df = df.dropna(subset=['Date', 'Depth To Water (Decimal Feet)'])

# Extract the year
df['Year'] = df['Date'].dt.year

# Group by year and calculate average depth
yearly_avg = df.groupby('Year')['Depth To Water (Decimal Feet)'].mean()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', linestyle='-', color='royalblue')
plt.title('Average Depth to Water by Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Depth to Water (ft)', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Load the CSV
df = pd.read_csv("WellDates.csv")
df.columns = df.columns.str.strip()

# Parse dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date', 'Depth To Water (Decimal Feet)'])

# Extract year
df['Year'] = df['Date'].dt.year

# Group by year and calculate average depth
yearly_avg = df.groupby('Year')['Depth To Water (Decimal Feet)'].mean()

# Smooth the average using Savitzky-Golay filter to find the trend
smooth_trend = savgol_filter(yearly_avg.values, window_length=11, polyorder=2)

# Detrend: subtract the smooth trend from the original data
residuals = yearly_avg.values - smooth_trend

# Plot the detrended residuals
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg.index, residuals, marker='o', linestyle='-', color='mediumvioletred')
plt.axhline(0, color='gray', linestyle='--', alpha=0.7)
plt.title('Detrended Water Level Oscillations (Yearly Average)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Deviation from Trend (ft)', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("WellDates.csv")
df.columns = df.columns.str.strip()

# Parse dates and clean data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date', 'Depth To Water (Decimal Feet)'])

# Extract year and calculate average depth per year
df['Year'] = df['Date'].dt.year
yearly_avg = df.groupby('Year')['Depth To Water (Decimal Feet)'].mean()

# Sort values to form a distribution curve
sorted_depths = np.sort(yearly_avg.values)
percentiles = np.linspace(0, 100, len(sorted_depths))

# Calculate 5th and 95th percentile values
bottom_percentile = 5
top_percentile = 95
bottom_value = np.percentile(sorted_depths, bottom_percentile)
top_value = np.percentile(sorted_depths, top_percentile)

# Plot the distribution curve
plt.figure(figsize=(12, 6))
plt.plot(percentiles, sorted_depths, color='royalblue', linewidth=2, label='Depth Distribution')

# Highlight 5th and 95th percentiles
plt.axhline(bottom_value, color='green', linestyle='--', linewidth=2, label=f'{bottom_percentile}th Percentile ({bottom_value:.2f} ft)')
plt.axhline(top_value, color='red', linestyle='--', linewidth=2, label=f'{top_percentile}th Percentile ({top_value:.2f} ft)')

# Formatting
plt.title('Water Depth Distribution with 5th and 95th Percentiles', fontsize=16)
plt.xlabel('Percentile', fontsize=14)
plt.ylabel('Average Depth to Water (ft)', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# Print values
print(f"{bottom_percentile}th percentile depth: {bottom_value:.2f} ft")
print(f"{top_percentile}th percentile depth: {top_value:.2f} ft")


# In[ ]:





# In[6]:


import pandas as pd

# Load the data
df = pd.read_excel("well depths .xlsx")

# Make sure Date is datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Extract the year
df['Year'] = df['Date'].dt.year

# Group by year and find maximum depth
yearly_max_depth = df.groupby('Year')['Depth to Water'].max().reset_index()

# Sort by depth descending
yearly_max_depth_sorted = yearly_max_depth.sort_values(by='Depth to Water', ascending=False)

# Display top 10 years
print("Top 10 Years with Deepest Waterline (Depth to Water):")
print(yearly_max_depth_sorted.head(10))

# (Optional) Save it to Excel
yearly_max_depth_sorted.to_excel("highest_waterline_depth_by_year.xlsx", index=False)


# In[7]:


import pandas as pd

# Load the data
df = pd.read_excel("well depths .xlsx")

# Make sure Date is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Extract year
df['Year'] = df['Date'].dt.year

# Group by year and find the minimum depth
yearly_min_depth = df.groupby('Year')['Depth to Water'].min().reset_index()

# Sort by shallowest depth (ascending)
yearly_min_depth_sorted = yearly_min_depth.sort_values(by='Depth to Water', ascending=True)

# Display top 10 years
print("Top 10 Years with Shallowest Waterline (Depth to Water):")
print(yearly_min_depth_sorted.head(10))

# (Optional) Save to Excel
yearly_min_depth_sorted.to_excel("shallowest_waterline_depth_by_year.xlsx", index=False)


# In[2]:


# Cell 1: Imports
import pandas as pd
import matplotlib.pyplot as plt
# Cell 2: Load the consolidated CSV
# (Adjust path if your file is elsewhere)
df = pd.read_csv('parameter_22_concentrations.csv', parse_dates=['Date'])
# Cell 3: Sort by date (and inspect)
df = df.sort_values('Date')
df.head()
# Cell 4: Plot concentration vs. time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Parameter 22 Concentration'], label='Parameter 22')
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('Parameter 22 Concentration Over Time')
plt.legend()
plt.tight_layout()
plt.show()


# In[3]:


# Cell 3: Compute daily average (group by exact date)
daily_avg = df.groupby('Date')['Parameter 22 Concentration'].mean().reset_index()
daily_avg.head()
# Cell 4: Plot daily average concentration over time
plt.figure(figsize=(12, 6))
plt.plot(daily_avg['Date'], daily_avg['Parameter 22 Concentration'], label='Daily Average')
plt.xlabel('Date')
plt.ylabel('Average Concentration')
plt.title('Daily Average of Parameter 22 Concentration Over Time')
plt.legend()
plt.tight_layout()
plt.show()


# In[4]:


# Cell 3: Extract just the concentration values
values = df['Parameter 22 Concentration'].dropna()
# Cell 4: Plot the distribution histogram
plt.figure(figsize=(10, 6))
plt.hist(values, bins=30, density=True)      # density=True normalizes to a PDF
plt.xlabel('Parameter 22 Concentration')
plt.ylabel('Density')
plt.title('Distribution of Parameter 22 Concentrations')
plt.tight_layout()
plt.show()


# In[7]:


# Cell 3: Extract just the concentration values
values = df['Parameter 22 Concentration'].dropna()
# Cell 4: Plot the distribution histogram
plt.figure(figsize=(10, 6))
plt.hist(values, bins=30, density=True)      # density=True normalizes the histogram to a PDF
plt.xlabel('Parameter 22 Concentration')
plt.ylabel('Density')
plt.title('Distribution of Parameter 22 Concentrations')
plt.tight_layout()
plt.show()



# In[9]:


# Jupyter Notebook: Daily Standard Deviation of Parameter 22 with Percentiles

# Cell 1: Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cell 2: Load consolidated data
df = pd.read_csv('parameter_22_concentrations.csv', parse_dates=['Date'])

# Cell 3: Compute daily standard deviation
daily_std = (
    df
    .groupby('Date')['Parameter 22 Concentration']
    .std()
    .reset_index(name='std_dev')
)

# Cell 4: Calculate 5th and 95th percentiles of the daily std dev values
p05, p95 = np.percentile(daily_std['std_dev'].dropna(), [5, 95])

# Cell 5: Plot daily std dev with percentile lines
plt.figure(figsize=(12, 6))
plt.plot(daily_std['Date'], daily_std['std_dev'], label='Daily Std Dev')
plt.axhline(p05, linestyle='--', linewidth=2, label=f'5th percentile ({p05:.2f})')
plt.axhline(p95, linestyle='--', linewidth=2, label=f'95th percentile ({p95:.2f})')
plt.xlabel('Date')
plt.ylabel('Standard Deviation')
plt.title('Daily Standard Deviation of Parameter 22 with 5th & 95th Percentiles')
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:




