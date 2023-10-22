from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializers import ItemSerializer
from base.models import Item

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)