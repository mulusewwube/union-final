# Generated by Django 4.1.5 on 2024-08-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORDER', '0026_alter_assignment_abstract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='business_plan',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='editing',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='graphicsdesignsubmission',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='programmingprojectsubmission',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='research',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transcription',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='videoeditingsubmission',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='website_project',
            name='ordered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
