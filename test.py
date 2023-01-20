from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.wikipedia.org/')

driver.find_element(By.ID, 'searchInput').send_keys('Test automation')
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

assert 'Test automation' in driver.page_source

driver.close()