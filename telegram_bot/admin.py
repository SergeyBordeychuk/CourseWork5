from django.contrib import admin

from telegram_bot.models import Habit, PleasantHabit


# Register your models here.

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(PleasantHabit)
class PleasantHabitAdmin(admin.ModelAdmin):
    exclude = ()
