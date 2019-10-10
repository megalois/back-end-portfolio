from django.http import Http404, HttpResponseRedirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from url_shortener.models import URL
from url_shortener.serializers import URLSerializer
from url_shortener.shortener import ShortURL


shortener = ShortURL()


class URLList(APIView):
    """List all urls or create a new url"""

    def get(self, request):
        urls = URL.objects.all()
        serializers = URLSerializer(urls, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            saved_url = serializer.save()
            return Response({"short_url": shortener.encode(saved_url.id)})
        # A better practice is to redirect after a POST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLDetail(APIView):
    """Retrieve a url"""

    def get(self, request, short_url):
        try:
            original_url = URL.objects.get(pk=shortener.decode(short_url))
        except URL.DoesNotExist:
            raise Http404
        else:
            serializer = URLSerializer(original_url)
            return HttpResponseRedirect(serializer.data['url'])

