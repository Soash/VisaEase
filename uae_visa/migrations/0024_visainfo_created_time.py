# Generated by Django 5.0.7 on 2024-08-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0023_visainfo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='visainfo',
            name='created_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
