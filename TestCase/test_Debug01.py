import allure
from Common.CommonFuntion import *
from Common.AssertResult import *

check_data = GetExcelData()
assert_data = AssertOutput()


class TestDemo:

    @allure.feature('pytest_debug03')
    def test_demo3(self, login_session):
        case_name = "test case 3"
        excel_name = "testDemo.xls"
        data = check_data.getXlsData(case_name, excel_name)
        assert_data.assertText(data)
