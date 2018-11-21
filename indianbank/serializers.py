from rest_framework import serializers
from .models import Branches

class BankInfoSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = Branches
		fields = '__all__'
