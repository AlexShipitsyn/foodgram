from django.urls import path

from . import views

app_name = 'short_link'

urlpatterns = [
    path(
        '<str:url_hash>/',
        views.load_url,
        name='load_url'
    ),
]
