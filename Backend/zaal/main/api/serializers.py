from rest_framework import serializers
from main.models import Court, Manager

class ManagerSerializer(serializers.ModelSerializer):
    manager = serializers.CharField(read_only=True)

    class Meta:
        model = Manager

class CourtSerializer(serializers.ModelSerializer):
    manager_name = serializers.CharField(source='manager.name', read_only=True)
    class Meta:
        model = Court
        fields = ['manager_name','name', 'description', 'created_at', 'modified_at', 'category', 'rating']
