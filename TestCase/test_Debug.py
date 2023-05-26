import allure
from Common.CommonFuntion import *
from Common.AssertResult import *

check_data = GetExcelData()
assert_data = AssertOutput()

path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class TestDemo:

    @allure.feature('pytest_debug')
    @allure.title("Testcase_1")  # 设置case的名字
    @allure.description("""测试前的描述""")  # 添加描述
    def test_demo1(self, login_session, fixture_with_conftest_step):
        case_name = "test case 1"
        excel_name = "testDemo.xls"
        data = check_data.getXlsData(case_name, excel_name)
        assert_data.assertText(data)
        # 运行完之后替换测试前的描述
        allure.dynamic.description("这是最后的描述")

    # 添加附件
    @allure.feature('pytest_debug')
    @allure.title("Testcase_2")
    @allure.description('前置附件' + '\n' + '测试附件' + '\n' + '后置附件')  # 添加描述
    @allure.link("www.zhihu.com", "这是该功能链接")
    @allure.testcase("www.baidu.com", "权限管理功能")
    @allure.issue("www.zhiliaol.com", "权限管理异常")
    def test_demo2(self, login_session, attach_file_in_module_scope_fixture_with_finalizer):
        # 测试body添加附件
        allure.attach('<head></head><body> 一个HTML页面, </body>', 'Attach with HTML type', allure.attachment_type.HTML)
        allure.attach.file(path_dir + '/TestCase/index.html', attachment_type=allure.attachment_type.HTML)
        case_name = "test case 2"
        excel_name = "testDemo.xls"
        data = check_data.getXlsData(case_name, excel_name)
        assert_data.assertText(data)

    @allure.feature('pytest_debug')
    @allure.story("pytest_debug_story")
    @allure.title("Testcase_3")
    def test_demo3(self, login_session):
        case_name = "test case 3"
        excel_name = "testDemo.xls"
        data = check_data.getXlsData(case_name, excel_name)
        assert_data.assertText(data)

    @allure.story("pytest_debug_story")
    @allure.title("Testcase_4_body_attachment")
    def test_multiple_attachments(self):
        allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
        allure.attach.file(path_dir + '/TestCase/index.html', attachment_type=allure.attachment_type.HTML)

# pytest --allure-features pytest_debug --allure-stories pytest_debug_story
# >pytest test_Debug.py --allure-features pytest_debug --allure-stories pytest_debug_story
