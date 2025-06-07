from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

# Setup driver
service = Service(executable_path=r"C:\Users\YD1RUH\Documents\kuliah\DataMining\pertemuan_11\Crawler_Media_Social\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.set_page_load_timeout(20)
    driver.get('https://www.youtube.com/')
    driver.maximize_window()
    sleep(5)
    
    # Search for the video
    search = driver.find_element(By.NAME, "search_query")
    search.clear()
    search.send_keys("ilc Jaksa Dijaga Tentara Negara aman atau justru bahaya")
    search.send_keys(Keys.ENTER)
    sleep(5)
    
    # Click first video link
    link = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    link.click()
    sleep(15)
    
    # Scroll to load comments
    for i in range(100):
        driver.execute_script("window.scrollBy(0, 700)")
        sleep(2)
    
    # Wait for comments to load
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="content-text"]')))
    
    # Extract comments
    comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
    comment_list = [comment.text for comment in comments]
    
    print(comment_list)
    print(f"Total comments: {len(comment_list)}")
    
    # Save to CSV
    df = pd.DataFrame({"comment": comment_list})
    df.to_csv("youtube_comments_1.csv", index=False)
    
finally:
    driver.quit()
