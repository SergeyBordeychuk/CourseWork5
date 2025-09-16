from django.urls import path
from rest_framework.routers import DefaultRouter

from telegram_bot.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitRetrieveAPIView, \
    HabitDestroyAPIView, PleasantHabitListAPIView, PleasantHabitCreateAPIView, PleasantHabitUpdateAPIView, \
    PleasantHabitRetrieveAPIView, PleasantHabitDestroyAPIView

app_name = 'habit'

router = DefaultRouter()

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('update/<int:pk>', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('<int:pk>', HabitRetrieveAPIView.as_view(), name='habit'),
    path('delete/<int:pk>', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('pleasant_habit/', PleasantHabitListAPIView.as_view(), name='pleasant_habit_list'),
    path('pleasant_habit/create/', PleasantHabitCreateAPIView.as_view(), name='pleasant_habit_create'),
    path('pleasant_habit/update/<int:pk>', PleasantHabitUpdateAPIView.as_view(), name='pleasant_habit_update'),
    path('pleasant_habit/<int:pk>', PleasantHabitRetrieveAPIView.as_view(), name='pleasant_habit'),
    path('pleasant_habit/delete/<int:pk>', PleasantHabitDestroyAPIView.as_view(), name='pleasant_habit_delete'),
    ] + router.urls