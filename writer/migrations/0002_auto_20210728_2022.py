# Generated by Django 3.2.4 on 2021-07-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_approved',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=1),
        ),
    ]
