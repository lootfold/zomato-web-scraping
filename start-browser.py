from time import sleep
from selenium import webdriver

DRIVER_PATH = '/home/pallav/sdk/chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.zomato.com/hyderabad/')

session_url = driver.command_executor._url
session_id = driver.session_id

print(session_url)
print(session_id)

file = open('session-details.txt', 'w')
file.write(f'{session_url},{session_id}')
file.close()

sleep(86400)
