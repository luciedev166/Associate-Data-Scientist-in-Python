# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 1000]

# See the result
print(ind_gt_10k)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[
    (homelessness["region"] == "Pacific") &
    (homelessness['family_members'] < 1000)
    ]

# See the result
print(fam_lt_1k_pac)