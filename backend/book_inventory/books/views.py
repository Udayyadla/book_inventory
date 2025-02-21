from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filtering and search capabilities
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    search_fields=['title','author']
    filterset_fields=['published_date','price']
