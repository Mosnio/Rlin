from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Proxy details

proxy = "http://Q0QcQarNb10aX315aoQESSDkVRJO0I:t62JJnQ4sNHoqIQA@residential.flashproxy.io:8082"

# Set up Chrome options with proxy
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://rglinks.com/b5tF')  # Change URL if needed

# Wait for 30 seconds
time.sleep(30)

# Click on the first button
button1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "tp-snp2"))
)
button1.click()
print('1clicked')
driver.switch_to.window(driver.window_handles[0])

# Wait for 30 seconds
time.sleep(30)

# Click on the second button
button2 = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.ID, "cross-snp2"))
)
button2.click()
print('2clicked')

# Wait for 30 seconds
time.sleep(30)

driver.switch_to.window(driver.window_handles[0])

# Click on the third button
button3 = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.ID, "tp-snp2"))
)
button3.click()
print('3clicked')

# Wait for 30 seconds
time.sleep(30)

driver.switch_to.window(driver.window_handles[0])

# Click on the fourth button
button4 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "tp-snp2"))
)
button4.click()
print('4clicked')
time.sleep(20)
driver.switch_to.window(driver.window_handles[0])
time.sleep(30)
