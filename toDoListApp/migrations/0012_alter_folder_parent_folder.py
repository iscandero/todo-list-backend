# Generated by Django 4.0.4 on 2022-06-16 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('toDoListApp', '0011_alter_folder_parent_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(blank=True, default=models.AutoField(primary_key=True, serialize=False, unique=True,
                                                                         verbose_name='ID'), null=True,
                                    on_delete=django.db.models.deletion.CASCADE, to='toDoListApp.folder',
                                    verbose_name='ID родительской папки'),
        ),
    ]
