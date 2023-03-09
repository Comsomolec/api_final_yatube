from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Добавление новых записей или редактирование доступно только автору.
    """

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (
            (request.method in permissions.SAFE_METHODS)
            or (obj.author == request.user)
        )


class IsOwner(permissions.BasePermission):
    """
    Добавление новых записей или редактирование доступно только владельцу.
    """

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user)
