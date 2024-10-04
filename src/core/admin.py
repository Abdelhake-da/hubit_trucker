from django.contrib import admin
from . models import Habit, HabitDone
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'start_date', 'is_visible', 'duration_of_use')
    search_fields = ('name', 'description', 'created_at', 'start_date')
class HabitDoneAdmin(admin.ModelAdmin):
    list_display = ('habit', 'created_at', 'done_date')
    search_fields = ('habit', 'created_at', 'done_date')


# Register your models here.
admin.site.register(Habit, HabitAdmin)
admin.site.register(HabitDone, HabitDoneAdmin)