from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def succesfulLogin():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    driver.find_element(By.ID, "email").send_keys("ikbal@test.com")
    driver.find_element(By.ID, "password").send_keys("ikbal1")
    driver.find_element(By.ID, "signin-btn").click()
    success = WebDriverWait(driver, 10).until(EC.url_contains('success.html'))
    driver.quit()
    return success

def unsuccesfulLogin():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    driver.find_element(By.NAME, "email").send_keys("abcd@abcd.com")
    driver.find_element(By.NAME, "password").send_keys("xyzt")
    driver.find_element(By.ID, "signin-btn").click()
    success = driver.current_url == "http://localhost:8080"
    driver.quit()
    return success

def copyPaste():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    driver.find_element(By.NAME, "email").send_keys("user1@example.com")
    passwordField = driver.find_element(By.ID, 'password')
    passwordField.send_keys("password1")
    actions = ActionChains(driver)
    passwordField.click()
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    passwordField.clear()
    passwordField.click()
    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    driver.find_element(By.ID, "signin-btn").click()
    success = driver.current_url == "http://localhost:8080"
    driver.quit()
    return success

def sqlInjection():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    driver.find_element(By.NAME, "email").send_keys("test@test.test' or 1=1; drop table user;--")
    driver.find_element(By.NAME, "password").send_keys("test")
    driver.find_element(By.ID, "signin-btn").click()
    success = driver.current_url == "http://localhost:8080"
    driver.quit()
    return success

def goBackForward():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    driver.find_element(By.ID, "email").send_keys("test@test.com")
    driver.find_element(By.ID, "password").send_keys("test")
    driver.find_element(By.ID, "signin-btn").click()
    WebDriverWait(driver, 10).until(EC.url_contains('success.html'))
    driver.execute_script("window.history.go(-1)")
    driver.find_element(By.ID, "signin-btn").click()
    success =  driver.current_url == "http://localhost:8080/"
    driver.quit()
    return success

# Run tests
successful_login = succesfulLogin()
unsuccessful_login = unsuccesfulLogin()
copy_paste = copyPaste()
sql_injection = sqlInjection()
go_back_forward = goBackForward()

# Check results and print
print("Successful Login Test:", "Passed" if successful_login else "Failed")
print("Unsuccessful Login Test:", "Passed" if not unsuccessful_login else "Failed")
print("Copy Paste Test:", "Passed" if not copy_paste else "Failed")
print("SQL Injection Test:", "Passed" if not sql_injection else "Failed")
print("Go Back Forward Test:", "Passed" if go_back_forward else "Failed")
