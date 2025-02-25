# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer
from .pagination import BookPagination
from .filters import BookFilter  # Assuming you have a BookFilter class
from rest_framework.filters import OrderingFilter
from django.db.models import Max, Min
from rest_framework.response import Response


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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # Apply filters if needed

        # compute filters
        max_price = queryset.aggregate(Max("price"))["price__max"]
        min_price = queryset.aggregate(Min("price"))["price__min"]
        authors = list(queryset.values_list("author", flat=True).distinct())

        # paginate queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.paginator.get_paginated_response(
                self.get_serializer(page, many=True).data,
                max_price=max_price,
                min_price=min_price,
                authors=authors,
            )
        return Response(self.get_serializer(queryset, many=True).data)
