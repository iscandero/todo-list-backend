# Generated by Django 4.0.4 on 2022-06-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('toDoListApp', '0002_alter_task_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=2, verbose_name='Название'),
        ),
    ]