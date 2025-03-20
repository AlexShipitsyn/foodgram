from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy
from users.models import Subscriber, User


@admin.register(User)
class UsersAdmin(UserAdmin):
    """Админка для пользователя."""

    list_display = (
        'id',
        'full_name',
        'username',
        'email',
        'is_staff',
        'recipe_count',
        'subscriber_count'
    )
    search_fields = (
        'username',
        'email'
    )
    search_help_text = 'Поиск по `username` и `email`'

    @admin.display(description='Имя фамилия')
    def full_name(self, obj):
        """Получение полного имени."""
        return obj.get_full_name()

    @admin.display(description='Количество рецептов')
    def recipe_count(self, obj):
        """Возвращает количество рецептов пользователя."""
        return obj.recipes.count()

    @admin.display(description='Количество подписчиков')
    def subscriber_count(self, obj):
        """Возвращает количество подписчиков пользователя."""
        return obj.subscribers.count()


admin.site.register(Subscriber)
admin.site.unregister([Group, TokenProxy])
