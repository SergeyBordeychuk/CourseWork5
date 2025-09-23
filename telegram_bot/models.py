from django.db import models

from users.models import CustomUser


# Create your models here.
class Pleasant_Habit(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    action_do = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "приятная привычка"
        verbose_name_plural = "приятные привычки"


class Habit(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    time = models.DateTimeField()
    action_do = models.CharField(max_length=100)
    time_do = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    connected_habit = models.ForeignKey(Pleasant_Habit, on_delete=models.CASCADE, null=True, blank=True)
    award = models.CharField(max_length=100, null=True, blank=True)
    period_days = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
