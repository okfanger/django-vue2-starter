from rest_framework.permissions import BasePermission


class IsSomeOne(BasePermission):

    def has_permission(self, request, view):
        try:
            # 里面是鉴权逻辑
            return True
        except AttributeError:
            return False

    def has_object_permission(self, request, view, obj):
        return True


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.type == 2:
                return True
            else:
                return False
        except AttributeError:
            return False