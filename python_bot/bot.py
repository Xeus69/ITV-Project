from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "shashwatpandey"
password = "ess123"

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000/login/")

wait = WebDriverWait(browser, 20)  # Wait for a maximum of 20 seconds

# Update the class name of the sign-in button
sign_in = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-dark')))

username_str = browser.find_element(By.ID, 'id_username')
username_str.send_keys(username)

password_str = browser.find_element(By.ID, 'password')
password_str.send_keys(password)

sign_in.click()

