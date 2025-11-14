import time
from selenium.webdriver.common.by import By


def test_window_size(browser):
    size = browser.get_window_size()
    assert size['width'] > 1000, f"窗口宽度不足，当前：{size['width']}"
    assert size['height'] > 600, f"窗口高度不足，当前：{size['height']}"
    print("窗口尺寸设置正确")


def test_login(browser):
    # 进入网站
    browser.get("https://democms.hiyubei.com/login")
    time.sleep(2)

    # 输入帐密并登录
    username = browser.find_element(By.CLASS_NAME, "el-input__inner")
    username.send_keys("")
    password = browser.find_elements(By.CLASS_NAME, "el-input__inner")[1]
    password.send_keys("")
    print("帐密已输入")

    # 登录按钮
    search_button = browser.find_element(
        By.CSS_SELECTOR,
        ".el-button.el-button--primary.el-button--large"
    )
    search_button.click()
    time.sleep(1)

    # 验证登录是否成功
    assert "login" not in browser.current_url.lower()
    print("登录成功")


