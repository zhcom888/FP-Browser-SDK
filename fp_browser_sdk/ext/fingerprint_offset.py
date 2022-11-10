from .module import Module
import random
import decimal


class FingerprintOffset(Module):
    def __init__(self):
        super(FingerprintOffset, self).__init__()
        self._audio_offset = None
        self._canvas_offset = None
        self._webgl_offset = None
        pass

    def _to_dict(self):
        """
        解析成 dict
        """
        result = {
            "fingerprint.audio-rand-value": self._audio_offset,
            "fingerprint.canvas-rand-value": self._canvas_offset,
            "fingerprint.webgl-rand-value": self._webgl_offset,
        }

        return result

    def _random(self, offset_min: float, offset_max: float):
        """
        生成对于偏移量
        """
        if decimal.Decimal(str(offset_min)).as_tuple().exponent == decimal.Decimal(str(offset_max)).as_tuple().exponent:
            exponent = abs(decimal.Decimal(str(offset_min)).as_tuple().exponent)
        else:
            exponent = 3

        rand = random.uniform(offset_min, offset_max)

        return "%.{}f".format(exponent) % rand
        # return round(random.uniform(offset_min, offset_max), exponent)

    def _random_audio_offset(self):
        """
        随机生成一个音频指纹 offset
        """
        return self._random(0.999, 99.999)

    def _random_canvas_offset(self):
        """
        随机生成一个 Canvas 指纹 offset
        """
        return self._random(0.999, 99.999)

    def _random_webgl_offset(self):
        """
        随机生成一个 Webgl 指纹 offset
        """
        return self._random(0.001, 0.999)

    def set_audio_offset(self, value: float):
        """
        音频指纹偏移量
        """
        self._audio_offset = value
        return self

    def auto_audio_offset(self):
        """
        自动音频指纹偏移量
        """
        return self.set_audio_offset(self._random_audio_offset())

    def set_canvas_offset(self, value: float):
        """
        Canvas 指纹偏移量
        """
        self._canvas_offset = value
        return self

    def auto_canvas_offset(self):
        """
        自动 Canvas 指纹偏移量
        """
        return self.set_canvas_offset(self._random_canvas_offset())

    def set_webgl_offset(self, value: float):
        """
        Webgl 指纹偏移量
        """
        self._webgl_offset = value
        return self

    def auto_webgl_offset(self):
        """
        自动 Webgl 指纹偏移量
        """
        return self.set_webgl_offset(self._random_webgl_offset())
