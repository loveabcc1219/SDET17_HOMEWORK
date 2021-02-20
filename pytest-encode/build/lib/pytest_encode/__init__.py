# -*- coding:utf-8 -*-

from typing import List
import logging
import pytest

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s (filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt="%a, %d %b %Y %H:%M:%S",
                    filename='report.log',
                    filemode='w'
                    )
logger = logging.getLogger(__name__)

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)


    for item in items:
        # 用例名称支持中文
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        logger.info(f"item.name : {item.name}")
        logger.info(f"item._nodeid : {item._nodeid}")



