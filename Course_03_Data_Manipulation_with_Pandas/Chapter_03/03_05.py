# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc["Pakistan": "Philippines"])

# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc["Lahore": "Manila"])

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[("Pakistan", "Lahore"): ("Philippines", "Manila")])
