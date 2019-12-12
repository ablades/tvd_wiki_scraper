# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
from bs4 import BeautifulSoup

def soupify():
    with open('table.html', 'r') as f:
            words = f.read()

    html = words

    soup = BeautifulSoup(html)

    transcripts_urls = list()

    #get all urls
    for a in soup.find_all('a', href=True):
        print ("Found the URL:", a['href'])
        transcripts_urls.append(a['href'])

    return transcripts_urls


if __name__ == "__main__":
    print(soupify())
