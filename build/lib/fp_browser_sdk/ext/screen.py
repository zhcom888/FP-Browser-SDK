from .module import Module
from .browser_enum import ScreenColorDepth, ScreenOrientationType


class Screen(Module):
    def __init__(self):
        super(Screen, self).__init__()
        self._color_depth = ScreenColorDepth.ColorDepth_30
        self._width = None
        self._height = None
        self._rect_width = None
        self._rect_height = None
        self._rect_scale_factor = None
        self._avail_width = None
        self._avail_height = None
        self._avail_top = None
        self._avail_left = None
        self._orientation = ScreenOrientationType.PORTRAIT_PRIMARY
        self._device_pixel_ratio = None
        self._device_pixel_ratio = None
        self._media_matchs = {}
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "screen.color-depth": self._color_depth.value,
            "screen.width": self._width,
            "screen.height": self._height,
            "screen.avail-width": self._avail_width,
            "screen.avail-height": self._avail_height,
            "screen.avail-top": self._avail_top,
            "screen.avail-left": self._avail_left,
            "screen.orientation-angle": self._orientation.value[1],
            "screen.orientation-type": self._orientation.value[0],
            "screen.device-pixel-ratio": self._device_pixel_ratio,
            "rect.width": self._rect_width,
            "rect.height": self._rect_height,
            "rect.scale-factor": self._rect_scale_factor,
            "media.matchs-json": ["{}:{}".format(key, item) for (key, item) in self._media_matchs.items()],
        }

        return result

    def set_color_depth(self, value: ScreenColorDepth):
        """
        colorDepth（屏幕的色彩深度）
        """
        self._color_depth = value
        return self

    def set_width(self, value: int):
        """
        屏幕宽度（单位：px）
        """
        self._width = value
        return self

    def set_height(self, value: int):
        """
        屏幕高度（单位：px）
        """
        self._height = value
        return self

    def set_avail_width(self, value: int):
        """
        可用空间的屏幕宽度（单位：px）
        """
        self._avail_width = value
        return self

    def set_avail_height(self, value: int):
        """
        可用空间的屏幕高度（单位：px）
        """
        self._avail_height = value
        return self

    def set_avail_top(self, value: int):
        """
        可用空间的顶部边界的第一个像素点
        """
        self._avail_top = value
        return self

    def set_avail_left(self, value: int):
        """
        可用空间的左边边界的第一个像素点
        """
        self._avail_left = value
        return self

    def set_device_pixel_ratio(self, value: float):
        """
        设备像素比
        """
        self._device_pixel_ratio = value
        return self

    def set_rect_width(self, value: int):
        """
        可视区域页面宽度
        """
        self._rect_width = value
        return self

    def set_rect_height(self, value: int):
        """
        可视区域页面高度
        """
        self._rect_height = value
        return self

    def set_rect_scale_factor(self, value: bool):
        """
        原始的屏幕缩放比例（注意：该值对应设备原始的缩放比例，不能随意设置该值。获取方法：window.devicePixelRatio）
        """
        self._rect_scale_factor = value
        return self

    def set_orientation(self, value: ScreenOrientationType):
        """
        屏幕方向
        """
        self._orientation = value
        return self

    def append_media_matchs(self, key: str, value: str):
        """
        媒体查询
        """
        self._media_matchs[key] = value
        return self
