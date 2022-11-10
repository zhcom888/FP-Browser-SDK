from .permission_type import PermissionType
from .permission_type_102 import PermissionType102
from .permission_type_93 import PermissionType93
from .permission_type_90 import PermissionType90
from .permission_type_88 import PermissionType88


def _get_permission_type_dict(version: int) -> dict:
    """
    根据浏览器版本获得指定的权限
    """
    if version and version > 0:
        if version == 93:
            return PermissionType93
        elif version == 90:
            return PermissionType90
        elif version == 88:
            return PermissionType88

    return PermissionType102


def get_permission_type(permission_type: PermissionType, version=102) -> int:
    """
    根据指定的版本获取对应的权限类型
    """
    types = _get_permission_type_dict(version)

    if permission_type in types:
        return types[permission_type]

    raise Exception("Permission Type Not Exists.")
