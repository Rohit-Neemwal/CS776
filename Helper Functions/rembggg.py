from selenium import webdriver
import time

driver_path = "C:\webdrivers\chromedriver"

driver = webdriver.Chrome(driver_path)

driver.get("https://www.photoroom.com/background-remover")

upload_button = driver.find_element("xpath","//*[@id=\"__next\"]/div/div[1]/main/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/button")
upload_button.send_keys("F:\CS776\dataset\croppedplantdoc\Train\Apple leaf\\3466fruit_apple_apple-tree_wallpaper_EA60026.jpg")


time.sleep(10)

time.sleep(20000)

# Close the browser
driver.quit()
