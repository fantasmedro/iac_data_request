from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create a ChromeOptions object to configure ChromeDriver
chrome_options = Options()

# Set the browser to run in headless mode
chrome_options.add_argument('--headless')

# Create a new instance of the ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

# Opens the formulary webpage
driver.get("http://iac-star.iac.es/cmd/www/form.htm")

# Setting arguments

# Personal arguments
name_field = driver.find_element(By.NAME,"name")
name_field.send_keys(args.name)
email_field = driver.find_element(By.NAME,"email")
email_field.send_keys(args.mail)

# Simulation parameters
tot_star = driver.find_element(By.NAME,"everformed")
tot_star.clear()
tot_star.send_keys(args.tot_star)

file_star = driver.find_element(By.NAME, "starsaved")
file_star.clear()
file_star.send_keys(args.file_stars)

magnitude = driver.find_element(By.NAME,"magnitude")
magnitude.clear()
magnitude.send_keys(args.mag)

filter_w = driver.find_element(By.NAME,"filter")
filter_w.clear()
filter_w.send_keys(args.filter)

sfr = driver.find_element(By.NAME,"SFR")
sfr.clear()
sfr.send_keys(args.sfr)


# "Finds" submit button and click it
submit_button = driver.find_element(By.NAME,"Submit")
submit_button.click()
