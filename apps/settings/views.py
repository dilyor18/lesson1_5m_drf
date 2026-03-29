from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class HelloView(APIView):
    def get(self, request):
        return Response({"name": "hello geeks"})


class AboutView(APIView):
    def get(self, request):
        return Response({"name": "гикс курсы программирования"})


class ContactView(APIView):
    def get(self, request):
        return Response({"name": "0995 123 456 связь "})

