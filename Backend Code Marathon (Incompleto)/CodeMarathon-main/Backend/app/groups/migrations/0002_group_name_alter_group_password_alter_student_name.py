# Generated by Django 4.0.2 on 2022-03-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='password',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
