# Generated by Django 3.2.4 on 2022-06-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220612_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='grade_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='step',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
