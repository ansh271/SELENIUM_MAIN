import time
from argparse import Action


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/@amv-master-st2xm/shorts")
driver.maximize_window()
#driver.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[3]/div/div[1]').click()

driver.find_element(By.XPATH, '//*[@id="interaction"]').click()


time.sleep(100)