from rest_framework import generics
from core.models import Contact
from .serializers import *

class ContacList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer