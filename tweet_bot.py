import chromedriver_binary
from selenium import webdriver
import datetime
import os
# Chrome のオプションを設定する
options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('user-agent=Chrome/68.0.3440.84')
# 背面で動かすとき
# options.add_argument('--headless')

today = datetime.date.today()

driver = webdriver.Chrome(options=options)

try:

    # login twitter
    driver.get("https://mobile.twitter.com/home")
    driver.implicitly_wait(3)
    # login
    user_name_input=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
    user_name_input.send_keys("@hitCanceledInfo")

    user_pass_input =driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
    user_pass_input.send_keys("Kazuking2840!")

    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span").click()

    driver.implicitly_wait(5)
    print("logged in")
    print(today)
    # send string
    input_field = driver.find_element_by_class_name("notranslate")
    input_field.click()
    input_field.send_keys(str(today))
    driver.implicitly_wait(5)

    # send img
    file_path = os.path.abspath("img/" + str(today)+".png")
    print(file_path)
    print(driver.find_element_by_xpath('//input[@type="file"]'))

    driver.find_element_by_xpath('//input[@type="file"]').send_keys(file_path)
    driver.implicitly_wait(10)

    # //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/input

    # push tweet button
    twitter_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
    twitter_button.click()
    driver.implicitly_wait(20)
except Exception as e:
    print("[ERROR] Twitterの投稿に失敗")

print(driver.find_elements_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"))


