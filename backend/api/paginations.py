from rest_framework.pagination import PageNumberPagination

from api.constants import PAGE_SIZE, PAGE_SIZE_QUERY_PARAM


class FoodgramPagination(PageNumberPagination):
    """Класс пагинации."""

    page_size = PAGE_SIZE
    page_size_query_param = PAGE_SIZE_QUERY_PARAM
