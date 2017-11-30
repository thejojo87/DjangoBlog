from django.views.generic.base import View
# Create your views here.
from blog.models import BlogInfo
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BlogListView(APIView):
    def get(self, request, format=None):
        """
        所有的文集
        :param request:
        :return:
        """
        blogs = BlogInfo.objects.all()
        blogs_serializer = BlogSerializer(blogs, many=True)
        return Response(blogs_serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
