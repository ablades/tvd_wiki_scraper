# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import re
import os
from bs4 import BeautifulSoup
import requests
import glob

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


def minimize_again():
    "transcript_webpages/Episode-1.html"
    #take all html files 
    for i in range(1,172):

        #get path for file
        path = f"transcript_webpages/Episode-{i}.html"
        print(path)

        #format file
        soup = BeautifulSoup(open(path), "html.parser")
        content = soup.find(id="mw-content-text")

        with open(path, 'w') as f:
            f.write(str(content))

        #get all urls
        #print(soup)


def pull_text():
    "transcript_webpages/Episode-1.html"
    #take all html files 
    for i in range(1,172):

        #get path for file
        path = f"transcript_webpages/Episode-{i}.html"
        print(path)

        #format file
        soup = BeautifulSoup(open(path), "html.parser")
        txt = soup.get_text()

        with open(path, 'w') as f:
            f.write(txt)

        # with open(path, 'w') as f:
        #     f.write(str(content))


        #get all urls
        #print(soup)


def change_file_extenstion():
    folder = '/Users/ablades/dev/MakeSchool/tvd_wiki_scraper/transcript_webpages'
    for filename in glob.iglob(os.path.join(folder, '*..txt')):
        os.rename(filename, filename[:-4] + 'txt')


def condense_txt():
    for i in range(1,172):
        #get path for file
        path = f"transcript_webpages/Episode-{i}.txt"

        lines = open(path).read().splitlines()

        cleaned_txt = list()

        for line in lines:
            if not line.isspace():
                cleaned_txt.append(line.strip())

        open(f'txt_transcripts/Episode-{i}.txt','w+').write('\n'.join(cleaned_txt))


#remove brackets that describe actions
def regex_brackets():

    for i in range(1,172):
        #get path for file
        path = f"txt_transcripts/Episode-{i}.txt"

        lines = open(path).read().splitlines()

        cleaned_txt = list()

        for line in lines:
            cleaned_string = re.sub('(\[([^\]]+)])', '\n', line)
            cleaned_txt.append(cleaned_string)

        open(f'txt_transcripts/Episode-{i}.txt','w').write('\n'.join(cleaned_txt))


        #Regex to capture character lines
        

#remove brackets that describe actions
def regex_character_lines():

    for i in range(1,172):
        #get path for file
        path = f"txt_transcripts/Episode-{i}.txt"

        lines = open(path).read().splitlines()

        cleaned_txt = list()

        for line in lines:
            cleaned_txt.append(''.join(re.findall('[A-z]*\:.*', line)))
            
            #cleaned_string = re.sub('(\[([^\]]+)])', '\n', line)
            #cleaned_txt.append(cleaned_string)


        cleaned_txt = list(filter(None, cleaned_txt))

        
        open(f'txt_transcripts/Episode-{i}.txt','w').write('\n'.join(cleaned_txt))

def character_dictionary():
    #character dictionary that stores all character lines
    character_dictionary = dict()

    for i in range(1,172):
        #get path for file
        path = f"txt_transcripts/Episode-1.txt"


        with open(path, 'r') as f:
            line = f.readline()
            

        lines = open(path).read().splitlines()

        for line in lines:
            line_list = line.split(" ")
            #character name
            character_name = line_list[0]
            character_name = character_name[:-1]

            sentence = ' '.join(line_list[1:])

            if character_dictionary.get(character_name) is not None:
                character_dictionary[character_name].append(sentence)
            #character does not exist yet. create list and add sentence
            else:
                character_dictionary[character_name] = list()
                character_dictionary[character_name].append(sentence)



    print(character_dictionary.keys())




            #print(line_list)


if __name__ == "__main__":

    #gets all the transcripts form the table.html
    #get_transcripts(transcripts_urls)

    #takes url and pulls html file
    #transcripts_urls = soupify()

    #minimizes html file
    #minimize()

    #reduces file again
    #minimize_again()

    #only takes text from remaining file
    #pull_text()

    #changes the file extension to .txt for easier parsing
    #change_file_extenstion()

    #strips whitespace
    #condense_txt()

    #regex_brackets()
    #regex_character_lines()

    character_dictionary()

