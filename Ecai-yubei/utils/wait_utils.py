from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(browser, locator, timeout=10):
    """等待元素可点击"""
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def wait_for_element_visible(browser, locator, timeout=10):
    """等待元素可见"""
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_and_click(browser, locator, timeout=10):
    """等待并点击元素"""
    element = wait_for_element(browser, locator, timeout)
    element.click()

def wait_and_send_keys(browser, locator, text, timeout=10):
    """等待元素并输入文本"""
    element = wait_for_element(browser, locator, timeout)
    element.clear()
    element.send_keys(text)


def wait_and_upload_file(browser, locator, file_path, timeout=10):
    """等待文件上传元素并上传文件（支持单文件和多文件）"""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    # presence_of_element_located能检测到DOM中隐藏不可点击的元素
    element = WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )

    # 支持文件路径列表，自动转换为换行分隔
    if isinstance(file_path, list):
        file_path = "\n".join(file_path)

    element.send_keys(file_path)


def wait_for_dialog_to_close(browser, timeout=120):
    """等待弹窗关闭"""
    try:
        WebDriverWait(browser, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "el-overlay-dialog"))
        )
        print("弹窗已关闭")
    except Exception as e:
        print(f"等待弹窗关闭超时: {e}")