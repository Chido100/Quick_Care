# Generated by Django 4.2.6 on 2023-10-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='childminderkyc',
            name='identity_image',
            field=models.ImageField(default='identity_image', upload_to='carer_file'),
        ),
        migrations.AddField(
            model_name='childminderkyc',
            name='photograph',
            field=models.ImageField(default='photograph', upload_to='minder_photo'),
        ),
        migrations.AlterField(
            model_name='childminderkyc',
            name='identity_type',
            field=models.CharField(choices=[('international passport', 'International Passport'), ('drivers licence', 'Drivers Licence')], default='identity_type', max_length=50),
        ),
        migrations.AlterField(
            model_name='childminderkyc',
            name='phone_number',
            field=models.CharField(max_length=14),
        ),
    ]
