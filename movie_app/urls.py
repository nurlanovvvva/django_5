from django.urls import path
from .views import DirectorListAPIView, DirectorDetailAPIView, MovieListAPIView, MovieDetailAPIView, ReviewListAPIView, ReviewDetailAPIView

urlpatterns = [
    path('directors/', DirectorListAPIView.as_view(), name='director-list'),
    path('directors/<int:id>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    path('movies/<int:id>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
