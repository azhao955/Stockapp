# Generated by Django 4.0.1 on 2022-01-22 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_alter_holdings_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holdings',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.accountholder'),
        ),
    ]
