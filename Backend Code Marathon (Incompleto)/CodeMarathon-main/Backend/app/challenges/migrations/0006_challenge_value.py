# Generated by Django 4.0.2 on 2022-03-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0005_alter_challenge_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='value',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
