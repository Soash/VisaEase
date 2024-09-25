# Generated by Django 5.0.7 on 2024-08-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0009_visaapplication_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaapplication',
            name='pot',
            field=models.CharField(blank=True, choices=[('----', '----'), ('WORK', 'WORK'), ('TRANSIT', 'TRANSIT'), ('VISIT', 'VISIT'), ('UMRAH', 'UMRAH'), ('RESIDENCE', 'RESIDENCE'), ('HAJJ', 'HAJJ'), ('DIPLOMACY', 'DIPLOMACY')], default='----', max_length=10, null=True),
        ),
    ]
