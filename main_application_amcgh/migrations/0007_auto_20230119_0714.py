# Generated by Django 3.2.15 on 2023-01-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_application_amcgh', '0006_auto_20230119_0657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={},
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sorting_order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
