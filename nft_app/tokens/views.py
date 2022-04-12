from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from .models import Token


class ListCreateTokenView(ListCreateAPIView):
    pass


class TotalSupplyView(APIView):
    pass
