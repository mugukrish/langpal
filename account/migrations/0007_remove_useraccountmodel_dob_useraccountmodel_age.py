# Generated by Django 4.1 on 2023-02-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_useraccountmodel_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccountmodel',
            name='dob',
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
