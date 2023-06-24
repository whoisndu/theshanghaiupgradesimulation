

## We featured engineered the data to derive the cumulative sum of Ethereum tokens deposited by each address weekly. The snippet below shows this task.


import pandas as pd
# import the data table
df = pd.read_csv(r"All Deposits and Time Filepath")
# convert the "time" column to datetime
df["time"] = pd.to_datetime(df["time"])
# pivot the data to get the weekly sums per depositor
df_pivot = df.pivot_table(values="deposited_eth", index="addresses",
columns="time", fill_value=0)
# calculate cumulative sum
cumulative_sum = df_pivot.cumsum(axis=1)
# fill in any NaN values with 0
cumulative_sum.fillna(0, inplace=True)
# export the results as a csv file
cumulative_sum.to_csv(r"Weekly Cumulative Deposits")
The result of the above query returns the ‘Weekly Cumulative Deposits’ dataset.
Using the ‘Weekly Cumulative Deposits’ and ‘Rewards per Week’ datasets, we could derive the
precise rewards each depositor earns weekly. The code snippet below shows this.
import pandas as pd
import numpy as np
# Read in the cumulative deposit data
cumulative_deposit_data = pd.read_csv(r"Weekly Cumulative Deposits
Filepath")
cumulative_deposit_data.columns = ['addresses'] + [f'week_{i}' for i in
range(len(cumulative_deposit_data.columns) - 1)]
# Read in the rewards per week data
rewards_per_week = pd.read_csv(r"Rewards per Week Filepath",
parse_dates=["time"], infer_datetime_format=True)
# Create a list of weekly dates to match with cumulative deposit data
week_dates = rewards_per_week['time'].values

## Calculating the Interests Earned

# Calculate the weekly interest earned for each depositor using vectorized
operations
interest_earned = np.multiply(cumulative_deposit_data.iloc[:,1:].values,
rewards_per_week['Weekly APR'].values)
# Create a dataframe to store the result
result = pd.DataFrame(interest_earned, columns=week_dates,
index=cumulative_deposit_data['addresses'])
# Export the result to a CSV file
result.to_csv(r"Depositor Reward per Week Filepath")

### The dataset returned (Depositor Reward per Week) contains the reward earned by each
depositor.