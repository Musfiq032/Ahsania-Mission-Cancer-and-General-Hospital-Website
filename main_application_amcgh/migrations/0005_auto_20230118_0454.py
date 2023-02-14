# Generated by Django 3.2.15 on 2023-01-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_application_amcgh', '0004_auto_20221214_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_image',
            field=models.ImageField(blank=True, null=True, upload_to='Department/'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='appointment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='governingbody',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='managementteam',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]