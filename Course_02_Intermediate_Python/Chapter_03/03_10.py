# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print sel
print(cars[cars['drives_right']])