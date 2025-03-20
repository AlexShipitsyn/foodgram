from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from foodgram.constants import (
    AMOUNT_MAX, AMOUNT_MIN, COOKING_TIME_MAX, COOKING_TIME_MIN,
    INGREDIENT_CHAR_MAX, INGREDIENT_UNIT_MAX, RECIPE_CHAR_MAX, TAG_CHAR_MAX
)
from users.models import User


class AuthorModel(models.Model):
    """Абстрактная модель Автора."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    class Meta:
        ordering = ('-author', )
        abstract = True

    def __str__(self):
        return self.author


class Tag(models.Model):
    """Класс модели тегов."""

    name = models.CharField(
        'Название',
        max_length=TAG_CHAR_MAX,
        unique=True
    )
    slug = models.SlugField(
        'Слаг',
        max_length=TAG_CHAR_MAX,
        unique=True
    )

    class Meta:
        ordering = ('-name', )
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Класс модели ингредиентов."""

    name = models.CharField(
        'Название',
        max_length=INGREDIENT_CHAR_MAX,
        db_index=True
    )
    measurement_unit = models.CharField(
        'Единицы измерения',
        max_length=INGREDIENT_UNIT_MAX
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='name_measurement_unit',
            )
        ]

    def __str__(self):
        return f'{self.name} ({self.measurement_unit})'


class Recipe(AuthorModel):
    """Класс модели рецептов."""

    image = models.ImageField(
        'Картинка',
        upload_to='recipes/'
    )
    name = models.CharField(
        'Название',
        max_length=RECIPE_CHAR_MAX
    )
    text = models.TextField(
        'Описание'
    )
    created_at = models.DateTimeField(
        'Создано',
        auto_now_add=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        through='RecipeIngredient'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[
            MinValueValidator(COOKING_TIME_MIN),
            MaxValueValidator(COOKING_TIME_MAX),
        ],
    )

    class Meta:
        ordering = ('-created_at',)
        default_related_name = 'recipes'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Количество ингредиента в рецепте."""

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
        validators=[
            MinValueValidator(AMOUNT_MIN),
            MaxValueValidator(AMOUNT_MAX),
        ],
    )

    class Meta:
        ordering = ('-recipe', )
        default_related_name = 'recipe_ingredients'
        constraints = [
            models.UniqueConstraint(
                fields=['ingredient', 'recipe'],
                name='unique ingredient'
            )
        ]
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.ingredient} - {self.amount}'


class AuthorRecipeModel(AuthorModel):
    """Абстрактная модель Автора и Рецепта."""

    recipe = models.ForeignKey(
        'recipes.Recipe',
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        abstract = True


class FavoriteRecipe(AuthorRecipeModel):
    """Избранные рецепты."""

    class Meta:
        default_related_name = 'favorites'
        verbose_name = 'Избранное'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique recipe favorite'
            )
        ]

    def __str__(self):
        return f'{self.recipe.name!r} в избранном у {self.author.username!r}'


class ShoppingCart(AuthorRecipeModel):
    """Корзина рецептов."""

    class Meta:
        default_related_name = 'shopping_carts'
        verbose_name = 'Корзина'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'recipe'],
                name='unique recipe shopping cart'
            )
        ]

    def __str__(self):
        return f'{self.recipe.name!r} в корзине у {self.author.username!r}'


class Import(models.Model):
    """Импорт CSV."""

    csv_file = models.FileField(
        'Файл',
        upload_to='uploads/'
    )
    date_added = models.DateTimeField(
        'Дата импорта',
        auto_now_add=True
    )

    class Meta:
        ordering = ('-date_added', )
        verbose_name = 'Учет импорта CSV'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.csv_file!r}'
