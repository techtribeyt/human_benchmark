from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import time

start_button = 'p'

# set up Selenium browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/memory")

# wait to start the program
keyboard.wait(start_button)

num_squares = 3
while True:
    active_elements = []
    while len(active_elements) != num_squares:
        active_elements = browser.find_elements_by_css_selector('div.active')
    
    time.sleep(2)
    
    for element in active_elements:
        element.click()


    time.sleep(1)
        
    # break out of loop
    if keyboard.is_pressed(start_button): break

    num_squares += 1