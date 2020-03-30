from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from subprocess import time
import urllib.request
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pyautogui
import os.path

def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

savingDir = os.getcwd()+"/ML_Videos_test"
try:
    os.mkdir(savingDir)
except OSError as e:
    print("Directory existed")
chromeOptions = Options()
prefs = {
    "profile.default_content_settings.popups": 0,
    "plugins.always_open_pdf_externally": True,
    "download": {
        'default_directory': savingDir,
    },
    "directory_upgrade": True
}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("https://ku.blackboard.com/webapps/ppto-PanoptoCourseTool-BBLEARN/Content.jsp?course_id=_28445_1&mode=view")
agree = driver.find_element_by_id("agree_button")
agree.click()
username = driver.find_element_by_id("user_id")
password = driver.find_element_by_id("password")
login = driver.find_element_by_id("entry-login")
username.send_keys("amasry17")
password.send_keys("1357997531")
login.click()
while True:
    content = driver.find_element_by_id("courseContent")
    driver.switch_to.frame(content.find_element_by_tag_name("iframe"))
    links = driver.find_elements_by_xpath("//a[@class='detail-title']")
    main_window = driver.current_window_handle
    print(len(links))
    for i in range(0, len(links)):
        link = links[i]
        try:
            link.click()
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            title_element = driver.find_element_by_id('deliveryTitle')
            title = title_element.get_attribute('innerHTML')
            print(title)
            video = driver.find_element_by_xpath("//meta[@name='twitter:player:stream']")
            url = video.get_attribute("content")
            driver.get(url)
            time.sleep(10)
            file = savingDir + '/' + title + '.mp4.crdownload'
            print(file)
            while not os.path.isfile(file):
                pyautogui.keyDown("command")
                pyautogui.press("s")
                pyautogui.keyUp("command")
                time.sleep(6)
                if i == 0:
                    pyautogui.keyDown("command")
                    pyautogui.keyDown("shift")
                    pyautogui.press("g")
                    pyautogui.keyUp("command")
                    pyautogui.keyUp("shift")
                    pyautogui.typewrite(savingDir)
                    time.sleep(6)
                    pyautogui.press("enter")
                    time.sleep(2)
                pyautogui.typewrite(title)
                time.sleep(5)
                pyautogui.press("enter")
                time.sleep(2)
            # driver.get('chrome://downloads/')
            # time.sleep(1)
            # driver.switch_to.window(driver.window_handles[1])
            # pause = driver.execute_script(
            #     'return document.querySelector("downloads-manager").shadowRoot.querySelector("downloads-item").shadowRoot.querySelector("cr-button")')
            # pause.click()
            driver.close()
            driver.switch_to.window(main_window)
            content = driver.find_element_by_id("courseContent")
            driver.switch_to.frame(content.find_element_by_tag_name("iframe"))
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
#
#
# driver.get('chrome://downloads/')
# time.sleep(1)
# driver.switch_to.window(driver.current_window_handle)
# downloadLise = driver.execute_script('return document.querySelector("downloads-manager").shadowRoot').find_elements_by_css_selector('downloads-item')
# print(len(downloadLise))
#
# for i in range(0, len(downloadLise)):
#     ele = downloadLise[i]
#     wait_time = 60*20
#     if i%5==0:
#         time.sleep(wait_time)
#     resume = driver.execute_script('return arguments[0].shadowRoot.querySelector("cr-button")', ele)
#     resume.click()
