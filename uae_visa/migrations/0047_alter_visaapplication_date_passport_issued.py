# Generated by Django 5.0.7 on 2024-08-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0046_alter_visaapplication_doa_alter_visaapplication_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaapplication',
            name='date_passport_issued',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
