from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet

app_name = 'movies'

router = DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('movies/', MovieAPIView.as_view(), name='movie-list'),
#     path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
#     path('movies/create/', MovieCreateAPIView.as_view(), name='movie-create'),

# ]
