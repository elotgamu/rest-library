# from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions

from .models import User

from .permissions import IsLibrarianUser

from .serializers import UserSerializer

# Create your views here.


class ListUsers(generics.ListAPIView):
    """Retrieve list of all Users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsLibrarianUser,)


class DetailUser(generics.RetrieveUpdateAPIView):
    """ Creates an user only if logged in as Librarian """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsLibrarianUser,)


class CreateUser(generics.CreateAPIView):
    """ Creates an user only if logged in as Librarian """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsLibrarianUser,)
