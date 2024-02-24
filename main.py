import pandas as pd
df = pd.read_csv('Booking Records - BookingDataAnon.csv')
sample_df = df.head(10)
sample_df.to_csv('sample_df.csv')