from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelField):
    class Meta:
        model = Item
        fields = '__all__'