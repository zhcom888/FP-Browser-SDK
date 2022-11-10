from .module import Module
from .browser_enum import PrefersColor
from .browser_enum import WebClientHintsType


class ClientHints(Module):
    def __init__(self):
        super(ClientHints, self).__init__()
        self._disable = True
        self._disable_json = []
        self._viewport_width = 980
        self._viewport_height = 980
        self._prefers_color = PrefersColor.LIGHT
        self._mobile = True
        self._platform = 'Android'
        self._platform_version = None
        self._architecture = ''
        self._bitness = ''
        self._wow64 = False
        self._model = None
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        if self._disable is False:
            result = {
                "client-hints.disable": self._bool_to_int(self._disable),
                "client-hints.disable-json": [str(item.value) for item in self._disable_json],
                "client-hints.viewport-width": self._viewport_width,
                "client-hints.viewport-height": self._viewport_height,
                "client-hints.prefers-color": self._prefers_color.value,
                "client-hints.mobile": self._bool_to_int(self._mobile),
                "client-hints.platform": self._platform,
                "client-hints.platform-version": self._platform_version,
                "client-hints.architecture": self._architecture,
                "client-hints.bitness": self._bitness,
                "client-hints.wow64": self._bool_to_int(self._wow64),
                "client-hints.model": self._model,
            }
        else:
            result = {
                "client-hints.disable": self._bool_to_int(self._disable),
            }

        return result

    def set_disable(self, value: bool):
        """
        是否启用 client hints
        """
        self._disable = value
        return self

    def append_disable_field(self, value: WebClientHintsType):
        """
        添加需要禁用的自读
        """
        self._disable_json.append(value)
        return self

    def set_viewport_width(self, value: int):
        """
        宽度
        """
        self._viewport_width = value
        return self

    def set_viewport_height(self, value: int):
        """
        高度
        """
        self._viewport_height = value
        return self

    def set_prefers_color(self, value: PrefersColor):
        """
        显示模式
        """
        self._prefers_color = value
        return self

    def set_mobile(self, value: bool):
        """
        是否是手机
        """
        self._mobile = value
        return self

    def set_platform(self, value: str):
        """
        平台
        """
        self._platform = value
        return self

    def set_platform_version(self, value: str):
        """
        平台版本
        """
        self._platform_version = value
        return self

    def set_architecture(self, value: str):
        """
        平台架构的字符串
        """
        self._architecture = value
        return self

    def set_bitness(self, value: str):
        """
        架构位数的字符串
        """
        self._bitness = value
        return self

    def set_wow64(self, value: bool):
        """
        如果二进制文件是在 32 位模式下构建并在 64 位上运行，则返回 true；否则返回 false
        """
        self._wow64 = value
        return self

    def set_model(self, value: bool):
        """
        手机型号
        """
        self._model = value
        return self
