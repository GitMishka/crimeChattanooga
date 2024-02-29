import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Booking Records - BookingDataAnon.csv')
df['DATE'] = pd.to_datetime(df['DATE'])
df['day'] = df['DATE'].dt.day_name()
df['month'] =df['DATE'].dt.month_name()
df['year'] = df['DATE'].dt.year

#df.head(10).to_csv('visualsSample.csv')


df['DATE'] = pd.to_datetime(df['DATE'])

df.set_index('DATE', inplace=True)

monthly_crimes = df.resample('M').size()

plt.figure(figsize=(10, 6))
monthly_crimes.plot(kind='line', marker='o', linestyle='-')
plt.title('Crime Trend Over Time (Monthly)')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.grid(True)
plt.tight_layout()
plt.show()