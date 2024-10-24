import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# Get the data and text from the URL
response = requests.get(URL)
web_page = response.text

# Create soup object and get the titles based on the webpages structure
soup = BeautifulSoup(web_page, "html.parser")
movie_data = soup.find_all(name="h3", class_="title")

# Create a list to hold the text from the h3 title tags
movie_titles = []
for movie in movie_data:
    title = movie.getText()
    #Attemp to fix : error for number 12 movie
    # title_clean = title.replace(":",")")
    movie_titles.append(title)

#Attemp to fix : error for number 12 movie
# print(movie_titles)
# movie_titles.sort()
# print(movie_titles)
# movie_titles_clean = movie_titles.replace(":",")")
# movie_number = [int(num.split(')')[0]) for num in movie_titles]
# [int(num.split()[0]) for num in movie_titles]
# print(movie_number)

# Reverse the order of the list so in numerical order (1,2,3...)
movie_titles.reverse()
# print(movie_titles)

# # Write the text file for the movie list. Stop from running every time
# with open("movies.txt", mode="w", encoding="utf-8") as file:
#     for movie in movie_titles:
#         file.write(f"{movie}\n")