# Generated by Django 5.0.7 on 2024-08-09 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0018_alter_visaapplication_visa_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visainfo',
            name='visa_iss_dt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
