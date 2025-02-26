# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import Book
from .serializers import BookSerializer, RegisterSerializer, UserSerializer
from .pagination import BookPagination
from .filters import BookFilter  # Assuming you have a BookFilter class
from rest_framework.filters import OrderingFilter
from django.db.models import Max, Min
from rest_framework.response import Response
from django.contrib.auth.models import User


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
    permission_classes=[permissions.IsAuthenticated]

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


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["POST"])
    def register(self, request):
        """Register a new User"""
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User registered successfully!", "user_id": user.id},
                status=201,
            )
        return Response(serializer.errors,status=400)
    @action(detail=False,methods=['POST'])
    def logout(self,request):
        """Logout a user (Client-side: Remove a token)"""
        return Response({"message":"Logged Out successfully!"})
        