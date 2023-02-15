from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

all_movies = (soup.find_all(name="h3", class_="title"))

movies_titles = [movie.getText() for movie in all_movies]

movies = (movies_titles[::-1])

with open("movies.txt", "w") as file:
  for movie in movies:
    try:
      file.write(f"{movie}\n")
    except:
      continue