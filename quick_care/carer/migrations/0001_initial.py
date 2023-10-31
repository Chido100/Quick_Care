# Generated by Django 4.2.6 on 2023-10-31 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildMinderKYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrt_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='gender', max_length=20)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=20)),
                ('house_number', models.CharField(max_length=10)),
                ('number_of_occupants', models.IntegerField()),
                ('identity_type', models.CharField(choices=[('international passport', 'International Passport'), ('drivers licence', 'Drivers Licence')], default='identity type', max_length=50)),
                ('child_minder_training', models.FileField(upload_to='carer_file')),
                ('first_aid_training', models.FileField(upload_to='carer_file')),
                ('dbs_criminal_record_check', models.FileField(upload_to='carer_file')),
                ('child_care_register', models.BooleanField(default=False)),
                ('home_risk_assessment', models.BooleanField(default=False)),
                ('approved_mider', models.BooleanField(default=False)),
                ('childminder', models.ForeignKey(default='childminder', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ChildMinderKYC',
                'ordering': ['-date_registered'],
            },
        ),
    ]
