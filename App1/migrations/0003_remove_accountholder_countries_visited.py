# Generated by Django 4.0.1 on 2022-01-21 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_stock_accountholder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountholder',
            name='countries_visited',
        ),
    ]
