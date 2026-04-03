from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.user.models import User

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.user.models import User
from apps.user.serializers import RegisterSerializers, TokenObtainPairSerializer

class RegisterAPI(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

class CustomToken(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class UserView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    