# Generated by Django 3.0.3 on 2020-02-25 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_customerbankaccount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerBankAccount',
            new_name='IndividualCustomerBankAccount',
        ),
        migrations.RenameModel(
            old_name='CustomerProfile',
            new_name='IndividualCustomerProfile',
        ),
        migrations.CreateModel(
            name='CompanyCustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('tax_code', models.CharField(max_length=30)),
                ('representatives', models.ManyToManyField(to='profiles.IndividualCustomerProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyCustomerBankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=60)),
                ('owner', models.CharField(max_length=50)),
                ('customer_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to='profiles.CompanyCustomerProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]