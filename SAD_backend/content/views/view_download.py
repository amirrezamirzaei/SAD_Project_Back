import mimetypes

from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from content.models import Content, FileAccess


class DownloadView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser,)
    permission_classes = [IsAuthenticated]

    def get(self, request, file_path):
        try:
            content = Content.objects.get(file=f'contents/{file_path}')
        except Content.DoesNotExist:
            return Response({'message': f'content with path={file_path} does not exist.', 'code': 'ERROR'}, status=400)

        # check access
        if not FileAccess.does_member_have_access(request.user, content):
            return Response({'message': f'you do not have permission to view this file.', 'code': 'ERROR'}, status=401)

        mime_type, _ = mimetypes.guess_type(content.file.path)

        with open(content.file.path, 'rb') as file:
            response = HttpResponse(file, status=status.HTTP_200_OK, content_type=mime_type)
            response['Content-Disposition'] = f'attachment; filename="{file.name.split("_")[-1]}"'
            return response


