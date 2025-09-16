from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from users.models import CustomUser
from users.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    queryset = CustomUser.objects.all()