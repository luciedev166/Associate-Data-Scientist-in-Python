# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

duration_series = netflix_df.loc[
    (netflix_df["type"]=="Movie") &
    (netflix_df["release_year"]>=1990) &
    (netflix_df["release_year"]< 2000),
    "duration"
]

duration = int(duration_series.mode()[0])
print(duration)

short_movie_series = netflix_df.loc[
    (netflix_df["type"]=="Movie") &
    (netflix_df["genre"]=="Action") &
    (netflix_df["release_year"]>=1990) &
    (netflix_df["release_year"]< 2000) &
    (netflix_df["duration"]< 90),
    "show_id"
]
short_movie_count = len(short_movie_series)
print(short_movie_count)