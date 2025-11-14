import os
from datetime import datetime
import time
from conftest import browser
from locators.script_management import ScriptManagement
from locators.script_management import QaPage
from utils.login import test_window_size, test_login
from utils.module_menu import module_menu
from utils.screenshot import take_screenshot
from utils.wait_utils import wait_and_click, wait_for_element, wait_and_send_keys, wait_and_upload_file, \
    wait_for_dialog_to_close, wait_for_element_visible


def test_main_flow(browser):
    print("开始测试...")


    """登录"""
    test_window_size(browser)
    test_login(browser)


    """选择模块"""
    module_menu(browser, partner_menu='脚本管理', son_menu=None)
    wait_and_click(browser, ScriptManagement.SCRIPT_CREATE)
    wait_and_click(browser, ScriptManagement.QA_SELECT)

    # 时间
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


    """写入脚本基本信息"""
    # 空内容保存校验并截图
    wait_and_click(browser, QaPage.SAVE)
    time.sleep(0.5)
    take_screenshot(browser,"nullcontext","test")

    # 脚本名称
    qa_script_name = wait_for_element(browser, QaPage.QA_SCRIPT_NAME)
    qa_script_name.send_keys(f"自动测试_{timestamp}")

    # 产品名称
    product_name = "爱全乐"
    product = browser.find_element(*QaPage.PRODUCT)
    product.send_keys(product_name)
    wait_and_click(browser, QaPage.PRODUCT_LIST(product_name=product_name))

    # 适用对象
    applicable_object = "医药代表"
    wait_and_click(browser, QaPage.APPLICABLE_OBJECT)
    wait_and_click(browser, QaPage.APPLICABLE_OBJECT_LIST(applicable_object=applicable_object))

    # 选择绑定E人
    e_name = "赵婷"
    wait_and_click(browser, QaPage.E_BIND)
    wait_and_click(browser, QaPage.E_SELECT(e_name=e_name))
    wait_and_click(browser, QaPage.E_SURE)

    # 提问方式
    q_method = "按顺序提问"
    wait_and_click(browser, QaPage.Q_METHOD)
    wait_and_click(browser, QaPage.Q_METHOD_LIST(q_method=q_method))

    #时间限制设置
    time_limit_type = "限制整体时长"
    time_limit_type1 = "限制单题时长"
    time_set = "30"
    wait_and_click(browser, QaPage.TIME_LIMIT_TYPE(time_limit_type=time_limit_type))
    wait_and_send_keys(browser, QaPage.TIME_SET(type="0"),time_set)
    time.sleep(1)
    take_screenshot(browser,"30秒","限制整体时长-")

    wait_and_click(browser,QaPage.TIME_LIMIT_TYPE(time_limit_type=time_limit_type1))
    wait_and_click(browser,QaPage.TIME_SET(type="1"))#自动设置单题时长
    time.sleep(1)
    take_screenshot(browser, "自动设置时长", "限制单题时长-")

    wait_and_click(browser,QaPage.TIME_SET(type="2"),time_set)
    wait_and_send_keys(browser,QaPage.TIME_SET(type="2-1"),time_set)#手动设置单题统一时长
    time.sleep(1)
    take_screenshot(browser, "手动设置单题统一时长30秒", "限制单题时长-")

    wait_and_click(browser,QaPage.TIME_SET(type="3"),time_set)
    wait_and_send_keys(browser,QaPage.TIME_SET(type="3-1"),time_set)#手动设置每题时长
    time.sleep(1)
    take_screenshot(browser,"手动设置每题时长30秒","限制单题时长-")

    wait_and_click(browser, QaPage.TIME_LIMIT_TYPE(time_limit_type=time_limit_type))
    wait_and_send_keys(browser, QaPage.TIME_SET(type="0"),time_set)


    """增加题目"""
    #简答题
    wait_and_send_keys(browser, QaPage.QUESTION(question_number="问题1"),text="简答题题目")
    wait_and_send_keys(browser,QaPage.SHORT_ANSWER(question_number="问题1"),text="简答题答案")

    # 滚动到页面底部
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #选择题
    wait_and_click(browser,QaPage.ADD_CHOICE_QUESTION)
    wait_and_send_keys(browser,QaPage.QUESTION(question_number="问题2"),text="选择题题目")
    wait_and_send_keys(browser,QaPage.CHOICE_QUESTION_ANSWER(question_number="问题2",answer_type="正确选项"),text="正确选项1")
    wait_and_send_keys(browser,QaPage.CHOICE_QUESTION_ANSWER(question_number="问题2",answer_type="错误选项"),text="错误选项1")

    #批量导入
    file_path = os.path.expanduser(f"~/Downloads/答题导入模板.xlsx")
    wait_and_click(browser,QaPage.BATCH_IMPORT_QUESTION)
    wait_and_click(browser,QaPage.DOWNLOAD_TEMPLATE)
    wait_and_upload_file(browser,QaPage.UPLOAD_FILE_SINGLE,file_path)
    wait_and_click(browser,QaPage.RESELECT)#重新选择文件
    print("重新选择文件")
    wait_and_upload_file(browser, QaPage.UPLOAD_FILE_SINGLE, file_path)
    wait_and_click(browser,QaPage.IMPORT_BUTTON)

    #AI生成
    file_path_AI = os.path.expanduser(f"~/Downloads/答题导入模板 (1).xlsx")
    time.sleep(0.5)
    wait_and_click(browser, QaPage.GENERATE_AI)
    wait_and_upload_file(browser, QaPage.UPLOAD_FILE_MULTIPLE, file_path_AI)
    time.sleep(0.5)
    take_screenshot(browser,"校验","单文件上传")
    wait_and_click(browser,QaPage.START_GENERATE)

    # 保存
    wait_for_dialog_to_close(browser)
    #wait_for_element_visible(browser,QaPage.CHECK_ALL,180)
    time.sleep(5)
    wait_and_click(browser,QaPage.CHECK_ALL,120)
    wait_and_click(browser,QaPage.SURE)
    wait_and_click(browser,QaPage.SAVE)

    print("测试完成")


