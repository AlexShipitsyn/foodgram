from django.contrib.auth.models import AbstractUser
from django.db import models

from users.constants import LAST_NAME_MAX_LENGTH, FIRST_NAME_MAX_LENGTH


class User(AbstractUser):
    """Модель пользователя."""

    email = models.EmailField(
        unique=True,
        verbose_name='Почта'
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Фамилия'
    )
    avatar = models.ImageField(
        upload_to='user/',
        blank=True, null=True,
        verbose_name='Аватар'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']


class Subscriber(models.Model):
    """Модель подписок пользователей."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber'
    )

    class Meta:
        default_related_name = 'subscribers'
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscriber'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='unique_subscriber_himself',
            ),
        ]

    def __str__(self):
        return f'{self.user.username!r} подписан на {self.author.username!r}'

    @classmethod
    def get_prefetch_subscribers(cls, lookup, user):
        """Получение подписок пользователя."""
        return models.Prefetch(
            lookup,
            queryset=cls.objects.all().annotate(
                is_subscribed=models.Exists(
                    cls.objects.filter(
                        author=models.OuterRef('author'),
                        user_id=user.id,
                    )
                )
            ),
            to_attr='subs',
        )
