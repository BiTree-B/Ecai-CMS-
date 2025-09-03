import pytest
from login import test_window_size, test_login
from screenshot import take_screenshot


def test_main_flow(browser):

    print("开始测试主要流程...")

    # 执行测试函数
    test_window_size(browser)
    test_login(browser)
    take_screenshot(browser,prefix="success",name="_login")
    print("所有测试完成！")

'''
if __name__ == "__main__":
    pytest.main([__file__ , "-v", "-s"])
'''