from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('movie', views.MovieViewSet, basename='movie')

urlpatterns = [
    # <-------Start Actor URl------------>
    path('actor/',views.ActorApiView.as_view()),
    path('actor/<int:pk>/',views.ActorRetrieveApiView.as_view()),
    # <-------End Actor URl------------>

    # <-------Start Genre URl------------>
    path('genre/', views.GenreApiView.as_view()),
    path('genre/<int:pk>/', views.GenreRetrieveApiView.as_view(), name='genre-detail'),
    # <-------End Genre URl------------>

    # <-------Start Director URl------------>
    path('director/', views.DirectorApiView.as_view()),
    path('director/<int:pk>/', views.DirectorRetrieveApiView.as_view()),
    # <-------End Director URl------------>

    # <-------Start Comment URl------------>
    path('movie/<int:movie_id>/comment/', views.CommentApiview.as_view()),
    path('movie/<int:movie_id>/comment/<int:comment_id>/', views.CommentRetrieveApiView.as_view()),
    # <-------End Comment URl------------>

    # <-------Start Movie URl------------>
    path('', include(router.urls)),
    ]# <-------End Movie URl------------>
