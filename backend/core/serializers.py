from rest_framework import serializers

from core.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('id', 'url', 'short_url', 'created_at', 'expire_at', 'user')
