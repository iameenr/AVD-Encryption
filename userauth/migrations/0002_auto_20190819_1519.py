# Generated by Django 2.2.1 on 2019-08-19 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operators',
            new_name='Administrators',
        ),
    ]
