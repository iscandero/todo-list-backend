# Generated by Django 4.0.4 on 2022-06-16 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('toDoListApp', '0013_alter_folder_parent_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='toDoListApp.folder', verbose_name='ID родительской папки'),
        ),
    ]
