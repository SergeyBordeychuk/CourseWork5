from django.contrib import admin

from telegram_bot.models import Habit, Pleasant_Habit


# Register your models here.

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Pleasant_Habit)
class PleasantHabitAdmin(admin.ModelAdmin):
    exclude = ()