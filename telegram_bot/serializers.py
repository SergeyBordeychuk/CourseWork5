from rest_framework import serializers

from telegram_bot.models import Habit, Pleasant_Habit
from telegram_bot.validators import HabitValidator, HabitTimeValidator, HabitPeriodValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidator(field1='connected_habit', field2='award'), HabitTimeValidator(field='time_do'), HabitPeriodValidator(field='period_days'),]


class PleasantHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pleasant_Habit
        fields = '__all__'
