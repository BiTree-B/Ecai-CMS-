import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    # 浏览器夹具
    # 清理可能存在的chrome进程
    os.system("taskkill /f /im chrome.exe /t")
    os.system("taskkill /f /im chromedriver.exe /t")

    # 初始化浏览器
    service = Service('C:/bin/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # 设置窗口尺寸
    window_width = driver.execute_script("return window.screen.availWidth")
    window_height = driver.execute_script("return window.screen.availHeight")
    driver.set_window_position(0, 0)
    driver.set_window_size(window_width, window_height)

    yield driver

    # 测试结束后清理
    print("\n等待5秒后关闭浏览器...")
    time.sleep(5)
    driver.quit()


@pytest.fixture
def screenshot_dir():
    # 截图保存目录夹具
    # 创建截图目录
    screenshot_path = "test_screenshots"
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)

    return screenshot_path
