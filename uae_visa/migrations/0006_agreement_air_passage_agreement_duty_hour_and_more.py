# Generated by Django 5.0.7 on 2024-08-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0005_alter_visaapplication_doa_alter_visaapplication_dod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='air_passage',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='duty_hour',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='food_and_accommodation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='holiday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='leave',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='medical_facilities',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='other_terms_and_conditions',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='overtime_and_benefits',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='period_of_contract',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='agreement',
            name='repatriation_arrangement',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
