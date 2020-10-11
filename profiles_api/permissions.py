from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to modify their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to modify theior own prof"""
        if request.method in permissions.SAFE_METHODS:
            return True
            # if request is get its okay you can do it without below validation
        return request.user.id == obj.id
