import pandas as pd
import numpy as np

data = {
    'Event': ['Meeting A', 'Project Deadline', 'Holiday', 'Birthday', 'Launch Event', 'Maintenance'],
    'Date_Time': pd.to_datetime([
        '2023-01-15 10:30:00',
        '2024-06-30 23:59:59',
        '2023-12-25 00:00:00',
        '2025-04-10 12:00:00',
        '2024-01-01 09:00:00',
        np.nan # Missing datetime value
    ]),
    'Value': [10, 20, 5, 15, 25, 30]
}
df = pd.DataFrame(data)
print(df)

df['Year'] = df['Date_Time'].dt.year
df['Month'] = df['Date_Time'].dt.month  
df['Day'] = df['Date_Time'].dt.day
df['Hour'] = df['Date_Time'].dt.hour
df['Minute'] = df['Date_Time'].dt.minute
df['Second'] = df['Date_Time'].dt.second
df['day of week'] = df['Date_Time'].dt.dayofweek
print(df)

df_yearly_summary = df.groupby(df['Date_Time'].dt.year)['Value'].sum().reset_index()
df_yearly_summary = df_yearly_summary.rename(columns={'Date_Time': 'Year'}) # Rename the grouped column
print(df_yearly_summary)
print(pd.Timestamp.now().year)