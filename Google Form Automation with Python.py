from selenium import webdriver
import pyautogui
import random
import time

index_number = 

browser = webdriver.Chrome()
browser.get('')

username = ""
user = browser.find_element_by_xpath('')
user.send_keys(username)

UserNext = browser.find_element_by_xpath('')
UserNext.click()

time.sleep(2)

password = ('')
passw = browser.find_element_by_xpath('')
passw.send_keys(password)

PassNext = browser.find_element_by_xpath('')
PassNext.click()

time.sleep(5)

userb = browser.find_element_by_xpath('')
userb.click()

time.sleep(2)

for _ in range(index_number):
    pyautogui.keyDown('down'); pyautogui.keyUp('down')
pyautogui.keyDown('enter'); pyautogui.keyUp('enter')

RandomNumber = random.randint(355,374)/10
Temperature = str(RandomNumber)
temper = browser.find_element_by_xpath('')
temper.send_keys(Temperature)

submitbutton = browser.find_element_by_xpath('')
submitbutton.click()
