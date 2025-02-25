from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BookPagination(PageNumberPagination):
    page_size = 5  # Set number of records per page
    page_size_query_param = "page_size"  # allow users to change records per page
    max_page_size = 100  # prevents users from requesting too many records





    def get_paginated_response(
        self, data, max_price=None, min_price=None, authors=None
    ):
        return Response(
            {
                "total_pages": self.page.paginator.num_pages,
                "page_size": self.page.paginator.per_page,
                "current_page": self.page.number,
                "total_items": self.page.paginator.count,  # total records in db
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "filters": {
                    "min_price": min_price,
                    "max_price": max_price,
                    "authors": authors if authors is not None else [],
                },
                "results": data,  # the actual paginated data
            }
        )
