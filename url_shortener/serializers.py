import re
from rest_framework import serializers
from url_shortener.models import URL


URL_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


class URLSerializer(serializers.ModelSerializer):

    def validate_url(self, value):
        if re.match(URL_REGEX, value) is None:
            raise serializers.ValidationError('Error: invalid url')
        return value

    class Meta:
        model = URL
        fields = ('id', 'url')
