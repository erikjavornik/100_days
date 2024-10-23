from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.find("a").get("href")
    # print(article_link)
    article_links.append(article_link)
    
# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(int(article_upvotes[0].split()[0]))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_upvotes_index = article_upvotes.index(max(article_upvotes))
# print(highest_upvotes)

print(f"Title of Article with the most upvotes: {article_texts[highest_upvotes_index]}")
print(f"Link to Article: {article_links[highest_upvotes_index]}")
