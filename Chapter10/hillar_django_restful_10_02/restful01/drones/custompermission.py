from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			# The method is a safe method
			return True
		else:
			# The method isn't a safe method
			# Only owners are granted permissions for unsafe methods
			return obj.owner == request.user
