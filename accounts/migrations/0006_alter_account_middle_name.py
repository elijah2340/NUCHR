# Generated by Django 3.2.4 on 2022-06-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220612_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]