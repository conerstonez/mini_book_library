from rest_framework import serializers
from book.models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'date_of_birth')
        model = Author


class AuthorCreationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
        model = Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'summary', 'author', 'genre', 'language')
        model = Book

    author = AuthorSerializer()


class BookCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'summary', 'ISBN', 'genre', 'language')
