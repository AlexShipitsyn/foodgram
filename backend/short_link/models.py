from django.db import models
from foodgram.constants import MAX_HASH_LENGTH, URL_MAX_LENGTH
from short_link.service import generate_hash


class LinkMapped(models.Model):
    """Модель ссылок."""

    url_hash = models.CharField(
        'Короткая ссылка',
        max_length=MAX_HASH_LENGTH,
        default=generate_hash,
        unique=True
    )
    original_url = models.CharField(
        'Оригинальная ссылка',
        max_length=URL_MAX_LENGTH)

    class Meta:
        ordering = ('-original_url', )
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return f'{self.original_url} -> {self.url_hash}'
