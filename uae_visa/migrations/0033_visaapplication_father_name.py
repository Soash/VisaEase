# Generated by Django 5.0.7 on 2024-08-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0032_remove_visainfo_broker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visaapplication',
            name='father_name',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True),
        ),
    ]
