import pytest
#如果实现部分前后置，则不能加autouse = true


from common.yaml_util import clean_yaml
from testcases.test_api import TestApi


@pytest.fixture(scope="session",autouse=True)
def execute_database_sql():
    # 前置
    print("在所有请求之前执行一次")
    clean_yaml()
    yield
    # 后置
    print("在所有请求之后执行一次")
    # TestApi().test_loginOut()
