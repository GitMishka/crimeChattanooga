import pandas as pd
df = pd.read_csv('Booking Records - BookingDataAnon.csv')

crimeTypes_nun = df['PRIMARY_CHARGE'].nunique()
crimeTypes_un = df['PRIMARY_CHARGE'].unique()


print(crimeTypes_nun)
print(crimeTypes_un)

import pandas as pd
import numpy as np


df = pd.DataFrame(crimeTypes_un)

df.to_csv('crimeTypes_un.csv', index=False)  
