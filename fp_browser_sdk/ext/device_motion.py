from .module import Module
import random


class DeviceMotion(Module):
    def __init__(self):
        super(DeviceMotion, self).__init__()

        self._interval = None
        self._x1 = None
        self._x1_left = None
        self._x1_right = None
        self._y1 = None
        self._y1_left = None
        self._y1_right = None
        self._z1 = None
        self._z1_left = None
        self._z1_right = None
        self._x2 = None
        self._x2_left = None
        self._x2_right = None
        self._y2 = None
        self._y2_left = None
        self._y2_right = None
        self._z2 = None
        self._z2_left = None
        self._z2_right = None
        self._alpha = None
        self._alpha_left = None
        self._alpha_right = None
        self._beta = None
        self._beta_left = None
        self._beta_right = None
        self._gamma = None
        self._gamma_left = None
        self._gamma_right = None
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "device-motion.interval": self._interval,
            "device-motion.x1": self._x1,
            "device-motion.x1-left": self._x1_left,
            "device-motion.x1-right": self._x1_right,
            "device-motion.y1": self._y1,
            "device-motion.y1-left": self._y1_left,
            "device-motion.y1-right": self._y1_right,
            "device-motion.z1": self._z1,
            "device-motion.z1-left": self._z1_left,
            "device-motion.z1-right": self._z1_right,
            "device-motion.x2": self._x2,
            "device-motion.x2-left": self._x2_left,
            "device-motion.x2-right": self._x2_right,
            "device-motion.y2": self._y2,
            "device-motion.y2-left": self._y2_left,
            "device-motion.y2-right": self._y2_right,
            "device-motion.z2": self._z2,
            "device-motion.z2-left": self._z2_left,
            "device-motion.z2-right": self._z2_right,
            "device-motion.alpha": self._alpha,
            "device-motion.alpha-left": self._alpha_left,
            "device-motion.alpha-right": self._alpha_right,
            "device-motion.beta": self._beta,
            "device-motion.beta-left": self._beta_left,
            "device-motion.beta-right": self._beta_right,
            "device-motion.gamma": self._gamma,
            "device-motion.gamma-left": self._gamma_left,
            "device-motion.gamma-right": self._gamma_right,
        }

        return result

    def set_interval(self, value: float):
        """
        加速度获取间隔
        """
        self._interval = value
        return self

    def set_x1(self, value: float, left: float = None, right: float = None):
        """
        X加速度
        """
        self._x1 = value
        self._x1_left = left
        self._x1_right = right
        return self

    def set_y1(self, value: float, left: float = None, right: float = None):
        """
        Y加速度
        """
        self._y1 = value
        self._y1_left = left
        self._y1_right = right
        return self

    def set_z1(self, value: float, left: float = None, right: float = None):
        """
        Z加速度
        """
        self._z1 = value
        self._z1_left = left
        self._z1_right = right
        return self

    def set_x2(self, value: float, left: float = None, right: float = None):
        """
        X加速度（该值包括重力的影响）
        """
        self._x2 = value
        self._x2_left = left
        self._x2_right = right
        return self

    def set_y2(self, value: float, left: float = None, right: float = None):
        """
        Y加速度（该值包括重力的影响）
        """
        self._y2 = value
        self._y2_left = left
        self._y2_right = right
        return self

    def set_z2(self, value: float, left: float = None, right: float = None):
        """
        Z加速度（该值包括重力的影响）
        """
        self._z2 = value
        self._z2_left = left
        self._z2_right = right
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
