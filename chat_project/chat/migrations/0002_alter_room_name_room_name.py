# Generated by Django 5.0.7 on 2024-07-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_name',
            name='room_name',
            field=models.CharField(max_length=200),
        ),
    ]