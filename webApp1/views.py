from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from .models import Update_data
import json  # used in earlier format
from django.views.generic import View
from API_Tutorial.mixins import JsonResponseMixin
from django.core.serializers import serialize


# Create your views here.

# def detail_view(request):
# #     return render(request, template, {}) # return JSON data or XML
# #     return HttpResponse(get_template().render({}))

def json_example_view(request):
    # GET Example
    # URI for REST API
    data = {
        "count": 1000,
        "content": "Some Content for testing"
    }
    return JsonResponse(data)
    # earlier version used below format
    # json_data = json.dumps(data)
    # return HttpResponse(json_data, content_type='application/json')


class jsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some Content for testing 1"
        }
        return JsonResponse(data)


class jsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some Content for testing 2"
        }
        return JsonResponse(data)

class serializeDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update_data.objects.get(id=1)
        data = {
            "user": obj.user.username,
            "content": obj.content
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class serializeListView(View):
        def get(self, request, *args, **kwargs):
            query_set = Update_data.objects.all()
            data = serialize("json", query_set)  # , fields=('user', 'content'))
            print(data)
            json_data = data
            return HttpResponse(json_data, content_type='application/json')
