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

def minimize():
    "transcript_webpages/Episode-1.html"
    #take all html files 
    for i in range(1,172):

        #get path for file
        path = f"transcript_webpages/Episode-{i}.html"
        print(path)

        #format file
        soup = BeautifulSoup(open(path), "html.parser")
        content = soup.find(id="WikiaMainContent")

        with open(path, 'w') as f:
            f.write(str(content))

        #get all urls
        #print(soup)





if __name__ == "__main__":
    #transcripts_urls = soupify()

    #minimize()

    #get_transcripts(transcripts_urls)
