# Generated by Django 2.2.1 on 2019-08-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enc', '0003_auto_20190820_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.TextField(default='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.TextField(default='name'),
            preserve_default=False,
        ),
    ]
