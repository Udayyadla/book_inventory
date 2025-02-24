from .models import Book
import django_filters


class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    published_year = django_filters.NumberFilter(
        field_name="published_date", lookup_expr="year"
    )
    published_month = django_filters.NumberFilter(
        field_name="published_date", lookup_expr="month"
    )

    class Meta:
        model = Book
        fields = ["min_price", "max_price", "published_year", "published_date"]
