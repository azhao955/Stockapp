# Generated by Django 4.0.1 on 2022-01-22 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0010_alter_holdings_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountholder',
            old_name='user',
            new_name='userid',
        ),
    ]
