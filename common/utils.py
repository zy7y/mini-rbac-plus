from typing import Any, Dict, List

# 源数据类型
SourceList = List[Dict[str, Any]]

SourceTree = SourceList


def list2tree(
    arr: SourceList, parent_name: str = "pid", children_name: str = "children"
) -> SourceTree:
    """
    列表转嵌套树
    :param arr: 传入的list
    :param parent_name: 关系的key名
    :param children_name: 嵌套数据使用的key名
    :return:
    """
    # 1. 将列表转换成字典，列表中元素的唯一标识作为key，列表元素作为value
    menu_map = {item["id"]: item for item in arr}

    tree = []
    for item in arr:

        if item.get(parent_name) is None:
            # 根节点
            tree.append(item)
        else:
            menu_item = menu_map.get(item[parent_name])
            if menu_item is None:
                break
            # 子节点
            if menu_item.get(children_name) is None:
                menu_item[children_name] = []
            menu_item[children_name].append(item)
    return tree


"""
pip install passlib bcrypt
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码 vs hash密码
    :param plain_password: 明文密码
    :param hashed_password: hash密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    加密明文
    :param password: 明文密码
    :return:
    """
    return pwd_context.hash(password)
