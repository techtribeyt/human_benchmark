from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import time

# button to start program
start_button = 'esc'

# setting up Selenium browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/typing")

# wait for us to start program
while True:
    if keyboard.is_pressed(start_button):
        break
    
# find elements that contain text
tic = time.perf_counter()
elements = browser.find_elements_by_class_name("incomplete")

# get complete text string for us to type
text = ""
for element in elements:
    element_text = element.text
    text += element_text if len(element_text) > 0 else ' '
    
# measure how long everything took because Selenium is slow (optional)
toc = time.perf_counter()
print(toc - tic)

# write the text
keyboard.write(text)
