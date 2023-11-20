import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Read the data from the CSV file into a DataFrame
    #df = pd.read_csv(".\\data\\AMUB_temp.TXT")
    df = pd.read_csv("f:\\Market_data\\eod_intraday_data_nasdaq_done\\AAPL_temp.TXT")

    # Convert the 'Datetime' column to datetime objects
    df['Datetime'] = pd.to_datetime(df['Datetime'])

    # Extract date and time components
    df['Date'] = df['Datetime'].dt.date
    df['Time'] = df['Datetime'].dt.time
    df_filtered = df[(df['Time'] >= pd.to_datetime('6:30').time()) & (df['Time'] <= pd.to_datetime('13:00').time())]

    # Group the data by date and find the high and low of the day
    daily_high_low = df_filtered.groupby('Date').agg({'High': 'max', 'Low': 'min'})

    # Find the corresponding times for the high and low
    high_times = df_filtered.loc[df_filtered.groupby('Date')['High'].idxmax()]['Time']
    low_times = df_filtered.loc[df_filtered.groupby('Date')['Low'].idxmin()]['Time']
    high_times_float = high_times.apply(lambda x: x.hour + x.minute / 60)

    # Combine the results into a new DataFrame
    result_df = pd.DataFrame({
        'Date': daily_high_low.index,
        'High': daily_high_low['High'],
        'High_Time': high_times.values,
        'Low': daily_high_low['Low'],
        'Low_Time': low_times.values
    })

    #print(result_df)

    # Create a distribution map for high times
    plt.figure(figsize=(12, 6))
    plt.hist(high_times_float, bins = 26, edgecolor='black')
    #plt.plot(high_times_float, marker='o', linestyle='-')
    plt.title('Distribution of High Times')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()

if __name__=="__main__":
    main()