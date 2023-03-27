from rest_framework import generics
from rest_framework.decorators import api_view
# from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import *


# function-based_api_view

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serialized_books = BookSerializer(books, many=True)
#         return Response(serialized_books.data)
#     elif request.method == 'POST':
#         new_book = BookCreationSerializer(data=request.data)
#         new_book.is_valid(raise_exception=True)
#         new_book.save()
#         return Response('book saved successfully')
#
#
# @api_view(['GET', 'DELETE'])
# def book_detail(request, pk):
#     found_book = Book.objects.get(id=pk)
#     if request.method == 'GET':
#         serialized_book = BookSerializer(found_book)
#         return Response(serialized_book.data, status=HTTP_302_FOUND)
#     elif request.method == 'DELETE':
#         found_book.delete()
#         return Response('deleted successfully', status=HTTP_200_OK)
#
#
# @api_view(['GET', 'POST'])
# def authors(request):
#     if request.method == 'GET':
#         author_list = Author.objects.all()
#         serialized_authors = AuthorSerializer(author_list, many=True)
#         return Response(serialized_authors.data)
#     elif request.method == 'POST':
#         new_author = AuthorCreationSerializer(data=request.data)
#         new_author.is_valid(raise_exception=True)
#         new_author.save()
#         return Response('Author saved successfully')
#
#
# @api_view(['GET', 'DELETE'])
# def author_detail(request, pk):
#     found_author = Author.objects.get(id=pk)
#     if request.method == 'GET':
#         serialized_author = AuthorSerializer(found_author, many=False)
#         return Response(serialized_author.data, status=HTTP_302_FOUND)
#     elif request.method == 'DELETE':
#         found_author.delete()
#         return Response('deleted successfully', status=HTTP_200_OK)


# class-based_api_view

class BookApiView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookCreationSerializer


class BookUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookCreationSerializer


class AuthorApiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorCreationSerializer


class AuthorUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Author.objects.all()
    serializer_class = AuthorCreationSerializer


@api_view(['GET'])
def get_author_books_view(request, id):
    author = Author.objects.get(id=id)
    queryset = Book.objects.select_related('author').filter(author=author)
    serialized_books = BookSerializer(queryset, many=True)
    return Response(serialized_books.data)


@api_view(['GET'])
def get_books_view(request, user_input):
    queryset = Book.objects.select_related('author')\
        .filter(Q(genre=user_input) | Q(language=user_input))
    serialized_books = BookSerializer(queryset, many=True)
    return Response(serialized_books.data)

    # genres = [genre.value for genre in Genre]
    # languages = [language.value for language in Language]
    # if genres.__contains__(user_input):
    #     queryset = Book.objects.filter(genre=user_input)
    #     serialized_books = BookSerializer(queryset, many=True)
    #     return Response(serialized_books.data)
    # elif languages.__contains__(user_input):
    #     queryset = Book.objects.filter(language=user_input)
    #     serialized_books = BookSerializer(queryset, many=True)
    #     return Response(serialized_books.data)
