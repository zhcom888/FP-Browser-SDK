from .module import Module
from .browser_enum import Floatinfinity
import random


class Battery(Module):
    def __init__(self):
        super(Battery, self).__init__()
        self._charging = False
        self._charging_time = None
        self._discharging_time = None
        self._level = None
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "battery-manager.charging": self._bool_to_int(self._charging),
            "battery-manager.charging-time": self._charging_time,
            "battery-manager.discharging-time": self._discharging_time,
        }

        if self._level is not None:
            if 0 < self._level <= 100:
                result["battery-manager.level"] = round(self._level / 100, 2)
            elif self._level == 0:
                result["battery-manager.level"] = 0.0
            else:
                self._level = None

        return result

    def set_charging(self, value: bool):
        """
        是否正在充电
        """
        self._charging = value
        return self

    def set_charging_time(self, value: float):
        """
        距离充电完毕还需多少秒
        """
        self._charging_time = value
        return self

    def set_discharging_time(self, value: float):
        """
        距离电池耗电至空且挂起需要多少秒
        """
        self._discharging_time = value
        return self

    def set_level(self, value: int):
        """
        电量
        """
        self._level = value
        return self

    def generate(self):
        """
        随机生成电量信息
        """
        chargin = False
        level = random.randint(10, 100)

        # 如果电量低于百分之四十，则随机概率设置为充电中
        if level < 40 and self._random_bool():
            chargin = True

        # 如果是充电状态，则设置：耗完电为 INFINITY
        if chargin:
            # 生成规则是：每百分之一的电花 30~60 秒时间
            charging_time = int((100 - level) * random.randint(30, 60))
            discharging_time = Floatinfinity.INFINITY.value
        else:
            # 如果是充电状态，则设置：还需要充电完成的时间为 INFINITY
            charging_time = Floatinfinity.INFINITY.value
            discharging_time = int(level * random.randint(150, 180))

            # 如果电量大于 65，则还是设置成：INFINITY
            if level >= 65:
                discharging_time = Floatinfinity.INFINITY.value

        # 如果电量为 100，则设置还需要充电完成的时间为 INFINITY，还有耗完电为 INFINITY
        if level == 100:
            # 有概率的充电时间为 0
            if self._random_bool():
                charging_time = Floatinfinity.INFINITY.value
                discharging_time = Floatinfinity.INFINITY.value
            else:
                charging_time = 0
                discharging_time = Floatinfinity.INFINITY.value

        self.set_charging(chargin)
        self.set_charging_time(charging_time)
        self.set_discharging_time(discharging_time)
        self.set_level(level)

        return self
