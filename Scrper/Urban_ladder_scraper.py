import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import logging
import time

# create a logger
logging.basicConfig(filename='Urban_ladder.log', level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')

# Read the Csv file
data = pd.read_csv(f'D:\\Project\\Udemy_practice\\Scrper\\links.csv')
# Get the URLs into the list
url_list = data['Links'].tolist()

# Go through the loops to extract data form the website URls

for url in url_list:
    try:
        page = requests.get(url=url)
        time.sleep(1)
        soup = BeautifulSoup(page.content, 'html.parser')
        product_name = soup.find(class_="page-heading product-title no-margin").text.split('\n')[1]
        images_src = [i.get('data-src') for i in soup.find_all("img")]
        count = 0
        os.mkdir(os.getcwd() + f"\\{product_name}")
        logging.info(product_name)
        for image in images_src:
            if image is not None:
                # The image is saved in the folder.
                urllib.request.urlretrieve(image, os.getcwd() + f'\\{product_name}\\{count}.png')
                count += 1
            else:
                pass
        time.sleep(1)
    except Exception as e:
        logging.info('Error Occurred!!')
        logging.error(e)
