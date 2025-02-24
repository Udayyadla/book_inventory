from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,filters
from .models import Book
from .serializers import BookSerializer
from .pagination import BookPagination
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class=BookPagination #apply custom pagination
    filterset_class=BookFilter
    

    # Add filtering and search capabilities
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    search_fields=['title','author']
 
