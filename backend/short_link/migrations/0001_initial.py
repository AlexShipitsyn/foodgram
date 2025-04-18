# Generated by Django 3.2.3 on 2025-03-10 09:41

from django.db import migrations, models

import short_link.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkMapped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_hash', models.CharField(default=short_link.models.generate_hash, max_length=15, unique=True, verbose_name='Короткая ссылка')),
                ('original_url', models.CharField(max_length=256, verbose_name='Оригинальная ссылка')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]
