# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer
from .pagination import BookPagination
from .filters import BookFilter  # Assuming you have a BookFilter class
from rest_framework.filters import OrderingFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination  # apply custom pagination
    filterset_class = BookFilter
    ordering_fields = ["price", "published_date"]
    # ordering = ["published_date"]

    # Add filtering and search capabilities
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ["title", "author", "published_date"]
