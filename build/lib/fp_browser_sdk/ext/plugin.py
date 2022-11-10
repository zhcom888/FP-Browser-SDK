from .module import Module


class MimeType(Module):
    def __init__(self, name=None, description=None, extensions: list = []):
        super(MimeType, self).__init__()
        self._name = name
        self._description = description
        self._extensions = extensions

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "name": self._name,
            "description": self._description,
            "extensions": self._extensions,
        }

        return result

    def set_name(self, value: str):
        """
        name
        """
        self._name = value
        return self

    def set_description(self, value: str):
        """
        description
        """
        self._description = value
        return self

    def append_extensions(self, value: str):
        """
        extensions
        """
        self._extensions.append(value)
        return self


class Plugin(Module):
    def __init__(self, name=None, filename=None, description=None, mime_types: list = []):
        super(Plugin, self).__init__()
        self._name = name
        self._filename = filename
        self._description = description
        self._mime_types = mime_types

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "name": self._name,
            "filename": self._filename,
            "description": self._description,
            "mime_types": [item.to_dict() for item in self._mime_types],
        }

        return result

    def set_name(self, value: str):
        """
        name
        """
        self._name = value
        return self

    def set_filename(self, value: str):
        """
        filename
        """
        self._filename = value
        return self

    def set_description(self, value: str):
        """
        description
        """
        self._description = value
        return self

    def append_mime_types(self, value: MimeType):
        """
        mime_types
        """
        self._mime_types.append(value)
        return self
