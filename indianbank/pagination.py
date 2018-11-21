from rest_framework.pagination import PageNumberPagination

class BankPagination(PageNumberPagination):
	page_size = 20
