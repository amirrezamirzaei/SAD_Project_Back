# Generated by Django 3.2.3 on 2022-08-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenttype',
            name='type',
            field=models.CharField(default='other', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contenttype',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]