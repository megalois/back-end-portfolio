from rest_framework.views import APIView
from rest_framework.response import Response


class RequestHeaderDetail(APIView):

    def get(self, request):
        return Response(request.META['HTTP_USER_AGENT'])
