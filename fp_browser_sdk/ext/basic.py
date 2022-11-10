from typing import List
import time
from .module import Module
from .browser_enum import TLSVersion
from .inject_js import InjectJS
from .media import Media


class Basic(Module):
    def __init__(self):
        super(Basic, self).__init__()
        self._global_disable_settings = False
        self._disable_window_status = False
        self._time_zone = "Asia/Shanghai"
        self._init_history_length = 0
        self._inject_js: InjectJS = InjectJS()
        self._allow_permissions: List = []
        self._reject_permissions: List = []
        self._font_list: List[str] = []
        self._product_name = "Google Chrome"
        self._info_number = None
        self._webgl_vendor = None
        self._webgl_renderer = None
        self._clipboard_text = None
        self._tls_min_ver = TLSVersion.TLS_1_2
        self._tls_max_ver = TLSVersion.TLS_1_3
        self._memory_info_total_js = None
        self._memory_info_used_js = None
        self._memory_info_limit_js = None
        self._disable_alert = False
        self._disable_window_open = False
        self._confirm = None
        self._media_list = []
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "global.setting-version": "0.1",
            "global.setting-timestamp": int(time.time()),
            "global.disable-settings": self._bool_to_int(self._global_disable_settings),
            "basic.disable-window-chrome": self._bool_to_int(self._disable_window_status),
            "basic.timezone": self._time_zone,
            "basic.init-history-length": self._init_history_length,
            "basic.inject-js": self._inject_js.to_dict(),
            "basic.allow-permissions": [item for item in self._allow_permissions],
            "basic.reject-permissions": [item for item in self._reject_permissions],
            "font.list-json": self._font_list,
            "version-info.product-name": self._product_name,
            "version-info.number": self._info_number,
            "webgl.vendor": self._webgl_vendor,
            "webgl.renderer": self._webgl_renderer,
            "clipboard.text": self._clipboard_text,
            "ja3.min-version": self._tls_min_ver.value,
            "ja3.max-version": self._tls_max_ver.value,
            "memoryinfo.total-js": self._memory_info_total_js,
            "memoryinfo.used-js": self._memory_info_used_js,
            "memoryinfo.limit-js": self._memory_info_limit_js,
            "frame.disable-alert": self._bool_to_int(self._disable_alert),
            "frame.disable-window-open": self._bool_to_int(self._disable_window_open),
            "frame.confirm": self._bool_to_int(self._confirm),
            "media.list-json": [item.to_dict() for item in self._media_list],
        }

        return result

    def set_disable_window(self, value: bool):
        """
        是否禁用 window 的 chrome 属性
        """
        self._disable_window_status = value
        return self

    def set_time_zone(self, value: str):
        """
        时区
        """
        self._time_zone = value
        return self

    def set_init_history_length(self, value: int):
        """
        设置初始化的历史记录数量
        """
        self._init_history_length = value
        return self

    def set_inject_js(self, value: InjectJS):
        """
        注入的js
        """
        self._inject_js = value
        return self

    def append_allow_permission(self, value):
        """
        直接允许的权限
        """
        self._allow_permissions.append(value)
        return self

    def append_reject_permission(self, value):
        """
        直接拒绝的权限
        """
        self._reject_permissions.append(value)
        return self

    def append_font(self, value: str):
        """
        字体
        """
        self._font_list.append(value)
        return self

    def set_product_name(self, value: str):
        """
        产品名称
        """
        self._product_name = value
        return self

    def set_info_number(self, value: str):
        """
        版本号
        """
        self._info_number = value
        return self

    def set_webgl_vendor(self, value: str):
        """
        显卡供应商
        """
        self._webgl_vendor = value
        return self

    def set_webgl_renderer(self, value: str):
        """
        显卡型号
        """
        self._webgl_renderer = value
        return self

    def set_clipboard_text(self, value: str):
        """
        剪切板
        """
        self._clipboard_text = value
        return self

    def set_global_disable_settings(self, value: bool):
        """
        是否禁用全部选项
        """
        self._global_disable_settings = value
        return self

    def set_tls_min_ver(self, value: TLSVersion):
        """
        tls 最小版本
        """
        self._tls_min_ver = value
        return self

    def set_tls_max_ver(self, value: TLSVersion):
        """
        tls 最大版本
        """
        self._tls_max_ver = value
        return self

    def set_memory_info_total_js(self, value: int):
        """
        已分配的堆体积（以字节计算）
        """
        self._memory_info_total_js = value
        return self

    def set_memory_info_used_js(self, value: int):
        """
        当前 JS 堆活跃段（segment）的体积（以字节计算）
        """
        self._memory_info_used_js = value
        return self

    def set_memory_info_limit_js(self, value: int):
        """
        上下文内可用堆的最大体积（以字节计算）
        """
        self._memory_info_limit_js = value
        return self

    def set_disable_alert(self, value: bool):
        """
        是否禁用 alert 弹框
        """
        self._disable_alert = value
        return self

    def set_disable_window_open(self, value: bool):
        """
        是否禁用 window.open 弹框
        """
        self._disable_window_open = value
        return self

    def set_confirm(self, value: bool):
        """
        强制 confirm 弹框的值
        """
        self._confirm = value
        return self

    def append_media(self, value: Media):
        """
        硬件设备信息
        """
        self._media_list.append(value)
        return self
