import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast


# Open the dataset
url = 'film_analysis/movies_metadata.csv'
movies_df = pd.read_csv(url)

# Output infos about the dataset
# movies_df.info()
# print(movies_df.head())
# print(movies_df.describe())

#---------

def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre['name'] for genre in genres]
    except ValueError:
        return []


movies_df['genres'] = movies_df['genres'].apply(extract_genres)
# print(movies_df['genres'])

#---------

movies_df['budget'] = pd.to_numeric(movies_df['budget'], errors='coerce')
movies_df['revenue'] = pd.to_numeric(movies_df['revenue'], errors='coerce')

movies_df.dropna(subset=['budget', 'revenue'], inplace=True)

# print(movies_df['budget'])
# print(movies_df['revenue'])

#---------

# print(movies_df['release_date'])
movies_df['release_year'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
# print(movies_df['release_year'])

#---------

movies_df['runtime'] = pd.to_numeric(movies_df['runtime'], errors='coerce')
# print(movies_df['runtime'])

#---------

genres_exploded = movies_df[['title', 'release_year', 'budget', 'revenue', 'genres']].explode('genres')
print(genres_exploded)

genre_count = genres_exploded['genres'].value_counts()
print(genre_count)

# Visualization of genres
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_count.index, y=genre_count.values)
plt.title('Number of movies by genre')
plt.xlabel('Genre')
plt.ylabel('Number of movies')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

#---------

movies_df['popularity'] = pd.to_numeric(movies_df['popularity'], errors='coerce')
popularity_trend = movies_df.groupby('release_year')['popularity'].mean()

# Visualization trends of popularity

plt.figure(figsize=(12, 6))
popularity_trend.plot()
plt.title('Average movies popularity by years')
plt.xlabel('Year')
plt.ylabel('Popularity')
# plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


