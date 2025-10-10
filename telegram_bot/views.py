from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from telegram_bot.models import Habit, PleasantHabit
from telegram_bot.paginators import HabitPagination
from telegram_bot.permissions import IsOwner
from telegram_bot.serializers import HabitSerializer, PleasantHabitSerializer
from telegram_bot.tasks import send_telegram_message


# Create your views here.
class HabitCreateAPIView(generics.CreateAPIView):
    '''Создание привычки'''
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        habit = serializer.save(owner=self.request.user)
        if habit.owner.telegram_chat_id:
            send_telegram_message(f'я буду {habit.action_do} в {habit.time} в {habit.place}',
                                  habit.owner.telegram_chat_id)


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
        habit = serializer.save(owner=self.request.user)
        if habit.owner.telegram_chat_id:
            send_telegram_message(f'я буду {habit.action_do}',
                                  habit.owner.telegram_chat_id)


class PleasantHabitListAPIView(generics.ListAPIView):
    '''Просмотр всех привычек'''
    serializer_class = PleasantHabitSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = PleasantHabit.objects.all()
    pagination_class = HabitPagination


class PleasantHabitRetrieveAPIView(generics.RetrieveAPIView):
    '''Просмотр привычки'''
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class PleasantHabitUpdateAPIView(generics.UpdateAPIView):
    '''Обновление инф. привычки'''
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]


class PleasantHabitDestroyAPIView(generics.DestroyAPIView):
    '''Удаление привычки'''
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
