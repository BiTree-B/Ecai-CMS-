"""
from locators.script_management import script_management
from utils.login import test_window_size, test_login
from tests.send_msg import send_msg
from utils.module_menu import module_menu


def test_main_flow(browser):

    
    # 发送通知测试
    print("开始测试主要流程...")
    test_window_size(browser)
    test_login(browser)
    module_menu(browser, partner_menu='脚本管理', son_menu=None)

    script_create_button = browser.find_element(*script_management.SCRIPT_CREATE)
    script_create_button.click()
    qa_select_button = browser.find_element(*script_management.QA_SELECT)
    qa_select_button.click()

    print("所有测试完成！")
    



'''
if __name__ == "__main__":
    pytest.main([__file__ , "-v", "-s"])
'''
"""

