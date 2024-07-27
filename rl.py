from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Define the list of URLs
select = [
    "https://rglinks.com/AaWUI",
    "https://rglinks.com/5a93",
    "https://rglinks.com/deAR6nr0",
    "https://rglinks.com/v8x7N6",
    "https://rglinks.com/m56n",
    "https://rglinks.com/9JGGbtl",
    "https://rglinks.com/my6A7fy",
    "https://rglinks.com/GmFr",
    "https://rglinks.com/fctF",
    "https://rglinks.com/VxZq5",
    "https://rglinks.com/WggwT"
]

# Randomly select a URL from the list
selc = random.choice(select)

# Print the selected URL
print(selc)

driver.get(selc)

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
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(30)
