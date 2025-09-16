from rest_framework.exceptions import ValidationError


class HabitValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        con_habit = value['connected_habit']
        award = value['award']
        if con_habit and award:
            raise ValidationError('Invalid habit value')

class HabitTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value['time_do']
        if time > 120:
            raise ValidationError('Invalid time do')

class HabitPeriodValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = value['period_days']
        if period > 7:
            raise ValidationError('Invalid period value')
