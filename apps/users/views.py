# from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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


class AuthToken(ObtainAuthToken):
    """ Customized view to get the user token and some basic user data """

    def post(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data,
                                            context={'request': request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.pk,
                'username': user.username,
                'email': user.email
            }
        })
