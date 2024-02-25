import pandas as pd
df = pd.read_csv('Booking Records - BookingDataAnon.csv')

df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y')

crime_counts_by_zip_and_time = df.groupby([df['ZIP_CODE'], df['DATE'].dt.to_period("M")]).size().reset_index(name='Count')

print(crime_counts_by_zip_and_time)
