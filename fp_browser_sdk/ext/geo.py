from .module import Module


class Geo(Module):
    def __init__(self):
        super(Geo, self).__init__()
        self._longitude = None
        self._latitude = None
        self._accuracy = None
        self._altitude = None
        self._altitude_accuracy = None
        self._heading = None
        self._speed = None

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "geo.longitude": self._longitude,
            "geo.latitude": self._latitude,
            "geo.accuracy": self._accuracy,
            "geo.altitude": self._altitude,
            "geo.altitude-accuracy": self._altitude_accuracy,
            "geo.heading": self._heading,
            "geo.speed": self._speed,
        }

        return result

    def set_longitude(self, value: str):
        """
        经度
        """
        self._longitude = value
        return self

    def set_latitude(self, value: str):
        """
        纬度
        """
        self._latitude = value
        return self

    def set_accuracy(self, value: str):
        """
        经度精确值
        """
        self._accuracy = value
        return self

    def set_altitude(self, value: str):
        """
        海平面高度（无法提供时为 null）
        """
        self._altitude = value
        return self

    def set_altitude_accuracy(self, value: str):
        """
        高度精确值（无法提供时为 null）	null
        """
        self._altitude_accuracy = value
        return self

    def set_heading(self, value: str):
        """
        前进方向（无法提供时为 null）
        """
        self._heading = value
        return self

    def set_speed(self, value: str):
        """
        速度（无法提供时为 null）
        """
        self._speed = value
        return self
