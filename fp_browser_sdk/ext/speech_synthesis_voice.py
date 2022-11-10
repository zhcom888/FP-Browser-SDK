from .module import Module
from .browser_enum import SpeechSynthesisVoiceAppendMode


class SpeechSynthesisVoiceItem(Module):
    def __init__(self):
        super(SpeechSynthesisVoiceItem, self).__init__()
        self._name = None
        self._lang = None
        self._is_local_service = True
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "name": self._name,
            "lang": self._lang,
            "is_local_service": self._bool_to_int(self._is_local_service)
        }

        return result

    def set_name(self, value: str):
        """
        名称
        """
        self._name = value
        return self

    def set_lang(self, value: str):
        """
        语言
        """
        self._lang = value
        return self

    def set_is_local_service(self, value: bool):
        """
        是否本地服务
        """
        self._is_local_service = value
        return self


class SpeechSynthesisVoice(Module):
    def __init__(self):
        super(SpeechSynthesisVoice, self).__init__()
        self._disable = False
        self._force_override = False
        self._append_mode = SpeechSynthesisVoiceAppendMode.PUSH
        self._list = []
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "speech-synthesis-voice.disable": self._bool_to_int(self._disable),
            "speech-synthesis-voice.force-override": self._bool_to_int(self._force_override),
            "speech-synthesis-voice.append-mode": self._append_mode.value,
            "speech-synthesis-voice.json": [item.to_dict() for item in self._list],
        }

        return result

    def set_disable(self, value: bool):
        """
        是否禁用
        """
        self._disable = value
        return self

    def set_force_override(self, value: bool):
        """
        是否强制覆盖本来的语音信息
        """
        self._force_override = value
        return self

    def set_append_mode(self, value: str):
        """
        追加方式
        """
        self._append_mode = value
        return self

    def append_list(self, value: SpeechSynthesisVoiceItem):
        """
         注入的语音信息
        """
        self._list.append(value)
        return self
