from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size=5 #Set number of records per page
    page_size_query_param='limit' #allow users to change records per page
    max_page_size=59 #prevents users from requesting too many records
    