# Generated by Django 3.2.3 on 2022-07-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
