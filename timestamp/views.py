from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from timestamp.models import Timestamp
from timestamp.serializers import TimestampSerializer


class TimestampList(APIView):

    def get(self, request):
        return Response("This is the base path. You have to pass a date to the url, such as 1450137600 or " 
                        "December%2015,%202015")


class TimestampDetail(APIView):

    def get(self, request, ts):
        try:
            timestamp = Timestamp.create(ts)
        except ValidationError:
            raise ParseError('Invalid date format')
        else:
            serializer = TimestampSerializer(timestamp)
            return Response(serializer.data)
