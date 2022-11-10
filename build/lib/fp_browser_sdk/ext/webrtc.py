from .module import Module
from .exception import IpErrorException

class Webrtc(Module):
    def __init__(self):
        super(Webrtc, self).__init__()
        self._privite_ip = None
        self._public_ip = None
        self._host_name = None
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "webrtc.privite-ip": self._privite_ip,
            "webrtc.public-ip": self._public_ip,
            "webrtc.host-name": self._host_name,
        }

        if "webrtc.privite-ip" in result:
            if not self._verify_ip(result['webrtc.privite-ip']):
                raise IpErrorException

        if "webrtc.public-ip" in result:
            if not self._verify_ip(result['webrtc.public-ip']):
                raise IpErrorException

        return result

    def set_privite_ip(self, value: str):
        """
        局域网 IP
        """
        self._privite_ip = value
        return self

    def set_public_ip(self, value: str):
        """
        外网 IP
        """
        self._public_ip = value
        return self

    def set_host_name(self, value: str):
        """
        hostname
        """
        self._host_name = value
        return self
