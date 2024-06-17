from rest_framework import serializers
from .models import Profile, Recipe, Comment


class ProfileSerializer(serializers.MocelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'created_at', 'author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'author', 'text', 'created_at']