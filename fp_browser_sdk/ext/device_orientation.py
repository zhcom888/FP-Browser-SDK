from .module import Module


class DeviceOrientation(Module):
    def __init__(self):
        super(DeviceOrientation, self).__init__()
        self._alpha = None
        self._alpha_left = None
        self._alpha_right = None
        self._beta = None
        self._beta_left = None
        self._beta_right = None
        self._gamma = None
        self._gamma_left = None
        self._gamma_right = None
        self._absolute = None
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "device-orientation.alpha": self._alpha,
            "device-orientation.alpha-left": self._alpha_left,
            "device-orientation.alpha-right": self._alpha_right,
            "device-orientation.beta": self._beta,
            "device-orientation.beta-left": self._beta_left,
            "device-orientation.beta-right": self._beta_right,
            "device-orientation.gamma": self._gamma,
            "device-orientation.gamma-left": self._gamma_left,
            "device-orientation.gamma-right": self._gamma_right,
            "device-orientation.absolute": self._bool_to_int(self._absolute),
        }

        return result

    def set_alpha(self, value: float, left: float = None, right: float = None):
        """
        alpha 旋转速度
        """
        self._alpha = value
        self._alpha_left = left
        self._alpha_right = right
        return self

    def set_beta(self, value: float, left: float = None, right: float = None):
        """
        beta 旋转速度
        """
        self._beta = value
        self._beta_left = left
        self._beta_right = right
        return self

    def set_gamma(self, value: float, left: float = None, right: float = None):
        """
        gamma 旋转速度
        """
        self._gamma = value
        self._gamma_left = left
        self._gamma_right = right
        return self

    def set_absolute(self, value: bool):
        """
        外网 IP
        """
        self._absolute = value
        return self
