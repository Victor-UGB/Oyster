from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj == request.user or request.user.groups.filter(name='Admin').exists())