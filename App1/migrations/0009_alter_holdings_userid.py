# Generated by Django 4.0.1 on 2022-01-22 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App1', '0008_rename_user_holdings_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holdings',
            name='userid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]