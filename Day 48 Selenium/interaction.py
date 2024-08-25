from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Navigate to wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.get("http://secure-retreat-92358.herokuapp.com/")


# Hone in on anchor tag using CSS selectors
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

# Find the "search" <input> by Name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")

# Sending keyboard input to selenium
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Abdullah Al")
last_name.send_keys("Towsif")
email.send_keys("dummy@email.com")

# Locate the "Sign Up" button and the click it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()