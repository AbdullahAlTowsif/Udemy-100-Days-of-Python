from bs4 import BeautifulSoup
with open("/Udemy/100 Days of Python/Day 45 Beautiful Soup/website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())


# h3_heading = soup.find_all("h3", class_ = "heading")
# print(h3_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

company_url = soup.select_one(selector="#name")
print(company_url)