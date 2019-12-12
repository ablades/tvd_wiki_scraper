# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

# website urls
base_url = "https://vampirediaries.fandom.com/wiki/Category:Episode_Transcripts"
#episode_url
driver = webdriver.Opera()
driver.get(videos_url)
driver.implicitly_wait(100)

//*[@id="mw-content-text"]/small[1]/i/table