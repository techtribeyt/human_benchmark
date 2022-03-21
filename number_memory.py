from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import time

start_button = 'p'

# set up Selenium browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/number-memory")

# wait to start the program
keyboard.wait(start_button)

while True:
    # read number
    number = browser.find_element(By.CLASS_NAME, 'big-number').text
    
    # find submit button
    submit_button = None
    while not submit_button:
        try:
            submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
        except NoSuchElementException:
            time.sleep(0.1)
        
    # enter input
    keyboard.write(number)
       
    # submit answer
    submit_button.click()
    
    time.sleep(0.2)
    
    # go to next number
    next_button = browser.find_element(By.XPATH, '//button[text()="NEXT"]')
    next_button.click()
    
    time.sleep(0.2)
        
    # break out of loop
    if keyboard.is_pressed(start_button): break