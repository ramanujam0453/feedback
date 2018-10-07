from rest_framework import serializers
from .models import EmpFeedBack


class EmpFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpFeedBack
        fields = '__all__'
