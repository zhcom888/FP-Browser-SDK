from .module import Module


class InjectJS(Module):
    def __init__(self):
        super(InjectJS, self).__init__()
        self._load_event = []

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "load": self._load_event
        }

        return result

    def append_load_event(self, value: str):
        """
        注入 load 事件
        """
        self._load_event.append(value)
        return self
