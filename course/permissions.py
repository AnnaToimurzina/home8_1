from rest_framework import permissions

class IsModeratorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Модераторы курсов').exists():
            # Пользователь принадлежит группе модераторов и имеет право на чтение
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Если объект принадлежит пользователю, то он имеет право на редактирование
        if obj.user == request.user:
            return True
        return False