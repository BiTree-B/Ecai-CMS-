from selenium.webdriver.common.by import By


class ScriptManagement(object):

    # 创建脚本按钮
    SCRIPT_CREATE = (By.XPATH,"//button[contains(@class, 'el-button--primary')]//span[text()='创建脚本']")

    # 创建QA脚本按钮
    QA_SELECT = (By.XPATH,"//button[contains(@class, 'el-button el-button--primary el-button--large script-type-title')]//span[text()='异议处理']")

    # 创建PPT脚本按钮
    PPT_SELECT = (By.XPATH,"//button[contains(@class,'el-button el-button--primary el-button--large script-type-title')]//span[text()='科室会']")


class QaPage(object):

    # 保存按钮
    SAVE = (By.XPATH,"//button[contains(@class, 'el-button el-button--primary el-button--default')]//span[text()='保存']")

    # 脚本名称文本框
    QA_SCRIPT_NAME = (By.XPATH,"//label[contains(., '脚本名称')]/following-sibling::div//input[@placeholder='请输入']")

    # 产品
    PRODUCT = (By.XPATH,"//label[text()='产品']/following-sibling::div//input[@class='el-select__input is-default']")

    @staticmethod
    def PRODUCT_LIST(product_name):
        return By.XPATH, f"//li[@class='el-select-dropdown__item']//span[text()='{product_name}']"

    # 适用对象
    APPLICABLE_OBJECT = (By.XPATH,"//label[contains(.,'适用对象')]/following-sibling::div//div[@class='el-select__wrapper el-tooltip__trigger el-tooltip__trigger']")

    @staticmethod
    def APPLICABLE_OBJECT_LIST(applicable_object):
        return By.XPATH, f"//li[@class='el-select-dropdown__item']//span[text()='{applicable_object}']"

    # 绑定E人
    E_BIND = (By.XPATH,"//button[@class='el-button el-button--primary el-button--default is-plain']//span[@class='' and text()='选择']")

    @staticmethod
    def E_SELECT(e_name):
        return By.XPATH, f"//div[contains(text(), '{e_name}') and contains(@class, 'user-name')]/ancestor::div[@class='eMan-item flex column']"

    E_SURE = (By.XPATH,"//button[@class='el-button el-button--primary el-button--default']//span[text()='确 定']")

    # 提问方式
    Q_METHOD = (By.XPATH,"//label[text()='提问方式']/following-sibling::div//div[@class='el-select__selected-item el-select__placeholder is-transparent']")

    @staticmethod
    def Q_METHOD_LIST(q_method):
        return By.XPATH, f"//li[contains(@class,'el-select-dropdown__item')]//span[text()='{q_method}']"

    # 时长限制方式
    @staticmethod
    def TIME_LIMIT_TYPE(time_limit_type):
        return By.XPATH, f"//div[contains(@class, 'radio-box') and contains(text(), '{time_limit_type}')]"

    """
    时长设置
        0：限制整体时长，设定总时长输入框，使用wait_and_send_keys
        1：限制单题时长，自动设置时长时长按钮，使用wait_and_click
        2：限制单题时长，统一设置时长按钮，使用wait_and_click
        2-1：限制单题时长，统一设置时长输入框，使用wait_and_send_keys
        3：限制单题时长，手动设置每题时长按钮，使用wait_and_click
        3-1:限制单题时长，手动设置每题时长输入框，使用wait_and_send_keys,一般获取所有输入框
    """
    @staticmethod
    def TIME_SET(type):
        match type:
            case '0':
                return By.XPATH, "//label[contains(., '整体时限')]/following-sibling::div//input[@class='el-input__inner']"
            case '1':
                return By.XPATH, "//label[contains(@class, 'el-radio')]//span[contains(@class, 'el-radio__label')]//div[contains(text(), '自动设置')]"
            case '2':
                return By.XPATH, "//label[contains(@class, 'el-radio')]//span[contains(@class, 'el-radio__label')]//div[contains(text(), '统一设置')]"
            case '2-1':
                return By.XPATH, "//label[contains(., '单题时限')]/following-sibling::div//input[@class='el-input__inner']"
            case '3':
                return By.XPATH, "//label[contains(@class, 'el-radio')]//span[contains(@class, 'el-radio__label')]//div[contains(text(), '手动设置')]"
            case '3-1':
                return By.XPATH, "//input[@placeholder='时限' and @class='el-input__inner']"

    # 添加简答题
    ADD_SHORT_ANSWER = (By.XPATH,"//button[contains(@class,'el-button el-button--primary el-button--default is-plain btn jd')]//span[@class='' and text()=' 添加简答题']")

    # 添加选择题
    ADD_CHOICE_QUESTION = (By.XPATH,"//button[contains(@class,'el-button el-button--primary el-button--default is-plain btn xz')]//span[@class='' and text()=' 添加选择题']")

    # 批量导入
    BATCH_IMPORT_QUESTION = (By.XPATH,"//button[contains(@class,'el-button el-button--primary el-button--default is-plain btn dr')]//span[@class='' and text()=' 批量导入']")

    # AI生成
    GENERATE_AI = (By.XPATH,"//button[contains(@class,'el-button el-button--primary el-button--default is-plain btn ai')]//span[@class='' and text()=' AI生成']")

    # 题目输入框
    @staticmethod
    def QUESTION(question_number):
        return By.XPATH, f"//label[text()='{question_number}']/following-sibling::div//input[@class='el-input__inner']"

    # 简答题答案输入框
    @staticmethod
    def SHORT_ANSWER(question_number):
        return By.XPATH, f"//label[text()='{question_number}']/../following-sibling::div//textarea[@placeholder='请输入参考答案']"

    # 选择题答案输入框
    @staticmethod
    def CHOICE_QUESTION_ANSWER(question_number,answer_type):
        return By.XPATH, f"//label[text()='{question_number}']/../following-sibling::div//label[contains(normalize-space(), '{answer_type}')]/following-sibling::div//input[@class='el-input__inner' and @placeholder='请输入']"

    # 批量导入中的导入文件
    UPLOAD_FILE_SINGLE = (By.CSS_SELECTOR, "input.el-upload__input[name='file'][type='file']")

    # AI生成中的导入文件
    UPLOAD_FILE_MULTIPLE = (By.CSS_SELECTOR, "input.el-upload__input[name='files'][type='file']")

    # 下载模版
    DOWNLOAD_TEMPLATE = (By.XPATH,"//button[@class='el-button el-button--primary el-button--default']//span[text()='下载模板表格']")

    # 批量导入中“导入”按钮
    IMPORT_BUTTON = (By.XPATH,"//button[contains(@class,'el-button el-button--primary el-button--default')]//span[text()='导入']")

    # AI生成中“开始生成”按钮
    START_GENERATE = (By.XPATH,"//button[contains(@class,'el-button el-button--primary el-button--default')]//span[text()='开始生成']")

    # 批量导入中“重新选择”按钮
    RESELECT = (By.XPATH, "//button//span[text()='重新选择']")

    # AI生成中取消按钮
    CANCEL = (By.XPATH, "//button//span[text()='取 消']")

    # 批量导入中的取消按钮
    CANCEL_BATCH = (By.XPATH, "//button//span[text()='取消']")

    # AI生成题目结果中全选
    CHECK_ALL = (By.XPATH, "//label[contains(@class, 'el-checkbox')]//span[text()='全选']/..")

    # AI生成题目结果中的“关 闭”按钮
    CLOSE = (By.XPATH, "//button[contains(@class, 'el-button')]//span[text()='关 闭']")

    # AI生成题目结果中的“确 定”按钮
    SURE = (By.XPATH, "//button[contains(@class, 'el-button--primary')]//span[text()='确 定']/..")

class PPTScript(object):

    # 产品输入框
    PRODUCT = (By.XPATH,"//label[text()='产品']/following-sibling::div//input[@class='el-select__input is-default']")

    @staticmethod
    def PRODUCT_SELECT(product_name):
        return By.XPATH,f"//li[@class='el-select-dropdown__item']//span[text()='{product_name}']"

    # 上传文件
    UPLOAD_FILE = (By.CSS_SELECTOR, "input.el-upload__input[name='file'][type='file']")

    # AI处理
    AI_PROCESS = (By.XPATH, "//label[contains(@class, 'el-checkbox')]//span[contains(text(), 'AI处理')]")

    # 取消
    CANCEL = (By.XPATH,"//buttton[@class='el-button el-button--default']//span[text()='取 消']")

    # 确定
    SURE = (By.XPATH, "//buttton[@class='el-button el-button--primary el-button--default']//span[text()='确 定']")

    # 幻灯片名称
    PPT_NAME = (By.XPATH,"//label[@class='el-form-item__label' and .,'幻灯片名称']/"
                         ""
                         "following-sibling::div//input[@class='el-input__inner' and  @placeholder='请输入']")