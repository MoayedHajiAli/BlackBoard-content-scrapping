from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from subprocess import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

savingDir = os.getcwd()+"/ML_Lectures"
try:
    os.mkdir(savingDir)
except OSError as e:
    print("Directory existed")
chromeOptions = Options()
prefs = {
    "profile.default_content_settings.popups": 0,
    "plugins.always_open_pdf_externally": True,
    "download.default_directory" : savingDir,
    "directory_upgrade": True
}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("https://ku.blackboard.com/webapps/blackboard/content/listContent.jsp?course_id=_28445_1&content_id=_202511_1&mode=reset")
agree = driver.find_element_by_id("agree_button")
agree.click()
username = driver.find_element_by_id("user_id")
password = driver.find_element_by_id("password")
login = driver.find_element_by_id("entry-login")
username.send_keys("mali18")
password.send_keys("Iamcry4u$$")
login.click()
while True:
    content = driver.find_element_by_id("content_listContainer")
    links = driver.find_elements_by_xpath("//div[@class='item clearfix']/h3/a")
    main_window = driver.current_window_handle
    print(len(links))
    for link in links:
        try:
            title = link.find_element_by_tag_name('span').text
            print(title)
            link.click()
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 's')
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            driver.close()
            driver.switch_to.window(main_window)
        except ElementNotInteractableException as e:
            print("Exception")
            break
    try:
        driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@id='nextPage']/a"))))
        next_button = driver.find_element_by_xpath("//li[@id='nextPage']/a")
        if next_button.get_attribute('class') == "compact-button disabled":
            print("Last page reached")
            break
        next_button.click()
        time.sleep(2)
        driver.switch_to.window(driver.current_window_handle)
    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break
