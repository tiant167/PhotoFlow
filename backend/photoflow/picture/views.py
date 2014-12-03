from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Picture
from .serializers import PictureSerialize

# Create your views here.

class PictureList(APIView):
    def get(self,request):
        pics = Picture.objects.all().order_by('-create_time')
        result = PictureSerialize(pics,many=True)
        return Response(result.data)