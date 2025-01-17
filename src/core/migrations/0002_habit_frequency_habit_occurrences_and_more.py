# Generated by Django 5.1.1 on 2024-10-03 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='frequency',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='daily', max_length=10),
        ),
        migrations.AddField(
            model_name='habit',
            name='occurrences',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='habit',
            name='occurrences_done',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='habit',
            name='duration_of_use',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='HabitDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('done_date', models.DateField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.habit')),
            ],
            options={
                'verbose_name': 'Habit Done',
                'verbose_name_plural': 'Habits Done',
                'ordering': ['-created_at'],
            },
        ),
    ]
