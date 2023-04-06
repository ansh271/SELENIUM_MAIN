import time
from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@podcastuploader1")
for i in range(1,4):
    driver.execute_script('window.open("");')
    driver.switch_to.window(driver.window_handles[i-1])
    driver.get("https://www.youtube.com/@podcastuploader1".format(i))
    x = '//*[@id="items"]/ytd-reel-item-renderer['
    x += str(i)
    x += ']'
    driver.find_element(By.XPATH,x).click()
time.sleep(100)
