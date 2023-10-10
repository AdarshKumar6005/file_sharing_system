from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Files
from datetime import date


class UploadFile(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        group = str(user.groups.first())
        if group.lower() == 'ops':
            f = request.FILES.get('file')
            filename = f.name
            if self.allowed_file(filename):
                file = Files.objects.filter(filename = filename)
                if file.exists():
                    return Response({'msg':"File with same name already exists"}, status=status.HTTP_400_BAD_REQUEST)
                Files.objects.create(filename=filename, date_uploaded=date.today(), file=f)
                return Response({'msg':"File uploaded"}, status=status.HTTP_201_CREATED)
            return Response({'msg':"Invalid file extension"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg':"User not allowed to perform this action"}, status=status.HTTP_403_FORBIDDEN)

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['pptx','docx','xlsx']