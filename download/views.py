from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from upload.models import Files
from django.http import FileResponse




class FileList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        files = Files.objects.values()
        return Response(files, status=status.HTTP_200_OK)


class FileDownload(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            file_obj = Files.objects.get(pk=pk)
            file_path = file_obj.file.path
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{file_obj.filename}"'
            return response
        except Files.DoesNotExist:
            return Response({'error': 'File not found'}, status=404)
