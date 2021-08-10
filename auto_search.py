from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
# pythonでpathを通さずにselenium使用するのに必要↓
import chromedriver_binary
import datetime
import os


# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
# 背面で動かすとき
options.add_argument('--headless')

# よく分からないけどcrashを防ぐためにいりそう
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
# user 認証に必要だった
options.add_argument('user-agent=Chrome/92.0.4515.131')

today = datetime.date.today()
month = today.month
day = today.day
print(month,day)

tomorrow = today + datetime.timedelta(days=35)
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
time.sleep(5)

# 休講情報をクリック

print(driver.find_element_by_link_text("休講補講参照"))
driver.find_element_by_link_text("休講補講参照").click()
print("休講情報")
driver.implicitly_wait(20)
iframe = driver.find_element_by_id("main-frame-if")
driver.switch_to.frame(iframe)

# 今日の日付を入力

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
time.sleep(4)
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



# Twitterへのアクセス開始

try:
    print("start access to twitter")
    # login twitter

    driver.get("https://mobile.twitter.com/home")
    driver.implicitly_wait(3)
    # login
    print("start log into twitter")

    driver.save_screenshot('img/logincheck.png')
    driver.implicitly_wait(4)
    time.sleep(5)
    driver.save_screenshot('img/logincheck2.png')
    user_name_input=driver.find_element_by_name("session[username_or_email]")
    print(user_name_input)
    user_name_input.send_keys("@hitCanceledInfo")

    user_pass_input =driver.find_element_by_name("session[password]")
    print(user_pass_input)
    user_pass_input.send_keys("Kazuking2840!")

    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span").click()
    driver.implicitly_wait(10)
    print("logged in")
    print(today)

except Exception as e:
    print("[ERROR] Twitterのloginに失敗")
    print(e)
    print(e.with_traceback())
try:
    # send string
    # errorpng = driver.find_element_by_id("react-root").screenshot_as_png

# 画像を保存

    # driver.save_screenshot('/Users/Kazuki/develop/kazuki/selenium_lecture_cancellation/img/errorpng.png')
    # print("captured")
    # driver.implicitly_wait(10)
    # input_field = driver.find_element_by_class_name("notranslate")
    # input_field.click()
    # input_field.send_keys(str(today))
    # driver.implicitly_wait(5)
    print("email form?")
    time.sleep(7)
    email_form = driver.find_element_by_id("challenge_response").send_keys("1120120u@g.hit-u.ac.jp")
    email_form.send_keys("1120120u@g.hit-u.ac.jp")
    time.sleep(3)
    submit_button = driver.find_element_by_id("email_challenge_submit")
    submit_button.click()
    time.sleep(5)
    driver.implicitly_wait(10)

    # ここで再びnotranslateにアクセス

    input_field = driver.find_element_by_class_name("notranslate")
    input_field.click()
    input_field.send_keys(str(today))
    driver.implicitly_wait(5)
except Exception as e:

    print("[ERROR] notranslate is nothing")
    print(e)
    print(e.__context__)
    time.sleep(5)

    # ここで再びnotranslateにアクセス

    input_field = driver.find_element_by_class_name("notranslate")
    input_field.click()
    input_field.send_keys(str(today))
    driver.implicitly_wait(5)

try:

    # send img
    file_path = os.path.abspath("img/" + str(today)+".png")
    print(file_path)
    print(driver.find_element_by_xpath('//input[@type="file"]'))
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(file_path)
    driver.implicitly_wait(10)

    # push tweet button
    twitter_button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span")
    twitter_button.click()
    time.sleep(5)
    print("click success")
    driver.implicitly_wait(20)
except Exception as e:
    print(e)
    print(e.with_traceback())
    print("[ERROR] 画像の添付もしくは投稿に失敗")


# ブラウザを終了する
driver.close()
driver.quit()