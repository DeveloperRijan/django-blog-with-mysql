# Generated by Django 3.2.4 on 2021-07-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0002_auto_20210728_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
    ]
