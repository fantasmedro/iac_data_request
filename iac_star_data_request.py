'''
Copyright 2023 Pedro Hernandez Cascales

This file software allows to make automated request in the IAC application: IAC Star.

@Author: Pedro Hernandez Cascales (pedrhe03@ucm.es)

:History:
24 Mar 23:  version 1.0
'''

import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

__version__ = "1.0"
__author__  = "Pedro Hernandez Cascales"


# Create a ChromeOptions object to configure ChromeDriver
chrome_options = Options()

# Set the browser to run in headless mode
chrome_options.add_argument('--headless')

# Create a new instance of the ChromeDriver
driver = webdriver.Chrome(options=chrome_options)


def data_request():
    with open('/home/pedro/master/iac_data_request/config.json', 'r') as config_file:
         config = json.load(config_file) #Loads info from configuration file
         names = list(config.keys()) #We create a list of different fields present in the form of IAC Star
         if config['nrequest'] >= 1:
             n = config['nrequest']
         else:
             raise SystemError(f'Invalid n ={config["nrequest"]}.')
         wait_time = config['time'] #We set the time that we will wait between requests
         driver.get("http://iac-star.iac.es/cmd/www/form.htm") #We open the webpage of the application
         
         #This loops completes the form of the application
         for i in range(0,n):
             for name in names[2:]:
                 value = config[str(name)]
                 field = driver.find_element(By.NAME,str(name))
                 field.clear()
                 field.send_keys(value[min(i, len(value)-1)])
             
             #We submit the request, we wait the time establised and reload the form to complete it again if necessary
             submit_button = driver.find_element(By.NAME,"Submit")
             submit_button.click()
             time.sleep(wait_time)
             driver.back()
             driver.refresh()
             print("Request number "+str(i+1)+" sent")
         driver.quit()

data_request()

