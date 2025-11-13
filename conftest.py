import subprocess
import time
import os
import pytest
import logging
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.screenshot import take_screenshot


@pytest.fixture(scope="session")
def browser():
    """
    # win版本
    # 浏览器夹具
    # 清理可能存在的chrome进程
    os.system("taskkill /f /im chrome.exe /t")
    os.system("taskkill /f /im chromedriver.exe /t")

    # 初始化浏览器
    service = Service('C:/bin/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    """

    # 浏览器夹具
    # 清理可能存在的chrome进程（macOS版本）
    os.system("pkill -f chrome")
    os.system("pkill -f chromedriver")

    # 更安全的进程清理方式（推荐）
    subprocess.run(['pkill', '-f', 'chrome'], capture_output=True)
    subprocess.run(['pkill', '-f', 'chromedriver'], capture_output=True)

    # 初始化浏览器
    # 路径指向文稿下的chrome-webdriver文件夹
    chrome_driver_path = os.path.expanduser('~/Documents/chrome-webdriver/chromedriver')
    service = Service(chrome_driver_path)
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


# 错误处理夹具
@pytest.fixture(autouse=True)
def error_handling(browser, request):

    try:
        yield
    except Exception as e:
        # 函数名作为截图名
        test_name = request.node.name
        error_type = type(e).__name__

        # 截图
        take_screenshot(browser, f"{test_name}_{error_type}", "error")

        # 日志
        logging.error(f"测试失败: {test_name}")
        logging.error(f"错误类型: {error_type}")
        logging.error(f"错误信息: {str(e)}")
        logging.error(f"错误追踪:\n{traceback.format_exc()}")

        # 重新抛出异常
        raise

"""
@pytest.fixture
def screenshot_dir():
    # 截图保存目录夹具
    # 创建截图目录
    screenshot_path = "test_screenshots"
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)

    return screenshot_path
"""