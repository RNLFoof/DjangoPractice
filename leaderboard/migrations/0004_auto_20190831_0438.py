# Generated by Django 2.2.4 on 2019-08-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_score_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='emoji',
            field=models.ImageField(upload_to='leaderboard/static/leaderboard/emojis/'),
        ),
    ]