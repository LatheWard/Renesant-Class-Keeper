# Generated by Django 3.1.4 on 2021-04-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20210429_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergrade',
            name='isCompleted',
            field=models.BooleanField(default=True),
        ),
    ]
