from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListUsers, CreateUser

urlpatterns = [
    path('', ListUsers.as_view(), name='user-list'),
    path('create/', CreateUser.as_view(), name='user-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
