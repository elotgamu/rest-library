from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (BookList, BookDetails, BookCreate, BookEdit,
                    AuthorList, AuthorDetails, EditorialList)


urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:pk>/', BookDetails.as_view(), name='book-detail'),
    path('create/', BookCreate.as_view(), name='book-create'),
    path('<int:pk>/edit/', BookEdit.as_view(), name='book-edit'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetails.as_view(), name='author-detail'),
    path('editorials/', EditorialList.as_view(), name='editorial-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
