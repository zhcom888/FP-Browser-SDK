class UrlErrorException(Exception):
    def __init__(self):
        self.msg = 'url 格式错误'

    def __str__(self):
        return self.msg


class IpErrorException(Exception):
    def __init__(self):
        self.msg = 'ip 格式错误'

    def __str__(self):
        return self.msg


class MotionErrorException(Exception):
    def __init__(self):
        self.msg = '重力感应数据错误'

    def __str__(self):
        return self.msg
