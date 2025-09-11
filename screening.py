import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def screening(browser,
              name: str = None,
              script_type: str = None,
              production_name: str = None,
              department: str = None,
              start_date: str = None,
              end_date: str = None,
              ):

    """ 学员名称 """
    if name is not None:
        try:
            name_content= WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//input[contains(@class, 'el-input__inner') and contains(@placeholder, '搜索姓名')]"))
        )
            name_content.send_keys(name)
            name_content.send_keys(Keys.ENTER)
            time.sleep(0.5)
        except Exception as e:
            print(f"学员名称输入错误:{e}")

    """ 时间筛选 """
    if start_date is not None and end_date is not None:
        # 开始日期
        try:
            start_date_content = browser.find_elements(By.CLASS_NAME, "el-range-input")
            start_date_content[0].click()
            start_date_content[0].send_keys(Keys.CONTROL + "a")
            start_date_content[0].send_keys(start_date)
            time.sleep(0.5)

        # 结束日期
            end_date_content = browser.find_elements(By.CLASS_NAME, "el-range-input")
            end_date_content[1].click()
            end_date_content[1].send_keys(Keys.CONTROL + "a")
            end_date_content[1].send_keys(end_date)
            end_date_content.send_keys(Keys.ENTER)
            time.sleep(0.5)
        except Exception as e:
            print(f"日期输入错误：{e}")
    elif start_date is not None or end_date is not None:
        print("警告: 需要同时提供开始日期和结束日期")

    """ 脚本类型 """
    if script_type is not None:
        # 点击脚本类型，弹出下拉框
        try:
            script_type_select_element = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//div[contains(@class, 'el-select__selected-item') and contains(@class, 'el-select__placeholder') and contains(@class, 'is-transparent') and contains(., '数据类型')]"))
            )
            script_type_select_element.click()
            time.sleep(0.5)
        except Exception as e:
            print(f"弹出脚本类型下拉框失败:{e}")

        # 等待选项出现并点击指定的选项
        try:
            script_type_option = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[@class='el-select-dropdown__item' and contains(., '{script_type}')]"))
            )
            script_type_option.click()
            time.sleep(0.5)
        except Exception as e:
            print(f"脚本类型下拉框选择失败:{e}")

    """ 产品名称 """
    if production_name is not None:
        #点击产品名称，弹出下拉框
        try:
            production_name_select_element = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//div[contains(@class, 'el-select__selected-item') and contains(@class, 'el-select__placeholder') and contains(@class, 'is-transparent') and contains(., '产品名称')]"))
            )
            production_name_select_element.click()
            time.sleep(0.5)
        except Exception as e:
            print(f"弹出产品名称下拉框失败:{e}")

        try:
            # 等待选项出现并点击指定的选项
            production_name_option = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[@class='el-select-dropdown__item' and contains(., '{production_name}')]"))
            )
            production_name_option.click()
            time.sleep(0.5)
        except Exception as e:
            print(f"产品名称下拉框选择失败:{e}")

    """ 部门 """
    # 功能未写完，勿用
    if department is not None:
        # 点击部门，弹出下拉框
        try:
            department_select_element = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//div[contains(@class, 'el-select__selected-item') and contains(., '请选择部门')]"))
            )
            department_select_element.click()
            time.sleep(0.5)
        except Exception as e :
            print(f"弹出部门下拉框失败:{e}")

        # 等待选项出现并点击指定的选项，考虑通过接口传输，网页模拟太过麻烦
        try:
            department_option = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,f"//li[@class='el-select-dropdown__item' and contains(., '{department}')]"))
            )
            department_option.click()
            time.sleep(0.5)
        except Exception as e:
            print(f"部门下拉框选择失败:{e}")



