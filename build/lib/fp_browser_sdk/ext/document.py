from .module import Module
from .browser_enum import VideoSupportType, CompatMode, MatchType
from .exception import UrlErrorException
from deprecation import deprecated


class VideoSupport(Module):
    def __init__(self):
        super(VideoSupport, self).__init__()
        self._type = None
        self._support = VideoSupportType.PROBABLY

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "type": self._type,
            "support": self._support.value,
        }

        return result

    def set_type(self, value: str):
        """
        mime type
        """
        self._type = value
        return self

    def set_support(self, value: VideoSupportType):
        """
        support
        """
        self._support = value
        return self


class DocumetMatch(Module):
    def __init__(self):
        super(DocumetMatch, self).__init__()
        self._target_url = None
        self._match_type = MatchType.FULL
        self._match_break = None
        self._current_url = None
        self._document_referrer = None
        self._header_referrer = None
        self._title = None

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "target_url": self._target_url,
            "match_type": self._match_type.value,
            "match_break": self._bool_to_int(self._match_break),
            "current_url": self._current_url,
            "document_referrer": self._document_referrer,
            "header_referrer": self._header_referrer,
            "title": self._title,
        }

        if "target_url" in result:
            if not self._verify_url(result['target_url']):
                raise UrlErrorException

        if "current_url" in result:
            if not self._verify_url(result['current_url']):
                raise UrlErrorException

        if "document_referrer" in result and len(result['document_referrer']) > 0:
            if not self._verify_url(result['document_referrer']):
                raise UrlErrorException

        if "header_referrer" in result and len(result['header_referrer']) > 0:
            if not self._verify_url(result['header_referrer']):
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

    def set_current_url(self, value: str):
        """
        强制修改后的链接
        """
        self._current_url = value
        return self

    def set_document_referrer(self, value: str):
        """
        document 来源
        """
        self._document_referrer = value
        return self

    def set_header_referrer(self, value: str):
        """
        header 来源
        """
        self._header_referrer = value
        return self

    def set_title(self, value: str):
        """
        强制修改标题
        """
        self._title = value
        return self


class Document(Module):
    def __init__(self):
        super(Document, self).__init__()
        self._global_match_target_url = None
        self._global_match_title = None
        self._global_match_current_url = None
        self._global_skip_current_url_header = True
        self._global_match_referrer = None
        self._match_list = []
        self._is_trusted = True
        self._compat_mode = CompatMode.CSS1COMPAT
        self._lastModified = None
        self._charset = None
        self._video_support_mime_types = []

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "document.global-match-target-url": self._global_match_target_url,
            "document.global-match-title": self._global_match_title,
            "document.global-match-current-url": self._global_match_current_url,
            "document.global-skip-current-url-header": self._bool_to_int(self._global_skip_current_url_header),
            "document.global-match-referrer": self._global_match_referrer,
            "document.match-json": [item.to_dict() for item in self._match_list],
            "document.is-trusted": self._bool_to_int(self._is_trusted),
            "document.compat-mode": self._compat_mode.value,
            "document.lastModified": self._lastModified,
            "document.charset": self._charset,
            "document.video-support-mime-types-json": [item.to_dict() for item in self._video_support_mime_types],
        }

        if "document-global-match-current-url" in result:
            if not self._verify_url(result['document-global-match-current-url']):
                raise UrlErrorException

        if "document-global-match-referrer" in result:
            if not self._verify_url(result['document-global-match-referrer']):
                raise UrlErrorException

        return result

    @deprecated(details="已废弃该参数注入")
    def set_global_match_target_url(self, value: str):
        """
        目标域名（标题、链接、来源只针对该域名下的网址才生效）
        """
        self._global_match_target_url = value
        return self

    @deprecated(details="已废弃该参数注入")
    def set_global_match_title(self, value: str):
        """
        强制修改标题
        """
        self._global_match_title = value
        return self

    @deprecated(details="已废弃该参数注入")
    def set_global_match_current_url(self, value: str):
        """
        强制修改后的链接
        """
        self._global_match_current_url = value
        return self

    @deprecated(details="已废弃该参数注入")
    def set_global_skip_current_url_header(self, value: str):
        """
        是否跳过修改 header 里的当前链接信息
        """
        self._global_skip_current_url_header = value
        return self

    @deprecated(details="已废弃该参数注入")
    def set_global_match_referrer(self, value: str):
        """
        来源
        """
        self._global_match_referrer = value
        return self

    def append_match_list(self, value: DocumetMatch):
        """
        多组匹配修改：标题、referrer、当前链接
        """
        self._match_list.append(value)
        return self

    def set_is_trusted(self, value: bool):
        """
        是否是用户执行的事件
        """
        self._is_trusted = value
        return self

    def set_compat_mode(self, value: str):
        """
        渲染模式
        """
        self._compat_mode = value
        return self

    def append_video_support_mime_types(self, value: VideoSupport):
        """
        支持播放的视频格式
        """
        self._video_support_mime_types.append(value)
        return self

    def set_lastModified(self, value: int):
        """
        文档最后更新时间
        """
        self._lastModified = value
        return self

    def set_charset(self, value: str):
        """
        文档编码
        """
        self._charset = value
        return self
