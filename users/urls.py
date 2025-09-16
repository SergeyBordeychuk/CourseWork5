from django.urls import path

from django.contrib.auth.views import LogoutView
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView, UserListAPIView

app_name = 'users'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateAPIView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>', UserRetrieveAPIView.as_view(), name='detail'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='delete'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
]