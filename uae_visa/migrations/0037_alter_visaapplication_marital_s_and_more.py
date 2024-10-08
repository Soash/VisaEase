# Generated by Django 5.0.7 on 2024-08-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0036_alter_visaapplication_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaapplication',
            name='marital_s',
            field=models.CharField(blank=True, default='MARRIED', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='poi_1',
            field=models.CharField(blank=True, default='DHAKA', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='poi_2',
            field=models.CharField(blank=True, default='DHAKA', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='profession',
            field=models.CharField(blank=True, default='WORKER', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='prs_nationality',
            field=models.CharField(blank=True, default='BANGLADESHI', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='prv_nationality',
            field=models.CharField(blank=True, default='BANGLADESHI', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='religion',
            field=models.CharField(blank=True, default='ISLAM', max_length=50, null=True),
        ),
    ]
