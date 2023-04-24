from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Данные от аккаунта нужны, чтобы войти в аккаунт
# чтобы цены были в рублях (если аккаунт русский).
# Эти данные никуда не распрастраняются и остаются конфиденциальными
login_account = input("Введите ваш логин от аккаунта Steam: ")
password_account = input("Введите ваш пароль от аккаунта Steam: ")
skin = input("Введите ссылку на игровой предмет: ")
min_price = float(input("Введите минимальную цену в рублях: "))

driver = webdriver.Chrome(ChromeDriverManager().install())

time.sleep(5)
driver.get("https://steamcommunity.com/")
time.sleep(5)
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[1]/div[4]/div/div[1]/div/div[1]/a[1]')
button.click()
time.sleep(5)

login = driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')
time.sleep(3)
login.send_keys(login_account)
time.sleep(0.5)

password = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input")
time.sleep(3)
password.send_keys(password_account)
time.sleep(0.5)
button = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button")
time.sleep(3)
button.click()
time.sleep(30)
# В течении 30 секунд вы должны подтвердить вход на телефоне в приложении Steam

while True:
    try:
        driver.find_element(By.CLASS_NAME, "global_action_link")
        break
    except:
        time.sleep(1)

# Открывает ссылку на игровой предмет
driver.get(skin)
time.sleep(5)

# Цикл проверки цены на игровой предмет
while True:
    try:
        price_element = driver.find_element(By.CLASS_NAME, "market_listing_price_with_fee")
        time.sleep(1)
        price = float(price_element.text.replace(",", ".")[:-5])
        time.sleep(1)
        if price <= min_price:
            print(f"Цена: {price} руб.")
            break
    except NoSuchElementException:
        pass

    driver.refresh()
    time.sleep(5)

# Закрытие браузера
driver.quit()