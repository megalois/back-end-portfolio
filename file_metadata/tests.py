from django.core.files import File
from rest_framework import status
from rest_framework.test import APITestCase


class UploadedFileTests(APITestCase):

    def test_file_upload(self):
        with open('file_metadata/test_files/test_file.JPG', 'rb') as f:
            my_file = File(f)
            data = {'file': my_file}
            response = self.client.post('/file-metadata/files/', data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['file_size'], my_file.size)

