from bs4 import BeautifulSoup
from urllib2 import urlopen
import logging

BASE_URL = "https://marinas.com/browse/marinas/us/TN/"

def get_category_links(section_url):
    html = urlopen(BASE_URL).read()
    console.log("please print\n")
    soup = BeautifulSoup(html, "lxml")
    boccat = soup.find("dl", "boccat")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links
