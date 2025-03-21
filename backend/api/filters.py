from django.contrib.auth import get_user_model
from django_filters.rest_framework import (AllValuesMultipleFilter,
                                           BooleanFilter, CharFilter,
                                           FilterSet)

from recipes.models import Ingredient, Recipe

User = get_user_model()


class IngredientFilter(FilterSet):
    """Фильтр для поиска по ингредиентам."""

    name = CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    """Фильтр для поиска по рецептам."""

    tags = AllValuesMultipleFilter(
        field_name='tags__slug',
    )
    is_favorited = BooleanFilter(
        method='is_favorite_filter',
        field_name='favorites__author',
    )
    is_in_shopping_cart = BooleanFilter(
        method='is_in_shopping_cart_filter',
        field_name='shopping_carts__author',
    )

    class Meta:
        model = Recipe
        fields = (
            'author',
            'tags',
            'is_favorited',
            'is_in_shopping_cart',
        )

    def is_favorite_filter(self, queryset, name, value):
        """Фильтр по избранным рецептам."""
        return self.filter_from_kwargs(
            queryset,
            value,
            name,
        )

    def is_in_shopping_cart_filter(self, queryset, name, value):
        """Фильтр по рецептам в списке покупок."""
        return self.filter_from_kwargs(
            queryset,
            value,
            name,
        )

    def filter_from_kwargs(self, queryset, value, name):
        """Фильтр по избранным рецептам и рецептам в списке покупок."""
        if value and self.request.user.id:
            return queryset.filter(**{name: self.request.user})
        return queryset
