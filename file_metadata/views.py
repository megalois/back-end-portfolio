from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request, *args, **kwargs):
        file_obj_size = request.FILES['file'].size
        serializer = UploadedFileSerializer(data={'file': request.FILES['file']})
        if serializer.is_valid():
            serializer.save()
        return Response({'file_size': file_obj_size})
