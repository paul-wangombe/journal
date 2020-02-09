from rest_framework.viewsets import ModelViewSet

from .serializers import JournalSerializer
from .models import Journal

# Create your views here.


class JournalViewSet(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
