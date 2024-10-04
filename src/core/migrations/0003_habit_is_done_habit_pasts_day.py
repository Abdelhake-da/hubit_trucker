# Generated by Django 5.1.1 on 2024-10-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_habit_frequency_habit_occurrences_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='habit',
            name='pasts_day',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
