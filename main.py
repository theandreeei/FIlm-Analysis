import pandas as pd
import matplotlib.pyplot as plt
import seaborn


# Open the dataset
url = 'film_analysis/movies_metadata.csv'
movies_df = pd.read_csv(url)

# Output infos about the dataset
movies_df.info()
print(movies_df.head())
print(movies_df.describe())




