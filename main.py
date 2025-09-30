from login import test_window_size, test_login
from send_msg import send_msg


def test_main_flow(browser):

    
    # 发送通知测试
    print("开始测试主要流程...")
    test_window_size(browser)
    test_login(browser)
    send_msg(browser,name = "your name")
    print("所有测试完成！")
    



'''
if __name__ == "__main__":
    pytest.main([__file__ , "-v", "-s"])
'''

