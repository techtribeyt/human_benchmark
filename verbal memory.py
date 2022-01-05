from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import keyboard

start_button = 'p'

# set up Selenium browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/verbal-memory")

# wait to start the program
keyboard.wait(start_button)

# get seen and new buttons
seen_button = browser.find_element(By.XPATH, '//button[text()="SEEN"]')
new_button = browser.find_element(By.XPATH, '//button[text()="NEW"]')

# store seen words
words = set()

while True:
    # get shown word
    word = browser.find_element(By.CLASS_NAME, 'word').text
    
    if word in words:
        seen_button.click()
    else:
        new_button.click()
        words.add(word)
        
    # break out of loop
    if keyboard.is_pressed(start_button): break