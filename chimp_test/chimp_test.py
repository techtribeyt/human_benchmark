from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import time

start_button = 'p'

# set up Selenium browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/chimp")

# wait to start the program
keyboard.wait(start_button)

numbers = 4
while True:
    for i in range(1, numbers + 1):
        el = browser.find_element_by_xpath('//div[@data-cellnumber="' + str(i) + '"]')
        el.click()

    time.sleep(0.05)
    
    # go to next level
    continue_button = browser.find_element(By.XPATH, '//button[text()="Continue"]')
    continue_button.click()
    
    time.sleep(0.05)
        
    # break out of loop
    if keyboard.is_pressed(start_button): break

    numbers += 1
