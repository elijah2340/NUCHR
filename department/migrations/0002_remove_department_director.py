# Generated by Django 3.2.4 on 2022-06-18 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='director',
        ),
    ]
