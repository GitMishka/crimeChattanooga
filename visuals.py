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

crime_categories = {
    'Aggravated Assault': 'Violent Crimes',
    'Domestic Assault': 'Violent Crimes',
    'Rape': 'Sexual Crimes',
    'Robbery': 'Violent Crimes',
    'Burglary': 'Property Crimes',
    'Theft of Property (Under $1,000)': 'Property Crimes',
    'Theft of Property (Over $1,000)': 'Property Crimes',
    'Theft of Property (Over $2,500)': 'Property Crimes',
    'Theft of Property (Motor Vehicle)': 'Property Crimes',
    'Vandalism/Malicious Mischief': 'Property Crimes',
    'Arson': 'Property Crimes',
    'Possession of Controlled Substance': 'Drug-Related Crimes',
    'Possession of Drug Paraphernalia': 'Drug-Related Crimes',
    'Possession of Controlled Substance for Resale (Schedule 1)': 'Drug-Related Crimes',
    'Possession of Controlled Substance for Resale (Schedule 2)': 'Drug-Related Crimes',
    'Manufacturing of Meth': 'Drug-Related Crimes',
    'Driving Under the Influence': 'Traffic and Vehicle-Related Crimes',
    'Reckless Driving': 'Traffic and Vehicle-Related Crimes',
    'Driving on Revoked, Suspended, or Canceled License': 'Traffic and Vehicle-Related Crimes',
    'Speeding': 'Traffic and Vehicle-Related Crimes',
    'Leaving the Scene of an Accident': 