from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import re
import logging

logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s %(name)s %(message)s')

df = pd.read_excel(r'C:\\Users\\user\\Desktop\\Full Stack Data Science\\Market Scraper\\Meticulous '
                   r'research\\Final_link_file.xlsx')

report_description = []
report_title = []
for url in df['Links']:
    try:
        time.sleep(0.5)
        logging.info('The Url : ' + str(url))
        # get and parse the html from url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # extract the report description and report title into various list
        x = soup.find(class_="col-md-12 mt-3 report-description").text
        report_description.append(x)
        y = soup.find(class_="text-justify").text
        report_title.append(y)
    except Exception as e:
        logging.info("Error Occurred!!!")
        logging.error(e)
        pass
