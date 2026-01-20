from rest_framework import viewsets
from .models import LogStream
from .serializers import LogStreamSerializer

class LogStreamViewSet(viewsets.ModelViewSet):
    queryset = LogStream.objects.all().order_by('-created_at')
    serializer_class = LogStreamSerializer