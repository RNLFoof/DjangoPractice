# Generated by Django 2.2.4 on 2019-08-29 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Score',
        ),
    ]
