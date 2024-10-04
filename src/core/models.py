from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    is_visible = models.BooleanField(default=True)
    duration_of_use = models.PositiveIntegerField(default=1)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    occurrences = models.PositiveIntegerField(default=1)
    occurrences_done = models.PositiveIntegerField(default=0)
    pasts_day = models.PositiveIntegerField(default=0)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " - " + self.description + " - " + str(self.created_at) + " - " + str(self.duration_of_use)

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"
        ordering = ["-created_at"]

class HabitDone(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    done_date = models.DateField()

    def save(self, *args, **kwargs):
        # Increment occurrences_done in the related habit
        self.habit.occurrences_done += 1
        self.habit.save()
        super(HabitDone, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.habit.name + " - " + str(self.done_date)

    class Meta:
        verbose_name = "Habit Done"
        verbose_name_plural = "Habits Done"
        ordering = ["-created_at"]