import pandas as pd

# Read the data from the CSV file into a DataFrame
df = pd.read_csv(".\\data\\AMUB_temp.TXT")

# Convert the 'Datetime' column to datetime objects
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Extract date and time components
df['Date'] = df['Datetime'].dt.date
df['Time'] = df['Datetime'].dt.time

# Group the data by date and find the high and low of the day
daily_high_low = df.groupby('Date').agg({'High': 'max', 'Low': 'min'})

# Find the corresponding times for the high and low
high_times = df.loc[df.groupby('Date')['High'].idxmax()]['Time']
low_times = df.loc[df.groupby('Date')['Low'].idxmin()]['Time']

# Combine the results into a new DataFrame
result_df = pd.DataFrame({
    'Date': daily_high_low.index,
    'High': daily_high_low['High'],
    'High_Time': high_times.values,
    'Low': daily_high_low['Low'],
    'Low_Time': low_times.values
})

print(result_df)