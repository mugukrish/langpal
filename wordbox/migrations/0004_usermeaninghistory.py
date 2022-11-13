# Generated by Django 4.1 on 2022-11-13 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wordbox', '0003_remove_globalmeaningmodel_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeaningHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_searched', models.JSONField()),
                ('is_favourite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
