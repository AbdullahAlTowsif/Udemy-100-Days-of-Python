import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]
# \Udemy\100 Days of Python\Day 45 Beautiful Soup\100 Greatest Movies

with open("/Udemy/100 Days of Python/Day 45 Beautiful Soup/100 Greatest Movies/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

