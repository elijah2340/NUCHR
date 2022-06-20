# Generated by Django 3.2.4 on 2022-06-18 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_director'),
        ('department', '0003_auto_20220618_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.director'),
        ),
        migrations.DeleteModel(
            name='Director',
        ),
    ]