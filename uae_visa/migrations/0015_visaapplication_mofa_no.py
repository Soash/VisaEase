# Generated by Django 5.0.7 on 2024-08-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0014_visaapplication_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='visaapplication',
            name='mofa_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
