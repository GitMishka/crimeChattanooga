import pandas as pd
df = pd.read_csv('Booking Records - BookingDataAnon.csv')
df['DATE'] = pd.to_datetime(df['DATE'])

df['day'] = df['DATE'].dt.day_name()
df['month'] =df['DATE'].dt.month_name()
df['year'] = df['DATE'].dt.year

#print(df.head(100))

df['DATE'] = pd.to_datetime(df['DATE']).dt.date  
crime_counts = df.groupby(['DATE', 'CITY']).size().reset_index(name='counts')
pivot_table = crime_counts.pivot("DATE", "CITY", "counts")
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap="YlGnBu", annot=False, linewidths=.5)
plt.title('Crime Frequency Heatmap')
plt.xlabel('CITY')
plt.ylabel('DATE')
plt.show()



grouped = df.groupby(['year','month','day'])

result = grouped.size().reset_index(name='counts')
#print(result)

import matplotlib.pyplot as plt
plt.figure(figsize=(12, 7))  
plt.bar(result['day'], result['counts'], color='royalblue')

plt.title('Aggregated Data Over Time')
plt.xlabel('Date')
plt.ylabel('Counts')  
plt.xticks(rotation=45)  


plt.tight_layout()  
plt.show()

# df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y')

# crime_counts_by_zip_and_time = df.groupby([df['ZIP_CODE'], df['DATE'].dt.to_period("M")]).size().reset_index(name='Count')

# print(crime_counts_by_zip_and_time)
