# Generated by Django 4.1 on 2023-01-07 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_delete_aboutcontactpostmodel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutideapostmodel',
            old_name='user_name',
            new_name='username',
        ),
    ]