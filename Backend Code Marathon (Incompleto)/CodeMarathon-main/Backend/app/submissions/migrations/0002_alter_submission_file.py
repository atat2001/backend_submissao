# Generated by Django 4.0.1 on 2022-01-21 18:21

from django.db import migrations, models
import submissions.models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(upload_to=submissions.models.submission_filename),
        ),
    ]
