# Generated by Django 4.1 on 2022-11-08 18:10

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('post_text', models.TextField()),
                ('user_name', models.CharField(max_length=100)),
                ('posted_on', models.DateField(verbose_name=datetime.datetime.now)),
            ],
        ),
    ]
