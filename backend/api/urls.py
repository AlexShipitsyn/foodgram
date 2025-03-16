from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    'users',
    views.UserViewSet,
    'users'
)
router.register(
    'tags',
    views.TagViewSet,
    'tag'
)
router.register(
    'recipes',
    views.RecipeViewSet,
    'recipe'
)
router.register(
    'ingredients',
    views.IngredientViewSet,
    'ingredient'
)
app_name = 'api'

urlpatterns = [

    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
