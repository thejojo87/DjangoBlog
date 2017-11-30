from django.shortcuts import render

from django.views.generic.base import View
# Create your views here.
from  book.models import BookInfo
from .serializers import BookSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets

# book的restapi的分页设置类
class BooksPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class BookListViewSet(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    """
    book列表
    """
    queryset = BookInfo.objects.all()
    pagination_class = BooksPagination
    serializer_class = BookSerializer

    # def get(self, request, format=None):
    #     """
    #     所有的文集
    #     :param request:
    #     :return:
    #     """
    #     books = BookInfo.objects.all()
    #     books_serializer = BookSerializer(books, many=True)
    #     return Response(books_serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)