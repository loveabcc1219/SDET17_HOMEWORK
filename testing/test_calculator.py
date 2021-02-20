
# -*- coding: utf-8 -*-
import allure
import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas(operate_method='add', case_set='int'):
    '''
    从yml文件中获取用例数据
    :param operate_method: 运算方法：[add, div]
    :param case_set: 用例集名称
    :return: 用例数据及ids
    '''
    with open("./datas/calculator.yml", encoding="utf-8") as f:
        all_datas = yaml.safe_load(f)

    mydata = all_datas[operate_method][case_set]['datas']
    ids = all_datas[operate_method][case_set]['ids']
    return mydata, ids

@pytest.fixture
def get_instance():
    print("开始计算...")
    calc = Calculator()
    yield calc
    print("结束计算!")

add_int_data, add_int_ids = get_datas('add', 'int')
@pytest.fixture(params=add_int_data, ids=add_int_ids)
def get_add_int(request):   # 获取【加法-整型】用例
    return request.param

add_float_data, add_float_ids = get_datas('add', 'float')
@pytest.fixture(params=add_float_data, ids=add_float_ids)
def get_add_float(request):   # # 获取【加法-浮点型】用例
    return request.param

add_negative_data, add_negative_ids = get_datas('add', 'negative')
@pytest.fixture(params=add_negative_data, ids=add_negative_ids)
def get_add_negative(request):  # # 获取【加法-反面】用例
    return request.param

div_int_data, div_int_ids = get_datas('div', 'int')
@pytest.fixture(params=div_int_data, ids=div_int_ids)
def get_div_int(request):   # 获取【除法-整型】用例
    return request.param

div_float_data, div_float_ids = get_datas('div', 'float')
@pytest.fixture(params=div_float_data, ids=div_float_ids)
def get_div_float(request):   # # 获取【除法-浮点型】用例
    return request.param

div_negative_data, div_negative_ids = get_datas('div', 'negative')
@pytest.fixture(params=div_negative_data, ids=div_negative_ids)
def get_div_negative(request):  # # 获取【除法-反面】用例
    return request.param

div_div_by_0_data, div_div_by_0_ids = get_datas('div', 'div_by_0')
@pytest.fixture(params=div_div_by_0_data, ids=div_div_by_0_ids)
def get_div_by_0(request):  # # 获取【除法-除数为0异常】用例
    return request.param

@allure.feature("加法&除法 功能")
class TestCalc(object):

    @allure.story("加法_整型")
    # @allure.title("title整型加法运算测试")    # allure报告中，会覆盖ids
    def test_add_int(self, get_instance, get_add_int):
        a, b, result = get_add_int
        print(f"a={a}, b={b}, result={result}")
        assert  result == get_instance.add(a,b)

    @allure.story("加法_浮点型")
    def test_add_float(self, get_instance, get_add_float):
        a, b, result = get_add_float
        print(f"a={a}, b={b}, result={result}")
        assert result == get_instance.add(a, b)

    @allure.story("加法_反面用例")
    def test_add_negative(self, get_instance, get_add_negative):
        a, b, result = get_add_negative
        print(f"a={a}, b={b}, result={result}")
        assert result != get_instance.add(a, b)

    @allure.story("除法_整型")
    # @allure.title("title整型加法运算测试")    # allure报告中，会覆盖ids
    def test_div_int(self, get_instance, get_div_int):
        a, b, result = get_div_int
        print(f"a={a}, b={b}, result={result}")
        assert result == get_instance.div(a, b)

    @allure.story("除法_浮点型")
    def test_div_float(self, get_instance, get_div_float):
        a, b, result = get_div_float
        print(f"a={a}, b={b}, result={result}")
        assert result == get_instance.div(a, b)

    @allure.story("除法_反面用例")
    def test_div_negative(self, get_instance, get_div_negative):
        a, b, result = get_div_negative
        print(f"a={a}, b={b}, result={result}")
        assert result != get_instance.div(a, b)

    @allure.story("除法_除数为0异常")
    def test_div_by_0(self, get_instance, get_div_by_0):
        a, b, result = get_div_by_0
        with pytest.raises(ZeroDivisionError):
            a/b

if __name__ == '__main__':
    pass