from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

file = open('session-details.txt', 'r')
session_details = file.read()
file.close()

session_details = session_details.split(',')

capabilities = DesiredCapabilities.CHROME

driver = webdriver.Remote(
    command_executor=session_details[0],
    desired_capabilities=capabilities)

driver.session_id = session_details[1]

sleep(5)
xpath_orders = '//*[@id="root"]/div/main/div/div[2]/div[1]/div[2]/ul/div/a[1]'
element = driver.find_element_by_xpath(xpath_orders)
element.click()

next_btn_class = 'gwZegf'

file = open('data.txt', 'w')

for i in range(0, 57):
    sleep(10)

    x = BeautifulSoup(driver.page_source, 'html.parser')
    x = x.find_all('section')[0].next_element.nextSibling.contents[0].contents

    for y in x:
        y = y.contents[0].contents
        rest_details = y[0]
        order_details = y[2]
        file.writelines(str(rest_details) + str(order_details))
        file.write('\n')

    next_btn = driver.find_element_by_class_name(next_btn_class)
    next_btn.click()

file.close()

# prev_btn_class = 'eOsZfi'
# for i in range(0, 57):
#     sleep(5)
#     prev_btn = driver.find_element_by_class_name(prev_btn_class)
#     prev_btn.click()

print('Done')
