# Generated by Django 5.0.6 on 2024-05-22 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]