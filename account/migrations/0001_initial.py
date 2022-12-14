# Generated by Django 4.1 on 2022-11-07 17:59

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
            name='UserAccountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('id_user', models.CharField(max_length=50)),
                ('emial', models.CharField(max_length=50)),
                ('about_me', models.TextField(blank=True)),
                ('dob', models.DateField()),
                ('profile_image', models.ImageField(default='blank-profile-picture.png', upload_to='profile_images')),
                ('location', models.CharField(blank=True, max_length=50)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
