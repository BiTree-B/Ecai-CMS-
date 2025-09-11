import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from screening import screening
from screenshot import take_screenshot


def send_msg(browser,
              name: str = None,
              script_type: str = None,
              production_name: str = None,
              department: str = None,
              start_date: str = None,
              end_date: str = None,
              ):

    # 发送通知按钮
    msg_button = browser.find_element(By.CSS_SELECTOR, ".el-button.el-button--default")
    msg_button.click()

    time.sleep(1)

    # 筛选
    screening(browser,
              name,
              script_type,
              production_name,
              department,
              start_date,
              end_date,
              )

    # 点击全选按钮选中发送通知对象
    checkbox_inner = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label.el-checkbox--large .el-checkbox__inner"))
    )
    checkbox_inner.click()
    time.sleep(0.5)

    # “下一步，填写通知内容”按钮
    msg_next_button = browser.find_element(
        By.CSS_SELECTOR,
        ".el-button.el-button--primary.el-button--default.mx-1"
    )
    msg_next_button.click()
    time.sleep(1)

    # 填写发送通知内容并进行发送
    # 通知标题元素
    msg_title = browser.find_element(By.CLASS_NAME, "el-input__inner")
    # 通知正文元素
    msg_content = browser.find_element(By.CLASS_NAME, "el-textarea__inner")

    # 超长内容校验
    msg_title.send_keys("123456789012345678901234567890")
    msg_content.send_keys("123456789012345678901234567890")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    take_screenshot(browser,prefix="max_content_",name="test")

    # 清除内容
    msg_title.clear()
    msg_content.clear()

    # 正式填写发送内容
    msg_title.send_keys("测试")
    msg_content.send_keys(f"测试_{timestamp}")

    # 发送通知
    msg_post_button = browser.find_element(By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--default")
    msg_post_button.click()
    time.sleep(1)

    # 完成按钮
    msg_fin_button = browser.find_element(By.CSS_SELECTOR,".el-button.el-button--primary.el-button--default")

    # 验证
    assert "msg_title" and "msg_content" not in browser.current_url
    print("发送通知成功")

    # 退出发送通知界面
    msg_fin_button.click()
