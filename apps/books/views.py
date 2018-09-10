# from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions

from .models import Book, Author, Editorial
from .serializers import (BookCreateSerializer, BookListSerializer,
                          BookDetailSerializer)

from .serializers import AuthorSerializer, BasicAuthorSerializer
from .serializers import EditorialListSerializer

from apps.users import permissions as user_permission

# Create your views here.


class BookCreate(generics.CreateAPIView):
    """Show all books or create a new one"""
    serializer_class = BookCreateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          user_permission.IsLibrarianUser)

    def perform_create(self, serializer):
        serializer.save(registered_by=self.request.user)
        return super(BookCreate, self).perform_create(serializer)


class BookEdit(generics.UpdateAPIView):
    """ Edit a Book instance """
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          user_permission.IsLibrarianUser,)


class BookList(generics.ListAPIView):
    """Show the list of existing Books"""
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookDetails(generics.RetrieveAPIView):
    """Get, update or remove books"""
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          user_permission.IsLibrarianUser,)


class AuthorList(generics.ListCreateAPIView):
    """Show all authors or create a new author"""
    queryset = Author.objects.all()
    serializer_class = BasicAuthorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AuthorDetails(generics.RetrieveAPIView):
    """Get, update or remove an authors"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          user_permission.IsLibrarianUser,)


class EditorialList(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
