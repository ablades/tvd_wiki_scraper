# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
from bs4 import BeautifulSoup
import requests

def soupify():
    with open('table.html', 'r') as f:
            words = f.read()

    html = words

    soup = BeautifulSoup(html)

    transcripts_urls = list()

    #get all urls
    for a in soup.find_all('a', href=True):
        transcripts_urls.append(a['href'])

    return transcripts_urls

def get_transcripts(transcripts_urls):

    #loop through all transcript urls
    episode_count = 0
    for transcript in transcripts_urls:
        episode_count += 1
        r = requests.get(f'https://vampirediaries.fandom.com{transcript}')

        #write webpage to html file
        with open(f"Episode-{episode_count}.html", 'w+') as f:
            f.write(r.text)




if __name__ == "__main__":
    transcripts_urls = soupify()

    get_transcripts(transcripts_urls)
