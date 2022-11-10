from .module import Module
from .browser_enum import MatchType
from .exception import UrlErrorException
from .browser_enum import PerformanceNavigationType


class PerformanceMatch(Module):
    def __init__(self):
        super(PerformanceMatch, self).__init__()
        self._target_url = None
        self._match_type = MatchType.FULL
        self._match_break = None
        self._navigation_type = None
        self._navigation_redirect_count = None
        self._timing_connectEnd_offset = 0
        self._timing_connectStart_offset = 0
        self._timing_domComplete_offset = 0
        self._timing_domContentLoadedEventEnd_offset = 0
        self._timing_domContentLoadedEventStart_offset = 0
        self._timing_domInteractive_offset = 0
        self._timing_domLoading_offset = 0
        self._timing_domainLookupEnd_offset = 0
        self._timing_domainLookupStart_offset = 0
        self._timing_fetchStart_offset = 0
        self._timing_loadEventEnd_offset = 0
        self._timing_loadEventStart_offset = 0
        self._timing_navigationStart_offset = 0
        self._timing_redirectEnd_offset = 0
        self._timing_redirectStart_offset = 0
        self._timing_requestStart_offset = 0
        self._timing_responseEnd_offset = 0
        self._timing_responseStart_offset = 0
        self._timing_secureConnectionStart_offset = 0
        self._timing_unloadEventEnd_offset = 0
        self._timing_unloadEventStart_offset = 0

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "target_url": self._target_url,
            "match_type": self._match_type.value,
            "match_break": self._bool_to_int(self._match_break),
            "navigation_redirect_count": self._navigation_redirect_count,
            "timing_connectEnd_offset": self._timing_connectEnd_offset,
            "timing_connectStart_offset": self._timing_connectStart_offset,
            "timing_domComplete_offset": self._timing_domComplete_offset,
            "timing_domContentLoadedEventEnd_offset": self._timing_domContentLoadedEventEnd_offset,
            "timing_domContentLoadedEventStart_offset": self._timing_domContentLoadedEventStart_offset,
            "timing_domInteractive_offset": self._timing_domInteractive_offset,
            "timing_domLoading_offset": self._timing_domLoading_offset,
            "timing_domainLookupEnd_offset": self._timing_domainLookupEnd_offset,
            "timing_domainLookupStart_offset": self._timing_domainLookupStart_offset,
            "timing_fetchStart_offset": self._timing_fetchStart_offset,
            "timing_loadEventEnd_offset": self._timing_loadEventEnd_offset,
            "timing_loadEventStart_offset": self._timing_loadEventStart_offset,
            "timing_navigationStart_offset": self._timing_navigationStart_offset,
            "timing_redirectEnd_offset": self._timing_redirectEnd_offset,
            "timing_redirectStart_offset": self._timing_redirectStart_offset,
            "timing_requestStart_offset": self._timing_requestStart_offset,
            "timing_responseEnd_offset": self._timing_responseEnd_offset,
            "timing_responseStart_offset": self._timing_responseStart_offset,
            "timing_secureConnectionStart_offset": self._timing_secureConnectionStart_offset,
            "timing_unloadEventEnd_offset": self._timing_unloadEventEnd_offset,
            "timing_unloadEventStart_offset": self._timing_unloadEventStart_offset,
        }

        if self._navigation_type is not None:
            result['navigation_type'] = self._navigation_type.value
        else:
            result['navigation_type'] = None

        if "target_url" in result:
            if not self._verify_url(result['target_url']):
                raise UrlErrorException

        return result

    def set_target_url(self, value: str):
        """
        目标域名
        """
        self._target_url = value
        return self

    def set_match_type(self, value: MatchType):
        """
        匹配模式
        """
        self._match_type = value
        return self

    def set_match_break(self, value: bool):
        """
        如果是正则匹配，是否匹配成功后就跳出匹配
        """
        self._match_break = value
        return self

    def set_navigation_type(self, value: PerformanceNavigationType):
        """
        强制修改后的链接
        """
        self._navigation_type = value
        return self

    def set_navigation_redirect_count(self, value: int):
        """
        强制修改后的链接
        """
        self._navigation_redirect_count = value
        return self

    def set_timing_connectEnd_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_connectEnd_offset = value
        return self

    def set_timing_connectStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_connectStart_offset = value
        return self

    def set_timing_domComplete_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_domComplete_offset = value
        return self

    def set_timing_domContentLoadedEventEnd_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_domContentLoadedEventEnd_offset = value
        return self

    def set_timing_domContentLoadedEventStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_domContentLoadedEventStart_offset = value
        return self

    def set_timing_domInteractive_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_domInteractive_offset = value
        return self

    def set_timing_domLoading_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_domLoading_offset = value
        return self

    def set_timing_domainLookupEnd_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_domainLookupEnd_offset = value
        return self

    def set_timing_domainLookupStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_domainLookupStart_offset = value
        return self

    def set_timing_fetchStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_fetchStart_offset = value
        return self

    def set_timing_loadEventEnd_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_loadEventEnd_offset = value
        return self

    def set_timing_loadEventStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_loadEventStart_offset = value
        return self

    def set_timing_navigationStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_navigationStart_offset = value
        return self

    def set_timing_redirectEnd_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_redirectEnd_offset = value
        return self

    def set_timing_redirectStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_redirectStart_offset = value
        return self

    def set_timing_requestStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_requestStart_offset = value
        return self

    def set_timing_responseEnd_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_responseEnd_offset = value
        return self

    def set_timing_responseStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_responseStart_offset = value
        return self

    def set_timing_secureConnectionStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_secureConnectionStart_offset = value
        return self

    def set_timing_unloadEventEnd_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_unloadEventEnd_offset = value
        return self

    def set__timing_unloadEventStart_offset(self, value: int):
        """
        强制修改后的链接
        """
        self._timing_unloadEventStart_offset = value
        return self


class Performance(Module):
    def __init__(self):
        super(Performance, self).__init__()
        self._match_json = []

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "performance.match-json": [item.to_dict() for item in self._match_json],
        }

        return result

    def append_match(self, value: PerformanceMatch):
        """
        添加匹配对象
        """
        self._match_json.append(value)
        return self
