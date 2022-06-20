# Generated by Django 3.2.4 on 2022-06-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('title', models.CharField(choices=[('MR', 'MR'), ('MRS', 'MRS')], max_length=5)),
                ('first_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('staff_no', models.CharField(max_length=50)),
                ('ipps_no', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10)),
                ('grade_level', models.IntegerField()),
                ('step', models.IntegerField()),
                ('date_of_first_appointment', models.DateField()),
                ('date_of_first_appointment_nuc', models.DateField()),
                ('date_of_present_appointment', models.DateField()),
                ('date_of_present_posting', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=255)),
                ('employment_description', models.CharField(max_length=255)),
                ('employment_type', models.CharField(max_length=255)),
                ('staff_category', models.CharField(max_length=255)),
                ('cadre', models.CharField(max_length=255)),
                ('is_director', models.BooleanField(default=False)),
                ('is_dhr', models.BooleanField(default=False)),
                ('is_es', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
