from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from telegram_bot.models import Habit, Pleasant_Habit
from telegram_bot.paginators import HabitPagination
from telegram_bot.permissions import IsOwner
from telegram_bot.serializers import HabitSerializer, PleasantHabitSerializer


# Create your views here.
class HabitCreateAPIView(generics.CreateAPIView):
    '''Создание привычки'''
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    '''Просмотр всех привычек'''
    serializer_class = HabitSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = Habit.objects.all()
    pagination_class = HabitPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    '''Просмотр привычки'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    '''Обновление инф. привычки'''
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class HabitDestroyAPIView(generics.DestroyAPIView):
    '''Удаление привычки'''
    queryset = Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class PleasantHabitCreateAPIView(generics.CreateAPIView):
    '''Создание привычки'''
    serializer_class = PleasantHabitSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        pleasant_habit = serializer.save()
        pleasant_habit.owner = self.request.user
        pleasant_habit.save()


class PleasantHabitListAPIView(generics.ListAPIView):
    '''Просмотр всех привычек'''
    serializer_class = PleasantHabitSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = Pleasant_Habit.objects.all()
    pagination_class = HabitPagination


class PleasantHabitRetrieveAPIView(generics.RetrieveAPIView):
    '''Просмотр привычки'''
    serializer_class = PleasantHabitSerializer
    queryset = Pleasant_Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class PleasantHabitUpdateAPIView(generics.UpdateAPIView):
    '''Обновление инф. привычки'''
    serializer_class = PleasantHabitSerializer
    queryset = Pleasant_Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class PleasantHabitDestroyAPIView(generics.DestroyAPIView):
    '''Удаление привычки'''
    queryset = Pleasant_Habit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]