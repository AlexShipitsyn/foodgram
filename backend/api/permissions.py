from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Права доступа для автора рецепта."""

    def has_object_permission(self, request, view, obj):
        """Проверяет, является ли пользователь автором рецепта."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
