# Generated by Django 5.0.7 on 2024-08-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uae_visa', '0037_alter_visaapplication_marital_s_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visaapplication',
            name='carriers_name',
        ),
        migrations.RemoveField(
            model_name='visaapplication',
            name='date_passport_expiry',
        ),
        migrations.RemoveField(
            model_name='visaapplication',
            name='destination',
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='auth',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='bus_add_and_tel_no',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='dosK',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='f_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='father_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='home_add_and_tel_no',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='id_number',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='mofa_no',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='name_employer',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='office_duration',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='office_employer',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='office_fee',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='office_id',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='office_type',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='passport_no',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='pob',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='relationship',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='sect',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
