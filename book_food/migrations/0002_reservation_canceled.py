# Generated by Django 4.2.11 on 2024-04-20 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
    ]
