
import pytest
from pytest_encode import logger


@pytest.mark.parametrize("name", ["哈利", "赫敏"])
def test_a(name):
    logger.info(f"测试数据: {name}")
    print(name)