import lxml
import bs4
import requests

query = input("Search: ")
r = requests.get("https///sexhd.pics/gallery/{query}")
soup = bs4.BeautifulSoup(r.text, "lxml")
div = soup.find("div", class_="photo1")
for pics in div.find_all("img"):
    pic = "https://sexhd.pics" + pics['src']
    print(pic)
