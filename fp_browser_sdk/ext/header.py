from .module import Module
from .browser_enum import CookieSameSite


class Cookie(Module):
    def __init__(self):
        super(Cookie, self).__init__()
        self._port = 80
        self._domain = None
        self._name = None
        self._value = None
        self._path = '/'
        self._secure = False
        self._httponly = False
        self._same_site = CookieSameSite.NO_RESTRICTION

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "port": self._port,
            "domain": self._domain,
            "name": self._name,
            "value": self._value,
            "path": self._path,
            "secure": self._bool_to_int(self._secure),
            "httponly": self._bool_to_int(self._httponly),
            "same_site": self._same_site.value
        }

        return result

    def set_port(self, value: int):
        """
        端口
        """
        self._port = value
        return self

    def set_domain(self, value: str):
        """
        域名
        """
        self._domain = value
        return self

    def set_name(self, value: str):
        """
        名称
        """
        self._name = value
        return self

    def set_value(self, value: str):
        """
        值
        """
        self._value = value
        return self

    def set_path(self, value: str):
        """
        path
        """
        self._path = value
        return self

    def set_secure(self, value: bool):
        """
        secure
        """
        self._secure = value
        return self

    def set_httponly(self, value: bool):
        """
        httponly
        """
        self._httponly = value
        return self

    def set_same_site(self, value: CookieSameSite):
        """
        same_site
        """
        self._same_site = value
        return self


class Header(Module):
    def __init__(self):
        super(Header, self).__init__()
        self._x_requested_with = None
        self._extra_json = {}
        self._cookie_status = True
        self._cookie_json = []
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "header.x-requested-with": self._x_requested_with,
            "header.extra-json": [{"name": key, "value": item} for (key, item) in self._extra_json.items()],
            "cookie.status": self._bool_to_int(self._cookie_status),
            "cookie.json": [item.to_dict() for item in self._cookie_json],
        }

        return result

    def set_x_requested_with(self, value: str):
        """
        设置 X-Requested-With 的值
        """
        self._x_requested_with = value
        return self

    def append_extra_json(self, key: str, value: str):
        """
        额外的 header（注意：如果强制设置原本存在的 key，不会有效果）
        """
        self._extra_json[key] = str(value)
        return self

    def set_cookie_status(self, value: bool):
        """
        是否开启 cookie
        """
        self._cookie_status = value
        return self

    def append_cookie(self, value: Cookie):
        """
        设置 cookie
        """
        self._cookie_json.append(value)
        return self
