# Generated by Django 3.2.15 on 2022-09-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_application_amcgh', '0002_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='governingbody',
            name='institution',
            field=models.CharField(default='None', max_length=255),
        ),
    ]
