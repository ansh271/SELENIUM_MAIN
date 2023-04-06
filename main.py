from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/@podcastuploader1")

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

reels = driver.find_elements_by_xpath("//a[@aria-label='Reel']")

print(f"Total Reels: {len(reels)}")

driver.quit()
