# Generated by Django 2.2.1 on 2019-06-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heredjapp', '0002_auto_20190621_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentismo',
            name='presente',
        ),
        migrations.AddField(
            model_name='presentismo',
            name='falta',
            field=models.FloatField(default=0),
        ),
    ]
