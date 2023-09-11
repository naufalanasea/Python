import pandas as pd

# Create a list of movies
movies = ["Suzanna", "The Raid Redemption", "Spiderman : Accross the Spider Verse", "Assalamu'alaikum Beijing", "Rush"]

# Create a list of genres
genres = ["Horror", "Action", "Sci-fi", "Romance", "Action"]

# Create a list of release dates
release_dates = [2023, 2011, 2023, 2011, 2013]

# Create a list of ratings
ratings = [8.7, 9.1, 8.6, 8.1, 9.5]

# Create a DataFrame
df = pd.DataFrame({
    "movie_id": range(len(movies)),
    "title": movies,
    "genre": genres,
    "release_date": release_dates,
    "rating": ratings
})

# Save the DataFrame to a CSV file
df.to_csv("movie.csv", index=False)