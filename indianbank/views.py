from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Branches,Banks
from .pagination import *

from rest_framework import exceptions

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	
	queryset=Branches.objects.all()
	query2=Banks.objects.all()
	serializer_class = BankInfoSerializer 
	def get_queryset(self, *args, **kwargs):
		ifsc = self.request.query_params.get('ifsc', None)
		bank = self.request.query_params.get('bank',None)
		city = self.request.query_params.get('city',None)
		name = self.request.query_params.get('name',None)	 
		if ifsc is not None:
			self.pages = BankPagination
			self.queryset = self.queryset.filter(ifsc=ifsc)
			return self.queryset
		elif city is not None and  name is not None:
			self.pages = BankPagination
			self.query2=self.query2.filter(name=name)
			self.queryset = self.queryset.filter(bank=bank,city=city)
			return   self.queryset
		else:
			raise exceptions.NotAcceptable(detail="improper data. missing data ", code= 'parametersMissing')
