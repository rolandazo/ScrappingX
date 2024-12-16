import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
from dotenv import load_dotenv


def initialize():
    load_dotenv()
    URL = "https://twitter.com/i/flow/login"
    X_USERNAME = os.getenv('X_USERNAME')
    X_PASSWORD = os.getenv('X_PASSWORD')
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    return driver


def login(pdriver):
    pdriver.get(URL)

    username = WebDriverWait(pdriver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
    username.send_keys(X_USERNAME)
    username.send_keys(Keys.ENTER)

    password = WebDriverWait(pdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password.send_keys(X_PASSWORD)
    password.send_keys(Keys.ENTER)
    time.sleep(10)

    
# MaIN EXECUTION:
running_driver = initialize()
login(running_driver)

