# Generated by Django 4.1 on 2022-12-25 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homefeed', '0003_userpostmodel_image_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpostmodel',
            name='downvote_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userpostmodel',
            name='upvote_count',
            field=models.IntegerField(null=True),
        ),
    ]
