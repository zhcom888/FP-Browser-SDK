from .module import Module
from .browser_enum import MediaKind
import random


class Media(Module):
    def __init__(self, device_id=None, label=None, group_id=None, device_type: MediaKind = None):
        super(Media, self).__init__()
        self._deviceId = device_id
        self._groupId = group_id
        self._kind = device_type
        self._label = label

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "device_id": self._deviceId,
            "label": self._label,
            "group_id": self._groupId,
            "device_type": self._kind.value,
        }

        return result

    def _auto_random(self, value: str):
        """
        重新随机生成
        """
        if value.lower() == 'default':
            return value

        data = []
        for item in value:
            if self._is_number(item):
                data.append(str(random.randint(0, 9)))
            else:
                data.append(random.choice(['a', 'b', 'c', 'd', 'e', 'f']))

        return ''.join(data)

    def set_device_id(self, value: str, auto_random: bool = True):
        """
        设置设备 id
        """
        if auto_random:
            self._deviceId = self._auto_random(value)
        else:
            self._deviceId = value
        return self

    def set_label(self, value: str):
        """
        设置设备 id
        """
        if value is None:
            value = ""
        self._label = value
        return self

    def set_groupId(self, value: str, auto_random: bool = True):
        """
        设置设备 id
        """
        if auto_random:
            self._groupId = self._auto_random(value)
        else:
            self._groupId = value
        return self

    def set_kind(self, value: MediaKind):
        """
        设置设备 id
        """
        self._kind = value
        return self

    @staticmethod
    def str_to_kind_type(value: str):
        """
        设置设备 id
        """
        if value == 'audioinput':
            return MediaKind.AUDIO_INPUT
        elif value == 'audiooutput':
            return MediaKind.AUDIO_OUTPUT
        else:
            return MediaKind.VIDEO_INPUT
