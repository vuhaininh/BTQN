# Generated by Django 3.0.3 on 2020-02-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=60)),
                ('owner', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(default='Nhân Viên', max_length=50)),
                ('dob', models.DateField(max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(default='Nhân Viên', max_length=50)),
                ('dob', models.DateField(max_length=10, null=True)),
                ('liability', models.FloatField(default=0, null=True)),
                ('liability_limit', models.FloatField(default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]