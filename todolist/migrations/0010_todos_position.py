# Generated by Django 4.1.5 on 2023-02-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_alter_lists_datetime_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]