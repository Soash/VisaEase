# Generated by Django 5.0.7 on 2024-08-08 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0016_alter_visaapplication_auth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visaapplication',
            name='mode_of_payment',
        ),
    ]
