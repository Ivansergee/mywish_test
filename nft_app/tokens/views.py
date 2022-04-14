import random
import string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Token
from .serializers import TokenSerializer
from .functions import get_total_supply, create_token


class TotalSupplyView(APIView):
    def get(self, request):
        total_supply = get_total_supply()
        return Response(data={'total_supply': total_supply})


class CreateTokenView(APIView):
    def post(self, request):
        unique_hash = ''.join([random.choice(string.hexdigits) for i in range(20)])
        owner = request.data.get('owner')
        media_url = request.data.get('media_url')
        token = Token(unique_hash=unique_hash, owner=owner, media_url=media_url)
        token.save()

        try:
            tx_hash = create_token(token.owner, token.unique_hash, token.media_url)
            Token.objects.filter(id=token.id).update(tx_hash=tx_hash)
        except Exception as e:
            Response(data={'error': e})

        token = Token.objects.get(id=token.id)
        serializer = TokenSerializer(token)
        return Response(serializer.data)


class ListTokenView(ListAPIView):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()
