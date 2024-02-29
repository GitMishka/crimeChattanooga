import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('categorized.csv')
df['DATE'] = pd.to_datetime(df['DATE'])
df['day'] = df['DATE'].dt.day_name()
df['month'] =df['DATE'].dt.month_name()
df['year'] = df['DATE'].dt.year


df['DATE'] = pd.to_datetime(df['DATE'])

df['YEAR_MONTH'] = df['DATE'].dt.to_period('M')

monthly_trends = df.groupby(['CRIME_CATEGORY', 'YEAR_MONTH']).size().unstack(fill_value=0).T

plt.figure(figsize=(14, 8))
for category in monthly_trends.columns:
    plt.plot(monthly_trends.index.to_timestamp(), monthly_trends[category], label=category)

plt.title('Crime Category Trends Over Time (Monthly Basis)')
plt.xlabel('Date')
plt.ylabel('Incidents Count')
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

plt.show()
