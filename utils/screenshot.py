import os
import inspect
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver


def take_screenshot(driver: WebDriver,
                    name: str = None,# 截图名称，none为自动生成,即使用调用者的函数名
                    prefix: str = "",# 文件名前缀
                    suffix: str = "",# 文件名后缀
                    directory: str = "screenshots") -> str:# 目录

    os.makedirs(directory, exist_ok=True)

    # 生成文件名
    if name is None:
        # 获取调用者的函数名
        caller_frame = inspect.stack()[1]
        caller_function = caller_frame.function
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}{caller_function}_{timestamp}{suffix}.png"
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}{name}_{timestamp}{suffix}.png"

    # 截图文件路径
    filepath = os.path.join(directory, filename)

    # 截图保存
    driver.save_screenshot(filepath)

    print(f"截图已保存: {filepath}")
    return filepath


# 步骤截图，自动使用调用函数名
def screenshot_step(driver: WebDriver, step_description: str = None):
    if step_description:
        return take_screenshot(driver, name=step_description)
    else:
        return take_screenshot(driver)


# 完全自定义文件名截图,不带日期
def screenshot_custom(driver: WebDriver, filename: str):
    directory = "screenshots"
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, f"{filename}.png")
    driver.save_screenshot(filepath)
    print(f"自定义截图: {filepath}")
    return filepath