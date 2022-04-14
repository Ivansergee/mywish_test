from rest_framework.serializers import ModelSerializer

from .models import Token


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'unique_hash', 'tx_hash', 'media_url', 'owner']
