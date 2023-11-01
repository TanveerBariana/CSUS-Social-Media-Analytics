import pandas as pd

# Read the Q1_part1.csv and Q1_part2.csv files into DataFrames
q1_part1_df = pd.read_csv("Q1_part1.csv")
q1_part2_df = pd.read_csv("Q1_part2.csv")

# Define the columns
columns_to_average = ['acousticness', 'danceability', 'energy', 'instrumentalness',
                       'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity']

# Calculate column-wise averages for both DataFrames
q1_part1_averages = q1_part1_df[columns_to_average].mean()
q1_part2_averages = q1_part2_df[columns_to_average].mean()

# Create a DataFrame with the desired structure
q1_stats_df = pd.DataFrame({
    'Feature': columns_to_average,
    'Q1 Part 1 Averages': q1_part1_averages,
    'Q1 Part 2 Averages': q1_part2_averages
})

# Write the combined DataFrame to Q1_stats.csv
q1_stats_df.to_csv("Q1_stats.csv", index=False)

print("done.")