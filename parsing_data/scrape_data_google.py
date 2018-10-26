from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json
from urllib.request import *
import sys
import time

"""
Dependencies include:
- Selenium
- Geckodriver: Download from Here: https://github.com/mozilla/geckodriver/releases
    1. Extract the file: tar -xvzf geckodriver*
    2. Make it executable: chmod +x geckodriver
    3. Add the driver to the path for other tools to use it:
    export PATH=$PATH:/Users/Marwa/Documents/Junior\ Year/Projects/6.819_Final_Project/geckodriver
    4. Command to run the file:
    python scrape_data_google.py <query> <number of images>
    5. Firefox Browser

"""
# adding path to geckodriver to the OS environment variable
os.environ["PATH"] += os.pathsep + os.getcwd()
data_path = "data/"

def scrape_google_data():
    # parsing data 
    keyword = sys.argv[1]
    requested_images = int(sys.argv[2])
    number_of_scrolls = requested_images / 400 + 1 

    # number_of_scrolls * 400 images will be opened in the browser
    if not os.path.exists(data_path + keyword.replace(" ", "_")):
        os.makedirs(data_path + keyword.replace(" ", "_"))

    url = "https://www.google.co.in/search?q=" + keyword + "&source=lnms&tbm=isch"
    driver = webdriver.Firefox()
    driver.get(url)

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    extensions = {"jpg", "jpeg", "png", }
    img_count = 0
    downloaded_img_count = 0
    
    for _ in range(int(number_of_scrolls)):
        for __ in range(10):
            # multiple scrolls needed to show all 400 images
            driver.execute_script("window.scrollBy(0, 1000000)")
            time.sleep(0.2)

        # to load next 400 images
        time.sleep(0.5)
        try:
            driver.find_element_by_xpath("//input[@value='Show more results']").click()
        except Exception as e:
            print ("Less images found: {}".format(e))
            break

    images = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')

    print ("Total images: {}\n".format(len(images)))

    for img in images:
        img_count += 1
        img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
        img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
        print ("Downloading image {}:{}".format(img_count,img_url))

        try:
            if img_type not in extensions:
                img_type = "jpg"
            req = Request(img_url, headers=headers)
            raw_img = urlopen(req).read()
            f = open(data_path+keyword.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type, "wb")
            f.write(raw_img)
            f.close
            downloaded_img_count += 1

        except Exception as e:
            print ("Download failed: {}".format(e))

        if downloaded_img_count >= requested_images:
            break

    print ("Total images downloaded: {}/{}".format(downloaded_img_count,img_count))
    
    driver.quit()

if __name__ == "__main__":
    scrape_google_data()