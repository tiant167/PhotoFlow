from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Website
from .serializers import WebsiteSerialize

# Create your views here.

class WebsiteConf(APIView):
    def get(self,request):
        conf = Website.objects.all()
        if len(conf) == 0:
            conf = [Website(title="Blog Title",subtitle="Fill in your title in Admin",photo_title="A New Day is Comming",photo_description="blablabla, you can fill in these words in the Admin Panel.")]
        result = WebsiteSerialize(conf[0])
        return Response(result.data)