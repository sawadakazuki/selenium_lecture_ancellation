from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import chromedriver_binary
import datetime
import os


# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
# 背面で動かすとき
options.add_argument('--headless')
options.add_argument('user-agent=Chrome/68.0.3440.84')
# Selenium Server に接続する
# driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     desired_capabilities=options.to_capabilities(),
#     options=options,
# )

today = datetime.date.today()
month = today.month
day = today.day
print(month,day)

tomorrow = today + datetime.timedelta(days=1)
tomorrow_month =tomorrow.month
tomorrow_day =tomorrow.day
print(tomorrow_month,tomorrow_day)

driver = webdriver.Chrome(options=options)
# Selenium 経由でブラウザを操作する

# celsにログインする
driver.get('https://cels.hit-u.ac.jp/campusweb')

driver.implicitly_wait(20)

# get URL
login_url = driver.current_url

print(login_url)

# ログインしているかどうかを確認する

if login_url != "https://cels.hit-u.ac.jp/campusweb/campusportal.do?page=main":

    driver.get(login_url)
    driver.implicitly_wait(20)

    studentId_form = driver.find_element_by_id("idToken1")
    studentId_form.send_keys("1120120U")

    studentPass_form = driver.find_element_by_id("idToken2")
    studentPass_form.send_keys("Kazuking2840!")

    driver.find_element_by_id("loginButton_0").click()

print("logged in")
# driver.implicitly_wait(20)
time.sleep(5)
# 休講情報をクリック
print(driver.find_element_by_link_text("休講補講参照"))
driver.find_element_by_link_text("休講補講参照").click()

print("休講情報")
driver.implicitly_wait(20)
iframe = driver.find_element_by_id("main-frame-if")
driver.switch_to.frame(iframe)
# 今日の日付を入力
# print(driver.page_source)
# print("month_select")
# a = driver.find_element_by_id("main-portlet-title")
# print(a)
driver.implicitly_wait(20)

month_elem = driver.find_element_by_id("startDay_month")
select_month = Select(month_elem)
# driver.switch_to.default_content()

select_month.select_by_value(str(month))

day_elem = driver.find_element_by_id("startDay_day")
select_day = Select(day_elem)
select_day.select_by_value(str(day))

# 一日後の日付を入力
tomorrow_month_elem =driver.find_element_by_id("endDay_month")
select_tomorrow_month = Select(tomorrow_month_elem)
select_tomorrow_month.select_by_value(str(tomorrow_month))

tomorrow_day_elem =driver.find_element_by_id("endDay_day")
select_tomorrow_day = Select(tomorrow_day_elem)
select_tomorrow_day.select_by_value(str(tomorrow_day))

driver.find_element_by_id("Button").click()

driver.implicitly_wait(20)

driver.switch_to.default_content()


# ページサイズを画面いっぱいにする　headlessじゃないとうまくいかないことがある
page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(page_width, page_height)

driver.implicitly_wait(5)
# タイトル部分の画像オブジェクトを取得する。
form = 'entryShowForm'
png = driver.find_element_by_id("main-frame").screenshot_as_png

# 画像を保存
with open(f'img/{today}.png', 'wb') as f:
    f.write(png)
print("captured")


try:
    print("access to twitter")
    # login twitter
    print(driver.get("https://mobile.twitter.com/home"))
    driver.get("https://mobile.twitter.com/home")
    driver.implicitly_wait(3)
    # login
    print("start log into twitter")
    driver.save_screenshot('img/logincheck.png')
    user_name_input=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
    print(user_name_input)
    user_name_input.send_keys("@hitCanceledInfo")

    user_pass_input =driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
    print(user_pass_input)
    user_pass_input.send_keys("Kazuking2840!")

    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span").click()

    driver.implicitly_wait(10)
    print("logged in")
    print(today)
except Exception as e:
    print(e)
    print(e.with_traceback())
    print("[ERROR] Twitterのloginに失敗")
try:
    # send string

    driver.save_screenshot('img/nontranslate.png')
    png2 = driver.find_element_by_class_name("notranslate").screenshot_as_png
    with open(f'img/nontranslate_check.png', 'wb') as f:
        f.write(png2)
    input_field = driver.find_element_by_class_name("notranslate")
    input_field.click()
    input_field.send_keys(str(today))
    driver.implicitly_wait(5)
except Exception as e:
    driver.find_element_by_xpath('//input[@type="form"]').send_keys("1120120u@g.hit-u.ac.jp")
    driver.find_element_by_name("送信").click()
    driver.implicitly_wait(5)
    print(e)
    print(e.with_traceback())
    print("[ERROR] notranslate is nothing")
    input_field = driver.find_element_by_class_name("notranslate")
    input_field.click()
    input_field.send_keys(str(today))
    driver.implicitly_wait(5)
    file_path = os.path.abspath("img/" + str(today)+".png")
    print(file_path)
    print(driver.find_element_by_xpath('//input[@type="file"]'))

    driver.find_element_by_xpath('//input[@type="file"]').send_keys(file_path)
    driver.implicitly_wait(10)
    twitter_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
    twitter_button.click()
    driver.implicitly_wait(20)
try:

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
    print(e)
    print(e.with_traceback())
    print("[ERROR] Twitterの投稿に失敗")

print(driver.find_elements_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"))

# ブラウザを終了する
driver.close()
driver.quit()