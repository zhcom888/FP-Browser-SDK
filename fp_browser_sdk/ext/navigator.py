from .module import Module
from .browser_enum import Platform, PerformanceNavigationType, DoNotTrackType, MaxTouchPoint
from .plugin import Plugin, MimeType
from deprecation import deprecated


class Navigator(Module):
    def __init__(self):
        super(Navigator, self).__init__()
        self._user_agent = None
        self._user_agent_auto_match = True
        self._reduced_major_in_minor_version_number = False
        self._webdriver_status = False
        self._platform = Platform.LINUX_ARMV8L
        self._vendor = 'Google Inc.'
        self._max_touch_points = MaxTouchPoint.MOBILE
        self._hardware_concurrency = 8
        self._device_memory = 4
        self._do_not_track = None
        self._enable_plugin = False
        self._enable_fake_plugin = False
        self._plugin_json = []
        self._online = True
        self._java_enabled = False
        self._pdf_viewer_enabled = False
        self._bluetooth_availability = True
        self._language = 'zh-CN'
        self._languages = 'zh-CN,zh'
        self._performance_type = None
        self._performance_redirect_count = None
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "navigator.user-agent": self._user_agent,
            "navigator.user-agent-auto-match": self._bool_to_int(self._user_agent_auto_match),
            "navigator.reduced-major-in-minor-version-number": self._bool_to_int(
                self._reduced_major_in_minor_version_number),
            "navigator.webdriver-status": self._bool_to_int(self._webdriver_status),
            "navigator.platform": self._platform.value,
            "navigator.vendor": self._vendor,
            "navigator.max-touch-points": self._max_touch_points.value,
            "navigator.hardware-concurrency": self._hardware_concurrency,
            "navigator.device-memory": self._device_memory,
            "navigator.enable-plugin": self._bool_to_int(self._enable_plugin),
            "navigator.enable-fake-plugin": self._bool_to_int(self._enable_fake_plugin),
            "navigator.plugin-json": [item.to_dict() for item in self._plugin_json],
            "navigator.online": self._bool_to_int(self._online),
            "navigator.java-enabled": self._bool_to_int(self._java_enabled),
            "navigator.pdf-viewer-enabled": self._bool_to_int(self._pdf_viewer_enabled),
            "navigator.bluetooth-availability": self._bool_to_int(self._bluetooth_availability),
            "navigator.language": self._language,
            "navigator.languages": self._languages,
        }

        if self._do_not_track is not None:
            result["navigator.do-not-track"] = self._do_not_track.value

        return result

    def set_user_agent(self, value: str):
        """
        设置 User-Agent
        """
        self._user_agent = value
        return self

    def set_user_agent_auto_match(self, value: bool):
        """
        设置 UserAgent 里的版本号，自动对应 "version-info.number" 字段的值
        """
        self._user_agent_auto_match = value
        return self

    def set_reduced_major_in_minor_version_number(self, value: bool):
        """
        强制只获取主版本号（例如：把 96.0.4664.104 变成 96.0.0.0）
        """
        self._reduced_major_in_minor_version_number = value
        return self

    def set_webdriver_status(self, value: bool):
        """
        设置  webdriver 状态
        """
        self._webdriver_status = value
        return self

    def set_platform(self, value: Platform):
        """
        平台
        """
        self._platform = value
        return self

    def set_vendor(self, value: str):
        """
        浏览器供应商的名称
        """
        self._vendor = value
        return self

    def set_max_touch_points(self, value: MaxTouchPoint):
        """
        设备能够支持的最大同时触摸的点数
        """
        self._max_touch_points = value
        return self

    def set_hardware_concurrency(self, value: int):
        """
        处理器数量
        """
        self._hardware_concurrency = value
        return self

    def set_device_memory(self, value: int):
        """
        设备内存数
        """
        self._device_memory = value
        return self

    def set_do_not_track(self, value: DoNotTrackType):
        """
        设置 Do Not Track
        """
        self._do_not_track = value
        return self

    def set_enable_plugin(self, value: bool):
        """
        是否启用插件
        """
        self._enable_plugin = value
        return self

    def set_enable_fake_plugin(self, value: bool):
        """
        是否启用默认 PC 端自带的五个插件
        """
        self._enable_fake_plugin = value
        return self

    def append_plugin(self, value: Plugin):
        """
        添加自定义插件
        """
        self._plugin_json.append(value)
        return self

    def set_online(self, value: bool):
        """
        是否在线
        """
        self._online = value
        return self

    def set_java_enabled(self, value: bool):
        """
        javaEnabled
        """
        self._java_enabled = value
        return self

    def set_pdf_viewer_enabled(self, value: bool):
        """
        pdfViewerEnabled
        """
        self._pdf_viewer_enabled = value
        return self

    def set_bluetooth_availability(self, value: bool):
        """
        蓝牙可用性
        """
        self._bluetooth_availability = value
        return self

    def set_language(self, value: str):
        """
        用户偏好语言
        """
        self._language = value
        return self

    def set_languages(self, value: str):
        """
        浏览器支持语言
        """
        self._languages = value
        return self

    @deprecated(details="已废弃该参数注入")
    def set_performance_type(self, value: PerformanceNavigationType):
        """
        如何导航到该页面
        """
        self._performance_type = value
        return self

    @deprecated(details="已废弃该参数注入")
    def set_performance_redirect_count(self, value: int):
        """
        如果有重定向的话，页面通过几次重定向跳转而来，默认为0
        """
        self._performance_redirect_count = value
        return self
