# Generated by Django 3.2.3 on 2022-08-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_content_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='library',
            name='type',
        ),
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(upload_to='.'),
        ),
    ]