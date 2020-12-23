from rest_framework import pagination

class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size= 1000


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size= 100

class SmalllResultsSetPagination(pagination.PageNumberPagination):
   page_size = 10
   page_size_query_param = 'page_size'
   max_page_size= 10
