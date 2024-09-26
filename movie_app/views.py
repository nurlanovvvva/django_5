from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Director, Movie, Review
from .serializers import (
    DirectorSerializer, MovieSerializer,
    ReviewSerializer, DirectorWithMoviesCountSerializer,
    MovieWithReviewsSerializer
)

# Director
class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorWithMoviesCountListAPIView(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorWithMoviesCountSerializer

# Movie
class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieWithReviewsListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieWithReviewsSerializer

# Review
class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
