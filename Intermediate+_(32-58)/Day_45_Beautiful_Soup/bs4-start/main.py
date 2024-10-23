from bs4 import BeautifulSoup

with open("./Intermediate+_(32-58)/Day_45_Beautiful_Soup/bs4-start/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
## Prints entire title line: <title>Angela's Personal Site</title>
# print(soup.title)

## Prints name of title tag: title
# print(soup.title.name)

# # Prints content of title tag: Angela's Personal Site
# print(soup.title.string)

# # Indents html 'properly'
# print(soup.prettify())

# # Prints 1st 'a' tag in html file
# print(soup.a)

# Print all 'a' tags in a list
all_a_tags = soup.find_all(name="a")
# print(all_a_tags)

# for tag in all_a_tags:
    # # Print text of all 'a' tags
    # print(tag.getText())
    
    ## Get value of any attributes    
    # print(tag.get("href"))
    
heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

company_url = soup.select_one(selector="#name")
# print(company_url)

headings = soup.select(".heading")
# print(headings)