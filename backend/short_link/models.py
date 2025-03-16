from django.db import models
from short_link.constants import MAX_HASH, URL
from short_link.service import generate_hash


class LinkMapped(models.Model):
    """Модель ссылок."""

    url_hash = models.CharField(
        'Короткая ссылка',
        max_length=MAX_HASH,
        default=generate_hash,
        unique=True
    )
    original_url = models.CharField(
        'Оригинальная ссылка',
        max_length=URL)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return f'{self.original_url} -> {self.url_hash}'
