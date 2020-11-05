
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

exe_path = '[your_absolute_path]\chromedriver.exe'
driver = webdriver.Chrome(executable_path=exe_path)
# main page
driver.get('https://lawv3.wkinfo.com.cn/')
print('Website Name:\n',driver.title)

'''
登录
'''
user_name = "user@[your_mail].com"
password = "password"

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(user_name)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password_text"))).send_keys(password)

# finish click action
# WTF, there are TRIPLE 't' in css-selector
login_button = driver.find_element_by_class_name("inputbuttton") 
login_button.click()
# another try using XPATH
# div_for_login_click_button = driver.find_element_by_class_name("user-login") 
# login_button = div_for_login_click_button.find_element_by_xpath("//form//p[6]//input[1]")


# clean previous content
user_name_table = driver.find_element_by_id("username")
user_name_table.clear()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(user_name)

password_table = driver.find_element_by_id("password_text")


# 点击其他部分，不然没法输入，会报错Element not iterable
other_content = driver.find_element_by_id("TB_overlay")
other_content.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password_text"))).send_keys(user_name)
