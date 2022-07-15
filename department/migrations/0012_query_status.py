# Generated by Django 3.2.14 on 2022-07-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0011_query_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='status',
            field=models.CharField(choices=[('SENT TO DHR', 'SENT TO DHR'), ('SENT TO EC', 'SENT TO EC'), ('RESOLVED', 'RESOLVED')], default='SENT TO DHR', max_length=255),
        ),
    ]