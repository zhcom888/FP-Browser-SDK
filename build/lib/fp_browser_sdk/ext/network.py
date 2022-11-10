from .module import Module
from .browser_enum import WebEffectiveConnectionType, WebConnectionType, Floatinfinity
import random


class Network(Module):
    def __init__(self):
        super(Network, self).__init__()
        self._effective_type = WebEffectiveConnectionType.kType4G
        self._type = WebConnectionType.CELLULAR
        self._downlink = None
        self._downlink_max = None
        self._rtt = None
        self._save_data = False
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "connection.effective-type": self._effective_type.value,
            "connection.type": self._type.value,
            "connection.downlink": self._downlink,
            "connection.downlink-max": self._downlink_max,
            "connection.rtt": self._rtt,
            "connection.save-data": self._bool_to_int(self._save_data),
        }

        return result

    def set_effective_type(self, value: WebEffectiveConnectionType):
        """
        网络有效类型
        """
        self._effective_type = value
        return self

    def set_type(self, value: WebConnectionType):
        """
        网络类型
        """
        self._type = value
        return self

    def set_downlink(self, value: float):
        """
        网络下行速度
        """
        self._downlink = value
        return self

    def set_downlink_max(self, value: float):
        """
        网络最大下行速度
        """
        self._downlink_max = value
        return self

    def set_rtt(self, value: int):
        """
        估算的往返时间
        """
        self._rtt = value
        return self

    def set_save_data(self, value: bool):
        """
        打开/请求数据保护模式
        """
        self._save_data = value
        return self

    def _generate_float(self, unit: int = 5):
        """
        生成浮点小数部分
        """
        step = int(100 / 5)

        return unit * random.randint(1, step)

    def _generate_wifi_downlink(self):
        """
        随机生成一个 wifi 的 downlink
        """
        # 随机一个带宽大小
        bite_item = random.choice([[50, 100], [100, 200], [200, 300], [300, 500]])
        min_bite = bite_item[0] / 8
        max_bite = bite_item[1] / 8
        percentage = random.randint(20, 100) / 100
        rand_bite = random.uniform(min_bite * percentage, max_bite * percentage)
        # 计算
        rand_bite = int(rand_bite)
        float_bite = self._generate_float()
        return float("{}.{}".format(rand_bite, float_bite))

    def generate_connect_type(self, connection_type: WebConnectionType, effective_type: WebEffectiveConnectionType):
        """
        根据设置的值生成对应网络参数（注意：因为现在 4G 普及率很高，所以没有生产小于 4g 的网络参数）
        """
        # 强制设置成 wifi 模式
        if connection_type != WebConnectionType.CELLULAR:
            # 设置 type
            self.set_type(WebConnectionType.WIFI)
            # 设置 数据类型
            self.set_effective_type(WebEffectiveConnectionType.kType4G)
            # 设置 downlink
            self.set_downlink(self._generate_wifi_downlink())
            # 设置 downlink max
            self.set_downlink_max(Floatinfinity.INFINITY.value)
            # 设置 rtt
            self.set_rtt(random.choice([50, 100, 200, 150, 175, 225]))
        else:
            # 设置 type
            self.set_type(connection_type)
            # 设置 数据类型
            self.set_effective_type(effective_type)
            # 设置 downlink
            self.set_downlink(random.choice([1.75, 1.85, 1.65, 1.45, 1.55]))
            # 设置 downlink max
            self.set_downlink_max(100)
            # 设置 rtt
            self.set_rtt(random.choice([100, 150, 200]))

        return self
