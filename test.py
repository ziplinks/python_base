from datetime import datetime

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
import win32com.client

# 用windows的话音功能，可以将文字转成语音，当抢到产品后，有一段语音播报
speaker = win32com.client.Dispatch("SAPI.SpVoice")
times = '2024-04-17 10:42:10'  # 秒杀开始时间
# 创建一个浏览器的驱动器对象，这个对象可以对浏览器实现自动化操作!!!
# driver = webdriver.Edge()

# 配置WebDriver和浏览器选项
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器界面
chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速
chrome_options.add_argument("--no-sandbox")  # 沙盒模式
chrome_options.add_argument("--disable-dev-shm-usage")  # 禁用/dev/shm使用

# 初始化WebDriver
driver = webdriver.Chrome(options=chrome_options)
# 浏览器最大化
driver.maximize_window()
# 通过动器自动打开某宝的首页!!!
driver.get("https://www.moretickets.com")
# 睡眠等待页面加载完成
time.sleep(3)
# 找到“请登录“按钮，并点击
login_btn = driver.find_element(By.XPATH, '//*[@id="js-open-login"]')
login_btn.click()
# 进入到登录贞面后，停顿30S，手动登录!!!
time.sleep(30)
# 进入到购物车贞面!!!
driver.get("https://www.moretickets.com/content/65a9e775b61f29000141f2ae")
time.sleep(10)

# 点击全选按钮
# driver.find_element(By.ID, "J_SelectAl11").click()

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(now)
    if now > times:
        driver.find_element(By.XPATH, '//*[@id="js-preorder-btn"]').click()
        break

wait = WebDriverWait(driver, 20)
element = wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'toPay')))
element.click()
speaker.Speak(f"主人，结算提交成功，我已帮你抢到商品啦，请及时支付订单")

