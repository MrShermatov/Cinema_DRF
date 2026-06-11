from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('movie', views.MovieViewSet, basename='movie')

router.register('actor', views.ActorAPIViewSet, basename='actor')

router.register('genre', views.GenreAPIViewSet, basename='genre')

router.register('director', views.DirectorAPIViewSet, basename='director')

urlpatterns = [
    path(
        'movie/<int:movie_id>/comment/',
        views.CommentApiViewSet.as_view({'get': 'list', 'post': 'create'})

    ),
    path(
        'movie/<int:movie_id>/comment/<int:comment_id>/',
        views.CommentApiViewSet.as_view(
            {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
    ),
    path('', include(router.urls)),
]