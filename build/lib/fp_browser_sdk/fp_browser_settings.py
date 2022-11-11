from .ext.module import Module


class FPBrowserSettings(object):
    def __init__(self):
        self.modules = []
        pass

    def add_module(self, module: Module):
        """
        追加模块
        """
        self.modules.append(module)
        return self

    def parse(self):
        """
        解析参数
        """
        result = {}
        for module in self.modules:
            result = {**result, **module.to_dict()}

        return result
