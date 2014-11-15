from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializer

# Create your views here.
class BlogList(APIView):
    
    def get(self,request):
        blogs = Blog.objects.get_blog_list()
        serializer = BlogSerializer(blogs,many=True)
        return Response(serializer.data)


class BlogDetail(APIView):

    def get_object(self,pk):
        return Blog.objects.get(pk=pk)

    def get(self,request,pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)