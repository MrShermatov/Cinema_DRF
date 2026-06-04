from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('movie', views.MovieViewSet, basename='movie')

urlpatterns = [
    path('actor/',views.ActorApiView.as_view()),
    path('actor/<int:pk>/',views.ActorRetrieveApiView.as_view()),

    path('genre/', views.GenreApiView.as_view()),
    path('genre/<int:pk>/', views.GenreRetrieveApiView.as_view()),

    path('director/', views.DirectorApiView.as_view()),
    path('director/<int:pk>/', views.DirectorRetrieveApiView.as_view()),

    path('', include(router.urls)),

]