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
    # Violent Crimes
    'Aggravated Assault': 'Violent Crimes',
    'Domestic Assault': 'Violent Crimes',
    'Rape': 'Violent Crimes',
    'Robbery': 'Violent Crimes',
    'Aggravated Robbery': 'Violent Crimes',
    'Kidnapping': 'Violent Crimes',
    'Aggravated Kidnapping': 'Violent Crimes',
    'Murder': 'Violent Crimes',
    'Criminal Homicide': 'Violent Crimes',
    'Vehicular Homicide': 'Violent Crimes',
    'Aggravated Rape': 'Violent Crimes',
    'Sexual Battery': 'Violent Crimes',
    'Aggravated Sexual Battery': 'Violent Crimes',
    'Attempted First Degree Murder': 'Violent Crimes',
    'Second Degree Murder': 'Violent Crimes',
    'First Degree Murder': 'Violent Crimes',
    'Aggravated Child Rape': 'Violent Crimes',
    'Rape of a Child': 'Violent Crimes',
    'Aggravated Child Abuse': 'Violent Crimes',
    'Aggravated Sexual Exploitation of A Minor': 'Violent Crimes',
    'Sexual Exploitation of a Minor': 'Violent Crimes',
    'Aggravated Criminal Trespassing': 'Violent Crimes',
    'Assault': 'Violent Crimes',
    'Aggravated Burglary': 'Violent Crimes',
    'Criminal Attempt Homicide': 'Violent Crimes',
    'Felony Murder': 'Violent Crimes',
    'Voluntary Manslaughter': 'Violent Crimes',
    'Involuntary Manslaughter': 'Violent Crimes',
    'Justifiable Homicide': 'Violent Crimes',
    # Property Crimes
    'Burglary': 'Property Crimes',
    'Theft of Property': 'Property Crimes',
    'Arson': 'Property Crimes',
    'Vandalism/Malicious Mischief': 'Property Crimes',
    'Carjacking': 'Property Crimes',
    'Forgery': 'Property Crimes',
    'Fraudulent Use of Credit or Debit Card': 'Property Crimes',
    'Money Laundering': 'Property Crimes',
    'Identity Theft': 'Property Crimes',
    'Bribery': 'Property Crimes',
    'Extortion': 'Property Crimes',
    'Burglary of Vehicle': 'Property Crimes',
    'Embezzlement': 'Property Crimes',
    'Counterfeiting': 'Property Crimes',
    'Theft by Deception': 'Property Crimes',
    'Theft of Services': 'Property Crimes',
    'Unlawful Entry': 'Property Crimes',
    'Shoplifting': 'Property Crimes',
    'Vandalism': 'Property Crimes',
    # Drug-Related Crimes
    'Possession of Controlled Substance': 'Drug-Related Crimes',
    'Manufacturing of Controlled Substance': 'Drug-Related Crimes',
    'Drug Trafficking': 'Drug-Related Crimes',
    'Possession with Intent to Distribute': 'Drug-Related Crimes',
    'Drug Paraphernalia': 'Drug-Related Crimes',
    # Traffic and Vehicle-Related Crimes
    'Driving Under the Influence': 'Traffic and Vehicle-Related Crimes',
    'Reckless Driving': 'Traffic and Vehicle-Related Crimes',
    'Driving on Revoked, Suspended, or Canceled License': 'Traffic and Vehicle-Related Crimes',
    'Leaving the Scene of an Accident': 'Traffic and Vehicle-Related Crimes',
    'Unlawful Vehicle Modifications': 'Traffic and Vehicle-Related Crimes',
    'Vehicle Theft': 'Traffic and Vehicle-Related Crimes',
    'Hit and Run': 'Traffic and Vehicle-Related Crimes',
    'Evading Arrest': 'Traffic and Vehicle-Related Crimes',
    'Traffic Offenses': 'Traffic and Vehicle-Related Crimes',
    # Public Order Crimes
    'Disorderly Conduct': 'Public Order Crimes',
    'Public Intoxication': 'Public Order Crimes',
    'Disturbing the Peace': 'Public Order Crimes',
    'Trespassing': 'Public Order Crimes',
    'Loitering': 'Public Order Crimes',
    'Resisting Arrest': 'Public Order Crimes',
    'Obstruction of Justice': 'Public Order Crimes',
    'Rioting': 'Public Order Crimes',
    'Inciting a Riot': 'Public Order Crimes',
    'Public Indecency': 'Public Order Crimes',
    'Prostitution': 'Public Order Crimes',
    'Solicitation': 'Public Order Crimes',
    'Gambling': 'Public Order Crimes',
    'Illegal Assembly': 'Public Order Crimes',
    # Financial Crimes
    'Fraud': 'Financial Crimes',
    'Embezzlement': 'Financial Crimes',
    'Money Laundering': 'Financial Crimes',
    'Bribery': 'Financial Crimes',
    'Tax Evasion': 'Financial Crimes',
    'Insurance Fraud': 'Financial Crimes',
    'Securities Fraud': 'Financial Crimes',
    'Bank Fraud': 'Financial Crimes',
    'Welfare Fraud': 'Financial Crimes',
    'Credit Card Fraud': 'Financial Crimes',
}

def map_crime_to_category(crime):
    return crime_categories.get(crime, 'Other')

df['CRIME_CATEGORY'] = df['PRIMARY_CHARGE'].apply(map_crime_to_category)

df.head(10).to_csv('categorized.csv')