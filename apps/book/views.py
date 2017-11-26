from django.shortcuts import render

from django.views.generic.base import View
# Create your views here.
from  book.models import BookInfo

class BookListView(View):
    def get(self, request):
        """

        :param request:
        :return:
        """
        json_list = []
        books = BookInfo.objects.all()
        for book in books:
            json_dict = {}
            json_dict["name"] = book.name
            json_list.append(json_dict)


        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list), content_type="application/json")
