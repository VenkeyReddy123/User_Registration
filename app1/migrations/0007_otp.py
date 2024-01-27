# Generated by Django 4.2.7 on 2024-01-27 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app1', '0006_delete_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('UserName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Otp', models.IntegerField()),
            ],
        ),
    ]