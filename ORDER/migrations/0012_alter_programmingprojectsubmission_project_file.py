# Generated by Django 4.1.5 on 2024-06-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORDER', '0011_programmingprojectsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmingprojectsubmission',
            name='project_file',
            field=models.FileField(upload_to='programming/'),
        ),
    ]
