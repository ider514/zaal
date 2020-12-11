from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import Court
from main.api.serializers import CourtSerializer

@api_view(['GET', 'POST'])
def api_detail_court_view(request, name):
    try:
        court = Court.objects.get(name=name)
    except Court.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CourtSerializer(court)
        return Response(serializer.data)
