import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movie_data = soup.find_all(name="h3", class_="title")

movie_titles = []

for movie in movie_data:
    title = movie.getText()
    movie_titles.append(title)
    
# print(movie_titles)
# movie_titles.sort()
# print(movie_titles)

movie_number = []

