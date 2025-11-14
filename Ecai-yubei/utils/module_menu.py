import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def module_menu(browser, partner_menu, son_menu):
    # 判断是否有子菜单
    if son_menu is not None:
        main_menu_button = browser.find_element(By.XPATH, f"//span[text()='{partner_menu}']/..")
        # 主菜单展开选择子菜单
        if is_menu_expanded(partner_menu):
            son_menu_button = browser.find_element(By.XPATH, f"//li[contains(@class, 'el-menu-item')][.//span[text()='{son_menu}']]")
            son_menu_button.click()
            time.sleep(1)
        else:
            main_menu_button.click()
            son_menu_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[@class='el-menu-item'][.//span[text()='{son_menu}']]"))
            )
            son_menu_button.click()
            time.sleep(1)
    else:
        main_menu_button = browser.find_element(By.XPATH, f"//li[@class='el-menu-item submenu-title-noDropdown']//span[text()='{partner_menu}']")
        main_menu_button.click()
        time.sleep(1)


def is_menu_expanded(browser, partner_menu) -> bool:
    try:
        menu_element = browser.find_element(By.XPATH, f"//span[text()='{partner_menu}']/..")

        # 找到箭头元素
        arrow_icon = menu_element.find_element(By.CSS_SELECTOR, ".el-sub-menu__icon-arrow")

        # 检查transform样式
        style = arrow_icon.get_attribute("style")

        # rotateZ(180deg)表示展开，transform: none表示折叠
        return "rotateZ(180deg)" in style

    except Exception as e:
        print(f"判断菜单状态时出错: {e}")
        return False
