# Generated by Django 3.0.3 on 2020-02-25 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_staffprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankAccount',
        ),
    ]