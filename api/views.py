from django.http import HttpResponse
from rest_framework import viewsets
from .models import Profile, Recipe, Comment
from .serializers import ProfileSerializer, RecipeSerializer, CommentSerializer


def home(request):
    return HttpResponse("Welcome to the Bitebond API")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



