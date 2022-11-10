from abc import ABCMeta, abstractmethod
from urllib.parse import urlparse
import socket
import random


class Module(object):
    __metaclass__ = ABCMeta  # 指定这是一个抽象类

    def __init__(self):
        self.raw = {}

    def set_raw(self, key, value):
        """
        设置原始的值
        """
        self.raw[key] = value
        return self

    @abstractmethod  # 抽象方法
    def _to_dict(self):
        """
        解析成 dict
        """
        pass

    def to_dict(self):
        """
        解析成 dict
        """
        # if hasattr(self.__class__, 'after') and callable(getattr(self.__class__, 'after')):
        #     pass

        result = {**self.raw, **self._to_dict()}
        data = {}
        for (key, item) in result.items():
            if item is not None:
                # 强制转换类型
                if isinstance(item, (int, float)):
                    item = str(item).strip()
                elif isinstance(item, list) and len(item) == 0:
                    continue
                elif isinstance(item, dict) and len(item) == 0:
                    continue

                # 去除空格
                data[key.strip()] = item

        return data

    def _bool_to_int(self, value: bool):
        """
        bool 类型转 int
        """
        if value:
            return 1
        else:
            return 0

    def _verify_url(self, value, allow_empty=True):
        """
        验证 url 是否合法
        """
        if allow_empty and value is None:
            return True

        try:
            result = urlparse(value)

            return all([result.hostname, result.netloc])
        except:
            pass

        return False

    def _verify_ip(self, value, allow_empty=True):
        """
        验证 ip 是否合法
        """

        if allow_empty and value is None:
            return True

        try:
            socket.inet_aton(value)
            return True
        except socket.error:
            pass
        return False

    def _is_number(self, s):
        """
        是否是数字
        """
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def _random_bool(self):
        """
        随机一个 bool 值
        """
        return random.randint(0, 1) == 1
