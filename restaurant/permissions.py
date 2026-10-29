from rest_framework.permissions import SAFE_METHODS, BasePermission

class ReadOnlyOrAuthenticated(BasePermission):
    """Allow anyone to read menu items; require login for mutations."""
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_authenticated
