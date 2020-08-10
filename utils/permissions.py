from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """方法的权限校验"""
    def has_object_permission(self, request, view, obj):
        # 如果是安全的方法则返回True
        if request.method in permissions.SAFE_METHODS:
            return True

        # 如果不是安全的方法，则判断是否为当前用户
        return obj.user == request.user