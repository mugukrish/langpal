# Generated by Django 4.1 on 2023-01-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbox', '0004_usermeaninghistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeaningSentences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('sentence', models.TextField()),
            ],
        ),
    ]
