import requests
from bs4 import BeautifulSoup
import time

class Scrapper():
    #initialize the main url
    def __init__(self,target):
        self.target_url=target;

    #getting main page content and return it parsed
    def scrape(self):
        #delay before doing anything to not-overcharging the website with http request
        time.sleep(1)
        #request
        website_response = requests.get(self.target_url)
        website_content  =website_response.content
        #parsing with beautifull soup
        soup=BeautifulSoup(website_content,"html.parser")
        self.soup=soup
        return website_response

